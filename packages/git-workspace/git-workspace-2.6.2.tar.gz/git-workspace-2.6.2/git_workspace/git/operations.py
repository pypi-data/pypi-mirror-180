# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import logging
import os
import subprocess
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

__DEFAULT_BRANCH = "main"
__MAX_RETRIES = 5
__RETRY_DELAY = 5


def __pick_directory(repo_object):
    if "directory" in repo_object:
        return repo_object["directory"]
    else:
        # Take the tail part of the path and then the part before the ".git"
        return os.path.split(repo_object["path"])[1].split(".")[0]


def git_clone(wsdir, repositories, git_configuration):
    gituser = git_configuration["gituser"]
    githost = git_configuration["githost"]

    def clone(repo):
        working_directory = wsdir
        if repo["path"].endswith(".git"):
            repo_path_without_git_ending = repo["path"][:-4]  # Remove .git from the end of the string
        else:
            repo_path_without_git_ending = repo["path"]
        check_for_emptiness = repo_path_without_git_ending.split("/")[-1]
        command = f"git clone {gituser}@{githost}:{repo['path']}"
        if "directory" in repo:
            # Working directory in this case is the same as the target where there repo is to be cloned
            # This could be done otherwise as well, would it be better?
            working_directory = os.path.join(wsdir, repo["directory"])
            os.makedirs(working_directory, exist_ok=True)
            command += " ."
            check_for_emptiness = working_directory

        if os.path.exists(check_for_emptiness) and os.listdir(check_for_emptiness):
            print(f"Skipping directory {check_for_emptiness}: Directory is not empty. Assuming it is already cloned.")
            return

        for attempt in range(1, __MAX_RETRIES + 1):
            print(f"Fetching {repo['path']}. Attempt {attempt}")
            sp = subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, cwd=working_directory)
            if sp.returncode > 0:
                logging.debug(sp.stderr.decode("utf-8"))
                if attempt != __MAX_RETRIES:
                    print(f"Failed to clone {repo['path']}. Retrying in  {__RETRY_DELAY}.")
                else:
                    print(f"Failed to clone {repo['path']}.")
                    time.sleep(__RETRY_DELAY)
            else:
                break
        print(f"Finished cloning {repo['path']}")

    with ThreadPoolExecutor() as executor:
        future_to_clone = {executor.submit(clone, repo): repo for repo in repositories}
        for future in as_completed(future_to_clone):
            repo = future_to_clone[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"Failed to clone {repo['path']}")
                logging.debug("Inside ThredPoolExecutor, caught an exception:")
                logging.debug("".join(traceback.extract_tb(e.__traceback__).format()))
                logging.debug(e)
                print()
            logging.debug(f"Completed execution for {repo['path']}")


def ws_state(wsdir, repositories):
    name_length = 10
    for repo in repositories:
        directory = __pick_directory(repo)

        if len(directory) + 2 > name_length:
            name_length = len(directory) + 4
    failures = []
    print(f"{'Directory':<{name_length}} "
          f"{'Current branch':<60} "
          f"{'Behind origin/master':<25} "
          f"{'Uncommitted files':<25} "
          f"{'Untracked files':<25}")
    for repo in repositories:
        directory = __pick_directory(repo)
        default_branch = repo.get("default_branch", __DEFAULT_BRANCH)
        working_dir = os.path.join(wsdir, directory)
        try:
            cbsp = subprocess.run(f"git branch | grep \* | cut -d ' ' -f2",
                                  shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                  cwd=working_dir)
            if cbsp.returncode > 0:
                current_branch = "error"
            else:
                current_branch = cbsp.stdout.strip().decode("utf-8")

            bdsp = subprocess.run(f"git rev-list --count {current_branch}..origin/{default_branch}",
                                  shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                  cwd=working_dir)
            if bdsp.returncode > 0:
                branch_diff = "error"
            else:
                branch_diff = bdsp.stdout.strip().decode("utf-8")

            mcsp = subprocess.run(f"git ls-files --modified | wc -w",
                                  shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL, cwd=working_dir)
            if mcsp.returncode > 0:
                modified_count = "error"
            else:
                modified_count = mcsp.stdout.strip().decode("utf-8")

            ucsp = subprocess.run(f"git ls-files --exclude-standard --others | wc -l",
                                  shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL, cwd=working_dir)
            if ucsp.returncode > 0:
                untracked_count = "error"
            else:
                untracked_count = ucsp.stdout.strip().decode("utf-8")

            print(f"{directory:<{name_length}} "
                  f"{current_branch:<60} "
                  f"{branch_diff:<25} "
                  f"{modified_count:<25} "
                  f"{untracked_count:<25}")
        except:
            failures.append(repo.get("path"))

    if len(failures) > 0:
        print("\nFailed to check the state of the following repositories:")
        print("\n".join(failures))


def in_repository_operation(op, repositories, wsdir):
    for item in repositories:
        directory = __pick_directory(item)

        if not os.path.exists(os.path.join(wsdir, directory)):
            print(f"{directory} not found. Skipping...")
            continue

        print(f"**** {directory} ****")
        sp = subprocess.run(op, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True, cwd=os.path.join(wsdir, directory))
        print(sp.stdout.decode("utf-8"))
        if sp.returncode > 0:
            print(sp.stderr.decode("utf-8"))

        print(f"{'':-^60}")


def change_to_default_branch_and_update(repositories, wsdir):
    failures = []

    def run_command(cmd):
        sp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                            cwd=os.path.join(wsdir, directory))

        print(sp.stdout.decode("utf-8"))
        if sp.returncode > 0:
            print("Stash failed. Skipping...")
            print(sp.stderr.decode("utf-8"))
            return False
        return True

    for item in repositories:
        directory = __pick_directory(item)

        if "default_branch" in item and not item["default_branch"]:
            print(f"Default branch defined for {item['path']} in configuration but left blank. Skipping...")
            failures.append(directory)
            continue

        default_branch = item.get("default_branch", "main")

        if not os.path.exists(os.path.join(wsdir, directory)):
            print(f"{directory} not found. Skipping...")
            failures.append(directory)
            continue

        print(f"**** Reset to default and update: {directory} ****")
        if not run_command("git stash"):
            failures.append(directory)
            continue

        if not run_command(f"git checkout {default_branch}"):
            failures.append(directory)
            continue

        if not run_command(f"git pull origin {default_branch}"):
            failures.append(directory)
            continue

    if len(failures):
        print("Switching to the default branch and updating it failed in the following paths:")
        for item in failures:
            print(item)

        exit(1)
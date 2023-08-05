from setuptools import setup, find_packages

try:
    with open("VERSION", "r") as vfile:
        version_line = vfile.readline()
except FileNotFoundError:
    version_line = "0.0.9999999"

version = version_line.strip()

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="git-workspace",
    packages=find_packages(),
    include_package_data=True,
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    description="Git 'extension' for managing multirepo workspaces",
    author="Aki Mäkinen",
    author_email="nenshou.sora@gmail.com",
    url="https://gitlab.com/blissfulreboot/python/git-workspace",
    keywords=["Git", "Workspace"],
    install_requires=[
        "requests>=2.26.0",
        "prompt-toolkit>=3.0.0",
        "keyring>=23.0.0,<24",
        "ruamel.yaml>=0.17.0",
        "click>=8.0.0"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    entry_points={
      "console_scripts": [
          "git-ws = git_workspace.cli:main"
      ]
    }
)

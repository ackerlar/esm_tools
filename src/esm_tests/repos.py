import os

from .test_utilities import sh

def update_resources_submodule(info, verbose=True):
    """
    Initiates and updates the module ``esm_tests_info``.
    """
    os.chdir(info["script_dir"])
    sh("git submodule init", verbose=verbose)
    sh("git submodule update", verbose=verbose)

def info_repo():
    """
    Return a git object for the esm_tests_info repo
    """
    pass

def esm_tools_repo():
    """
    Return a git object for the esm_tools repo
    """
    pass

def checkout_info():
    """
    Checks out the release branch in the resources repo and pulls
    """
    pass

def commit_info_changes():
    """
    commits
    """

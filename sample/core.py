"""Short description of the main script/module

This is considered the main or core script for a project/task.  It is likely where the __main__ function
would be defined.

Any imports/dependencies/requirements should be noted here (e.g. argparse, etc)

"""

# import any functions inside or outside of this module.  If no helpers are needed it can be removed from here
# as well as remove the file from the sample module.

from . import helpers

def get_hmm():
    """This is a place holder for an internal function to the module.  it should be removed/replaced as needed.

    """
    return 'hmmm...'


def hmm():
    """This is a that can be called outside this module by way of an import."""
    if helpers.get_answer():
        print(get_hmm())

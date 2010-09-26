import os
import os.path
import sys

def add_pytpm_to_path(args, dirname, names):
    """Find pytpm in the build dir. and add to sys.path"""
    if (dirname not in sys.path) and ("pytpm" in dirname):
        # Add dir. containing pytpm not pytpm itself
        sys.path.append(os.path.dirname(dirname))

def add_path():
    build_dir = os.path.join(os.pardir, "build")
    os.path.walk(build_dir, add_pytpm_to_path, None)

# If package is installed then use it else add build directory to path and
# import the package from there.
def run():
    try:
        from pytpm import tpm
    except:
        try:
            add_path()
            from pytpm import tpm
        except:
            print "Cannot find pytpm."
            sys.exit()

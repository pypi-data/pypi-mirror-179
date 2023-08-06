# Anchorer
Plugin for [`virtualenvwrapper`](https://pypi.org/project/virtualenvwrapper/) that extends `mkvirtualenv` behaviour to
add code that is loaded by the python interpreter for every run. The loaded code resolves symlinks in discovered
site-package directories, allowing symlinks to virtualenvs to be updated while scripts/services are running.

## Example problem anchorer solves
```shell
# assuming you have the virtualenvwrapper python package installed, and have sourced virtualenvwrapper.sh
mkvirtualenv env-v1
mkvirtualenv env-v2

# create a pseudo-virtualenv which is a symlink to a particular version
ln -s "$WORKON_HOME/env-v1" "$WORKON_HOME/active-env"

# now use the linked environment to start something in env-v1
workon active-env

# start some imaginary python service which may import modules a long time after starting
python -m my_long_runner &

# update the active symlink, switching what version
ln -sT "$WORKON_HOME/env-v2" "$WORKON_HOME/active-env"

# imagine at this point that my_long_runner tries to import a module, it will be using un-resolved paths which will mean
# the modules will be loaded from an environment that is not the one it started in
```

## Architecture
 1. `virtualenvwrapper.anchorer.fix.main()` resolves paths that are used at runtime
    * current working directory
    * paths used for determining where packages are found
 2. `virtualenvwrapper` runs `virtualenvwrapper.anchorer.plugin.pre_mkvirtualenv(...)` during calls to `mkvirtualenv` to
    modify the virtualenv's site-packages directory:
    1. `__anchorer.py` is added, it is a copy of the fix module
    2. `__anchorer.pth` is added, it simply imports `__anchorer` which causes the main method to run. See
    [site docs](https://docs.python.org/3/library/site.html) for more information on the mechanism

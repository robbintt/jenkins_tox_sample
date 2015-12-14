### Dead simple sample of tox with jenkins.

This is a template project, it defines a simple pattern to follow.

Have recommendations? Please post them as issues.


#### Notes:
- The Jenkins Project Name cannot have any spaces because it is used in the build path. Whitespace in the virtualenv path breaks the build. See: http://lists.idyll.org/pipermail/testing-in-python/2013-June/004995.html
- Python 2 and 3 current are installed, corresponding to TOXENV = py27 py34

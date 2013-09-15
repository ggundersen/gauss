Gauss
=====
Gregory Gundersen

2013-09-14

Intro
-----
Gauss is a web application for testing, analyzing, and documenting Project
Euler solutions and associated libraries. All calculations are performed at
runtime.

Version log
-----------
- 0.4 Set timeout on XMLHttpRequest, so that the user always receives progress bar feedback; added progress bar legend
- 0.3 Refactored out datastore (data is now stored in single Python array); removed any stubbed functionality for gmath unit testing; this will be built for the 2.0 release
- 0.2 Refactored out jQuery library; added progress bar on problem test suite
- 0.1 Refactored URL-to-handler mapping to be more clear; stubbed out gmathHandler; modified main.css for more clear styling of code blocks; added favicon
- 0.0 Initial commit

### TODO
- Do not check answer based on index of odb.get_canonical_data()
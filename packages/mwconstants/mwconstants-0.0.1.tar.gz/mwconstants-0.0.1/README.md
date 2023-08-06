# mwconstants

Various utilities and constants useful for analyses of wikitext. This package contains three types of artifacts:
* Data generating functions: Python functions for calling various APIs to build useful data structures -- e.g., all Wikipedia language codes
* Static data snapshots: Python variables that contain the most recent result of a data generating function
* Utilities: Python functions for handling various wikitext-related processing tasks -- e.g., mapping links to namespaces.

## Modules
All modules generally contain relevant constants, functions for generating those constants, and other useful utilities for manipulating them: 
* `languages.py`: functions for identifying languages associated with a given Wikimedia project.
* `media.py`: functions for identifying media in wikitext and parsing wikitext media syntax into its components
* `namespaces.py`: functions for identifying namespace prefixes

## Limitations
* Links have many edge-cases, especially around interwiki prefixes. For now, just the basics are covered: language-specific namespaces and interlanguage links
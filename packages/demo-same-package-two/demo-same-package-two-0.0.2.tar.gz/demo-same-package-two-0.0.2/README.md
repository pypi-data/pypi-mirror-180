# OVERVIEW
* a experiment for verifying if two pypi packages can have the same {namespace} or not

# STRUCTURE
* PACKAGES
  * one : demo_same_package/one.py
  * two : demo_same_package/two.py

# THIS PACKAGE
* two


### EXPECTATION
* PACKAGE INSTALLATION
``` bash
pip install demo-same-package-one
pip install demo-same-package-two
```

* EXPECTED RESULTS
  * the source code would be
    * demo_same_package/
      - one
      - two


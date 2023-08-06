# sdk-python

# TODO add instructions for testing package locally

Python SDK for Sahale

Make sure to bump up the version number in setup.py? or pyproject.toml

Building and publishing to Test PyPi repo: 
Activate virtual env
```
python3 -m build
python3 -m twine upload --repository testpypi dist/*
````

Installing package:
`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps sahale`

Note: need to first create a test PyPi account and create an API key and put it in the `$HOME/.pypirc` file as per https://packaging.python.org/en/latest/tutorials/packaging-projects/

Can then view the package on Test PyPi i.e. https://test.pypi.org/project/sahale


Building and publishing to PyPi repo:
```
python3 -m build
python3 -m twine upload dist/*
```
And we can install normally using
`pip install sahale`


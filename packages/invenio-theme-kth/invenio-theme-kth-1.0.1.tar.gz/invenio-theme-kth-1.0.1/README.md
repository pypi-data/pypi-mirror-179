# invenio-theme-kth
This module provides templates overrides and modifications to invenio default theme
## Installation
In your Invenio instance make sure your venv is active then run:
```bash
pip install invenio-theme-kth
```
You are done at this point, as the installation will trigger `invenio-cli assets build` automatically
## Components
`views.py`: provides a Blueprint that registers both the static/ and templates/ folders to be usable by Invenio

`webpack.py`: registers the front-end assets (in the assets/ folder) to webpack

`config.py`: overrides several configuration items related to theming Invenio If new files is been added, first run:

## Development
This section intended if you want to further develop this module.
## Local setup
```bash
make install
# if you use pyenv
make install-pipenv
make test
```

While developing on assets you can watch it using:
```bash
invenio-cli assets watch
```
When you are done with your development you build it with:
```bash
invenio-cli assets build
```

## Upload to pypi
make package # this will zip the package into dist dir
make package-check # verify if the package pass twine checks
twine upload -u <USERNAME> -p <PASSWORD> --repository-url https://test.pypi.org/legacy/ dist/* --verbose
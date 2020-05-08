==============
repo-templates
==============
Repository templates.

repo set-up

needed packages: ``git``

create a virtual environment

run:::

  $ git init
  $ pip install -r requirements.txt
  $ pre-commit install
  $ pre-commit autoupdate

update the template structure and the ``__init__.py`` in the top-level package

list of project repo files:

CHANGELOG.md
LICENSE.txt
MANIFEST.in
.pre-commit-config.yaml
.pylintrc
README.rst
requirements.txt
setup.cfg
setup.py
tox.ini
.travis.yml
tests/test_template.py
.gitignore

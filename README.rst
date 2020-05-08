==============
repo-templates
==============
Repository templates.

repo set-up

needed packages: ``git``, ``pre-commit``

optionally create a virtual environment

run:::

  $ pre-commit install
  $ pre-commit autoupdate
  $ pip install pylint isort

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

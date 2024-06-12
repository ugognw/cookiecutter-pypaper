Changelog
#########

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

`Unreleased`_
-------------

Added
~~~~~

* Optional Coveralls_, Codecov_, Codacy_, or `Code Climate`_ integration for GitLab or GitHub
* Default GitHub actions and GitLab pipelines for documentation and changelog generation, package publishing, dependency tracking, and license compatability tracking
* Automated dependency updates with Dependabot_ (if hosting with GitHub) or dependabot-standalone_ (if hosting with GitLab)
* Additional CLI engine options:
  * `Python Fire`_ and Typer_ (with rich_)
* Badges in ``README.rst`` for Poetry_, mypy_, `Code Climate`_, nox_
* Support for optional `pytest`_ plugins (pytest_datadir_ and pytest_xdist_)
* Support for optional gitchangelog_
* Support for furo_ documentation theme with Sphinx_ and ReadTheDocs_
* Options to initialize git repository and install the package
* Optional ``py.typed`` file to indicate `PEP 561`_-compliant support for type-checking (e.g., with mypy_)

Changed
~~~~~~~

* setuptools_ -> Poetry_ for packagement management and building
* Transition from ``setup.py`` to ``pyproject.toml``
* Tox_ -> Nox_ + nox-poetry_ for managing test environments
* Replace Pylint_ with mypy_ for type-checking


Removed
~~~~~~~

* C-extension support
* Optional tests inside of packagement
* Optional coverage testing separate from tests
* Support for hosting domains other than ``github.com`` and ``gitlab.com``
* Removed support for version control via tbump_
* Scrutinizer_ support
* Option for non-Sphinx docs engine

`0.0.1`_ (2023-06-24)
---------------------

Added
~~~~~

* Forked from `ionelmc's version <https://github.com/ionelmc/cookiecutter-pylibrary>`_.

.. _Unreleased: https://github.com/ugognw/cookiecutter-pylibrary/tree/main
.. _`0.0.1`: https://github.com/ugognw/cookiecutter-pylibrary/tree/main
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Tox: https://tox.wiki/
.. _Nox: https://nox.thea.codes/en/stable/
.. _nox-poetry: https://nox-poetry.readthedocs.io/
.. _pytest: http://pytest.org/
.. _Dependabot: https://github.com/dependabot/dependabot-core
.. _dependabot-standalone: https://gitlab.com/dependabot-gitlab/dependabot-standalone
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _Black: https://black.readthedocs.io/
.. _Ruff: https://beta.ruff.rs/docs/
.. _Pylint: http://pylint.readthedocs.io
.. _mypy: https://mypy.readthedocs.io/
.. _Coveralls: https://coveralls.io/
.. _Codecov: http://codecov.io/
.. _Codacy: https://codacy.com/
.. _Code Climate: https://codeclimate.com/
.. _setuptools: http://setuptools.pypa.io
.. _Poetry: https://python-poetry.org
.. _pip-licenses: https://github.com/raimon49/pip-licenses
.. _`Python Fire`: https://github.com/google/python-fire
.. _Typer: https://typer.tiangolo.com
.. _gitchangelog: https://github.com/vaab/gitchangelog
.. _tbump: https://github.com/your-tools/tbump
.. _Scrutinizer: https://scrutinizer-ci.com
.. _rich: https://rich.readthedocs.io/
.. _PEP 561: https://peps.python.org/pep-0561/
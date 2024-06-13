======================
cookiecutter-pypaper
======================

Cookiecutter_ template for a scientific paper data repository as a Python library.

*Notes*:

* This is largely designed to address this `blog post about packaging python
  libraries <https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.

  * ... and it will save you from `packaging pitfalls
    <https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/>`_.

* Although this cookiecutter is based off of that of
  `ionelmc <https://github.com/ionelmc/cookiecutter-pylibrary>`_, it also takes
  inspiration from `python-blueprint <https://github.com/johnthagen/python-blueprint/tree/main>`_
  and `cookiecutter-hypermodern-python <https://github.com/cjolowicz/cookiecutter-hypermodern-python/tree/main>`_
* There's a bare library using this template (if you're curious about the final
  result): https://github.com/ugognw/python-no-name-paper.
* If you have a web application (not a library) you might want to take a look at
  `django-docker <https://github.com/evozon/django-docker>`_.

.. contents:: Table of Contents

Features
--------

This is an "all inclusive" sort of template.

* Choice of various licenses.

* Configuration for hosting on GitHub

* ``src/package_name`` directory structure

* tests outside of package

* Nox_ and nox-poetry_ for managing test environments for Python 3.11+

* pytest_ for testing (with `Coverage.py`_ for coverage analysis)

* Ruff_ for static checks and import sorting

* mypy_ for type-checks to supplement Ruff_

* Virtual environment management and package building/publishing with Hatch

* *Optional* git hooks via pre-commit_

* *Optional* command-line interface via argparse_, click_, `Python Fire`_, or Typer_ (and rich_)

* Configurations for:

  * pytest_

  * mypy_

  * pre-commit_

  * `Coverage.py`_

  * Ruff_

Requirements
------------

Projects using this template have the following minimal dependencies:

* click_, `Python Fire`_, or Typer_ (and rich_)

To get quickly started on a new system, just `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. That's the bare minimum to required
install Cookiecutter_. To install , just run this in your shell or command prompt::

  pip install cookiecutter

Usage and options
-----------------

This template is more involved than the regular `cookiecutter-pypackage
<https://github.com/audreyr/cookiecutter-pypackage>`_.

First generate your project::

  cookiecutter gh:ugognw/cookiecutter-pypaper

You will be asked for these fields:

.. note:: Fields that work together usually use the same prefix. If you answer "no" on the first one then the rest
   won't have any effect so just ignore them. Maybe in the future cookiecutter will allow option hiding or something
   like a wizard.

.. list-table::
    :header-rows: 1

    * - Field
      - Default
      - Description

    * - ``full_name``
      - .. code:: python

            "Ugochukwu Nwosu"
      - Main author of this library or application (used in ``AUTHORS.md`` and ``pyproject.toml``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``email``
      - .. code:: python

            "ugognw@gmail.com"
      - Contact email of the author (used in ``AUTHORS.md`` and ``pyproject.toml``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``website``
      - .. code:: python

            "https://www.law-two.com"
      - Website of the author (used in ``AUTHORS.md``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``project_name``
      - .. code:: python

            "Nameless Paper"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``project_short_description``
      - .. code:: python

            "An example package [...]"
      - One line description of the project (used in ``README.md`` and ``pyproject.toml``).

    * - ``package_name``
      - .. code:: python

            "nameless_paper"
      - Python package name (whatever you would import via a Python `import` statement).

    * - ``distribution_name``
      - .. code:: python

            "nameless-paper"
      - PyPI distribution name (what you would ``pip install``).

    * - ``repo_name``
      - .. code:: python

            "python-nameless-paper"
      - Repository name on GitHub or GitLab (and project's root directory name).

    * - ``repo_username``
      - .. code:: python

            "ugognw"
      - GitHub or GitLab user name of this project (used for GitHub link).

        Can be set in your ``~/.cookiecutterrc`` config file.
    
    * - ``repo_main_branch``
      - .. code:: python
            "main"
      - The name of the default branch for this project.

    * - ``year_from``
      - .. code:: python

            "today"
      - The effective start date of the project license. (ISO 8601 format) Defaults to today.

    * - ``year_to``
      - .. code:: python

            "today"
      - The effective end date of the project license. (ISO 8601 format) Defaults to today.

    * - ``keywords``
      - .. code:: python

            "now"
      - List of comma-separated keywords to use in `pyproject.toml` (e.g., `physics,math,chemistry`).

    * - ``chemistry_related``
      - .. code:: python

            "yes"
      - Whether or not the paper is chemistry-related. If "yes", will add the appropriate classifier.

    * - ``physics_related``
      - .. code:: python

            "yes"
      - Whether or not the paper is physics-related. If "yes", will add the appropriate classifier.

    * - ``license``
      - .. code:: python

            "BSD license"
      - License to use. Available options:

        * BSD license
        * MIT license
        * ISC license
        * Apache Software License 2.0

        What license to pick? https://choosealicense.com/

    * - ``version``
      - .. code:: python

            "0.0.0"
      - The initial version of the package.

    * - ``command_line_interface``
      - .. code:: python

            "plain"
      - Option to enable a CLI (a bin/executable file). Available options:

        * ``plain`` - a very simple command.
        * ``argparse`` - a command implemented with argparse_.
        * ``fire`` - a command implemented with `Python Fire`_.
        * ``typer`` - a command implemented with Typer_ (and rich_).
        * ``click`` - a command implemented with click_ - which you can use to build more complex commands.
        * ``no`` - no CLI at all.

    * - ``cli_bin_name``
      - .. code:: python

            "nameless"
      - Name of the CLI bin/executable file (verify that the console script name in
        ``pyproject.toml`` matches your desired implementation; see
        `here <https://python-poetry.org/docs/pyproject/#scripts>`_).

    * - ``support_type_checking``
      - .. code:: python

            "yes"
      - Whether or not to support type checking. If "yes", a ``py.typed`` file will
        be placed at ``src/package_name``.

    * - ``pypi_disable_upload``
      - .. code:: python

            "yes"
      - Whether or not to disable uploading the package to PyPI.

    * - ``pre_commit``
      - .. code:: python

            "yes"
      - Whether or not to enable pre-commit_.

    * - ``install_precommit_hooks``
      - .. code:: python

            "yes"
      - Whether or not to install pre-commit_ hooks. Requires that a .git repository exists in
        the current working directory. If pre-commit_ is not already installed, then it will be
        installed via ``pip``.

    * - ``pytest_datadir``
      - .. code:: python

            "yes"
      - Whether or not to install pytest-datadir_ as a testing dependency.

    * - ``pytest_xdist``
      - .. code:: python

            "yes"
      - Whether or not to install pytest-xdist_ as a testing dependency.

    * - ``initialize_git_repository``
      - .. code:: python

            "yes"
      - Whether or not to initialize a Git repository using `git init`. This also creates an
        initial commit and an initial tag with the version number specified in ``cookiecutter.version``.
        Both are pushed to the repository specified by `repo_name` and `repo_username`.

    * - ``install_package``
      - .. code:: python

            "yes"
      - Whether or not to include install the newly created package via Hatch_.
        If a virtual environment is not already active, this will create a new virtual environment
        in which to install the current package.

Developing the project
``````````````````````

To run all the tests, just run::

  nox

To see all the nox environments::

  nox -l

To only build the docs::

  nox -s docs

To build and verify that the built package is proper and other code QA checks::

  nox -s format,lint

Not Exactly What You Want?
--------------------------

No way, this is the best. :stuck_out_tongue_winking_eye:


If you have criticism or suggestions please open up an Issue or Pull Request.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Nox: https://nox.thea.codes/en/stable/
.. _nox-poetry: https://nox-poetry.readthedocs.io/
.. _pytest: http://pytest.org/
.. _Ruff: https://beta.ruff.rs/docs/
.. _mypy: https://mypy.readthedocs.io/
.. _pre-commit: https://pre-commit.com
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Hatch: https://hatch.pypa.io/latest/
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _click: http://click.pocoo.org/
.. _`Python Fire`: https://github.com/google/python-fire
.. _Typer: https://typer.tiangolo.com
.. _rich: https://rich.readthedocs.io/

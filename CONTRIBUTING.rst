============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Bug reports
===========

When `reporting a bug <https://github.com/ugognw/cookiecutter-pylibrary/issues>`_ please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

cookiecutter-pylibrary could always use more documentation, whether as part of the
official cookiecutter-pylibrary docs, in docstrings, or even on the web in blog posts,
articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at https://github.com/ugognw/cookiecutter-pylibrary/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

Development
===========

To set up `cookiecutter-pylibrary` for local development:

1. `Fork cookiecutter-pylibrary on GitHub <https://github.com/ugognw/cookiecutter-pylibrary/fork>`_.
2. Clone your fork locally::

    git clone git@github.com:your_username_here/cookiecutter-pylibrary.git

3. Create a branch for local development::

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes run all the checks and docs builder with pytest_ one command::

    pytest tests

5. Commit your changes and push your branch to GitHub::

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Include passing tests (run ``pytest tests``).
2. Update documentation when there's new API, functionality etc.
3. Add a note to ``CHANGELOG.rst`` about the changes.

Tips
----

If you want to add a context option, you need to:

* Add the actual option in `cookiecutter.json <https://github.com/ugognw/cookiecutter-pylibrary/blob/main/cookiecutter.json>`_
* Add it in the cookiecutter test builder suite:

  * Edit `conftest.py <https://github.com/ugognw/cookiecutter-pylibrary/blob/main/tests/conftest.py>`_
* Change the `post_gen_hook.py <https://github.com/ugognw/cookiecutter-pylibrary/blob/main/hooks/post_gen_hook.py>`_ to make any necessary changes.
* Add the option and a description to `README.rst <https://github.com/ugognw/cookiecutter-pylibrary/blob/main/README.rst>`_.
* Add an entry in the `CHANGELOG.rst <https://github.com/ugognw/cookiecutter-pylibrary/blob/main/CHANGELOG.rst>` under the heading "unreleased".

.. _pytest: http://pytest.org/
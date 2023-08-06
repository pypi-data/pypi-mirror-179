=========================
pytest-reporter-html-dots
=========================

This is a fork of the great template `pytest-reporter-html1 <https://pypi.org/project/pytest-reporter-html1/>`_ with one detail changed: Instead of grouping the tests and showing only a number how many tests have failed and how many have passed, this template tries to mimic the standard pytest output with one dot for every test.
This has the advantages that (1) even without expanding a file it's visible which tests have failed and whether they are the same like in the last run and (2) it gives a better visualization how many tests have failed in a specific file.

A basic HTML report for `pytest`_ using `Jinja2`_ template engine.
Based on `pytest-reporter`_ which provides the data to the template.


Features
--------

* Overview of files, tests, and phases with expandable sections
* Includes information about tests such as documentation, markers, and fixtures
* Fairly mobile friendly
* Complies with Jenkins default CSP policy (with ``--split-report``)
* Support for `pytest-metadata`_ and `pytest-rerunfailures`_
* May be used as a base template for customization

.. image:: https://gitlab.com/erzo/pytest-reporter-html-dots/-/raw/master/screenshot.png
    :alt: Screenshot


Installation
------------

You can install "pytest-reporter-html-dots" via `pip`_ from `PyPI`_::

    $ pip install pytest-reporter-html-dots


Usage
-----

Specify the html-dots template and the output path of the report::

    $ pytest --template=html-dots/index.html --report=report.html

By default the report is self-contained, but you can separate CSS, images,
and JavaScript by specifying the ``--split-report`` option.


Customization
-------------

You can inherit this template in your own to tailor parts of it to your own needs.
It defines various blocks which you can override using `template inheritance`_.

.. code:: html

    {% extends "html-dots/index.html" %}
    {% block style %}
        {{ super() }}
        header {
            background-color: black;
        }
    {% endblock %}

Some additional filters are available for templates to use:

``asset(path_or_content, extension)``
    Takes a path to a local file or a raw bytes object and either returns a
    base64 encoded URL or a new relative URL to a copy depending on if the
    report is self-contained or not.

    .. code:: html

        <img src="{{ 'path/to/image.png'|asset }}">
        <img src="{{ raw_byte_data|asset('png') }}">

``ansi(s)``
    Convert ANSI color codes to HTML.

``strftime(value, format)``
    Format a Unix timestamp using `datetime.strftime`_.

    .. code:: html

        Started: {{ started|strftime('%Y-%m-%d %H:%M:%S') }}

``timedelta(value)``
    Convert a time in seconds to a `timedelta`_ object.

``rst(s)``
    Convert reStructuredText to HTML.


.. _`Jinja2`: https://jinja.palletsprojects.com/
.. _`template inheritance`: https://jinja.palletsprojects.com/en/master/templates/#template-inheritance
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pytest-reporter`: https://github.com/christiansandberg/pytest-reporter
.. _`pytest-metadata`: https://github.com/pytest-dev/pytest-metadata
.. _`pytest-rerunfailures`: https://github.com/pytest-dev/pytest-rerunfailures
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`datetime.strftime`: https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
.. _`timedelta`: https://docs.python.org/3/library/datetime.html#timedelta-objects

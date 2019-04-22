=============================
djangocms_simple_news
=============================

.. image:: https://badge.fury.io/py/djangocms_simple_news.svg
    :target: https://badge.fury.io/py/djangocms_simple_news

.. image:: https://travis-ci.org/dmodules/djangocms_simple_news.svg?branch=master
    :target: https://travis-ci.org/dmodules/djangocms_simple_news

.. image:: https://codecov.io/gh/dmodules/djangocms_simple_news/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dmodules/djangocms_simple_news

DjangoCMS simple news app.

Documentation
-------------

The full documentation is at https://djangocms_simple_news.readthedocs.io.

Quickstart
----------

Install djangocms_simple_news::

    pip install djangocms_simple_news

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djangocms_simple_news.apps.DjangocmsSimpleNewsConfig',
        ...
    )

Add djangocms_simple_news's URL patterns:

.. code-block:: python

    from djangocms_simple_news import urls as djangocms_simple_news_urls


    urlpatterns = [
        ...
        url(r'^', include(djangocms_simple_news_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

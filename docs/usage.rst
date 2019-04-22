=====
Usage
=====

To use djangocms_simple_news in a project, add it to your `INSTALLED_APPS`:

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

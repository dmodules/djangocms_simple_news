DJANGOCMS Simple news
===============

Djangocms simpe news is a very basic news application.

Installation
--------------------

Divio Platrofm Users
---------------------

Choose a site you want to install the add-on to from the dashboard. Then go to ``Apps -> Install app`` and click ``Install`` next to ``Djangocms_smple_news`` app.

Redeploy the site.

Manuall Installation
--------------------

Run ``pip install djangocms_simple_news``.

Add below apps to ``INSTALLED_APPS``: ::

    INSTALLED_APPS = [
        …
        'djangocms_simple_news',
        …
    ]

********
Features
********


* Add, Edit, Delete news with django admin
* Show news in templates with templates tags

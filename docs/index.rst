.. Rohypnol documentation master file, created by
   sphinx-quickstart on Thu Jan  8 17:26:48 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Rohypnol's documentation!
====================================

Rohypnol offers syntactic sugar to easily connect Django signals to cache keys
deletion.


Requirements
------------

======  ======
Django  >= 1.5
======  ======


Installation
------------

Install the ``rohypnol`` package::

    pip install rohypnol

Make sure ``rohypnol`` is listed among your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # [...]
        'rohypnol',
    ]


Usage
-----

The code below will connect the built-in Django ``post_save`` signal to
``cache.delete('article_list')`` when the sender is an ``Article`` instance.

.. code-block:: python

    from myapp.models import Article
    from rohypnol import rohypnol

    rohypnol.register(Article, 'article_list')


In your `urls.py` file:

.. code-block:: python

    from rohypnol import connect_all_signals

    urlpatterns = ...

    connect_all_signals()


This is roughly equivalent to:


.. code-block:: python

    from django.db.models.signals import post_save
    from django.core.cache import cache

    from myapp.models import Article

    def delete_cache(key):
        cache.delete(key)

    post_save.connect(delete_cache, sender=Article)

Actually the callback function is defined as a closure. Have a look at the
``RohypnolRegister`` class if interested.

Advanced usage
--------------
The example above is pretty trivial and, in fact, useless.
But you can save yourself a lot of typing with this application by doing something like this:

.. code-block:: python

    from myapp.models import Article, Paragraph, Category
    from rohypnol import rohypnol

    rohypnol.register((Article, Paragraph, Category),
                      ('article_list', 'top_articles'))

Basically, the register method accepts three arguments:

1. ``models``, which can be a single model class or a list of models that will be
considered as the *sender* of the signals.

2. ``keys``, which can be a string or a list of strings. These will be the cache keys
that are going to be deleted.

3. ``signals``, which can be a signal instance or a list of signals. If none is
specified, it defaults to built-in Django ``post_save`` of the models above.

A more complete example:

.. code-block:: python

    from django.db.models.signals import post_save
    from django.dispatch import Signal

    custom_signal = Signal()

    rohypnol.register((Article, Category, Paragraph), 
                      ('article_list', 'top_articles'),
                      (post_save, custom_signal))

This will delete the cache fragments identified by the keys ``'article_list'``
and ``'top_articles'`` whenever a ``post_save`` or a ``custom_signal`` is sent
by one of the listed models.

.. note::

    As noted in Django documentation, the ``models.py`` is the best place to connect
    signals and you should do the same with ``rohypnol.register`` **if you are using
    Django < 1.7**.

    Starting from that version, you should use the ``ready()`` method of your
    application configuration class.
    `See the documentation <https://docs.djangoproject.com/en/1.7/topics/signals/#connecting-receiver-functions>`_
    for further explanation.

    Also, it is fundamental to call the ``connect_all_signals`` method in your ``urls.py``,
    because `it is executed only once <http://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only>`_,
    after all you models have been loaded.



Contents:

.. toctree::
   :maxdepth: 2

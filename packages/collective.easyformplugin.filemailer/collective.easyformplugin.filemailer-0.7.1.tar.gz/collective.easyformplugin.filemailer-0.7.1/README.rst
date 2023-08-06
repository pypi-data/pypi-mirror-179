.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/collective/collective.easyformplugin.filemailer/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.easyformplugin.filemailer/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.easyformplugin.filemailer/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.easyformplugin.filemailer?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.easyformplugin.filemailer/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.easyformplugin.filemailer

.. image:: https://img.shields.io/pypi/v/collective.easyformplugin.filemailer.svg
    :target: https://pypi.python.org/pypi/collective.easyformplugin.filemailer/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.easyformplugin.filemailer.svg
    :target: https://pypi.python.org/pypi/collective.easyformplugin.filemailer
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.easyformplugin.filemailer.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.easyformplugin.filemailer.svg
    :target: https://pypi.python.org/pypi/collective.easyformplugin.filemailer/
    :alt: License


====================================
collective.easyformplugin.filemailer
====================================

This add'on registers a new Easyform Action File Mailer. 

Features
--------

This File Mailer action is almost identical to the normal Mailer action, but adds an extra tab 'attachment' in the Action.
Here you can specify the internal url path to a private File Item in Plone. This file will be added as an attachment to the Mail sent. 
The main use case is to send PDF white papers or other documents that you want to distribute only to visitors leaving their contact details.


Examples
--------

-



Translations
------------

This product has been translated into

- Dutch


Installation
------------

Install collective.easyformplugin.filemailer by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.easyformplugin.filemailer


and then running ``bin/buildout``


Authors
-------

- Fred van Dijk  - Zest Software


Contributors
------------

- 

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.easyformplugin.filemailer/issues
- Source Code: https://github.com/collective/collective.easyformplugin.filemailer



License
-------

The project is licensed under the GPLv2.

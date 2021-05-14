
============
Installation
============


Stable release
--------------

To install mdm, run this command in your terminal:

.. code-block:: console

    $ pip install mdm

This is the preferred method to install mdm, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

To run the api from docker, run this commands in your terminal at the root of the package:

.. code-block:: console

    $ docker build -t mdm-restapi .
    $ docker run -d -p 5000:5000 --name mdm mdm-restapi

From sources
------------

The sources for mdm can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/audreyr/mdm

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/audreyr/mdm/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/audreyr/mdm
.. _tarball: https://github.com/audreyr/mdm/tarball/master

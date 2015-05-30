similar - A similar text finder written in Python 
=================================================

.. image:: https://travis-ci.org/ncrocfer/similar.svg?branch=master
    :target: https://travis-ci.org/ncrocfer/similar


:code:`similar` is a Python library used to find the correct spelling from a misspelled text.

Usage
-----

.. code-block:: python

    >>> from similar import best_match
    >>> best_match('rasbery', ['apple', 'raspberry', 'pear'])
    raspberry


Installation
------------

The tool works with Python 2 and Python 3. It can be installed with `Pip` :

::

    pip install similar


Notes
-----

You can also use a file object for the wordlist :

.. code-block:: python

    from similar import Similar

    s = Similar('rasbery', open('wordlist.txt'))
    print(s.best())


Or a generator :

.. code-block:: python

    from similar import Similar

    def genwords():
        for line in ['apple', 'raspberry', 'pear']:
            yield line

    s = Similar('rasbery', genwords())
    print(s.best())
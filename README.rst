================================================================
 jupyter_abc: ABC music notation extension for Jupyter Notebook
================================================================

This extension makes it easy to render ABC_ markup as graphical music notation
in a Jupyter notebook.

For rendering, the extension uses the abcjs_ Javascript library
by Paul Rosen and Gregory Dyke.

Installing
==========

To install the extension, use ``pip`` or ``setup.py``::

    cd /path/to/jupyter_abc
    python setup.py install  # with setup.py
    pip install .            # with pip

If you want to develop or debug the extension,
install it in development mode so changes are reflected immediately
without needing to re-install::

    cd /path/to/jupyter_abc
    python setup.py develop  # with setup.py
    pip install -e .         # with pip

Usage
=====

To use the extension, start Jupyter in the same Python environment
in which you installed the extension::

    jupyter notebook

Start a new notebook in which you load and use the extension:

.. code-block:: python

   %load_ext jupyter_abc

.. code-block:: text

   %%abc
   %%score (R1 R2) (L)
   V:R1
   [cc']2 z ((3g/a/b/ [cc']2) z ((3g/a/b/ | [cc']2) z2 z2 z c | (c3 B d3 c) | (g4 f2) z2 |
   V:R2
   x8 | x8 | G8- | G6 z2 |
   V:L clef=bass middle=d
   [cc']2 z ((3g/a/b/ [cc']2) z ((3g/a/b/ | [cc']2) z2 z4 | ([d'f']4 [c'e']4) | [bd']6 z2 |

.. raw:: html
   :file: jupiter.html

.. _ABC: http://abcnotation.com/
.. _abcjs: https://abcjs.net/

==================================================================
jsh_py3 - a Junos-style CLI library, Made for Python3 by fatihusta
==================================================================

**jsh_py3** is a Junos-inspired CLI library for your Python apps.
If you've ever logged into a Junos_ device, you'll know how good the CLI is.
It offers:

- tab-completion, including completion of names of items in the config
- help by pressing "?" at any point
- completion on pressing either space, tab or enter

jsh_py3 attempts to reproduce some of these features (and others) in a Python library
based on Readline, to allow you to build better quality CLIs for your apps.

Installation
============

Install from PyPI using ``pip install jsh_py3``.

Basic Usage
===========

The library takes a CLI "layout", which is a dictionary-based tree structure
describing your CLI commands. For example, a completely useless CLI with
just an ``exit`` command, you would define it like this:

.. code-block:: python

    import jsh_py3

    layout = {
        'exit': jsh_py3.exit,
    }

    jsh_py3.run(layout)

``jsh_py3.run`` is a shortcut for the following:

.. code-block:: python

    cli = jsh_py3.JSH(layout)

    while True:
        try:
            cli.read_and_execute()
        except jsh_py3.JSHError as err:
            print err
        except EOFError:
            break

This creates a basic layout with a single available command (``exit``), passes
it to an instance ``jsh_py3.JSH``, and starts an infinite loop, using the ``read_and_execute``
method of the ``jsh_py3`` CLI object to interact with the user. For more control
over this loop, you should write your own instead of using ``jsh_py3.run``.

This provides a CLI that looks like the following:

::

    > ?
    Possible completions:
      exit
    > ex?
    Possible completions:
      exit
    > exit ?
    Possible completions:
      <[Enter]>   Execute this command
    > exit

.. _Junos: http://www.juniper.net/us/en/products-services/nos/junos/

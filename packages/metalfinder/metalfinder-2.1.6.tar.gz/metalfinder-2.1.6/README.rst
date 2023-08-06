``metalfinder`` is a command-line tool that scans a music directory to find
concerts near a specified location.

Installation
============

Using pip
---------

You can install ``metalfinder`` using pip::

    $ pip install metalfinder

Using the Debian package
------------------------

``metalfinder`` is available in the `Debian archive`_, starting with Debian 12
(Bookworm). You can install it by running::

    $ apt install metalfinder

.. _Debian archive: https://packages.debian.org/search?keywords=metalfinder

From source
-----------

You can install ``metalfinder`` from source using flit::

    $ apt install flit
    $ git clone https://gitlab.com/baldurmen/metalfinder
    $ cd metafinder
    $ flit install

Run without installing
----------------------

If you already have all the required dependencies, you can run ``metalfinder``
directly from the source without installing it::

    $ python3 -m metalfinder

API Providers
=============

Bandsintown
-----------

To use the `Bandsintown`_ API provider, you will need a `Bandsintown App ID`_.
This is your API key and it should be kept private.

.. _Bandsintown: https://bandsintown.com
.. _Bandsintown App ID: https://www.artists.bandsintown.com/support/api-installation

Other providers
---------------

Do you know a good website that tracks concerts and has a somewhat public API?
If keys are not too hard to get, I'd be more than happy to implement it!

CLI options
===========

Here is an example of how to use ``metalfinder``::

     $ export METALFINDER_BIT_APPID=mysecretapikey
     $ metalfinder -d "/home/foo/Music" -o "/home/foo/metalfinder.atom" -l "Montreal"

The complete CLI parameters can be found below and in the man page::

    Usage:
        metalfinder [-d <directory>] -o <output> -l <location> -b <app_id> [-c <cache>] [-m <date>] [--verbose]
        metalfinder (-h | --help)
        metalfinder --version

    Options:
        -h  --help                   Show the help screen
        --version                    Output version information
        --verbose                    Run the program in verbose mode
        -d  --directory <directory>  Music directory to scan to create artist list
        -o  --output    <output>     Path to the desired output file. You can either
                                     chose a text file (foo.txt), a JSON file (foo.json)
                                     or an ATOM file (foo.atom)
        -l  --location  <location>   Name of the city to use when looking for concerts
        -b  --bit-appid <app_id>     Bandsintown App ID (API key). Optional when the
                                     METALFINDER_BIT_APPID environment variable is set.
        -c  --cache-dir <cache_dir>  Path to the cache directory. Defaults to
                                     $HOME/.cache/metalfinder/
        -m  --max-date  <date>       Max date in YYYY-MM-DD format (ISO 8601)

Environment Variables
=====================

``metalfinder`` uses the following environment variables:

*METALFINDER_BIT_APPID*: Bandsintown API key. Useful to keep your API key from
leaking when running metalfinder on the command line.

Running without a local directory
=================================

Even though ``metalfinder`` defaults to scanning a local directory to create a
list of artists, it is possible to use an existing artist list created by some
other program.

Using a subsonic server
-----------------------

This feature has not yet been implemented. See `issue #15`_.

.. _issue #15: https://gitlab.com/baldurmen/metalfinder/-/issues/15

Using an MDP server
-------------------

Since the ``--directory`` option is optional, if it is missing, only the cache
directory will be inspected. In this directory, ``metalfinder`` looks for a file
named ``artist_cache`` which consists of a list of artist names separated by
new lines.

If you have an `MPD`_ server, you can generate this file with the help of the
`mpc`_ client::

    $ mpc list Artist > ~/.cache/metalfinder/artist_cache

.. _MPD: https://musicpd.org/
.. _mpc: https://www.musicpd.org/clients/mpc/

Development
=============

Running the test suite
----------------------

You can run the test suite locally using ``pip`` and ``pytest``::

    $ python3 -m venv metalfinder
    $ cd metalfinder
    $ source bin/activate
    $ git clone https://gitlab.com/baldurmen/metalfinder
    $ cd metafinder
    $ python3 -m pip install .[test]
    $ python3 -m pytest

Building the man page
---------------------

The man page for ``metalfinder`` can be generated using the ``rst2man`` command
line tool provided by the ``docutils`` project::

    $ rst2man manpage.rst metalfinder.1

License
=======

This project was written by `Louis-Philippe Véronneau`_ and is licensed under
the GNU GPLv3 or any later version.

The code to query the Bandsintown API (``metalfinder/api/bandsintown.py``) and
the tests that accompany it (``tests/test_api_bandsintown.py``) come from the
`python-bandsintown`_ project. These files were written by Chris Forrette and
are licensed under the MIT license. As such, specific license headers have been
added to them.

.. _Louis-Philippe Véronneau: https://veronneau.org
.. _python-bandsintown: https://github.com/chrisforrette/python-bandsintown

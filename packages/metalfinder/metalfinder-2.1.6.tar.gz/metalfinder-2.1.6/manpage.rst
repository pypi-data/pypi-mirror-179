===========
metalfinder
===========

------------------------------------------------
CLI tool to find concerts from a music directory
------------------------------------------------

:Author: Louis-Philippe Véronneau
:Date: 2022
:Manual section: 1

Synopsis
========

| metalfinder [**-d** *<directory>*] **-o** *<output>* **-l** *<location>* **-b** *<app_id>* [**-c** *<cache>*] [**-m** *<date>*] [**--verbose**]
| metalfinder (**-h** \| **--help**)
| metalfinder **--version**

Description
===========

**metalfinder** is a command-line tool that scans a music directory to find
concerts near a specified location.

Options
=======

| **-h** | **--help**
|     Show the help screen

| **--version**
|     Output version information

| **--verbose**
|     Run the program in verbose mode

| **-d** | **--directory** *<directory>*
|     Music directory to scan to create artist list

| **-o** | **--output** *<output>*
|     Path to the desired output file. You can either chose a text file
|     (foo.txt), a JSON file (foo.json) or an ATOM file (foo.atom)

| **-l** | **--location** *<location>*
|     Name of the city to use when looking for concerts

| **-b** | **--bit-appid** *<app_id>*
|     Bandsintown App ID (API key). Optional when the METALFINDER_BIT_APPID
|     environment variable is set.

| **-c** | **--cache-dir** *<cache_dir>*
|     Path to the cache directory. Defaults to $HOME/.cache/metalfinder/

| **-m** | **--max-date** *<date>*
|     Max date in YYYY-MM-DD format (ISO 8601)

Environment Variables
=====================

| **metalfinder** uses the following environment variables:

| METALFINDER_BIT_APPID
|     Bandsintown API key. Useful to keep your API key from leaking when
|     running metalfinder on the command line.

Examples
========

|    $ export METALFINDER_BIT_APPID=mysecretapikey
|    $ metalfinder -d "/home/foo/Music" -o "/home/foo/metalfinder.atom" -l "Montreal"

Bugs
====

Bugs can be reported to your distribution's bug tracker or upstream
at https://gitlab.com/baldurmen/metalfinder/issues.

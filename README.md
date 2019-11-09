# startech.py

This is a simple library made to help make common tasks easier, and is not necessarily made to introduce any new features. Maintained by Star Technology in the UK. This module WILL NOT work on any platform except Linux.

Testing has not yet been completed, and not all python versons have been tested. These are the versions we absolutely know work:
- Python 3.7

*Compatability is not guaranteed with any unlisted versions!*

*NOTE:* This library is in RELEASE CANDIDATE stage and is due many changes. Stability is not yet guaranteed.

# General Info
## Identifier tokens (aka tokens)
Identifier tokens (often referred to as just "tokens") are a feature that enable *blacklisting*. In the future, they may also enable other features like *telemetry* or *ratelimiting*. Tokens listed in the blacklist file (see below) will be listed as invalid when checked, unless the *include* argument is set to true - thus the log module won't accept it.

Tokens should be hard-coded into scripts and should be human-readable as there main purpose is to identify the writing script of a log entry to the user when the log is read. 

Token criteria are as follows:

 - 4-12 char length
 - chars a-z (any case), 0-9, - and _ only

## File structure
The logfile is available for direct reading at *"/usr/share/stech/api/log.txt"*, if required.
The blacklist file is located at *"/usr/share/stech/api/blacklist.txt"*.
Registry files containing settings are available at *"/usr/share/stech/api/reg_token.txt"*, where *token* is the string format of the identifier.
Temporary files without persistance are stored at *"/tmp/tfile-token.txt"*, where *token* is the string format of the identifier.

## Temporary files
Temporary files __without persistance__ are handled by the system - on mosts systems, this means they're deleted at boot or upon elapse of a certain duration.
Temporary files __with persistance__ are written into *settings* associated with *token* and are deleted upon being retrieved.
In most cases where persistence is required, utilising *settings* directly is more advisable.

# Installation

Pre-requisites:
- Python 3.x must be installed NOT python 2.x, to check this run `$ ls /usr/bin | grep python`
- Run the highest number installed you have installed, i.e. *"python3.4"* or *"python3.7"* (we recommend 3.7)
- If you only have python 2.x, install python3.7. To do this in Ubuntu, `$ apt install python3.7`
- You may need to update your default python version, in Ubuntu, run `$ update-alternatives --install /usr/bin/python python /usr/bin/python3.7 5 && update-alternatives --config python` and if asked, choose the highest offered version
- Install *python3-pip*, in Ubuntu run `$ apt install python3-pip`

This library is available via PyPI, after the pre-requisites are satisfied, `$ python -m pip install startech`. Once finished, run `*$ sudo python3.x*`, then type `*from startech import setupFiles*`and press enter, then type `*setupFiles()*` and press enter again. Finally, type `*exit()*` and press enter to return to the standard command line - installation complete!

# Functions
A general breakdown of the functions available.

*NOTE:* As a rule, if a function fails due to processing problems or bad arguments, a function will return the following values:

 - If a boolean is returned when successful, False will be returned if failed
 - If a string is returned when successful, a blank string (i.e. "") will be returned if failed
 - If a list is returned when successful, a blank list (i.e. []) will be returned if failed

Unless otherwise stated - this is to help enable clean error-handling in scripts.

## checkToken(*token*,*include*)
Checks if an identifier token will meet the criteria for the log and settings modules, and returns a boolean. Inclusion of blacklisted tokens is set by *include* argument. If it's not passed, it assumes False.

## getVersion()
Returns a string of the current library version.

## getDate(*format*) and getTime(*format*)
Return a formatted time string based on the string provided in *format* or the following templates:
 - "uk" - "%d/%m/%Y" and "%H:%M:%S" respectively (*assumed if no string provided*)
 - "us" - "%Y/%m/%d" and "%H:%M:%S" respectively

## getDateTime(*format*,*seperator*)
Very similar to getDate and getTime, but takes an additional argument - "seperator" which specifies the character(s) which should separate the date and time. If no arguments are passed, "uk" and "@" are assumed respectively.

## checkRoot()
Takes no arguments, returns True if it is being run as root or False otherwise.

## combineLists(*list1*,*list2*)
Progresses through the entries of *list2* and appends them to *list1* if not already present, returning the resulting list.

## alignList(*list*)
Removes blank entries from the provided list and returns the resulting list.

## insertList(*list*,*pos*,*data*)
Inserts *data* into *list* at the specified *pos* and returns the resulting list.

## setupFiles()
Creates required files and folders for the module if they don't exist already. Returns *boolean* for success.

*NOTE:* This function WILL fail unless run by a root user for file permission and ownership reasons.

## *log*.write(*token*,*statement*)
Records *statement* to logfile using the identifier from *token*. Returns boolean of success.

## *log*.read(*count*,*token*)
Read the most recent entries based on *count*. *token* is an optional argument, which limits the output to entries made using that identifier. Returns the entries in a list.

## *settings*.getList(*token*)
Returns a list of the names of all settings associated with *token*.

## *settings*.get(*token*,*name*,*stg*)
Returns the recorded value of the setting *name* associated with *token*. Output format depends on the settings content, see *"settings.set"* below for more info. If no setting is found or there is an error, a blank string is returned.

*NOTE:* Value strings that are numeric-only or are "true" or "false* in any case will be returned in the wrong format. To return in absolute string format, set the *stg* to true - if it's omitted, false is assumed.

## *settings*.set(*token*,*name*,*value*)
Adds or updates the setting *name* associated with *token* to the specified *value*. Accepted value formats are string, integer or boolean.

*NOTE:* Value strings that are numeric-only or are "true" or "false* in any case will be returned in the wrong format. To learn more, see above *get* function.

## *settings*.unset(*token*,*name*)
Deletes the setting *name* associated with *token* and returns a boolean based on success.

## *tfile*.getPath(*tkn*)
Returns path to a temporary file which can be accessed directly by the script, if required.

## *tfile*.readLines(*tkn*,*pttrn*)
Reads all lines contained in the temporary file contained for *token* - unless *pttrn* is specified, in which case lines containing that search pattern will be return. Both returns are in string format.

NOTES: Newline escape chars (i.e. "\n") aren't included in the results.

## *tfile*.writeLines(*tkn*,*lines*)
Takes the table *lines* and writes them one-by-one as individual lines to the provided temp file.

NOTES: Newline escape chars (i.e. "\n") don't need to be incuded in this argument, but can be handled if they are.

## *tfile*.append(*tkn*,*lines*):
Appends *line* to temporary file associated with *tkn*.

NOTES: Newline escape chars (i.e. "\n") don't need to be incuded in this argument, but can be handled if they are.

# Troubleshooting
## Many functions are always failing
The log and setting modules require *"/usr/share/stech/api"* to exist and be accessible to all users in order to function correctly. Without access to it, those modules won't work.
## The library won't work on my version of Python
We haven't tested the library on different versions of Python and thus don't know what versions it supports for definite. It was written in Python 3.7, where it worked to our original expectations, given it's pre-release status.
## My token is showing as invalid but it meets the specified criteria
Tokens that are found in the blacklist file for the library are rejected as invalid, even if they meet the criteria.
## I installed the module through pip but it's not available. What happened?
Pip installs it's installed modules to the version of python from which it was installed. By default in Ubuntu, this will be Python2.4 and won't work. Please follow the installation instructions as above to install properly.
## If you experience any other errors, feel free to open a pull request or contact us and let us know what the issue is. We appreciate any help.
*Up-to-date links for contacting us:* <https://startechnology.uk/>, <startechsheffield@gmx.com>

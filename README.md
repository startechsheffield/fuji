# FUJI Python Module

This is a simple module made to help make common tasks easier, and is not necessarily made to introduce any new features. Maintained by Star Technology in the UK. This module WILL NOT work on any platform except Linux.

This module is part of the Project FUJI initiative from Star Technology, and is a dependency of all software developed under that initiative. For more information please visit <https://www.startechsheffield.wixsite.com/fuji>.

Testing has not yet been completed, and not all python versons have been tested. These are the versions we absolutely know work:
- Python 3.6
- Python 3.7
- Python 3.8

We don't support Python 2.x, but it can potentially be installed manually although this is not recommended. We are not responsible for instability while running using Python 2.x.

__Compatability is not guaranteed with any unlisted versions!__

*NOTE: This module is newly released. Stability is not yet guaranteed and more features are planned in updates.*

# General Info
## Identifier tokens (aka tokens)
Identifier tokens (often referred to as just "tokens") are a feature that enable *blacklisting*. In the future, they may also enable other features like *telemetry* or *ratelimiting*. Tokens listed in the blacklist file (see below) will be listed as invalid when checked, unless the *include* argument is set to true - thus the log module won't accept it.

Tokens should be hard-coded into scripts and should be human-readable as there main purpose is to identify the writing script of a log entry to the user when the log is read. 

Token criteria are as follows:

 - 4-16 char length
 - chars a-z (any case), 0-9, "-" (Hyphen), "_" (Underscore) and "." (Full stop) only

## File structure
The logfile is available for direct reading at *"/usr/share/fuji/api/log.txt"*, if required.
The blacklist file is located at *"/usr/share/fuji/api/blacklist.txt"*.
Registry files containing settings are available at *"/usr/share/fuji/api/reg_token.txt"*, where *token* is the string format of the identifier.
Temporary files without persistance are stored at *"/tmp/tfile-token.txt"*, where *token* is the string format of the identifier.

## Temporary files
Temporary files __without persistance__ are handled by the system - on most systems, this means they're deleted at boot or upon elapse of a certain duration.
Temporary files __with persistance__ are only limited via this module - In most cases where persistence is required, utilising *settings* directly is more advisable. These files can be written or appended without issue but will be deleted after reading for space saving reasons.

*NOTE: "persistence" in this context refers to the ability to remain for extended periods, across reboots, etc.*

To enable persistence, you'll need to use the Python3 interperter directly:
 1. Run `$ python3` to access the interpreter
 2. Type `from fuji import settings` and press enter
 3. Type `settings.set("fuji-tfile","persist",True)` and press enter
 4. You should see "True" appear in the command line
 5. Finally, type `exit()` and press enter one last time

# Installation via PyPI

Pre-requisites:
- Python 3.x must be installed - python 2.x is not supported. To check your version run `$ ls /usr/bin | grep python`
- If you see *"python3.x"*, you have Python3 installed.
- If you only have python 2.x, install Python3. We recommend 3.8 - to get this in Ubuntu, `$ apt install python3.8`
- Install *python3-pip*, in Ubuntu run `$ apt install python3-pip`

To install this module via PyPI, once the pre-requisites are satisfied, run the following commands in a terminal:
 1. `$ sudo pip3 install fuji` *NOTE: "sudo" is vital in this command because we need to work with system files for a successful installation!*
 2. `$ sudo python3 -m fuji`*NOTE: Again, "sudo" is needed here. The function won't proceed without it.*
 3. Installation complete!

__NOTE: If `$ python3 ...` command fails with error "Command not found" or "setuptools: module not found", see Troubleshooting below.__

# Manual installation

*__BEFORE YOU CONTINUE:__ Manual installation is NOT recommended! We are not responsible for any issues or instability that arise as a result of improper installation or unsupport Python versions!*

To install manually, take the following steps:
 1. Discover your Python version:
  - In a command line, run `"$ python3"`
  - Run `from sys import version`
  - Run `print(version)`
  - You'll see `python 3.x.x ...` REMEMBER that 3.x.x version number!
  - Quit the interpreter with `exit()`
 2. Download the latest release tarball (".tar.gz" file)
 3. Extract it in a command line:
  - Set `$ tarfile="/path/to.your/tarball"`
  - Run `$ cd $tarfile`
  - Run `$ tar -xf $tarfile/fuji-release-x.x.x.tar.gz` (*NOTE: You can press tab after typing "fuji-" for autofill*)
 4. OR, right-click -> Extract Here on GUI
 5. Run `$ mkdir /usr/share/fuji`
 6. Run `$ cp ./YOUR-EXTRACTED-DIRECTORY/LICENSE.txt /usr/share/fuji/`
 7. Run `$ cp -r /PATH/TO/YOUR-EXTRACTED-DIRECTORY/fuji /usr/lib/pythonYOUR-VERSION-NUMBER`
 8. Finally, run `$ python3 -m fuji` to complete the setup

# Functions
A general breakdown of the functions available.

*NOTE: As a rule, if a function fails due to processing problems or bad arguments, a function will return the following values:*

 - If a boolean is returned when successful, False will be returned if failed
 - If a string is returned when successful, a blank string (i.e. "") will be returned if failed
 - If a list is returned when successful, a blank list (i.e. []) will be returned if failed

Unless otherwise stated - this is to help enable clean error-handling in scripts.

## checkToken(*token*,*include*)
Checks if an identifier *token* will meet the criteria for the log and settings modules, and returns a boolean. Inclusion of blacklisted tokens is set by *include* argument. If it's not passed, it assumes False.

## getVersion()
Returns a string of the current module version.

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

*NOTE: This function WILL fail unless run by a root user for file permission and ownership reasons.*

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
Reads all lines contained in the temporary file contained for *token* - unless *pttrn* is specified, in which case lines containing that search pattern will be returned. Both returns are in string format.

NOTES: Newline escape chars (i.e. "\n") aren't included in the results. This function will delete persistant files for space-saving reasons.

## *tfile*.writeLines(*tkn*,*lines*)
Takes the list *lines* and writes them one-by-one as individual lines to the provided temp file.

NOTES: Newline escape chars (i.e. "\n") don't need to be incuded in this argument, but can be handled if they are.

## *tfile*.append(*tkn*,*lines*):
Appends *line* to temporary file associated with *tkn*.

*NOTES: Newline escape chars (i.e. "\n") don't need to be incuded in this argument, but can be handled if they are.*

# Troubleshooting

## Many functions are always failing
The log and setting modules require *"/usr/share/stech/api"* to exist and be accessible to all users in order to function correctly. Without access to it, those modules won't work.

## The module won't work on my version of Python
Our module was written in Python3, and does not (and WILL not) officially support any version of Python2. Given it's newly-released status, tests are not yet completed. Python 3 versions that are known to work are listed at the head of this document.

Pip won't install the module to a Python2.x installation, but it can be downloaded manually and files setup can be forced by using the "-f" or "--force" flags if required. In this case, we aren't responsible for any instability.

## My token is showing as invalid but it meets the specified criteria
Tokens that are found in the blacklist file for the module are rejected as invalid, even if they meet the criteria.

## I installed the module through pip but it's not available. What happened?
Pip installs it's installed modules to the version of python from which it was installed. By default in Ubuntu, this will be Python2.4 and won't work. Please make sure to use Pip3 to install, not simply "Pip".

*NOTE: This should no longer occur as we've added config to our Pip manifest that sets the minimum Python version to 3.0 or higher.*

## I run *`$ python3`* as instructed but get error "Command not found" (or similar)
In some Linux versions, Python3 is not set by default. If this is the case for your distribution, there are some additional steps you'll need to take (*without these, no software from Project FUJI will function, not just the module!*):
 1. Run `$ ls /usr/bin | grep python3`
 2. You SHOULD see a list of commands, e.g. *python3.6*, if not install a python3 version as instructed above
 3. Run `$ ln -s /usr/bin/python3.x /usr/bin/python3` where "*python3.x"* is your version of python found in the previous command. If you saw mutiple versions, you can choose any you like, however generally the highest installed version is recommeded for compatibility reasons.
 
 ## You may experience the error "setuptools: Module not found" when installing via pip:
 To fix this, run command `$ apt install python3-setuptools` in Ubuntu.

## If you experience any other errors, feel free to open a pull request or contact us and let us know what the issue is. We appreciate any help.

*Up-to-date links for contacting us:* <https://startechnology.uk/>, <startechsheffield@gmx.com>

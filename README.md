#### SUMMARY

cheetah.py was created to help facilitate the debugging of customer issues by parsing the Agent and Agent Error logs. Rather than searching piecemeal through the log files cheetah should privide you with compartmentalized lists of important items. 

Why cheetah? Because it's faster than doing it manually (hopefully).

#### DETAILS

- Tested using Python 2.7.5
- Collections module
- Was created with the intention of making Agent and Agent_Error log files easier to parse.

#### USAGE:

```
python cheetah.py <filename>
```

#### Sample OUTPUT:

```
======================================
==Printing Analysis...
======================================

======================================
==Total Message Counts
======================================
Total Assertions: 3
Total Errors: 	  1
Total Failures:   7
Total Info: 	 65
Total Warnings:  31
Total Local Node:  24
Total Remote Node: 9

======================================
==Message Details
======================================
ASSERTIONS:
#Lists all ASSERTIONS, in order.

ERRORS:
#Lists all ERROR messages.

FAILURES:
#Lists all FAILURE messages.

INFO:
#Lists the last 10 INFO messages 

WARNING:
#Lists the last 10 WARNING messages.

NODELIST:
#Lists all of the Local and Remot node messages, in order. Useful for creating a timeline of when TEs and SMs joined and left the database.
```

----------
#### migrate_scripts.zip

### Summary:
    script to migrate a NuoDB or non-NuoDB database to a NuoDB database.
    Unzip to a directory
    Edit the env file for the correct env you are running (see read_me.txt file)
    run the migrate script (shell or bat), passing the correct parameter (see the read_me.txt file)

----------

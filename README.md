xchat-social-net-graph
======================

XChat social network graphing plugin

Requires
--------
Python requirements:
 - networkx
 - numpy
 - matplotlib

These can be installed with 'pip install <library>'. Additionally, you will need GTK or wxwidgets or Qt linked against matplotlib for the grapher to work. A normal install of matplotlib will likely have this already.

 Xchat requirements:
 - python.so Python scripting interface

Installing
----------
Load the plugin in xchat.

Bugs
----
Matplotlib/numpy is broken under XChat's python.so

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
Load the 'soc_net_xc_plugin.py' plugin in xchat. By default it will create an edgefile in /tmp/soc_net.txt and update that file as chatters start mentioning each others' nicks.
Use 'python draw_map.py' to display a graph.

Caveats
----
Weights aren't yet implemented.

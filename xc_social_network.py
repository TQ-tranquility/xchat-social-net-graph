import xchat
import re
import networkx as nx
import matplotlib.pyplot as plt

__module_name__ = "TQ Social Network Map" 
__module_version__ = "0.1" 
__module_description__ = "Graph a channel's social network"
__module_author__ = "tranquility"

print "loaded %s" % __module_name__

# Populate users[] with nicks
v = []
users = []
c = xchat.find_context(channel="#test_1")
v = c.get_list("users")
for a in range(0, len(v)):
	users.append(v[a].nick)
# Build graph
G = nx.MultiDiGraph()

def priv_cb(word, word_eol, userdata):
	temp = []
	temp2 = []
	# Populate temp list with stripped words 
	for b in range(3, len(word)):
		temp.append(word[b].strip(':.?,!;'))
	for d in range(0, len(temp)):
		temp2.append(temp[d].replace("'s", ""))
	temp = temp2
	# scan temp list for nicks
	intersection = []
	intersection = list(set(temp) & set(users))
	# if there's a nick mentioned
	if len(intersection) > 0:
		m = re.search(':(\S+)!.*', word[0])
		sayer = m.group(1)
		for e in range(0, len(intersection)):
			G.add_edge(sayer, intersection[e])
		# debug info:
		#print sayer, ' mentioned ', intersection
	return xchat.EAT_NONE

def makeplot():
	print "Drawing map..."
	pos = nx.spring_layout(G)
	nx.draw(G, pos, node_size=100, alpha=0.2, edge_color='b', font_size=11, linewidths=0, width=2)
	plt.show()
	return xchat.EAT_ALL

def unload_cb(userdata): 
	print "unloaded %s" % __module_name__

xchat.hook_server("PRIVMSG", priv_cb)
xchat.hook_command("GRAPH", makeplot, help="/GRAPH draws a socia network map")
xchat.hook_unload(unload_cb) 

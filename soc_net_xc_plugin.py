import xchat
import re
import networkx as nx
import os.path

## Config info

output_location = "/tmp/soc_net.txt"

## End of config info

__module_name__ = "TQ Social Network Map" 
__module_version__ = "0.1" 
__module_description__ = "Graph a channel's social network"
__module_author__ = "tranquility"

print "loaded %s" % __module_name__

# Populate users[] with nicks
v = []
users = []
c = xchat.find_context(channel="#lobby")
v = c.get_list("users")
for a in range(0, len(v)):
	users.append(v[a].nick)
# Build graph
G = nx.MultiDiGraph()
if os.path.isfile(output_location) == True:
	G = nx.read_edgelist(output_location, delimiter=',', data=False)

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
		nx.write_edgelist(G, output_location, delimiter=',', data = False)
		# uncomment for debug info:
		#print sayer, ' mentioned ', intersection
	return xchat.EAT_NONE

def unload_cb(userdata): 
	print "unloaded %s" % __module_name__

xchat.hook_server("PRIVMSG", priv_cb)
xchat.hook_unload(unload_cb) 

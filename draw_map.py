import networkx as nx
import matplotlib.pyplot as plt

## Config info

output_location = "/tmp/soc_net.txt"

## End of config info

G = nx.read_edgelist(output_location, delimiter=',', data=False)
pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=100, alpha=0.2, edge_color='b', font_size=11, linewidths=0, width=2)
plt.show()

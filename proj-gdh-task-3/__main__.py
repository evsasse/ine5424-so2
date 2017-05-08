from string import ascii_lowercase

from node import Node
from gateway import Gateway

# N should be at least 3
N = 5
node_names = ascii_lowercase[:N-1]

gateway = Gateway('G', None)

nodes = [Node(node_names[0], None, gateway)]
for name in node_names[1:]:
    nodes.append(Node(name, nodes[-1], gateway))

nodes[0].next_node = nodes
gateway.all_nodes = nodes

nodes[-1].stage_1([])

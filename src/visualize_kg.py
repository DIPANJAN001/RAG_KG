from pyvis.network import Network


def plot_kg(index):
    g = index.get_networkx_graph()

    # Create a pyvis network
    net = Network(notebook=True,cdn_resources='remote',directed=True)

    # Add nodes and edges to the network
    net.from_nx(g)

    # Save the graph to an HTML file
    net.save_graph("Naruto.html")
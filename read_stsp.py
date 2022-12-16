import sys
import numpy as np

def read_header(fd):
    "Parse a .tsp file and return a dictionary with header data."

    converters = {'NAME': str, 'TYPE': str, 'COMMENT': str, 'DIMENSION': int,
                  'EDGE_WEIGHT_TYPE': str, 'EDGE_WEIGHT_FORMAT': str,
                  'EDGE_DATA_FORMAT': str, 'NODE_COORD_TYPE': str,
                  'DISPLAY_DATA_TYPE': str}
    sections = converters.keys()
    header = {}

    # Initialize header.
    for section in sections:
        header[section] = None

    fd.seek(0)
    for line in fd:
        data = line.split(':')
        firstword = data[0].strip()
        if firstword in sections:
            header[firstword] = converters[firstword](data[1].strip())

    return header


def read_nodes(header, fd):
    """
    Parse a .tsp file and return a dictionary of nodes, of the form
    {id:(x,y)}. If node coordinates are not given, an empty dictionary is
    returned. The actual number of nodes is in header['DIMENSION'].
    """

    nodes = {}

    node_coord_type = header['NODE_COORD_TYPE']
    display_data_type = header['DISPLAY_DATA_TYPE']
    if node_coord_type not in ['TWOD_COORDS', 'THREED_COORDS'] and \
            display_data_type not in ['COORDS_DISPLAY', 'TWOD_DISPLAY']:
        # Node coordinates are not given.
        dim=header['DIMENSION']
        for j in range(dim):
            nodes[j]=(float(j+1),float(j+1))
        return nodes
    

    dim = header['DIMENSION']
    fd.seek(0)
    k = 0
    display_data_section = False
    node_coord_section = False

    for line in fd:
        if line.strip() == "DISPLAY_DATA_SECTION":
            display_data_section = True
            continue
        elif line.strip() == "NODE_COORD_SECTION":
            node_coord_section = True
            continue

        if display_data_section:
            data = line.strip().split()
            nodes[ int(data[0])-1 ] = tuple(map(float,data[1:]))
            k += 1
            if k >= dim: break
            continue

        elif node_coord_section:
            data = line.strip().split()
            nodes[ int(data[0])-1 ] = tuple(map(float,data[1:]))
            k += 1
            if k >= dim: break
            continue

    return nodes


def read_edges(header, fd):
    "Parse a .tsp file and return the collection of edges as a Python set."

    edges = set()
    edge_weight_format = header['EDGE_WEIGHT_FORMAT']
    known_edge_weight_formats = ['FULL_MATRIX', 'UPPER_ROW', 'LOWER_ROW',
                                 'UPPER_DIAG_ROW', 'LOWER_DIAG_ROW',
                                 'UPPER_COL', 'LOWER_COL', 'UPPER_DIAG_COL',
                                 'LOWER_DIAG_COL']
    if edge_weight_format not in known_edge_weight_formats:
        return edges

    dim = header['DIMENSION']

    def n_nodes_to_read(n):
        format = edge_weight_format
        if format == 'FULL_MATRIX':
            return dim
        if format == 'UPPER_ROW' or format == 'LOWER_ROW' or \
                format == 'UPPER_COL' or format == 'LOWER_COL':
            return dim-n-1
        if format == 'UPPER_DIAG_ROW' or format == 'LOWER_DIAG_ROW' or \
                format == 'UPPER_DIAG_COL' or format == 'LOWER_DIAG_COL':
            return dim-n

    fd.seek(0)
    edge_weight_section = False
    line_completed = True
    k = 0
    n_edges = 0
    i = 0
    n_to_read = n_nodes_to_read(k)
    n_lines = n_to_read

    for line in fd:
        if line.strip() == "EDGE_WEIGHT_SECTION":
            edge_weight_section = True
            continue

        if edge_weight_section:
            data = line.strip().split()
            n_data = len(data)

            start = 0

            while n_data > 0:

                # Number of items that we read on this line
                # for the current node.
                n_on_this_line = min(n_to_read, n_data)
                # Read edges.
                #In this part we need to add "float(data[j]" as third part of "edge" 
                #to consider the weights
                for j in xrange(start,start+n_on_this_line):
                    n_edges += 1
                    if edge_weight_format in ['UPPER_ROW', 'LOWER_COL']:
                        edge = (k,i+k+1,float(data[j]))
                    elif edge_weight_format in ['UPPER_DIAG_ROW', 'LOWER_DIAG_COL']:
                        edge = (k,i+k,float(data[j]))
                    elif edge_weight_format in ['UPPER_COL', 'LOWER_ROW']:
                        edge = (i+k+1,k,float(data[j]))
                    elif edge_weight_format in ['UPPER_DIAG_COL', 'LOWER_DIAG_ROW']:
                        edge = (i+k,k,float(data[j]))
                    elif edge_weight_format == 'FULL_MATRIX':
                        edge = (k,i,float(data[j]))
                    edges.add(edge)
                    i += 1
                # Update number of items remaining to be read.
                n_to_read -= n_on_this_line
                n_data -= n_on_this_line

                if n_to_read == 0:
                    start = n_on_this_line
                    k += 1
                    i = 0
                    n_to_read = n_nodes_to_read(k)

            if k >= n_lines: break
            continue

    #print 'Read %d edges' % n_edges
    return edges


def plot_graph(nodes, graph_edges=None, mst_edges=None):
    """
    Plot the graph represented by `nodes` and `edges` using Matplotlib.
    Very basic for now.
    """

    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot nodes.
    x = [node[0] for node in nodes.values()]
    y = [node[1] for node in nodes.values()]
    plt.scatter(x,y,s=70,c='g',antialiased=True)

    # Plot graph edges.
    if graph_edges is not None:
        
        edge_pos=np.asarray([(nodes[e[0]],nodes[e[1]]) for e in graph_edges])
        edge_collection = LineCollection(edge_pos,linewidth=2,antialiased=True,colors='y')
        ax.add_collection(edge_collection)
    
    # plot mst edges.
    if mst_edges is not None:
        edge_pos=np.asarray([(nodes[e[0]],nodes[e[1]]) for e in mst_edges])
        edge_collection = LineCollection(edge_pos,label='Minimum Tree',\
                                         linewidth=1,antialiased=True,colors='b')
        ax.add_collection(edge_collection)
    ax.legend(loc='upper left')
    
    plt.show()
    return ax


if __name__=="__main__":

    import sys

    finstance = 'test2.tsp'#sys.argv[1]

    with open(finstance,"r") as fd:

        header = read_header(fd)
        print 'Header: ', header
        dim = header['DIMENSION']

        print "Reading nodes"
        nodes = read_nodes(header, fd)
        print nodes

        print "Reading edges"
        edges = read_edges(header,fd)
        print edges

    if len(nodes) > 0:
        plot_graph(nodes, edges)

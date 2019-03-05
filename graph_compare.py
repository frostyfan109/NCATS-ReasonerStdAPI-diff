import networkx as nx
class GraphComparator:    
    def get_network (self, kg):
        """ Answer to networkx. """
        nodes = kg['nodes']
        edges = kg['edges']
        g = nx.MultiDiGraph()
        for n in nodes:
            #print (n['id'])
            g.add_node(n['id'], attr_dict=n)
        for e in edges:
            #print (e['id'])
            g.add_edge (e['source_id'], e['target_id'], attr_dict=e)
        return g
    def diff_graphs (self, g1, g2):
        """ Diff nx graphs. """
        g1_copy = g1.copy ()
        g1_copy.remove_nodes_from(n for n in g1 if not n in g2)
        g2_copy = g2.copy ()
        g2_copy.remove_nodes_from(n for n in g2 if not n in g1)

        g1_minus_g2 = nx.difference (g1_copy, g2_copy)
        self.print_graph (g1_minus_g2)
        return g1_minus_g2
    def print_graph (self, g):
        for n in g.nodes (data=True):
            print (f"--n--> {n}")
        for e in g.edges (data=True):
            print (f"---e-> {e}")

    def get_diff_edges_with_data (self, graph_diff, orig_graph):
        """ This needs help. Maybe we can only say the endpoints of the nodes if difference does not return data. """
        graph_diff_edge_map = {
            f"e['source_id']-e['target_id']" : e for e in graph_diff.edges (data=True)
        }
        return [ e[2]['attr_dict'] for e in orig_graph.edges (data=True) if f"e['source_id']-e['target_id']" in graph_diff_edge_map ]

    def compare (self, request):
        answer1 = request.json['answer_1']
        answer2 = request.json['answer_2']
        g1 = self.get_network (answer1['knowledge_graph'])
        g2 = self.get_network (answer2['knowledge_graph'])

        g1_g2 = self.diff_graphs (g1, g2)
        g2_g1 = self.diff_graphs (g2, g1)
        self.print_graph (g2_g1)
        return {
                "g1-g2" : {
                    """ Looks like we an know whether there is an edge but it's unclear if we can distinguish edges. """
                    "edges" : [ e for e in g1_g2.edges () ] #self.get_diff_edges_with_data (g1_g2, g1)
                },
                "g2-g1" : {
                    "edges" : [ e for e in g2_g1.edges () ] #self.get_diff_edges_with_data (g2_g1, g2)
                },
                "intersection" : {
                    "nodes" : [ ],
                    "edges" : [ ]
                }
            }

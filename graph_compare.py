import json
import networkx as nx
import sys
import traceback

class GraphComparator:
    """ Compare knowledge graphs. """

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
    
    def diff_graphs0 (self, g1, g2):
        """ Diff nx graphs. """
        g1_copy = g1.copy ()
        g1_copy.remove_nodes_from(n for n in g1 if not n in g2)
        g2_copy = g2.copy ()
        g2_copy.remove_nodes_from(n for n in g2 if not n in g1)

        g1_minus_g2 = nx.difference (g1_copy, g2_copy)
        #self.print_graph (g1_minus_g2)
        return g1_minus_g2

    def diff_graphs (self, g1, g2):
        """ Diff nx graphs. """
        g1_copy_2 = g1.copy ()
        edges_to_delete = []
        #print (f"0. edges in g1_copy_2: {len(list(g1_copy_2.edges ()))}")
        for e in g1_copy_2.edges(data=True, keys=True):
            source = e[0]
            target = e[1]
            """ e is a node in g1 matching the missing node's source and target. """
            for g2e in g2.edges (data=True, keys=True):
                g2source = g2e[0]
                g2target = g2e[1]
                found = False
                if source == g2source and target == g2target:
                    if self.edge_equals (e[3]['attr_dict'], g2e[3]['attr_dict']):
                        """ g2 contains this edge. """
                        edges_to_delete.append (e)
                        found = True
                    else:
                        '''
                        print (f"========================================")
                        print (f"e in g1: {json.dumps(e[3]['attr_dict'], indent=2)}")
                        print (f"g2e in g2: {json.dumps(g2e[3]['attr_dict'], indent=2)}")
                        print (f"========================================")
                        '''
                        pass                    
        for de in edges_to_delete:
            try:
                g1_copy_2.remove_edge (de[0], de[1], key=de[2])
            except:
                print ("exception deleting edge")
                pass
        #print (f"1. edges in g1_copy_2: {len(list(g1_copy_2.edges ()))}")
                   
        return g1_copy_2
    
    def edge_equals0 (self, e1, e2):
        fields = [ "source_id", "target_id", "edge_source", "relation", "type" ]
        return all([ field in e1 and field in e2 and e1[field] == e2[field] for field in fields ])
            
    def edge_equals (self, e1, e2):
        equal = True
        #fields = [ "source_id", "target_id", "type", "edge_source", "source_database" ]
        fields = [ "source_id", "target_id", "type", "source_database" ]
        for f in fields:
            if not (f in e1 and f in e2 and e1[f] == e2[f]):
                #print (f"7777777>>>>>>>>>    {f}    bad")
                equal = False
                break
        return equal
            
    def intersect (self, g1, g2):        
        g1_copy = g1.copy ()
        g1_copy.remove_nodes_from(n for n in g1 if not n in g2)
        intersection = nx.MultiDiGraph ()
        try:
            intersection = nx.intersection (g1_copy, g2)
        except:
            traceback.print_exc ()
        g1_copy_2 = g1.copy ()
        g1_copy_2.remove_nodes_from(n for n in g1 if not n in intersection)
        return g1_copy_2
    
    def print_graph (self, g):
        """ Print graph. """
        for n in g.nodes (data=True):
            pass #print (f"--n--> {n}")
        for e in g.edges (data=True):
            pass #print (f"---e-> {e}")

    def compare (self, answer1, answer2):
        """ Compare graphs from a request. """
        g1 = self.get_network (answer1['knowledge_graph'])
        g2 = self.get_network (answer2['knowledge_graph'])
        g1_g2 = self.diff_graphs (g1, g2)
        g2_g1 = self.diff_graphs (g2, g1)
        intersection = self.intersect (g1, g2)
        return {
            "g1-g2" : {
                "edges" : [ e[2]['attr_dict'] for e in g1_g2.edges (data=True) ],
		"nodes" : [ n[1]['attr_dict'] for n in g1_g2.nodes(data=True)]
            },
            "g2-g1" : {
                "edges" : [ e[2]['attr_dict'] for e in g2_g1.edges (data=True) ],
		"nodes" : [ n[1]['attr_dict'] for n in g2_g1.nodes(data=True) ]
            },
            "intersection" : {
                "nodes" : [ n[1]['attr_dict'] for n in intersection.nodes (data=True) if 'attr_dict' in n[1] ],
                "edges" : [ e[2]['attr_dict'] for e in intersection.edges (data=True) ]
            }
        }

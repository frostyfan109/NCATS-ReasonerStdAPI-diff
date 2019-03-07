# Point of this script is to ingest two 0.9.0 spec outputs and perform comparisons between them
import json
import networkx as nx
import os
import requests

class NodeDiff():
    def __init__(self, input1 = None, input2 = None):
        self.input1 = input1
        self.input2 = input2
        self.node_dict1 = None
        self.node_dict2 = None

    def populate(self, fid1, fid2):
        """
        Populate the class with the json info
        :param fid1: file stream for first json object
        :param fid2: file stream for the other json object
        :return: None
        """
        self.input1 = json.load(fid1)
        self.input2 = json.load(fid2)

    def make_node_dict(self):
        """
        Creates a dictonary of nodes listed by currie id from answers 1 and 2
        """
        if self.input1 is None or self.input2 is None:
            raise Exception("Missing input: please run the populate() method first")
        self.node_dict1 = {}
        for node in self.input1['knowledge_graph']['nodes']:
            self.node_dict1[node['id']] = node
        self.node_dict2 = {}
        for node in self.input2['knowledge_graph']['nodes']:
            self.node_dict2[node['id']] = node

    def node_diff(self):
        """
        Runs through all of the nodes in the json responses
            storing the intersection and set differences into a
            dictonary organized by tuples of node ids or the
            tuple (-1, -1) for all nodes.
        NOTE: This assumes that nodes in answers hve been 
            preprosessed to have the same curie ids when synonyms.
        """
        if self.input1 is None or self.input2 is None:
            raise Exception("Missing input: please run the populate() method first")
        if self.node_dict1 is None or self.node_dict2 is None:
            self.make_node_dict()
        # Initialize dictonaries to keep track of the nodes in respnse 1 and response 2
        g1={}
        g2={}
        # Set to keep track of the union of all curie ids
        curie_set = set()
        for curie in self.node_dict1.keys():
            g1[curie] = {}
            # intersection is only in the g1 dictionary
            g1[curie]['intersection'] = set()
            # node section keeps track of node ids associated with each node i.e. "n0"
            g1[curie]['node'] = set()
            curie_set.add(curie)
        for curie in self.node_dict2.keys():
            g2[curie] = {}
            # node section keeps track of node ids associated with each node i.e. "n0"
            g2[curie]['node'] = set()
            curie_set.add(curie)
        node_names1 = []
        node_names2 = []

        # extract all node ids (i.e. "n0","n1",ect...)
        if len(self.input1['question_graph']['nodes'])>0:
            if 'id' in self.input1['question_graph']['nodes'][0]:
                node_names1 = [x['id'] for x in self.input1['question_graph']['nodes']]
            elif 'node_id' in self.input1['question_graph']['nodes'][0]:
                node_names1 = [x['node_id'] for x in self.input1['question_graph']['nodes']]
        if len(self.input2['question_graph']['nodes'])>0:
            if 'id' in self.input2['question_graph']['nodes'][0]:
                node_names2 = [x['id'] for x in self.input2['question_graph']['nodes']]
            elif 'node_id' in self.input2['question_graph']['nodes'][0]:
                node_names2 = [x['node_id'] for x in self.input2['question_graph']['nodes']]
        
        # initialize the result dictonary
        diff_dict = {}
        diff_dict["-1|-1"] = {'intersection':[],'g1-g2':[],'g2-g1':[]}
        # initialize node id tuple keys
        for id1 in node_names1:
            for id2 in node_names2:
                diff_dict[id1+"|"+id2] = {'intersection':[],'g1-g2':[],'g2-g1':[]}
        # iterate through answers
        for answer1 in self.input1['answers']:
            for answer2 in self.input2['answers']:
                for id1 in answer1['node_bindings'].keys():
                    # This is to handle cases where answer node id has a list or a string
                    if isinstance(answer1['node_bindings'][id1], str):
                        bindings1 = [answer1['node_bindings'][id1]]
                    elif isinstance(answer1['node_bindings'][id1], list):
                        bindings1 = answer1['node_bindings'][id1]
                    for curie1 in bindings1:
                        # store node id
                        g1[curie1]['node'].add(id1)
                        for id2 in answer2['node_bindings'].keys():
                            # This is to handle cases where answer node id has a list or a string
                            if isinstance(answer2['node_bindings'][id2], str):
                                bindings2 = [answer2['node_bindings'][id2]]
                            elif isinstance(answer2['node_bindings'][id2], list):
                                bindings2 = answer2['node_bindings'][id2]
                            for curie2 in bindings2:
                                # store node id
                                g2[curie2]['node'].add(id2)
                                if curie1 == curie2:
                                    # stor intersection tuple
                                    g1[curie1]['intersection'].add(id1+"|"+id2)
        # iterate through all curies
        for curie in curie_set:
            # check if curie is from answer 1
            if curie in g1.keys():
                # check if in intersection
                if len(g1[curie]['intersection'])>0:
                    diff_dict["-1|-1"]['intersection'] += [self.node_dict1[curie]]
                    for id1 in node_names1:
                        for id2 in node_names2:
                            node_tuple = id1+"|"+id2
                            if id1 in g1[curie]['node'] and id2 in g2[curie]['node']:
                                diff_dict[node_tuple]['intersection'] += [self.node_dict1[curie]]
                            elif id1 in g1[curie]['node']:
                                diff_dict[node_tuple]['g1-g2'] += [self.node_dict1[curie]]
                            elif id2 in g2[curie]['node']:
                                diff_dict[node_tuple]['g2-g1'] += [self.node_dict1[curie]]
                # If not in intersection store in g1-g2
                else:
                    diff_dict["-1|-1"]['g1-g2'] += [self.node_dict1[curie]]
                    for id1 in g1[curie]['node']:
                        # iterate through all answer 2 ids
                        for id2 in node_names2:
                            diff_dict[id1+"|"+id2]['g1-g2'] += [self.node_dict1[curie]]
            # if not in g1 but in g2 then in g2-g1
            elif curie in g2.keys():
                diff_dict["-1|-1"]['g2-g1'] += [self.node_dict2[curie]]
                for id2 in g2[curie]['node']:
                    # iterate through all answer 1 ids
                    for id1 in node_names1:
                        diff_dict[id1+"|"+id2]['g2-g1'] += [self.node_dict2[curie]]
        return diff_dict


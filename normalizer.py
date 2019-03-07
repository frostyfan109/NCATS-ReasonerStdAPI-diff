import json
import requests

class Normalizer:
    def normalize (self, graph):
        '''
        print (json.dumps(graph, indent=2))
        if not 'question_graph' in graph:
            graph['question_graph'] = {
                "nodes" : [],
                "edges" : []
            }
        '''
        response = requests.post('http://robokop.renci.org:6011/api/normalize/', json=graph)
        #print (f"output: {response.text}")
        return response.json ()

import json
import requests

class Normalizer:
    def normalize (self, graph):
        print (json.dumps(graph, indent=2))
        response = requests.post('http://robokop.renci.org:6011/api/normalize/', json=graph)
        print (f"output: {response.text}")
        return response.json ()
    
'''
test_answer = None
with open('test.json', 'r') as stream:
    test_answer = json.load (stream)

class R:
    def __init__(self):
        self.json = {
            'answer_1' : test_answer,
            'answer_2' : test_answer
        }
request = R ()

normalizer = Normalizer ()
answer_1 = request.json['answer_1']
answer_2 = request.json['answer_2']
answer_1_norm = normalizer.normalize (answer_1)
answer_2_norm = normalizer.normalize (answer_2)
'''

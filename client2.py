import copy
import json
import requests
import test_rtx
import test_robokop
import sys

""" copy an answer, delete a random edge. See if our differ can find the discrepancy. """
proto_rtx = copy.deepcopy(test_rtx.answer)
del proto_rtx['knowledge_graph']['edges'][-1]

proto_rtx2 = copy.deepcopy(test_rtx.answer)
del proto_rtx2['knowledge_graph']['edges'][-2]

env = sys.argv[1]
input_file_1 = sys.argv[2]
input_file_2 = sys.argv[3]
def get_obj (file_name):
    result = None
    with open(file_name, 'r') as stream:
        result = json.load (stream)
    return result

url = {
    "local" : "http://localhost:9999/compare_answers",
    "dev"   : "https://compare-kg.renci.org/compare_answers"
}
response = requests.post (
    url[env],
    json = {
        "answer_1" : get_obj(input_file_1),
        "answer_2" : get_obj(input_file_2)
    },
    headers = {
        'accept': 'application/json'
    })
print (json.dumps (response.json (), indent=2))

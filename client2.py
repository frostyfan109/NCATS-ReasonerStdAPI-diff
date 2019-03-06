import copy
import json
import requests
import test_rtx
import test_robokop

""" copy an answer, delete a random edge. See if our differ can find the discrepancy. """
proto_rtx = copy.deepcopy(test_rtx.answer)
del proto_rtx['knowledge_graph']['edges'][-1]

proto_rtx2 = copy.deepcopy(test_rtx.answer)
del proto_rtx2['knowledge_graph']['edges'][-2]

test_answer = None
with open('test.json', 'r') as stream:
    test_answer = json.load (stream)
url = "http://localhost:9999/compare_answers"
#url = "https://compare-kg.renci.org/compare_answers"
response = requests.post (
    url,
    json = {
        "answer_1" : test_answer, #2, #test_rtx.answer,
        "answer_2" : test_answer
    },
    headers = {
        'accept': 'application/json'
    })
print (json.dumps (response.json (), indent=2))

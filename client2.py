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

response = requests.post (
    "http://localhost:9999/compare_answers",
    json = {
        "answer_1" : proto_rtx2, #test_rtx.answer,
        "answer_2" : proto_rtx
    },
    headers = {
        'accept': 'application/json'
    })
print (json.dumps (response.json (), indent=2))

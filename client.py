import json
import requests
import test_rtx
import test_robokop

response = requests.post (
    "http://localhost:9999/compare_answers",
    json = {
        "answer_1" : test_rtx.answer,
        "answer_2" : test_rtx.answer #test_robokop.answer)
    },
    headers = {
        'accept': 'application/json'
    })
print (json.dumps (response.json (), indent=2))

"""
Provide a standard protocol for asking graph oriented questions of Translator data sources.
"""

import argparse
import json
import os
import yaml
import jsonschema
import requests
from graph_compare import GraphComparator
from node_diff import NodeDiff
from normalizer import Normalizer
from qmap import q_map
from flask import Flask, request, abort, Response
from flask_restful import Api, Resource
from flasgger import Swagger
from flask_cors import CORS
import networkx as nx
app = Flask(__name__)

api = Api(app)
CORS(app)

""" https://github.com/NCATS-Gamma/NCATS-ReasonerStdAPI """
filename = 'translator_interchange_0.9.0.yaml'
with open(filename, 'r') as file_obj:
    template = yaml.load(file_obj)
app.config['SWAGGER'] = {
    'title': 'Translator Answer Tools',
    'description': 'hi',
    'uiversion': 3
}
swagger = Swagger(app, template=template)

class StandardAPIResource(Resource):
    def validate (self, request):
        with open(filename, 'r') as file_obj:
            specs = yaml.load(file_obj)
        to_validate = specs["components"]["schemas"]["DiffRequest"]
        to_validate["components"] = specs["components"]
        to_validate["components"].pop("DiffRequest", None)
        try:
            jsonschema.validate(request.json, to_validate)
        except jsonschema.exceptions.ValidationError as error:
            #print (f"ERROR: {str(error)}")
            abort(Response(str(error), 400))
    def get_opt (self, request, opt):
        return request.get('option', {}).get (opt)
    
class DiffQuery(StandardAPIResource):
    """ Diff two answers. """
        
    def post(self):
        """
        compare
        ---
        tag: compare
        description: Compare two answers.
        requestBody:
            description: Input message
            required: true
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/DiffRequest'
        responses:
            '200':
                description: Success
                content:
                    text/plain:
                        schema:
                            type: string
                            example: "Successfully validated"
            '400':
                description: Malformed message
                content:
                    text/plain:
                        schema:
                            type: string
        """
        self.validate (request)
        #print (json.dumps(request.json, indent=2))
        
        normalizer = Normalizer ()
        answer_1 = request.json ['answer_1']
        answer_2 = request.json ['answer_2']

        if 'query_graph' in answer_1:
            answer_1['question_graph'] = answer_1['query_graph']
            del answer_1['query_graph']

        if 'query_graph' in answer_2:
            answer_2['question_graph'] = answer_2['query_graph']
            del answer_2['query_graph']

        if 'results' in answer_1:
            answer_1['answers'] = answer_1['results']
            del answer_1['results']

        if 'results' in answer_2:
            answer_2['answers'] = answer_2['results']
            del answer_2['results']

        if 'question_graph' not in answer_1 and 'reasoner_id' in answer_1 and 'query_type_id' in answer_1:
            if answer_1['reasoner_id'] == 'RTX' and answer_1['query_type_id'] in q_map:
                answer_1['question_graph'] = q_map[answer_1['query_type_id']]['question_graph']
                answer_1['question_graph']['nodes'][0]['curie'] = answer_1['terms'][answer_1['question_graph']['nodes'][0]['type']]

        if 'question_graph' not in answer_2 and 'reasoner_id' in answer_2 and 'query_type_id' in answer_2:
            if answer_2['reasoner_id'] == 'RTX' and answer_2['query_type_id'] in q_map:
                answer_2['question_graph'] = q_map[answer_2['query_type_id']]['question_graph']
                answer_2['question_graph']['nodes'][0]['curie'] = answer_2['terms'][answer_2['question_graph']['nodes'][0]['type']]


        answer_1_norm = normalizer.normalize (answer_1)
        answer_2_norm = normalizer.normalize (answer_2)
        
        if isinstance(answer_1_norm,str):
            raise Exception(answer_1_norm)
        if isinstance(answer_2_norm,str):
            raise Exception(answer_2_norm)

        node_diff = NodeDiff(answer_1_norm, answer_2_norm)
        graph_comparator = GraphComparator ()

        return {
            'node_diff' : node_diff.node_diff(),
            'graph_diff' : graph_comparator.compare (
                answer_1_norm,
                answer_2_norm)
        }
        
###############################################################################################
#
# Define routes.
#
###############################################################################################

api.add_resource(DiffQuery, '/compare_answers')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Diff standard responsees')
    parser.add_argument('-port', action="store", dest="port", default=9999, type=int)
    args = parser.parse_args()

    server_host = '0.0.0.0'
    server_port = args.port

    app.run(
        host=server_host,
        port=server_port,
        debug=False,
        use_reloader=True
    )

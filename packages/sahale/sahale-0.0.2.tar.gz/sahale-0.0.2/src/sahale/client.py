from __future__ import print_function

import logging

import grpc
import sahale_pb2
import sahale_pb2_grpc
import json

class Client:
    def __init__(self, app, user_id): # TODO: infer user id
        self.app = app

    def start_new_activity(self, name, request):
        endpoint = user_id + '-' + app + '-' + name + ".fly.dev" # TODO convert to all lower case and dashes only
        print("Found fly endpoint: " + endpoint) # TODO remove this later so customer can't see this
        
        with grpc.insecure_channel('localhost:50051') as channel:
        # with grpc.insecure_channel(endpoint + ':50051') as channel:
            stub = sahale_pb2_grpc.SahaleStub(channel)
            response = stub.RunActivity(sahale_pb2.Request(parameters=json.dumps(request)))
            print("response: " + response.result)

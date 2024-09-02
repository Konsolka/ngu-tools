import json

from src.serialization.deserialize_dot_net import DictQuery

class Handler:
    def __init__(self, handler:DictQuery):
        self.handler = handler

    def handle_name(self, name):
        self.handler.get(name)

    def json_print_handler(self):
        with open('output.json', 'w') as file:
            json.dump(self.handler, file, ensure_ascii=False, indent=4)
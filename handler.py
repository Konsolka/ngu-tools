from deserialize_dot_net import DictQuery

class Handler:
    def __init__(self, handler:DictQuery):
        self.handler = handler

    def handle_name(self, name):
        self.handler.get(name)
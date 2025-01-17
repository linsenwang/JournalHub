class Namespace:
    def __init__(self, path, name, url, handler):
        self.path = path
        self.name = name
        self.url = url

class Route:
    def __init__(self, path, name, url, handler, description=None):
        self.path = path
        self.name = name
        self.url = url
        self.description = description
        self.handler = handler

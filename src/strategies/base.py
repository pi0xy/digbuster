class DNSStrategy:
    def __init__(self, resolver=None):
        self.resolver = resolver

    def run(self, target):
        raise NotImplementedError("The strategy needs to implement the run() method.")
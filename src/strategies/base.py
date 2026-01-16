class DNSStrategy:
    def __init__(self, resolver=None):
        self.resolver = resolver

    def run(self, target):
        raise NotImplementedError("La stratégie doit implémenter la méthode run()")

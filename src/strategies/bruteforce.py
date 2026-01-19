import dns.resolver
from src.strategies.base import DNSStrategy


class BruteForce(DNSStrategy):
    def __init__(self, resolver=None, wordlist_path="wordlist.txt"):
        super().__init__(resolver)
        self.subdomains = self.load_wordlist(wordlist_path)


    def load_wordlist(self, path):
        with open(path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def run(self, domain):
        found = []
        for sub in self.subdomains:
            target = f"{sub}.{domain}"
            try:
                dns.resolver.resolve(target, "A")
                found.append(target)
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception):
                continue
        return found

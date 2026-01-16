import dns.resolver
from src.strategies.base import DNSStrategy


class BruteForce(DNSStrategy):
    def __init__(self, resolver=None):
        super().__init__(resolver)
        # Wordlist (to expand)
        self.subdomains = ["www", "mail", "dev", "api", "remote", "blog", "test"]

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

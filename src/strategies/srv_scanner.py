import dns.resolver
from src.strategies.base import DNSStrategy


class SRVScanner(DNSStrategy):
    def __init__(self, resolver=None):
        super().__init__(resolver)
        self.services = [
            ("_sip", "_tcp"),
            ("_ldap", "_tcp"),
            ("_xmpp-server", "_tcp"),
            ("_autodiscover", "_tcp")
        ]

    def run(self, domain):
        found = []
        for service, protocol in self.services:
            target = f"{service}.{protocol}.{domain}"
            try:
                answers = dns.resolver.resolve(target, "SRV")
                for rdata in answers:
                    host = str(rdata.target).rstrip('.')
                    found.append(host)
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception):
                continue
        return list(set(found))

import dns.resolver
from src.strategies.base import DNSStrategy


class StandardRecords(DNSStrategy):
    def __init__(self, resolver=None):
        super().__init__(resolver)
        self.record_types = ["A", "AAAA", "MX", "CNAME", "SOA", "NS"]

    def run(self, domain):
        found = []
        for record_type in self.record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                for rdata in answers:
                    if record_type == "A" or record_type == "AAAA":
                        found.append(str(rdata.address))
                    elif record_type == "MX":
                        found.append(str(rdata.exchange).rstrip('.'))
                    elif record_type in ["CNAME", "NS"]:
                        found.append(str(rdata.target).rstrip('.'))
                    elif record_type == "SOA":
                        found.append(str(rdata.mname).rstrip('.'))
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception):
                continue

        return list(set(found))



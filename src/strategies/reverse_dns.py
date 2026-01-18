import ipaddress
import dns.resolver
import dns.reversename
from src.strategies.base import DNSStrategy


class ReverseDNS(DNSStrategy):
    def run(self, ip_address):
        try:
            addr = dns.reversename.from_address(ip_address)
            answers = dns.resolver.resolve(addr, "PTR")
            return [str(rdata).rstrip('.') for rdata in answers]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception):
            return []


class IPNeighbors(DNSStrategy):
    def run(self, ip_address):
        found = []
        try:
            ip = ipaddress.ip_address(ip_address)
            found.append(str(ip - 1))
            found.append(str(ip + 1))
        except (ValueError, Exception):
            pass
        return found

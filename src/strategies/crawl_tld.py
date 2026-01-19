import ipaddress
from src.strategies.base import DNSStrategy


class CrawlTLD(DNSStrategy):

    def run(self, domain):

        try:
            ipaddress.ip_address(domain)
            return []
        except ValueError:
            pass

        parts = domain.strip('.').split('.')
        if len(parts) <= 2:
            return []

        parent_domain = ".".join(parts[1:])
        return [parent_domain]

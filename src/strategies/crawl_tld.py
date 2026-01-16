from src.strategies.base import DNSStrategy


class CrawlTLD(DNSStrategy):
    def run(self, domain):
        """
        Remonte d'un niveau dans la hiérarchie DNS.
        """
        parts = domain.strip('.').split('.')

        if len(parts) <= 2:
            return []

        parent_domain = ".".join(parts[1:])
        return [parent_domain]

import re
import dns.resolver
from src.strategies.base import DNSStrategy


class TXTParser(DNSStrategy):
    def run(self, domain):
        found = []
        targets = [domain, f"_dmarc.{domain}"]

        for target in targets:
            try:
                answers = dns.resolver.resolve(target, "TXT")
                for rdata in answers:
                    txt_content = str(rdata).strip('"')

                    found.extend(re.findall(r"include:([^\s]+)", txt_content))

                    found.extend(re.findall(r"ip4:(\d{1,3}(?:\.\d{1,3}){3})", txt_content))

                    found.extend(re.findall(r"ip6:([a-fA-F0-9:]+)", txt_content))
                    
                    found.extend(re.findall(r"@([a-zA-Z0-9.-]+\.[a-z]{2,})", txt_content))

            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception):
                continue

        return list(set(found))

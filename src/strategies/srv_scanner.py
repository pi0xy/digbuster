import dns.resolver
from src.strategies.base import DNSStrategy

class SRVScanner(DNSStrategy):
    def __init__(self, resolver=None):
        super().__init__(resolver)
        self.services = [
            ("_sip", "_tcp"), 
            ("_sip", "_udp"), 
            ("_sip", "_tls"),
            ("_ldap", "_tcp"), 
            ("_gc", "_tcp"), 
            ("_kerberos", "_tcp"),
            ("_kpasswd", "_tcp"), 
            ("_xmpp-server", "_tcp"),
            ("_xmpp-client", "_tcp"), 
            ("_jabber", "_tcp"),
            ("_autodiscover", "_tcp"), 
            ("_matrix", "_tcp"),
            ("_caldav", "_tcp"), 
            ("_carddav", "_tcp"),
            ("_http", "_tcp")
        ]

    def run(self, domain):
        import ipaddress
        try:
            ipaddress.ip_address(domain)
            return []
        except ValueError:
            pass

        found = []
        
        for service, protocol in self.services:
            target = f"{service}.{protocol}.{domain}"
            try:
                res = self.resolver if self.resolver else dns.resolver
                answers = res.resolve(target, "SRV")
                for rdata in answers:
                    host = str(rdata.target).rstrip('.')
                    found.append(host)
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, Exception):
                continue
        return list(set(found))
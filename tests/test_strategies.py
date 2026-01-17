from src.strategies.reverse_dns import ReverseDNS
from src.strategies.crawl_tld import CrawlTLD
from src.strategies.bruteforce import BruteForce
from src.strategies.srv_scanner import SRVScanner



def test_reverse_dns_logic():
    strategy = ReverseDNS()
    results = strategy.run("8.8.8.8")
    assert any("dns.google" in r for r in results)


def test_reverse_dns_invalid_ip():
    strategy = ReverseDNS()
    results = strategy.run("999.999.999.999")  # Impossible IP
    assert results == []


def test_crawl_tld_logic():
    strategy = CrawlTLD()
    assert strategy.run("sub.example.com") == ["example.com"]
    assert strategy.run("example.com") == []
    assert strategy.run("a.b.c.d.fr") == ["b.c.d.fr"]


def test_bruteforce_syntax():
    strategy = BruteForce()
    results = strategy.run("google.com")
    assert isinstance(results, list)


def test_srv_scanner_structure():
    strategy = SRVScanner()
    results = strategy.run("nonexistent.example.com")
    assert isinstance(results, list)
    assert len(results) == 0

def test_srv_scanner_integration():
    strategy = SRVScanner()
    results = strategy.run("microsoft.com")
    assert isinstance(results, list)

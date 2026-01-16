import pytest
from src.strategies.reverse_dns import ReverseDNS

def test_reverse_dns_logic():
    strategy = ReverseDNS()
    results = strategy.run("8.8.8.8")
    assert any("dns.google" in r for r in results)

def test_reverse_dns_invalid_ip():
    strategy = ReverseDNS()
    results = strategy.run("999.999.999.999") # IP impossible
    assert results == []
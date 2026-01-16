import pytest
from src.strategies.txt_parser import TXTParser


def test_txt_parser_integration():
    strategy = TXTParser()
    results = strategy.run("google.com")
    assert any("_spf.google.com" in r for r in results)
    assert isinstance(results, list)


def test_txt_parser_no_record():
    strategy = TXTParser()
    results = strategy.run("fakedomainithink.com")
    assert results == []

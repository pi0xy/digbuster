import concurrent.futures
from src.strategies.standard_records import StandardRecords
from src.strategies.reverse_dns import ReverseDNS, IPNeighbors
from src.strategies.txt_parser import TXTParser
from src.strategies.srv_scanner import SRVScanner
from src.strategies.bruteforce import BruteForce
from src.strategies.crawl_tld import CrawlTLD

class DiscoveryEngine:
    def __init__(self, depth=2):
        self.depth = depth
        self.visited = set()
        self.results = {}
        self.strategies = [
            StandardRecords(),
            ReverseDNS(),
            TXTParser(),
            SRVScanner(),
            BruteForce(),
            CrawlTLD(),
            IPNeighbors()
        ]

    def run(self, start_node):
        current_layer = {start_node}
        
        for level in range(self.depth + 1):
            print(f"[*] Scanning level {level} ({len(current_layer)} targets)...")
            next_layer = set()
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                future_to_target = {
                    executor.submit(self._scan_target, target): target 
                    for target in current_layer if target not in self.visited
                }
                
                total = len(future_to_target)
                completed = 0

                for future in concurrent.futures.as_completed(future_to_target):
                    target = future_to_target[future]
                    self.visited.add(target)

                    try:
                        new_found = future.result()
                        self.results[target] = new_found
                        next_layer.update(new_found)
                    except Exception as e:
                        print(f"[!] Error scanning {target}: {e}")

            current_layer = next_layer - self.visited
            if not current_layer:
                break
        
        return self.results

    def _scan_target(self, target):
        found_for_target = set()
        for strategy in self.strategies:
            results = strategy.run(target)
            valid_results = [r for r in results if "." in r and len(r) >= 7]
            found_for_target.update(valid_results)
        return list(found_for_target)
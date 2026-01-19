import argparse
import sys
from src.engine import DiscoveryEngine
from src.formatters.text import export_to_markdown
from src.formatters.graph import export_to_graphviz


def parse_args():

    parser = argparse.ArgumentParser(
        description="Digbuster: Discover infrastructure around a domain using only DNS."
    )

    parser.add_argument(
        "domain",
        help="The target domain name to analyse (e.g., example.com)"
    )

    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=2,
        help="Recursion depth limit (default: 2)"
    )

    parser.add_argument(
        "-o", "--output",
        choices=["text", "graph"],
        default="text",
        help="Output format (default: text)"
    )

    parser.add_argument(
        "-f", "--file",
        help="Output filename (default: report.md or map.dot)"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(f"[+] Digbuster starting on: {args.domain} (depth: {args.depth})")
    
    engine = DiscoveryEngine(depth=args.depth)
    results = engine.run(args.domain)
    
    print(f"[+] Scan complete. Found {len(engine.visited)} entities.")
    
    if args.output == "text":
        filename = args.file if args.file else "report.md"
        export_to_markdown(results, filename)
    elif args.output == "graph":
        filename = args.file if args.file else "map.dot"
        export_to_graphviz(results, filename)

if __name__ == "__main__":
    main()

import argparse
import sys


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

    return parser.parse_args()


def main():
    args = parse_args()

    print(f"[+] Targeting domain: {args.domain}")
    print(f"[+] Max depth: {args.depth}")
    print(f"[+] Output format: {args.output}")


if __name__ == "__main__":
    main()

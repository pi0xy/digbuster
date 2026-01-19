def export_to_markdown(results, output_file="report.md"):
    with open(output_file, "w") as f:
        f.write("# Digbuster Scan Report\n\n")
        for target, found in results.items():
            if found:
                f.write(f"### {target}\n")
                for item in sorted(found):
                    f.write(f"* {item}\n")
                f.write("\n")
    print(f"[+] Report saved to {output_file}")
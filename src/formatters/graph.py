def export_to_graphviz(results, output_file="map.dot"):
    with open(output_file, "w") as f:
        f.write("digraph DNSMap {\n")
        f.write('  rankdir="LR";\n')
        f.write('  node [shape=box, fontname="Arial"];\n')
        
        for target, found in results.items():
            for item in found:
                f.write(f'  "{target}" -> "{item}";\n')
        
        f.write("}\n")
    print(f"[+] Graph saved to {output_file}")
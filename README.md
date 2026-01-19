Digbuster is a recursive DNS reconnaissance tool designed for attack surface mapping. It combines several enumeration techniques to discover hidden assets and visualize a target's network topology.

Digbuster is a recursive dns recognition tool made 


🛠 Installation

Digbuster use Graphviz to render the graph.

```bash
sudo pacman -S graphviz
sudo apt install graphviz
```


```bash
git clone https://github.com/pi0xy/digbuster.git
cd digbuster
pip install -r requirements.txt
```

📖 Usage

Standard scan

```bash
python3 -m src.cli oteria.fr
```


Options

```bash
-d, --depth : search depth (default 2)
-o, --output : output format (text, graph)
```
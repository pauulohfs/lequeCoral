import re
import json

def rgb_para_hex(r, g, b):
    return f"#{int(r):02X}{int(g):02X}{int(b):02X}"

arquivo_entrada = "leque_coral.txt"
arquivo_saida = "cores.json"

pattern = re.compile(
    r"<colorName>(.*?)</colorName>.*?<red>(\d+)</red>.*?<green>(\d+)</green>.*?<blue>(\d+)</blue>",
    re.DOTALL
)

with open(arquivo_entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()

resultados = pattern.findall(conteudo)

cores = []

for nome, r, g, b in resultados:
    hex_code = rgb_para_hex(r, g, b)
    cores.append({
        "nome": nome,
        "rgb": [int(r), int(g), int(b)],
        "hex": hex_code
    })

with open(arquivo_saida, "w", encoding="utf-8") as f:
    json.dump(cores, f, ensure_ascii=False, indent=2)

print(f"{len(cores)} cores extraídas e salvas em '{arquivo_saida}'.")

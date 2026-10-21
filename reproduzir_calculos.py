"""Reproduz os números derivados do dossiê a partir dos CSVs desta pasta.

Uso:
    python reproduzir_calculos.py

Só usa a biblioteca padrão do Python (3.8+).
Regra do projeto: números de fontes oficiais e não oficiais nunca são somados
entre si. Cada bloco abaixo usa uma única fonte, exceto o cruzamento
exploratório da seção 4, que combina duas fontes oficiais e está sinalizado.
"""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent


def ler(nome):
    with open(DATA / nome, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(valor):
    return float(valor) if valor not in ("", None) else None


def spearman(x, y):
    """Correlação de Spearman sem empates (suficiente para estas séries)."""
    def ranks(v):
        ordem = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for pos, i in enumerate(ordem):
            r[i] = pos + 1
        return r

    rx, ry, n = ranks(x), ranks(y), len(x)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))


def br(valor, casas=1):
    return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# 1. Bacen: ranking do 2T26 (fonte oficial)
print("== 1. Bacen, Ranking de Reclamações 2T26 ==")
rk = ler("bacen_ranking_top15_2t26.csv")
proc = sum(num(r["procedentes_2t26"]) for r in rk)
cli = sum(num(r["clientes_2t26"]) for r in rk)
print(f"Procedentes no top 15: {br(proc, 0)} | clientes: {br(cli, 0)}")
print(f"Índice agregado do top 15: {br(proc / cli * 1e6, 2)} por milhão de clientes")

for grupo in ("privado_tradicional", "publico", "digital_ip"):
    linhas = [r for r in rk if r["grupo"] == grupo]
    p = sum(num(r["procedentes_2t26"]) for r in linhas)
    c = sum(num(r["clientes_2t26"]) for r in linhas)
    print(f"  {grupo:20s} índice agregado {br(p / c * 1e6, 2):>6} | {br(p / proc * 100)}% das procedentes")

rho = spearman([num(r["clientes_2t26"]) for r in rk], [num(r["indice_2t26"]) for r in rk])
print(f"Spearman clientes x índice (n={len(rk)}): {br(rho, 2)}")

print("Variação do índice 1T26 -> 2T26:")
for r in rk:
    a, b = num(r["indice_1t26"]), num(r["indice_2t26"])
    if a:
        print(f"  {r['instituicao']:25s} {br(a, 2):>6} -> {br(b, 2):>6}  ({(b / a - 1) * 100:+.0f}%)")

print("\nMotivos (procedentes):")
for m in ler("bacen_motivos_top5_2t26.csv"):
    atual = num(m["procedentes_2t26"])
    base, rotulo = None, ""
    if num(m["procedentes_1t26"]):
        base, rotulo = num(m["procedentes_1t26"]), "vs 1T26"
    elif num(m["procedentes_3t25"]):
        base, rotulo = num(m["procedentes_3t25"]), "vs 3T25"
    var = f"{(atual / base - 1) * 100:+.0f}% {rotulo}" if base else "sem série"
    print(f"  {m['motivo_resumido']:45s} {br(atual, 0):>6}  {var}")
cons = [num(m["procedentes_2t26"]) for m in ler("bacen_motivos_top5_2t26.csv") if "Consignado" in m["motivo_resumido"]]
print(f"Consignado somado (duas linhas): {br(sum(cons), 0)}")

# 2. consumidor.gov.br (fonte oficial; números via compilação jornalística)
print("\n== 2. consumidor.gov.br, 2026 ==")
tot = {(r["indicador"], r["periodo"]): num(r["valor"]) for r in ler("consumidor_gov_totais_2026.csv")}
print(f"Respondidas em ago/26: {br(tot[('respondidas', '2026-08')] / tot[('reclamacoes_total', '2026-08')] * 100)}%")
print(f"Avaliadas / total ago/26: {br(tot[('avaliadas', '2026-08')] / tot[('reclamacoes_total', '2026-08')] * 100)}%")
print(f"Resolvidas / avaliadas ago/26: {br(tot[('avaliadas_resolvidas', '2026-08')] / tot[('avaliadas', '2026-08')] * 100)}%")
var_sf = (tot[('servicos_financeiros', '2026-07')] / tot[('servicos_financeiros', '2026-01')] - 1) * 100
print(f"Serviços financeiros jan -> jul/26: +{br(var_sf)}%")
temas = {r["tema"]: num(r["reclamacoes_ago26"]) for r in ler("consumidor_gov_temas_ago26.csv")}
cartao_emp = temas["Cartão de crédito, débito ou de loja"] + temas["Crédito pessoal e outros empréstimos"]
print(f"Cartão + empréstimos em serviços financeiros (ago/26): {br(cartao_emp / tot[('servicos_financeiros', '2026-08')] * 100)}%")

# 3. Reclame Aqui (fonte NÃO oficial; nunca somada às anteriores)
print("\n== 3. Reclame Aqui, abr-set/26 (não oficial) ==")
ra = ler("reclame_aqui_abr_set26.csv")
for r in ra:
    gap = num(r["solucao_pct"]) - num(r["voltariam_pct"])
    print(f"  {r['banco']:25s} solução {br(num(r['solucao_pct']))}% | voltariam {br(num(r['voltariam_pct']))}% | diferença {br(gap)} p.p.")
gaps = [num(r["solucao_pct"]) - num(r["voltariam_pct"]) for r in ra]
print(f"Diferença solução - voltariam: de {br(min(gaps))} a {br(max(gaps))} p.p.")
rho_ra = spearman([num(r["tempo_resposta_dias"]) for r in ra], [num(r["solucao_pct"]) for r in ra])
print(f"Spearman tempo de resposta x solução (n={len(ra)}): {br(rho_ra, 2)}  (negativo = mais tempo, menos solução)")

# 4. Cruzamento exploratório entre duas fontes OFICIAIS
print("\n== 4. Cruzamento exploratório: consumidor.gov.br (jun/26) x clientes BC (2T26) ==")
clientes = {r["instituicao"]: num(r["clientes_2t26"]) for r in rk}
indices = {r["instituicao"]: num(r["indice_2t26"]) for r in rk}
for r in ler("consumidor_gov_bancos_jun26.csv"):
    if r["reclamacoes_jun26"]:
        taxa = num(r["reclamacoes_jun26"]) / clientes[r["banco"]] * 1e6
        print(f"  {r['banco']:25s} {br(taxa, 0)} reclamações por milhão de clientes | índice BC {br(indices[r['banco']], 2)}")
print(f"Razão entre os índices BC (BB / Nubank): {br(indices['Banco do Brasil'] / indices['Nubank'], 2)}x")

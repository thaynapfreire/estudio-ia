# Dados

Tabelas pequenas transcritas das fontes consultadas em 19/10/2026. Servem para reproduzir os cálculos do dossiê com `reproduzir_calculos.py`.

> **Regra do projeto:** números de fontes oficiais (Bacen, consumidor.gov.br) e não oficiais (Reclame Aqui) ficam em arquivos separados e nunca são somados entre si.

| Arquivo | Fonte | Oficial? | Período | Como foi obtido |
|---|---|---|---|---|
| `bacen_ranking_top15_2t26.csv` | Banco Central, Ranking de Reclamações | Sim | 2T26 (coluna `indice_1t26`: 1T26) | Top 3 conferido na [página oficial do BC](https://www3.bcb.gov.br/ranking/). Tabela completa via [Finsiders Brasil](https://finsidersbrasil.com.br/noticias-sobre-fintechs/c6-mercado-pago-e-pan-lideram-queixas-contra-fintechs-no-2o-tri/) (Murilo Melo, 23/07/2026), que reproduz o BC. Índices do 1T26 via Finsiders e Brasil 247 |
| `bacen_motivos_top5_2t26.csv` | Banco Central, Ranking de Reclamações | Sim | 2T26, 1T26 e 3T25 | Ordem dos 3 primeiros conferida no BC. Contagens via Finsiders (2T26 e 1T26) e Monitor Mercantil (3T25) |
| `consumidor_gov_totais_2026.csv` | consumidor.gov.br (Senacon/MJSP) | Sim | jan, jul e ago/2026 | Compilação dos arquivos mensais feita por [Consumo em Pauta](https://www.consumoempauta.com.br/alertas/reclamacoes-recuam-em-agosto-facebook-lidera-ranking-no-mes/) (Angela Crespo) |
| `consumidor_gov_temas_ago26.csv` | consumidor.gov.br | Sim | ago/2026 | Idem. Não verificado se as contagens de "problema" incluem setores fora de serviços financeiros |
| `consumidor_gov_bancos_jun26.csv` | consumidor.gov.br | Sim | jun/2026 | [Consumo em Pauta](https://www.consumoempauta.com.br/especiais/reclamacoes-crescem-45-em-2026-bancos-lideram-ranking/) (Redação, 16/07/2026). Células vazias: valor não publicado na fonte |
| `reclame_aqui_abr_set26.csv` | Reclame Aqui | **Não** | 01/04 a 30/09/2026 | Leitura única da página pública de cada empresa, sem raspagem. `tempo_resposta_dias` converte "X dias e Y horas" em dias. Os percentuais de produto e problema cobrem até 3 anos de reclamações |

## Dicionário de colunas

- `indice_*`: reclamações procedentes estimadas por milhão de clientes (metodologia do BC).
- `procedentes_*`: estimativa estatística de reclamações procedentes, ou seja, com indício de descumprimento de norma.
- `clientes_2t26`: clientes informados ao BC (CCS/SCR).
- `grupo`: classificação desta análise (privado tradicional, público, digital/instituição de pagamento). Não é categoria oficial do BC.
- `indice_solucao_pct` (consumidor.gov.br) e `solucao_pct` (Reclame Aqui) têm definições diferentes e **não são comparáveis em nível**.

## Pendente

- Conferir os números de segunda mão nos CSVs oficiais: [Ranking BC](https://dadosabertos.bcb.gov.br/dataset/ranking-de-instituicoes-por-indice-de-reclamacoes) e [consumidor.gov.br](https://dados.mj.gov.br/dataset/reclamacoes-do-consumidor-gov-br). Os portais bloquearam acesso automatizado durante a análise.
- Baixar as taxas de juros por instituição (cartão rotativo e parcelado) em [Taxas de juros por instituição financeira](https://dadosabertos.bcb.gov.br/dataset/taxas-de-juros-de-operacoes-de-credito).

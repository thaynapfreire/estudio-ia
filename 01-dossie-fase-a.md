# 01 · Dossiê, Fase A: o que os dados revelam

**Skill:** [`analise-publico-por-dados`](skill-analise-publico-por-dados.md)
**Pedido:** bancos brasileiros, pessoa física, sem recorte de produto, hipótese ou persona.
**Fontes:** Bacen e consumidor.gov.br (oficiais); Reclame Aqui (complementar, só páginas públicas).
**Data da análise:** 19/10/2026.

> **Viés de todas as fontes:** medem insatisfação **registrada**, não insatisfação real. Só aparece quem conhece o canal, tem acesso e decide usá-lo.
> **[DADO]** = está na fonte. **[INFERÊNCIA]** = leitura da análise, a validar.

---

## Bloco 1 · Banco Central, Ranking de Reclamações

**Oficial** · 2º trimestre de 2026, publicado em 23/07/2026 · [bcb.gov.br/ranking](https://www3.bcb.gov.br/ranking/)

### Top 5 motivos (reclamações procedentes)

| # | Tema | Procedentes 2T26 | Tendência |
|---|---|---|---|
| 1 | Cartão de crédito: irregularidade | 5.365 | ▲ +47% vs 1T26 |
| 2 | Consignado: irregularidade | 4.019 | ▲ +5% vs 1T26 |
| 3 | Atendimento do SAC ou central | 3.379 | ▼ −5% vs 3T25 |
| 4 | Crédito, exceto consignado: irregularidade | 2.872 | ▼ −10% vs 1T26 |
| 5 | Consignado: informação inadequada | 2.768 | sem série |

A página oficial confirma o top 3 de instituições e a ordem dos três primeiros motivos. Contagens e tabela completa via Finsiders Brasil, que reproduz o BC. Dados em [`bacen_motivos_top5_2t26.csv`](bacen_motivos_top5_2t26.csv).

### Leituras

1. **Consignado é o maior tema quando somado.** [DADO] As duas linhas somam 6.787 procedentes, acima das 5.365 de cartão. [INFERÊNCIA] A divisão em duas categorias dilui o peso do tema.
2. **O pico de cartão pode ser um incidente.** [DADO] Cartão subiu 47% e o Bradesco 74% (48,92 → 84,90). O Bradesco atribui a alta a uma instabilidade no Digio; é a versão da empresa, não verificada. [INFERÊNCIA] Cruzar instituição × motivo no CSV.
3. **Incumbentes pioram, digitais melhoram.** [DADO] BB +69%, Itaú +37%; Inter −25%, Neon −28%. Índice agregado no 2T26: privados tradicionais **58,6**, digitais e IPs **27,1**, públicos **26,5**. Os três privados tradicionais concentram 45,8% das procedentes do top 15.
4. **Tamanho não explica o índice.** [DADO] Spearman entre clientes e índice: 0,28 (n=15). Nubank, com 117 mi de clientes, tem 9,20.
5. **SAC em 3º é um metaproblema.** [INFERÊNCIA] Sintoma de falha no primeiro nível de atendimento.

### Limitações

Conta só reclamações procedentes; índice extrapolado de amostra; categorias regulatórias nomeiam a norma, não o sintoma vivido; canal favorece quem conhece o BC; sem demografia do reclamante; defasagem de cerca de 1 mês.

---

## Bloco 2 · consumidor.gov.br (Senacon/MJSP)

**Oficial** · jan a ago/2026 · [dados.mj.gov.br](https://dados.mj.gov.br/dataset/reclamacoes-do-consumidor-gov-br)

⚠️ Os CSVs brutos não abriram (bloqueio de acesso automatizado). Números via compilações do Consumo em Pauta.

### Top 5 temas (ago/2026)

| # | Tema | Tipo | Reclamações | Tendência |
|---|---|---|---|---|
| 1 | Cartão de crédito, débito ou loja | assunto | 67.084 | ▲ +64% jan→jul |
| 2 | Crédito pessoal e empréstimos | assunto | 45.917 | ▲ +73% jan→jul |
| 3 | Cálculo de juros e saldo devedor | problema | 30.889 | sem série |
| 4 | Cobrança para alterar ou cancelar contrato | problema | 30.754 | sem série |
| 5 | Renegociação ou parcelamento de dívida | problema | 25.525 | sem série |

Cartão e empréstimos somam 48,4% de serviços financeiros em agosto. Aceleração jan→jul/2026: consignado +107%, atendimento bancário +111%.

### Leituras

1. **Responder não é resolver.** [DADO] Ago/26: 93,9% respondidas, 31,3% avaliadas, e só 37,5% das avaliadas marcadas como resolvidas. Nota média 2,40 de 5. Solução em jun/26: Caixa 38,9%, BB 31,6%, Itaú 24,2%, Nubank 21,6%, Bradesco 21,4%, Santander 16,4%.
2. **A dor é entender e sair da dívida.** [INFERÊNCIA] Juros, saldo, cancelamento e renegociação dominam os problemas.
3. **Mesma taxa, procedência diferente.** Cruzamento exploratório entre duas fontes oficiais: Nubank e BB têm cerca de 194 e 192 reclamações por milhão de clientes (jun/26), mas índice BC de 9,20 e 32,68 (3,5×). [INFERÊNCIA] Diferença de procedência ou de canal por perfil.
4. **O volume explodiu.** [DADO] Ago/26 ficou 84,8% acima de ago/25. [INFERÊNCIA] Parte pode ser adoção do canal.
5. **Chega depois de tentar a empresa.** [DADO] 81% procuraram a empresa antes (2025).

### Demografia

**Não tenho dado suficiente** para bancos em 2026. A única referência encontrada (estudo de 2019 a 2022, todos os setores) aponta 57,3% homens, 32,7% entre 31 e 40 anos e 48,1% no Sudeste; não serve como dado de bancos em 2026.

### Limitações

Só empresas cadastradas; exige login gov.br; cerca de 70% sem avaliação; números de segunda mão.

---

## Bloco 3 · Reclame Aqui

**NÃO oficial, complementar** · 01/04 a 30/09/2026 · 6 páginas públicas, uma leitura cada, sem raspagem

| Banco | Reputação | Reclamações (6m) | Solução | Voltariam | Nota | Resposta | Produto mais citado |
|---|---|---|---|---|---|---|---|
| Nubank | RA1000 · 8,7 | 56.623 | 93,1% | 81,2% | 7,76 | 4 dias | Cartão (45,4%) |
| Itaú | Ótima · 8,1 | 17.947 | 85,8% | 74,1% | 7,03 | 7 dias | Conta (36,5%) |
| C6 | Boa · 7,2 | 19.253 | 75,9% | 60,4% | 5,72 | 11 dias | Cartão (28,2%) |
| BB | Boa · 7,3 | 25.433 | 71,6% | 64,9% | 6,07 | 9 dias | Cartão (21,5%) |
| Bradesco | Regular · 6,9 | 31.185 | 68,1% | 58,5% | 5,61 | 8 dias | Conta (32,7%) |
| Caixa | Boa · 7,0 | 37.464 | 66,6% | 63,3% | 5,79 | 10 dias | Conta (15,8%) |

### Leituras

1. **"Cobrança indevida" é o problema nº 1 nos 6 bancos**, entre 16,5% e 23,1% (percentuais cobrem até 3 anos). [DADO]
2. **Dois grupos de fricção:** cartão em Nubank, C6 e BB; conta em Itaú, Bradesco e Caixa. [DADO]
3. **Resolver não recupera toda a confiança:** "voltariam" fica de 3,3 a 15,5 pontos abaixo da solução. [DADO]
4. **Rapidez e solução andam juntas:** Spearman entre tempo de resposta e solução = −0,60 (mais tempo, menos solução; n=6, não conclusivo). [DADO]

### Limitações

Público autosselecionado; plataforma privada; nota e solução dependem da avaliação após a resposta da empresa; marcas fragmentadas em várias páginas; definição de "solução" diferente da do consumidor.gov.br.

---

## Comparativo entre fontes (números mantidos separados)

| Tema | Bacen 2T26 | consumidor.gov 2026 | Reclame Aqui | Leitura |
|---|---|---|---|---|
| Cartão de crédito | Motivo nº 1, ▲47% | Assunto nº 1 | Produto nº 1 em 3 de 6 | **Converge** |
| Custo e saída da dívida | Como "irregularidade" de crédito | Problemas nº 3, 4 e 5 | Cobrança indevida nº 1 em 6 de 6 | **Converge** (BC nomeia a norma; as outras, o sintoma) |
| Consignado | Nº 2 e nº 5 | ▲107% | Fora do topo | **Diverge** |
| Atendimento que não resolve | SAC nº 3 | 37,5% resolvidas | 4 a 11 dias de resposta | **Converge** (metaproblema) |
| Conta | Fora do top 5 | Sem dado | Nº 1 em 3 de 6 | **Sinal fraco** |
| Nubank | 13º de 15 | Mais reclamado em volume | RA1000 | **Diverge** (base e métricas) |

---

## Checklist de verificação

| Afirmação | Como confirmei | Status |
|---|---|---|
| Top 3 do 2T26 e ordem dos motivos | Página oficial do BC | ✅ Oficial |
| Tabela completa e contagens por motivo | Finsiders, conferido com Metrópoles e Poder360 | 🟡 Secundária |
| Agregados, Spearman, variações | `reproduzir_calculos.py` | ✅ Reproduzível |
| Números do consumidor.gov.br | Consumo em Pauta, 3 matérias consistentes | 🟡 Secundária |
| Demografia de bancos 2026 | Não encontrada | ❌ Lacuna |
| Indicadores do Reclame Aqui | Páginas públicas, uma leitura cada | ✅ Primária, não oficial |

## Problemas que emergiram

| | Problema | Força da evidência |
|---|---|---|
| **A** | Cartão de crédito: cobrança e contestação | Converge nas 3 fontes |
| **B** | Consignado: informação e contratação | Maior tema no BC somado; ▲107% no consumidor.gov |
| **C** | Custo e saída da dívida | Top 3 de problemas no consumidor.gov |
| D | Atendimento que responde mas não resolve | Metaproblema nas 3 fontes |
| E | Fricção em conta nos incumbentes | Sinal fraco, só Reclame Aqui |

O grupo escolheu aprofundar **A, B e C** → [02 · Personas](02-personas-fase-b.md).

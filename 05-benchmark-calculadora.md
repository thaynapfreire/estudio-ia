# 05 · Benchmark: Calculadora de decisão (Fase 4)

**Skill:** [`kickoff-dados`](skill-kickoff-dados.md)
**Recorte escolhido pelo grupo:** simuladores dos bancos (páginas públicas, sem login).
**Data:** 19/10/2026.

## Achado principal

Nenhum dos cinco simuladores de banco verificados conecta a contestação ao pagamento da fatura. Mesmo assim, o **CDC, art. 54-G, I** (incluído pela Lei 14.181/2021) já garante que, se o cliente avisar o banco **pelo menos 10 dias antes do vencimento**, o valor contestado não pode ser cobrado enquanto a disputa não for resolvida, e ele pode **pagar só a parte não contestada** (TJDFT, Direito Fácil, 10/09/2022).

Isso muda a pergunta da Fase 4:
1. **Avisei o banco a tempo?** Se sim, pago só a parte não contestada.
2. **Se não, quanto custa cada caminho?**

Nome de trabalho sugerido: **Calculadora da fatura contestada**.

## 1. Público

| Dado | Valor | Fonte |
|---|---|---|
| Usuários de cartão | 96,6 mi; 52,8 mi (54,7%) com dívida com juros | BC, Cidadania Financeira (Forbes, 24/04/2026) |
| Cartão na renda | 38,5% (2020) → 54% (2024) | Idem |
| Jovens (A1) | 27,6 mi com crédito; 70% até 2 SM; 19% em atraso grave | Idem |
| Rotativo | 444,9% a.a.; 66,2% da carteira inadimplente | BC, Estatísticas de Crédito (Seu Crédito Digital, ago/2026) |
| Parcelado | 184,5% a.a. | BC via Suno (fev/**2024**). **Sem dado de 2026** |

## 2. Dor documentada

- Cartão: motivo nº 1 no Bacen (5.365, +47%, 2T26) e assunto nº 1 no consumidor.gov.br (67.084, ago/26).
- Só 37,5% das avaliadas resolvidas (consumidor.gov.br, ago/26).
- Rotativo limitado a um mês, depois parcelamento obrigatório (Res. CMN 4.549/2017).
- Teto de 100% de juros e encargos sobre a dívida original desde 03/01/2024.
- **Não sei** quantas pessoas pagam valor contestado por desconhecer o art. 54-G.

## 3. Benchmark: simuladores dos bancos

| Banco | Onde | Sem login? | Simula | Custo/CET | Contestação | Regra citada |
|---|---|---|---|---|---|---|
| Nubank | App | ❌ | Parcelamento da fatura | ✅ CET no app | ❌ | ✅ Rotativo 1 mês, teto 100% |
| Itaú | App, bankline, central | ❌ | Parcelamento da fatura | 🟡 Só recomenda consultar | ❌ | 🟡 Pagamento parcial em meses seguidos |
| Inter | App | ❌ | Parcelamento de **uma compra** | ✅ Parcela e total | ❌ | ❌ |
| C6 | App | ❌ | Parcelamento até 36x | ❌ | ❌ | ❌ |
| Santander | App, chat, consultor | ❌ | Parcelamento com/sem entrada | ❌ | ❌ | ❌ |
| Bradesco, BB, Caixa | — | n/d | n/d | n/d | n/d | Não verificado (páginas não carregaram) |

**Padrão:** só dentro do app; só o produto do próprio banco; nenhum compara caminhos; nenhum menciona contestação; nenhuma taxa nas páginas públicas.

## 4. Gaps

| Gap | Oportunidade | Evidência |
|---|---|---|
| 1. Contestação desconectada do pagamento | Mostrar o art. 54-G e calcular quanto pagar agora | [DADO] direito existe e nenhuma das 5 páginas o cita. [INFERÊNCIA] público não conhece |
| 2. Sem comparação neutra | Comparar pagar tudo, só o não contestado, mínimo, parcelar | [DADO] BC publica taxas por instituição |
| 3. Exige login e app | Calculadora aberta, por conversa ou impressa | [DADO] |
| 4. Teto de 100% invisível | Mostrar o custo máximo | [DADO] só Nubank cita |

## 5. As taxas de cada banco são públicas?

Em parte. O BC publica a **taxa média** de cada banco por modalidade, incluindo cartão rotativo total e parcelado. A taxa de cada cliente não é pública.

| Camada | O que mostra | Por banco | Atualização | Uso na calculadora |
|---|---|---|---|---|
| Taxas de juros por instituição (BC) | Média ponderada dos últimos 5 dias úteis, com encargos | Sim | Semanal e mensal; JSON e API aberta | Fonte principal, com data |
| Juros acumulados no cartão (BC) | Percentis dos juros acumulados / dívida original (teto 100%) | 15 maiores (~80% do mercado) | Mensal | Complementar |
| Taxa do cliente | Contrato, fatura, app | Não pública | — | Só se a pessoa digitar |

Limitações a mostrar ao usuário: é média; pode faltar banco; defasagem de ~14 dias úteis; bancos não exibem essas taxas nas próprias páginas. Os valores de 2026 por banco **não foram baixados** (API bloqueou acesso automatizado).

## Cuidados

A calculadora informa direitos e custos, não dá aconselhamento jurídico nem financeiro. Validar com especialista como os bancos aplicam o art. 54-G (prazo de 10 dias, crédito em confiança, desfecho da apuração).

Bônus para consignado: os §§ 1º e 2º do mesmo artigo obrigam a entrega da cópia do contrato.

## Checklist

| Afirmação | Como confirmei | Status |
|---|---|---|
| Art. 54-G, I | TJDFT + LegJur | 🟡 Falta o texto no Planalto |
| Padrão dos 5 simuladores | Páginas públicas | ✅ Primária |
| Bradesco, BB, Caixa | Não carregaram | ❌ Lacuna |
| Indicador por instituição | O Povo, Suno; página do BC precisa de JavaScript | 🟡 |
| Parcelado 2026 | Não encontrado | ❌ Lacuna |
| Taxas por instituição publicadas | Portal de dados abertos do BC | ✅ Oficial |

# 03 · Discovery: cartão de crédito

**Skill:** [`discovery-a-partir-de-dados`](skill-discovery-a-partir-de-dados.md)
**Decisão do grupo:** fazer o discovery só com o problema A (cartão), personas A1 e A2, sem restrição de recorte.

**[D]** = dado do dossiê · **[I]** = inferência a validar

## Etapa 0 · Formalização

**Problema:** Clientes de bancos não reconhecem ou não entendem cobranças no cartão de crédito e não conseguem contestá-las com sucesso.

| Fonte | Evidência |
|---|---|
| Bacen | Motivo nº 1: 5.365 procedentes no 2T26, +47% |
| consumidor.gov.br | Assunto nº 1: 67.084 em ago/26 |
| Reclame Aqui | Cobrança indevida nº 1 nos 6 bancos; cartão mais citado em 3 |

Lacunas: os dados não separam fraude, tarifa e juros do rotativo; o pico pode ser o incidente do Digio; perfil vem de quem usa crédito.

## Etapa 1 · Mapas de empatia

### A1 · Jovem de baixa renda

| Dimensão | Conteúdo |
|---|---|
| Pensa e sente | Cartão como autonomia [I]; não sabe quanto vai pagar [I]; medo de sujar o nome: 19% em atraso grave [D] |
| Vê | Crédito fácil: 30 mi entraram no crédito em 4 anos [D]; limite cresceu só 7% [D]; apostas online como risco (BC) [D] |
| Fala e faz | Tudo pelo app, entrada aos 20 anos [D]; usa rotativo ou parcela quando a conta não fecha [I] |
| Dores | Rotativo a 444,9% a.a., 66,2% da carteira inadimplente [D]; renda até 2 SM em 70% [D] |
| Ganhos | Saber quanto vai pagar antes de fechar; não cair no rotativo; contestar pelo app [I] |

### A2 · Adulto(a) com orçamento no cartão

| Dimensão | Conteúdo |
|---|---|
| Pensa e sente | O mês depende do cartão: 54% da renda [D]; desconfia de cobranças embutidas [I] |
| Vê | Tarifas não informadas: 19.221 queixas; serviços não contratados: 36.078 no ProConsumidor [D]; mais de 220 mi de cartões ativos [D] |
| Fala e faz | 81% procuram a empresa antes [D]; SAC é motivo nº 3 no BC [D] |
| Dores | 37,5% resolvidas [D]; 4 a 11 dias de resposta no Reclame Aqui [D, não oficial]; "voltariam" 3 a 16 pontos abaixo da solução [D, não oficial] |
| Ganhos | Estorno; prova do que contratou; resolver no primeiro contato [I] |

## Etapa 2 · Jornada: um ciclo de fatura

| Fase | O que acontece | Emoção | Decisão | Atrito |
|---|---|---|---|---|
| 1. Uso no dia a dia | Compras, parcelas, serviços agregados | Controle [I] | Parcelar? Aceitar seguro? | Custo total invisível na compra [I] |
| 2. Fatura chega | Cobrança não reconhecida ou valor maior | Susto [I] | Pagar tudo, mínimo, parcelar ou contestar? | Fatura não explica a origem [I]; rotativo a 444,9% a.a. [D] |
| 3. Contato com o banco | App, chat ou SAC | Esperança → frustração | Insistir ou escalar? | SAC nº 3 no BC [D]; 4 a 11 dias [D] |
| **4. Pagar com a dúvida aberta** | Vence antes da resposta | Ansiedade [I] | Pagar o contestado ou arriscar? | Rotativo ou negativação; 66,2% inadimplente [D] |
| 5. Escalada externa | consumidor.gov, Reclame Aqui, Bacen | Indignação | Qual canal? | Login gov.br, provas, regras diferentes [I] |
| 6. Desfecho | Estorno ou não | Alívio parcial | Ficar ou cancelar? | 37,5% resolvidas [D] |

Variação: em A1 o susto é de juros [I] e a exposição ao rotativo é maior [D]; em A2 o susto é de tarifa [D] e tende a pagar e contestar depois [I].

**Fases críticas:** 2 (origem; evidência mais fraca) e **4** (onde as duas dores se encontram; candidata a validar em entrevista).

## Etapa 3 · Oportunidades

Restrições do grupo: roda no Claude, sem integração; só dados públicos; explicável; protótipo de workshop; funciona sem app.

| Fase | Oportunidade | Aderência | Complexidade |
|---|---|---|---|
| 1 | Simulador de custo total | Alta | Baixa |
| 2 | Tradutor de cobrança (descrita em palavras) | Média | Média |
| 2 | Leitura automática da fatura | **Baixa** (dado privado) | Fora |
| 3 | Roteiro de contestação | Alta | Baixa |
| **4** | **Calculadora de decisão** | Alta | Média |
| 5 | Guia de canal com índice de solução público | Alta | Média |
| 6 | Painel público de resolução em cartão | Alta | Média a alta |
| 6 | Checklist de fechamento | Alta | Baixa |

### Top 3

1. **Calculadora de decisão (Fase 4).** Fase mais crítica; aderência alta; explicável.
2. **Tradutor de cobrança + roteiro de contestação (Fases 2 e 3).** Atua na origem e no primeiro contato.
3. **Guia de canal com dados públicos de resolução (Fase 5).** Evidência mais forte.

## Resumo executivo

- **Problema:** cobranças no cartão que a pessoa não reconhece ou não entende, sem contestação bem-sucedida.
- **Personas:** A1 (susto com juros, 19% em atraso grave); A2 (susto com cobrança, cartão = 54% da renda).
- **Jornada:** ciclo de fatura em 6 fases; crítica: **Fase 4, pagar com a dúvida aberta**.
- **Top 3:** Calculadora de decisão · Tradutor + roteiro · Guia de canal.

Próximo: [05 · Benchmark da calculadora](05-benchmark-calculadora.md)

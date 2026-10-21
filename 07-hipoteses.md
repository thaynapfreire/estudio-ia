# 07 · Registro de hipóteses

Tudo o que o discovery assume e ainda não foi confirmado. Cada linha tem a evidência atual e como validar.

**Status:** ✅ dado confirmado em fonte · 🟡 parcial (dado indireto ou amostra limitada) · ⚪ inferência a validar

## Problema

| ID | Hipótese | Status | Evidência atual | Como validar |
|---|---|---|---|---|
| H1 | A causa comum das dores é não ter em mãos a prova do que contratou ou do que deve | ⚪ | Contrato não entregue, saldo divergente e cobrança não reconhecida aparecem nas 6 personas | Entrevistas: "tem cópia do contrato? sabe o saldo atual?" |
| H2 | A alta de 47% em cartão no 2T26 é tendência, não só o incidente do Digio | ⚪ | Bradesco atribui a alta ao Digio (versão da empresa) | Ranking 3T26; cruzar instituição × motivo no CSV do BC |
| H3 | A fatura não explica a origem da cobrança (Fase 2) | ⚪ | Evidência mais fraca do dossiê; só sintoma indireto (tarifas não informadas: 19.221) | Análise de faturas cedidas voluntariamente e anonimizadas; entrevistas |
| H4 | Parte do crescimento do consumidor.gov.br é adoção do canal, não aumento real de problemas | ⚪ | +84,8% ago/25 → ago/26 | Comparar com Procon e BC no mesmo período |
| H5 | Consignado aparece pouco no Reclame Aqui por fragmentação de páginas e canal por perfil | ⚪ | Forte no BC, fora do topo no Reclame Aqui | Somar páginas de consignado por marca (consulta manual) |
| H6 | Fricção em "conta" nos incumbentes não configura violação de norma | ⚪ | Conta nº 1 em Itaú, Bradesco, Caixa no RA; fora do top 5 no BC | Abrir subcategorias no CSV do BC |

## Público e personas

| ID | Hipótese | Status | Evidência atual | Como validar |
|---|---|---|---|---|
| H7 | O perfil de quem reclama espelha o perfil de quem usa crédito | ⚪ | Premissa das personas; sem demografia do reclamante em 2026 | Processar faixa etária, sexo e UF nos CSVs do consumidor.gov.br |
| H8 | Canal de reclamação varia por perfil (Nubank e BB: mesma taxa no consumidor.gov, índice BC 3,5× diferente) | 🟡 | Cruzamento exploratório entre duas fontes oficiais | Entrevistas: "onde reclamou e por quê?" |
| H9 | B1 (60+) prefere canais não digitais | 🟡 | 54% desistiram de empresa só-app (Procon-SP 2026, amostra de conveniência, n=812) | Entrevistas com apoio presencial |
| H10 | A1 decide pagar com base no mínimo, não no custo total | ⚪ | Rotativo inadimplente em 66,2% | Entrevistas A1 |

## Jornada

| ID | Hipótese | Status | Evidência atual | Como validar |
|---|---|---|---|---|
| H11 | A Fase 4 (pagar com a dúvida aberta) é o momento crítico de decisão sem informação | ⚪ | Deduzida da jornada; não existe como categoria de reclamação | Entrevistas A1/A2: "o que fez quando a fatura venceu?" |
| H12 | O prazo de vencimento não acompanha o prazo de análise da contestação | ⚪ | Resposta de 4 a 11 dias no Reclame Aqui (não oficial) | Regulação de SAC e prazos de contestação dos bancos |
| H13 | O bloqueio de consignado no Meu INSS é pouco conhecido | ⚪ | O serviço existe | Pergunta em entrevista 60+ |

## Solução (Calculadora da fatura contestada)

| ID | Hipótese | Status | Evidência atual | Como validar |
|---|---|---|---|---|
| H14 | O direito do art. 54-G, I (pagar só a parte não contestada) é pouco conhecido | 🟡 | Nenhuma das 6 páginas de bancos o menciona | Entrevistas; teste de compreensão |
| H15 | Nenhum simulador de banco conecta contestação a pagamento | 🟡 | 6 bancos verificados; Bradesco, BB e Caixa não | Verificar os 3 restantes |
| H16 | Mostrar o custo de cada caminho reduz pagamento indevido e entrada no rotativo | ⚪ | Hipótese de valor | Teste com protótipo: decisão antes × depois |
| H17 | Taxas médias públicas do BC bastam como referência | 🟡 | BC publica por instituição; média ≠ taxa do cliente | Comparar média com taxas de faturas reais (voluntárias) |
| H18 | É possível usar a calculadora sem colar dado pessoal | ⚪ | Desenho pede só valores e datas | Teste de uso: alguém tenta colar a fatura? |
| H19 | A calculadora pode ser entendida por quem tem baixo letramento financeiro (A1) | ⚪ | Risco 4 do Future Wheel | Teste de compreensão com A1 |

## Prioridade de validação sugerida

1. **H11 e H16** — sustentam a escolha da calculadora.
2. **H14** — se o direito for conhecido, o valor da calculadora muda.
3. **H2** — sai com o ranking 3T26.
4. **H7** — depende só de processar os CSVs do consumidor.gov.br.

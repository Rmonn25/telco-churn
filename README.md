# Telco Customer Churn Analysis

>  Projeto em andamento  
> Este projeto ainda está em desenvolvimento e continuará evoluindo com novas análises e modelagem preditiva.

---

## Sobre o Projeto

Este projeto tem como objetivo analisar e prever o churn (cancelamento) de clientes de uma empresa de telecomunicações.
Através de análise exploratória de dados (EDA), buscamos identificar padrões e variáveis que influenciam o cancelamento de clientes.
O foco principal é aplicar conceitos de Ciência de Dados e Machine Learning em um problema real de negócio.

---

## Objetivos

- Realizar limpeza e tratamento de dados
- Explorar padrões relacionados ao churn
- Identificar variáveis com maior poder preditivo
- Construir um modelo de classificação (em breve)
- Gerar insights estratégicos para retenção de clientes

---

```bash
telco-churn/
│
├── data/         # Dataset (.csv)
├── notebooks/    # Notebooks com análises (EDA, modelagem, etc.)
├── output/       # Imagens e gráficos gerados
└── README.md
```

## Tratamento de Dados

Durante a etapa de limpeza, foram realizadas as seguintes ações:

- Conversão da variável `TotalCharges` para formato numérico
- Identificação de valores ausentes
- Substituição de valores ausentes por 0 nos casos em que `tenure = 0`
- Verificação de consistência dos tipos de dados

---

## Principais Insights da EDA

### 1. Tenure (Tempo de permanência)

- Clientes que churnam possuem tempo de permanência significativamente menor.
- Aproximadamente 50% dos cancelamentos ocorrem nos primeiros 10 meses.
- A mediana de tenure para churn é muito inferior à de clientes ativos.

**Conclusão:** Clientes novos representam o grupo de maior risco.

---

### 2. MonthlyCharges (Cobrança mensal)

- Clientes que cancelam apresentam mensalidade média superior.
- A mediana de MonthlyCharges é maior no grupo churn.
- Planos mais caros parecem estar associados a maior probabilidade de cancelamento.

**Conclusão:** Pode existir sensibilidade a preço.

---

### 3. TotalCharges

- Forte relação com tenure (valor acumulado ao longo do tempo).
- Clientes que churnam tendem a ter menor valor acumulado, pois permanecem menos tempo.

---

## Perfil Inicial de Cliente com Maior Risco

Com base na análise exploratória:

> Clientes com baixa permanência (tenure baixo) e mensalidades mais altas apresentam maior probabilidade de churn.

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn (em breve)

---

## Status do Projeto

Em desenvolvimento — novas atualizações serão adicionadas conforme o avanço da modelagem.

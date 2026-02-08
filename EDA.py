#%%

# Bibliotecas 
import pandas as pd
import numpy as np 
import matplotlib as plt  
from matplotlib.ticker import StrMethodFormatter


# Configurações
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#%%

# Extraindo os dados e dando e visualizando as 5 primeiras linhas 
df = pd.read_csv("data/Telco-Customer-Churn.csv")

df.head()

# %%

# Informações gerais
df.info()

# %%

print(f"O dataset possui {df.shape[0]} linhas e {df.shape[1]} colunas")

# %%

df.isnull().sum()

# %%
df["gender"].unique()

# %%
df["SeniorCitizen"].unique()

# %%
df["Partner"].unique()

# %%
df["Dependents"].unique()

# %%
df["tenure"].unique()
# %%

df["PhoneService"].unique()
#%%

df["MultipleLines"].unique()
# %%

df["InternetService"].unique()
# %%

df["OnlineSecurity"].unique()
# %%
df["OnlineBackup"].unique()

# %%

df["DeviceProtection"].unique()
# %%

df["TechSupport"].unique()
# %%

df["StreamingTV"].unique()
# %%

df["StreamingMovies"].unique()
# %%

df["Contract"].unique()
# %%

df["PaperlessBilling"].unique()
# %%

df["PaymentMethod"].unique()
# %%

df["MonthlyCharges"].unique()

# %%

df["TotalCharges"].unique()
# %%

df["Churn"].unique()
# %%

# Questão 1. Qual a proporção de clientes que deram churn em relação ao total de clientes ?

df["Churn"].value_counts(normalize=True) * 100
# %%


# %%

# Grafico de histograma
ax = df.hist(column="MonthlyCharges", 
             bins=25, 
             grid=False, 
             figsize=(12, 8), 
             color='#3385e8', 
             zorder=2, 
             rwidth=0.9)

ax = ax[0]
for x in ax:

    x.spines["right"].set_visible(False)
    x.spines["top"].set_visible(False)
    x.spines["left"].set_visible(False)

    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    x.set_title("")

    x.set_xlabel("Valor cobrado mensalmente em Dólares", labelpad=20, weight='bold', size=12)

    x.set_ylabel("Clientes", labelpad=20, weight='bold', size=12)

    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
# %%

#%%

# Bibliotecas 
import pandas as pd
import numpy as np  
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
np.set_printoptions(threshold=np.inf)
pd.set_option("display.max_seq_items", None)

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



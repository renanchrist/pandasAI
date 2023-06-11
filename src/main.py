# Libraries import
import os
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

df_salaries = pd.read_csv("data_source/ds_salaries.csv")
df_salaries.head()

# Reading ENV variables from .ENV file
OPEN_API_KEY = os.getenv("OPEN_API_KEY", "")
if not OPEN_API_KEY:
    Exception("OPEN_API_KEY not specified")

# Loading the API token to OpenAI environment
openAPILLM = OpenAI(api_token=OPEN_API_KEY)

# Initializing an instance of PandasAI with OpenAI environment
pandasAI = PandasAI(openAPILLM)

# 1st question
prompt = "What is the highest salary in USD?"
print(f"{prompt}: {pandasAI.run(df_salaries, prompt=prompt)}")

# 2nd question
prompt = "Top 10 most well paid job?"
print(f"{prompt}: {pandasAI.run(df_salaries, prompt=prompt)}")

# 3rd question
prompt = "Plot a bar chart based on locations showing average salary by continent."
print(f"{prompt}: {pandasAI.run(df_salaries, prompt=prompt)}")
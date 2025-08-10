# mobile_price_project.py
# Lightweight reproduction script
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_excel("Processed_Flipdata.xlsx")
# Basic cleaning and feature extraction steps (simplified)
df.columns = [c.strip().lower() for c in df.columns]
price_col = "prize"
df = df[df[price_col].notna()]
# (Further processing omitted for brevity; see full project files)
print("Loaded data and prepared for modeling.")


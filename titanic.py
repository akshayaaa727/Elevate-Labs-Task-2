import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from google.colab import files
import io

# Upload dataset
print("📤 Please upload Titanic-Dataset.csv")
uploaded = files.upload()

# Read uploaded file dynamically
filename = list(uploaded.keys())[0]
df = pd.read_csv(io.BytesIO(uploaded[filename]))

print(f"✅ Dataset '{filename}' loaded successfully!")
print("Shape:", df.shape)
df.head()# Basic summary
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Check missing values
print("\nMissing values:\n", df.isnull().sum())

# Data types
print("\nData types:\n", df.dtypes)
# Histograms for numeric features
df.hist(bins=30, figsize=(12,8))
plt.suptitle("Histograms of Numeric Features")
plt.show()

# Boxplots for numeric features
numeric_cols = df.select_dtypes(include=[np.number]).columns
plt.figure(figsize=(12,6))
df[numeric_cols].boxplot()
plt.title("Boxplots of Numeric Features")
plt.xticks(rotation=45)
plt.show()
# Correlation matrix
corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
sns.pairplot(df.select_dtypes(include=[np.number]).dropna(), diag_kind='kde')
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.show()
# Example: Survival by Age & Sex
if 'Survived' in df.columns and 'Age' in df.columns and 'Sex' in df.columns:
    fig = px.histogram(df, x="Age", color="Sex", barmode="overlay", facet_col="Survived")
    fig.update_layout(title="Age Distribution by Sex & Survival")
    fig.show()
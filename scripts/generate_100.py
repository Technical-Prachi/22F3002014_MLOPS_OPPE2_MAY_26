import pandas as pd

df = pd.read_csv("data/data.csv")

# Remove rows having missing values
df = df.dropna().reset_index(drop=True)

# Randomly select exactly 100 samples
sample = df.sample(n=100, random_state=42)

# Remove target because prediction API expects input features only
sample = sample.drop(columns=["target"])

sample.to_csv("results/random_100.csv", index=False)

print("Generated:", sample.shape)
print(sample.head())

from ucimlrepo import fetch_ucirepo
import pandas as pd

# Load dataset
phishing = fetch_ucirepo(id=327)

X = phishing.data.features
y = phishing.data.targets

# Flatten target (fix)
y = pd.Series(y.values.ravel(), name="class")

# Combine features + target
df = pd.concat([X, y], axis=1)

# Save to CSV
df.to_csv("phishing_websites.csv", index=False)

print("CSV file saved successfully!")


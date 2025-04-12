import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
dataset = pd.read_csv("heart_disease.csv")

# Preprocessing
dataset['education'].fillna('Unknown', inplace=True)
dataset['Gender'].fillna(dataset['Gender'].mode()[0], inplace=True)
dataset['glucose'].fillna(method='ffill', inplace=True)
dataset['glucose'].fillna(method='bfill', inplace=True)
dataset.dropna(inplace=True)

# Map categorical fields
dataset["Gender"] = dataset["Gender"].map({'Male': 1, 'Female': 0}).fillna(0).astype(int)
dataset["Heart_ stroke"] = dataset["Heart_ stroke"].map({'yes': 1, 'no': 0}).fillna(0).astype(int)
dataset["prevalentStroke"] = dataset["prevalentStroke"].map({'yes': 1, 'no': 0}).fillna(0).astype(int)

# Drop unused columns
dataset = dataset.drop('education', axis=1)

# Features & target
X = dataset.drop('Heart_ stroke', axis=1)
y = dataset['Heart_ stroke']

# Train/test split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(xtrain, ytrain)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")

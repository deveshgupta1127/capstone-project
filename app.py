import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("/content/drive/MyDrive/heart/heart_disease.csv")

dataset.head(5)

dataset.isnull().sum()

dataset['education'].fillna('Unknown', inplace=True)

# Fill missing values in 'gender' with the mode
dataset['Gender'].fillna(dataset['Gender'].mode()[0], inplace=True)

dataset['glucose'].fillna(method='ffill', inplace=True)  # Forward fill
dataset['glucose'].fillna(method='bfill', inplace=True)  # Backward fill

dataset.dropna(inplace=True)

dataset.shape

model = RandomForestRegressor()

e = dataset["Gender"]

e.tail(5)

e = dataset["Gender"]

# Option 1: Iterate over values directly
for index, value in e.items():
  if value == "Male" or value == 1:
    e.loc[index] = 1  # Use .loc to update by label
  else:
    e.loc[index] = 0  # Use .loc to update by label

# Option 2: Use .map() for more efficient replacement
e = e.map({'Male': 1, 1: 1}).fillna(0).astype(int)

dataset["Gender"].tail()

f = dataset["Heart_ stroke"]

# Option 1: Iterate over values directly
for index, value in f.items():
  if value == "yes" or value == 1:
    f.loc[index] = 1  # Use .loc to update by label
  else:
    f.loc[index] = 0  # Use .loc to update by label

dataset["Heart_ stroke"].tail()

r = dataset["prevalentStroke"]

# Option 1: Iterate over values directly
for index, value in r.items():
  if value == "no" or value == 0:
    r.loc[index] = 0  # Use .loc to update by label
  else:
    r.loc[index] = 1  # Use .loc to update by label

dataset.head()

dataset = dataset.drop('education', axis=1)

dataset.head()

dataset.shape

x = dataset.drop('Heart_ stroke', axis=1)
y = dataset['Heart_ stroke']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=3)

model.fit(xtrain, ytrain)

train_accuracy = model.score(xtrain, ytrain)
print(f'Training Accuracy: {train_accuracy}')

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
y_pred = model.predict(xtest)
print("MSE:", mean_squared_error(ytest, y_pred))
print("R-squared:", r2_score(ytest, y_pred))

model1 = LogisticRegression()

ytrain = ytrain.astype(int)

model1.fit(xtrain, ytrain)

train_accuracy = model1.score(xtrain, ytrain)
print(f'Training Accuracy: {train_accuracy}')

y_pred = model1.predict(xtest)
print("MSE:", mean_squared_error(ytest, y_pred))
print("R-squared:", r2_score(ytest, y_pred))

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
model2 = KNeighborsClassifier(n_neighbors=5)
model2.fit(xtrain, ytrain)
y_pred = model.predict(xtest)
ytest = ytest.astype(int)
y_pred = y_pred.astype(int)
accuracy = accuracy_score(ytest, y_pred)
print(f"Accuracy: {accuracy}")


y_pred = model2.predict(xtest)
print("MSE:", mean_squared_error(ytest, y_pred))
print("R-squared:", r2_score(ytest, y_pred))

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Train model
model3 = GaussianNB()
model3.fit(xtrain, ytrain)

# Predictions
y_pred = model3.predict(xtest)

# Accuracy
accuracy = accuracy_score(ytest, y_pred)
print(f"Accuracy: {accuracy}")


y_pred = model2.predict(xtest)
print("MSE:", mean_squared_error(ytest, y_pred))
print("R-squared:", r2_score(ytest, y_pred))
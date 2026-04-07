import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# load data
data = pd.read_csv("data.csv")

X = data[['hours_studied', 'focus_level', 'sleep_hours', 'difficulty']]
y = data['study_time_needed']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = LinearRegression()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "model.pkl")

print("model trained and saved")
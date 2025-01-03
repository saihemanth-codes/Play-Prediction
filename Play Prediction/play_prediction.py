# -*- coding: utf-8 -*-
"""Play Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hUC7v4kgBjh4GdDfdRrKz40bAU0OhFQy
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Load your play-by-play data
df = pd.read_csv('/content/NFL 2024.csv')

print(df.columns)

# Step 2: Data Cleaning
# Drop columns that are not useful for prediction
df = df.drop(columns=["Unnamed: 10", "Unnamed: 12", "Unnamed: 16", "Unnamed: 17"])

# Step 3: Preprocessing
# Convert 'GameDate' to datetime and extract the relevant time features if needed (optional)
df['GameDate'] = pd.to_datetime(df['GameDate'], errors='coerce')
df['Quarter'] = df['Quarter'].astype(int)
df['Minute'] = df['Minute'].astype(int)
df['Second'] = df['Second'].astype(int)

# Fill missing values (if any)
df['YardLine'].fillna(0, inplace=True)  # Example: Fill missing YardLine with 0

#Step 4: Feature Selection
# Select the relevant columns
features = [
    "OffenseTeam", "DefenseTeam", "Down", "ToGo", "YardLine", "Formation",
    "IsRush", "IsPass", "IsTouchdown", "IsSack", "IsFumble", "IsInterception",
    "IsPenalty", "IsIncomplete", "PenaltyYards"
]

# Target variable: "IsRush" or "IsPass" (binary classification)
target = "IsRush"

# Step 5: Split data into features (X) and target (y)
X = df[features]
y = df[target]

# Step 6: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Create a preprocessing pipeline for categorical and numeric features
numeric_features = ["Down", "ToGo", "YardLine", "PenaltyYards"]
categorical_features = ["OffenseTeam", "DefenseTeam", "Formation"]

# Create transformers for the preprocessing pipeline
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Handle missing values in numeric columns
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing values in categorical columns
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encoding for categorical features
])

# Combine both transformers into a ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Step 8: Create a full pipeline with preprocessing and the model (Random Forest)
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Step 9: Train the model
model_pipeline.fit(X_train, y_train)

# Step 10: Make predictions
y_pred = model_pipeline.predict(X_test)

# Step 11: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plotting the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Rush', 'Pass'], yticklabels=['Rush', 'Pass'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Plotting the distribution of target variable (Rush vs Pass)
plt.figure(figsize=(6, 4))
df['IsRush'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Distribution of Rush vs Pass Plays')
plt.xlabel('Play Type (0: Rush, 1: Pass)')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['Rush', 'Pass'], rotation=0)
plt.show()
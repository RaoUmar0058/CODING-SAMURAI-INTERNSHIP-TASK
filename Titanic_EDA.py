# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)
# Author: Khadija  Rao

# ==============================
# 📦 Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Enable inline plotting (for Jupyter/VS Code)
# %matplotlib inline   # Uncomment if using Jupyter Notebook

# ==============================
# 📥 Load Dataset
# ==============================
print("📥 Loading Titanic dataset...")
titanic = sns.load_dataset("titanic")

# Check first few rows
print("\n🔹 First 5 rows:")
print(titanic.head())

# ==============================
# 🧭 Basic Info
# ==============================
print("\n📊 Dataset Info:")
print(titanic.info())

print("\n📈 Summary Statistics:")
print(titanic.describe(include='all'))

# ==============================
# 🔍 Missing Values
# ==============================
print("\n🚨 Missing Values:")
print(titanic.isnull().sum())

# Fill or drop missing values (for clean visuals)
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna(titanic['embarked'].mode()[0])
titanic.drop(columns=['deck'], inplace=True)

# ==============================
# 👩‍👩‍👧‍👦 Gender & Survival
# ==============================
plt.figure(figsize=(6,4))
sns.countplot(x='sex', hue='survived', data=titanic, palette='pastel')
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(['Not Survived', 'Survived'])
plt.show()

# ==============================
# 🎟️ Class vs Survival
# ==============================
plt.figure(figsize=(6,4))
sns.countplot(x='class', hue='survived', data=titanic, palette='cool')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# ==============================
# 🧓 Age Distribution
# ==============================
plt.figure(figsize=(6,4))
sns.histplot(titanic['age'], kde=True, bins=30, color='skyblue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# ==============================
# ⚓ Embarkation Port Analysis
# ==============================
plt.figure(figsize=(6,4))
sns.countplot(x='embarked', hue='survived', data=titanic, palette='muted')
plt.title('Survival by Embarkation Port')
plt.xlabel('Embarked From')
plt.ylabel('Count')
plt.show()

# ==============================
# 💰 Fare vs Survival
# ==============================
plt.figure(figsize=(6,4))
sns.boxplot(x='survived', y='fare', data=titanic, palette='Set2')
plt.title('Fare Paid vs Survival')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Fare')
plt.show()

# ==============================
# 🧠 Correlation Heatmap
# ==============================
plt.figure(figsize=(8,5))
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title('Correlation Heatmap')
plt.show()

# ==============================
# 🌟 Insights
# ==============================
print("\n📊 Key Insights:")
print("1️⃣ Females had a much higher survival rate than males.")
print("2️⃣ Passengers in 1st class were more likely to survive.")
print("3️⃣ Younger passengers had a slightly better survival chance.")
print("4️⃣ People who paid higher fares often belonged to higher classes and had better survival odds.")
print("5️⃣ Most passengers boarded from 'S' port.")

print("\n✅ EDA Completed Successfully!")

import pandas as pd
import re
import os

# -------------------------------
# 1. Load dataset
# -------------------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "Resume.csv")

df = pd.read_csv(file_path)

# Select required columns
df = df[['Resume_str', 'Category']]

# -------------------------------
# 2. Clean text
# -------------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

df['clean_text'] = df['Resume_str'].apply(clean_text)

# -------------------------------
# 3. Vectorization
# -------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words='english',
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(df['clean_text'])
y = df['Category']

# -------------------------------
# 4. Train-test split
# -------------------------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# -------------------------------
# 5. Model (Improved)
# -------------------------------
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# -------------------------------
# 6. Evaluation
# -------------------------------
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -------------------------------
# 7. Cross Validation
# -------------------------------
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print("\nCross Validation Accuracy:", scores.mean())

# -------------------------------
# 8. Save model
# -------------------------------
import pickle

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel saved successfully ✅")
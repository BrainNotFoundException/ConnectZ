import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import MultiLabelBinarizer

model_path = './fine_tuned_bert'  
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
test_df = pd.read_csv('sample_test_dataset.csv')  
def preprocess_data(examples):
    return tokenizer(examples['Description'], padding="max_length", truncation=True)

test_dataset = test_df.apply(preprocess_data, axis=1)
def predict(model, tokenizer, texts):
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    return torch.sigmoid(logits).detach().numpy()  # Apply sigmoid to get probabilities

# Step 5: Make predictions on the test dataset
test_descriptions = test_df['Description'].tolist()  # Get all test descriptions
predictions = predict(model, tokenizer, test_descriptions)

# Step 6: Convert the predictions to binary labels using a threshold (e.g., 0.5)
threshold = 0.6
predicted_labels = (predictions > threshold).astype(int)

# Step 7: Initialize MultiLabelBinarizer to get the correct labels (used during training)
mlb = MultiLabelBinarizer()
mlb.fit(test_df['Labels'].apply(lambda x: x.split(', ')))  # Fit on the test dataset labels (or use training labels)

# Step 8: Ensure predicted labels match the classes from MultiLabelBinarizer
print(f"Number of expected labels: {len(mlb.classes_)}")
print(f"Classes from MultiLabelBinarizer: {mlb.classes_}")

# Check the predicted labels shape
print(f"Predicted labels shape: {predicted_labels.shape}")

# Align the predicted labels to match the expected classes
if predicted_labels.shape[1] != len(mlb.classes_):
    print(f"Mismatch detected. Aligning predicted labels to the correct number of columns.")
    # If there is a shape mismatch, trim or pad the predicted labels
    min_columns = min(predicted_labels.shape[1], len(mlb.classes_))
    predicted_labels = predicted_labels[:, :min_columns]

# Step 9: Map binary labels back to words
# Convert the binary predictions back to words (labels)
predicted_words = []
for row in predicted_labels:
    words = [mlb.classes_[i] for i in range(len(row)) if row[i] == 1]
    predicted_words.append(words)

# Step 10: Print the predicted labels (words)
for idx, description in enumerate(test_descriptions):
    print(f"Description: {description}")
    print(f"Predicted labels: {predicted_words[idx]}")
    print('-' * 50)  # Print a separator line between outputs
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
from sklearn.model_selection import train_test_split


df = pd.read_csv('EventCategorization.csv')  

def clean_labels(label_str):
    return [label.strip() for label in label_str.split(', ')]

df['Labels'] = df['Labels'].apply(clean_labels)

mlb = MultiLabelBinarizer()
df['Labels'] = mlb.fit_transform(df['Labels']).tolist()

train_df, val_df = train_test_split(df, test_size=0.1)

train_dataset = Dataset.from_pandas(train_df)
val_dataset = Dataset.from_pandas(val_df)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def tokenize_function(examples):
    # Tokenize the descriptions and include the labels in the returned dictionary
    tokenized = tokenizer(examples['Description'], padding="max_length", truncation=True)
    tokenized['labels'] = torch.tensor(examples['Labels'], dtype=torch.float)  # Cast labels to float
    return tokenized

train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)

model = BertForSequenceClassification.from_pretrained(
    'bert-base-uncased',
    num_labels=len(mlb.classes_),
    problem_type="multi_label_classification"
)

training_args = TrainingArguments(
    output_dir="./results",  
    eval_strategy="epoch",   
    per_device_train_batch_size=8,  
    per_device_eval_batch_size=8,   
    num_train_epochs=3,            
    weight_decay=0.01,             
    logging_dir="./logs",          
    logging_steps=10,              
)


trainer = Trainer(
    model=model, 
    args=training_args,
    train_dataset=train_dataset,  
    eval_dataset=val_dataset,     
    compute_metrics=None          
)


trainer.train()


trainer.save_model("./fine_tuned_bert")

print("Model fine-tuned and saved!")
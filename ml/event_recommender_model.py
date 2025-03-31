import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Sample data
user_data = {
    "User ID": [1, 2, 3, 4, 5, 6],
    "Interests": ["AI, Machine Learning", "Web Development, Frontend", "Data Science, AI", 
                  "Cybersecurity, Networking", "Blockchain, Technology", "Deep Learning, Healthcare"],
    "Skills": [["Python", "TensorFlow", "Keras"], ["HTML", "CSS", "JavaScript"], 
               ["R", "Machine Learning", "Statistics"], ["Python", "Networking", "Linux"], 
               ["Solidity", "Ethereum", "Smart Contracts"], ["TensorFlow", "Keras", "CNNs"]],
    "Career Goals": ["Data Scientist", "Full Stack Developer", "Data Analyst", "Security Engineer", 
                     "Blockchain Developer", "AI Specialist"]
}

events_data = {
    "Event ID": [101, 102, 103, 104, 105, 106],
    "Event Title": ["AI Workshop on Neural Networks", "Data Science Seminar", "Web Development Bootcamp", 
                    "Deep Learning in Healthcare", "Cybersecurity 101", "Blockchain Basics"],
    "Description": ["This workshop will cover AI basics and neural networks. Learn about TensorFlow and deep learning.",
                    "Dive into the world of data science with this seminar covering machine learning and data analysis.",
                    "Learn web development with HTML, CSS, and JavaScript in this 6-week bootcamp.",
                    "Explore the application of deep learning in healthcare, particularly in medical imaging.",
                    "Understand the basics of cybersecurity, threats, and defenses in this introductory course.",
                    "This session introduces the fundamentals of blockchain technology and its applications."],
    "Tags": ["AI, Deep Learning, Neural Networks", "Data Science, Machine Learning", "Web Development, Frontend", 
             "Deep Learning, Healthcare", "Cybersecurity, Networking", "Blockchain, Technology"],
    "Category": ["Workshop", "Seminar", "Bootcamp", "Webinar", "Workshop", "Seminar"]
}

# Convert to DataFrame
user_df = pd.DataFrame(user_data)
event_df = pd.DataFrame(events_data)

# Preprocess Interests and Descriptions
user_df['Interests'] = user_df['Interests'].apply(lambda x: x.lower())  # Lowercase
event_df['Description'] = event_df['Description'].apply(lambda x: x.lower())  # Lowercase

# Vectorize Interests and Event Descriptions using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
user_interests_vec = vectorizer.fit_transform(user_df['Interests'])
event_descriptions_vec = vectorizer.transform(event_df['Description'])

# Compute Cosine Similarity between User Interests and Event Descriptions
cosine_sim = cosine_similarity(user_interests_vec, event_descriptions_vec)

# Function to recommend events based on user ID
def recommend_events(user_id, cosine_sim, event_df, top_n=3):
    user_idx = user_df[user_df['User ID'] == user_id].index[0]

    sim_scores = list(enumerate(cosine_sim[user_idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    top_events = sim_scores[:top_n]
    
    event_recommendations = []
    for event in top_events:
        event_idx = event[0]
        event_id = event_df.iloc[event_idx]['Event ID']
        event_title = event_df.iloc[event_idx]['Event Title']
        event_recommendations.append({'Event ID': event_id, 'Event Title': event_title})
    
    return event_recommendations

# Test with User 1
recommended_events = recommend_events(1, cosine_sim, event_df, top_n=3)
print("Recommended Events for User 1:")
for event in recommended_events:
    print(f"- {event['Event Title']}")

# Save the TF-IDF vectorizer and cosine similarity matrix
joblib.dump(vectorizer, 'user_interest_vectorizer.pkl')
joblib.dump(cosine_sim, 'cosine_similarity_matrix.pkl')

print("Models saved successfully!")
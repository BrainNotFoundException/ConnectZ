import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib  # For saving the model

# Sample Data: User Interests
user_data = {
    "User ID": [1, 2, 3, 4, 5, 6],
    "Interests": [
        "AI, Machine Learning", 
        "Web Development, Frontend", 
        "Data Science, AI", 
        "Cybersecurity, Networking", 
        "Blockchain, Technology", 
        "Deep Learning, Healthcare"
    ]
}

# Convert to DataFrame
user_df = pd.DataFrame(user_data)

# Preprocess User Interests (to be vectorized)
user_df['Interests'] = user_df['Interests'].apply(lambda x: x.lower())

# Vectorizing Interests using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
user_interests_vec = vectorizer.fit_transform(user_df['Interests'])

# Compute Cosine Similarity between Users' Interests
cosine_sim = cosine_similarity(user_interests_vec, user_interests_vec)

# Function to recommend similar users based on interests
def recommend_similar_users(user_id, cosine_sim, user_df, top_n=3):
    # Get the index of the user in the user dataframe
    user_idx = user_df[user_df['User ID'] == user_id].index[0]
    
    # Get the pairwise cosine similarity scores for the user
    sim_scores = list(enumerate(cosine_sim[user_idx]))
    
    # Sort the users based on similarity scores (in descending order)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top N similar users (excluding the user itself)
    similar_users = sim_scores[1:top_n+1]
    
    user_recommendations = []
    for user in similar_users:
        similar_user_idx = user[0]
        similar_user_id = user_df.iloc[similar_user_idx]['User ID']
        user_recommendations.append({'User ID': similar_user_id})
    
    return user_recommendations

# Test with User 1
recommended_users = recommend_similar_users(1, cosine_sim, user_df, top_n=3)
print("Recommended Users for User 1:")
for user in recommended_users:
    print(f"- User ID: {user['User ID']}")

# Save the vectorizer and cosine similarity matrix to files
joblib.dump(vectorizer, 'user_interests_vectorizer.pkl')
joblib.dump(cosine_sim, 'cosine_similarity_matrix.pkl')

print("\nModel and cosine similarity matrix saved successfully!")

# To load the saved models
# Loaded_vectorizer = joblib.load('user_interests_vectorizer.pkl')
# Loaded_cosine_sim = joblib.load('cosine_similarity_matrix.pkl')
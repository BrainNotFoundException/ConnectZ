import pandas as pd
import joblib
import sys
import json

# Load the model and vectorizer
vectorizer = joblib.load('./user_interests_vectorizer.pkl')
cosine_sim = joblib.load('./cosine_similarity_matrix.pkl')

# User Data
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

user_df = pd.DataFrame(user_data)

# Function to recommend similar users based on interests
def recommend_similar_users(user_id, cosine_sim, user_df, top_n=3):
    user_idx = user_df[user_df['User ID'] == user_id].index[0]
    sim_scores = list(enumerate(cosine_sim[user_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_events = sim_scores[:top_n]
    user_recommendations = []
    for event in top_events:
        similar_user_idx = event[0]
        similar_user_id = user_df.iloc[similar_user_idx]['User ID']
        user_recommendations.append({'User ID': int(similar_user_id)})
    return user_recommendations

# Accept user_id as command-line argument
user_id = int(sys.argv[1])

# Get recommendations for the provided user_id
recommended_users = recommend_similar_users(user_id, cosine_sim, user_df, top_n=3)

# Output the result as JSON
#for i in recommended_users:
#    recommended_users[i] = int(recommended_users[i])
print(json.dumps(recommended_users))
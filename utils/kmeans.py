import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Step 1: Generate a synthetic dataset
np.random.seed(42)  # For reproducibility
data = {
    'Gender': np.random.choice(['Male', 'Female'], 1000),
    'Income': np.random.randint(30000, 120000, 1000),
    'Age': np.random.randint(18, 65, 1000),
    'Employment Status': np.random.choice(['Employed', 'Unemployed', 'Self-employed'], 1000),
    'Education Level': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 1000)
}
df = pd.DataFrame(data)

# Step 2: Filter the dataset based on specified criteria
filtered_df = df[(df['Income'] < 80000) & (df['Gender'] == 'Male')]

# Select columns for K-means
features = filtered_df[['Income', 'Age', 'Education Level']]

# Convert categorical data to numerical
features = pd.get_dummies(features, columns=['Education Level'])

# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Step 3: Perform K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(features_scaled)
filtered_df['Cluster'] = clusters  # Assign cluster to each row

# Display the first few rows of the clustered dataset
filtered_df.head()
# Import libraries
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
import numpy as np
from src.utils import config

# Import data
data_boa_raw = pd.read_excel(config.data_boa, index_col = 0)


# Assuming df is your DataFrame

# Automatically identify numerical and categorical columns
numerical_features = data_boa_raw.select_dtypes(include=['int64', 'float64']).columns
categorical_features = data_boa_raw.select_dtypes(include=['object']).columns

# Create transformers for both numerical and categorical features
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')), # Handle missing values
    ('scaler', MinMaxScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), # Handle missing values
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine transformers into a ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Apply the preprocessing
data_boa_processed = preprocessor.fit_transform(data_boa_raw)

# Step 2: Choose the number of clusters (k) - for example, let's choose 3
# Note: You might want to use methods like the elbow method to choose k
n_clusters = 5

# Step 3: Create and fit the KMeans model
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(data_boa_processed)

# Step 4: Predict clusters
clusters = kmeans.predict(data_boa_processed)

# If you want to attach the cluster labels back to your original DataFrame:
data_boa_raw['Cluster'] = clusters

print(data_boa_raw['Cluster'])
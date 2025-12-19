import pandas as pd

# Load dataset
df = pd.read_csv(
    "/kaggle/input/social-media-mental-health-indicators-dataset/mental_health_social_media_dataset.csv"
)
print("Original shape:", df.shape)

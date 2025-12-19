import pandas as pd
import joblib
from sqlalchemy import create_engine

# Load preprocessor
preprocessor = joblib.load("artifacts/preprocessor.pkl")

# DB connection
engine = create_engine(
    "mysql+pymysql://root:newpassword123@localhost/student_db"
)

# Read raw data from SQL
raw_df = pd.read_sql("SELECT * FROM student_raw", engine)

# Separate input & target
X = raw_df.drop(columns=["math_score"])
y = raw_df["math_score"]

# Apply preprocessing
X_processed = preprocessor.transform(X)

# Convert to DataFrame
processed_df = pd.DataFrame(X_processed)

# Add target back
processed_df["math_score"] = y.values

# Push to SQL
processed_df.to_sql(
    "student_preprocessed",
    con=engine,
    if_exists="replace",
    index=False
)

print(" Preprocessed data pushed to SQL")

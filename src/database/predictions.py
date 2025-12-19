import joblib
import pandas as pd
from sqlalchemy import create_engine

# Load model
model = joblib.load("artifacts/model.pkl")

# DB connection
engine = create_engine(
    "mysql+pymysql://root:newpassword123@localhost/student_db"
)

# Read preprocessed data
processed_df = pd.read_sql(
    "SELECT * FROM student_preprocessed",
    engine
)

# Split features & target
X_processed = processed_df.drop(columns=["math_score"])
y_actual = processed_df["math_score"]

# Predict
y_pred = model.predict(X_processed)

# Create prediction dataframe
prediction_df = pd.DataFrame({
    "actual_math_score": y_actual,
    "predicted_math_score": y_pred,
    "error": y_actual - y_pred
})

# Push predictions to SQL
prediction_df.to_sql(
    "student_predictions",
    con=engine,
    if_exists="replace",
    index=False
)

print(" Predictions pushed to SQL")

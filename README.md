## End to End  Machine Learnig Project




#  Student Performance Prediction – End-to-End ML Project with Docker & AWS

##  Project Overview
This project is an **end-to-end Machine Learning system** designed to analyze and predict student academic performance based on demographic, socio-economic, and educational factors.

The project demonstrates the **complete ML lifecycle**, including:
- Data analysis (EDA)
- Feature engineering
- Model training and evaluation
- Prediction pipeline
- Docker containerization
- Cloud deployment on AWS

This project follows **industry-level ML engineering and MLOps practices**.

---

##  Problem Statement
Student performance depends on multiple factors such as:
- Gender
- Parental education level
- Test preparation
- Socio-economic background

Manual analysis of these factors is inefficient and subjective.  
This project builds a **data-driven machine learning solution** to predict student scores and provide insights that can help educators improve learning outcomes.

---

##  Key Features
- Exploratory Data Analysis (EDA)
- Feature engineering and preprocessing
- Multiple ML model comparison
- Model evaluation and selection
- Prediction pipeline
- Docker-based containerization
- AWS cloud deployment (EC2 + ECR)
- Scalable and modular project structure

---

##  Exploratory Data Analysis (EDA)

EDA was performed to understand data distributions, relationships, and key influencing factors.

### Key Insights:
- Parental education has a strong impact on student performance
- Students completing test preparation perform better
- Math, reading, and writing scores are highly correlated
- Gender-based differences observed in certain subjects

### Techniques Used:
- Univariate analysis
- Bivariate analysis
- Correlation heatmaps
- Distribution plots

---

##  Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature scaling
- Train-test split
- Pipeline-based preprocessing for consistency

---

##  Machine Learning Models Used
Multiple regression models were trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Regressor
- Random Forest Regressor
- AdaBoost Regressor
- XGBoost Regressor
- CatBoost Regressor

---

##  Model Evaluation
Models were evaluated using:
- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

### Best Performing Models:
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor

The final model was selected based on accuracy, robustness, and generalization ability.

---

##  Prediction Pipeline
- Raw input data is preprocessed using the same pipeline as training
- Trained model is serialized using `joblib`
- Predictions are generated consistently for new inputs
- Ready for API or UI-based inference

---

##  Docker Deployment

Docker is used to containerize the ML application to ensure consistency across environments.

### Why Docker?
- Avoids “it works on my machine” issues
- Packages code, dependencies, and model together
- Simplifies cloud deployment

### Docker Workflow:
1. Create a Dockerfile
2. Build Docker image locally
3. Test container locally
4. Push image to AWS Elastic Container Registry (ECR)

Example commands:
```bash
docker build -t student-performance-ml .
docker run -p 8080:8080 student-performance-ml

## ☁️ AWS EC2 Deployment

The Machine Learning application is deployed on **AWS EC2** to enable cloud-based model inference and remote access.

- An **EC2 instance** was provisioned to host the application
- Docker was installed and configured on the EC2 instance
- The Dockerized ML application was pulled from **Amazon ECR**
- The application runs inside a container on EC2
- EC2 **security groups** were configured to allow external access
- The deployment ensures scalability, portability, and reliability

Once deployed, the application can be accessed using the EC2 public IP address.

## Demo Screenshot
![mlproject](screenshots/mlproject_prediction
_ui.png




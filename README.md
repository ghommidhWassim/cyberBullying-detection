# Cyberbullying Detection App

## Overview
This project implements an **end-to-end machine learning pipeline** to detect cyberbullying in social media texts. It uses a **two-stage classification system**:  

1. **Stage 1:** Predict whether a message is bullying or not.  
2. **Stage 2:** Predict the type of bullying (if any).  

The models are trained using **Logistic Regression** and **Random Forest**, with preprocessing steps including **text cleaning**, **tokenization**, and **TF-IDF vectorization**.  

The application is exposed via a **FastAPI REST API** and **containerized with Docker**, with MongoDB storing predictions for analysis. This setup allows easy deployment and scalability.

---

## Key Features
- Two-stage ML pipeline: Label → Bullying Type  
- Model evaluation using **F1-score**, precision, recall, and confusion matrices  
- Real-time predictions via FastAPI REST API  
- Dockerized deployment with MongoDB integration  
- Scripts for preprocessing, model training, testing, and visualization  

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ghommidhWassim/cyberBullying-detection.git
cd cyberBullying-detection
```
2.Project Structure (make sure all files exists in the same folder)
```bash
├─ appcyberBullying.py        # FastAPI application
├─ cyberbullying.ipynb         # Notebook for full pipeline
├─ model_label_lr.pkl          # Stage 1: Label prediction model
├─ model_type_lr.pkl           # Stage 2: Type prediction model
├─ types_le.pkl                # LabelEncoder for bullying types
├─ requirements.txt            # Python dependencies
├─ docker-compose.yml          # Docker configuration
├─ Dockerfile                  # FastAPI Docker image setup
```

3. **Ensure Docker and Docker Compose are installed**
4. **Build and start the containers**
```bash
docker-compose up --build
```
5. FastAPI server will run at **http://localhost:8000**
6. API docs available at **http://localhost:8000/docs**
   
## Usage
Predict Cyberbullying

Send a POST request to /predict with JSON data:
```bash
{
  "text": "Your text here"
}
```


Example response:
```bash
{
  "text": "Your text here",
  "label": "Bullying",
  "type": "sexual"
}
```

Stop the application
```bash
docker-compose down
```

## Evaluation

Stage 1 (Label Prediction) F1-score: 0.85 – 0.91

Stage 2 (Bullying Type) F1-score: 0.84 – 0.97

Confusion matrices and training/test F1 gap used to evaluate overfitting

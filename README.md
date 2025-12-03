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
git clone https://github.com/your-username/cyberbullying-detection.git
cd cyberbullying-detection
```

2. **Ensure Docker and Docker Compose are installed**
3. **Build and start the containers**
```bash
docker-compose up --build
```
4. FastAPI server will run at **http://localhost:8000**
5. API docs available at **http://localhost:8000/docs**
   
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

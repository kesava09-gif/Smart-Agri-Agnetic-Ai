# 🌾 SmartAgri Agentic AI

**SmartAgri Agentic AI** is an intelligent farming assistant that uses AWS and NVIDIA Agentic AI technologies to help farmers make data-driven decisions about soil, irrigation, and crop management.

## 🚀 Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Model:** Llama-3 NIM, Retrieval Embedding NIM
- **Infrastructure:** AWS EKS + NVIDIA NIM microservices

## 🧠 Architecture
![Architecture](docs/SmartAgri_Architecture.png)

## 🧩 Features
- Crop yield prediction based on soil and weather data
- Real-time advice using Llama-3 reasoning
- Data retrieval from agricultural knowledge base (Retrieval NIM)
- User-friendly interface built in Streamlit

## ⚙️ Setup Instructions
1. Clone repo:  
   ```bash
   git clone https://github.com/Kesava09-gif/SmartAgri-AgenticAI.git
   ```
2. Run backend (FastAPI):  
   ```bash
   cd backend/app
   uvicorn main:app --reload
   ```
3. Run frontend (Streamlit):  
   ```bash
   cd frontend
   streamlit run app.py
   ```

## 📽️ Demo
A short 3-minute demo video showcasing system features will be uploaded soon.

---
Developed by **Kesava09-gif** for the *AWS x NVIDIA Agentic AI Hackathon*.

![banner](https://github.com/user-attachments/assets/3b92c249-3956-49c8-88fb-811fa400f6e4)
<h1 align="center">🐕 RedBag Predictor</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=Cloudinary&logoColor=white" />
  <img src="https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
</p>

<p align="center">
  <a href="https://bitbucket.org/lbesson/ansi-colors"><img src="https://img.shields.io/badge/Maintained%3F-no-red.svg" /></a>
  <a href="https://github.com/Naereen/StrapDown.js/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Naereen/StrapDown.js.svg" /></a>
  <a href="https://GitHub.com/Naereen/ama"><img src="https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg" /></a>
</p>

## 📌 **Project Overview**

The **RedBag-Predictor** is a predictive microservice developed at Fatec Registro, designed to provide fast and accurate diagnoses for dogs with cataracts. Using Convolutional Neural Networks (CNNs), this API classifies images to determine whether an animal is healthy or affected by cataracts.

This Python-based microservice works in conjunction with the **RedBag-Core**, which acts as the core backend, handling user management, database operations, and API integrations.

👉 Access the [RedBag-Core](https://github.com/MateusOK/Redbag-Core) for more details.

---

## 🚀 **Getting Started**

### **Prerequisites**

Before running this project, ensure you have the following installed:

- [Python](https://www.python.org/)
- [Cloudinary Account](https://cloudinary.com/)
- [RedBag-Core](https://github.com/MateusOK/Redbag-Core) (must be running for full functionality)

### **Cloning the Repository**

Clone this project to your local machine:

```bash
git clone https://github.com/MateusOK/RedBag-Predictor.git
```

After cloning, navigate to the project directory and install dependencies:

```bash
cd RedBag-Predictor
pip install -r requirements.txt
```

### **Environment Variables**

Set up a `.env` file with your Cloudinary credentials:

```yaml
CLOUD_NAME={YOUR_CLOUD_NAME}
API_KEY={YOUR_API_KEY}
API_SECRET={YOUR_API_SECRET}
```

### **Starting the API**

Run the application:

```bash
python app.py
```

Ensure the **Java API** is running for full system functionality.

---

## 📍 **API Endpoints**

| Method | Route                        | Description                                    |
|--------|-----------------------------|------------------------------------------------|
| GET    | `/result/{public_id}`        | Returns the prediction result for an uploaded image |
| GET    | `/health`                    | Checks if the API is running correctly         |

### **Example Responses**

#### **GET /result/{public_id}**

_Response:_
```json
{
  "prediction": "unhealthy",
  "confidence": 0.89
}
```

#### **GET /health**

_Response:_
```json
{
  "status": "alive"
}
```

---

## 🤝 **Collaborators**

Special thanks to all contributors to this project:

- [Mateus Ribeiro](https://www.linkedin.com/in/dev-mateus-ribeiro)
- [Gustavo Eyros](https://www.linkedin.com/in/gustavoeyros)
- [Rian Yuri](https://www.linkedin.com/in/rian-yuri-b36563158/)
- [Luiz Lopes](https://www.linkedin.com/in/luizlopes12)

---

This project is licensed under the [MIT License](LICENSE).

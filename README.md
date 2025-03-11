[PYTHON_BADGE]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[FastAPI_BADGE]:https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[CLOUDINARY_BADGE]:https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=Cloudinary&logoColor=white
[KERAS_BADGE]:https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white
[TENSORFLOW_BADGE]:https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white

![banner](https://github.com/user-attachments/assets/3b92c249-3956-49c8-88fb-811fa400f6e4)
# 🐕 **RedBag API (Python)**

![Python][PYTHON_BADGE] ![FastAPI][FastAPI_BADGE] ![CLOUDINARY][CLOUDINARY_BADGE] ![KERAS][KERAS_BADGE] ![TENSORFLOW][TENSORFLOW_BADGE]

[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)

## 📌 **Project Overview**

The **RedBag API** is a project developed at **Fatec Registro**, designed to provide a fast and accurate diagnosis for **dogs with cataracts**. Using **Convolutional Neural Networks (CNNs)**, this API implements a predictive model capable of classifying animals as **healthy or affected by cataracts** efficiently.

This **Python-based API** works in conjunction with the **RedBag API (Java)**, which serves as a **Backend for Frontend (BFF)** to handle interactions between the front-end and backend services.

👉 Access the [RedBag API (Java)](https://github.com/MateusOK/Redbag.git) for more details.

---

## 🚀 **Getting Started**

### **Prerequisites**

Before running this project, ensure you have the following installed:

- [Python](https://www.python.org/)
- [Cloudinary Account](https://cloudinary.com/)
- [RedBag API (Java)](https://github.com/MateusOK/Redbag.git) (must be running for full functionality)

### **Cloning the Repository**

Clone this project to your local machine:

```bash
git clone https://github.com/MateusOK/RedBag-Python-API.git
```

After cloning, navigate to the project directory and install dependencies:

```bash
cd RedBag-Python-API
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

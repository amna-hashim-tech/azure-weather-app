#  Azure Weather App

A simple **serverless weather app** built with **Azure Functions (Python)** and **Azure Static Website Hosting**.  
It fetches live weather data from the **OpenWeather API** and displays it in a clean, responsive UI.  

---

## Live Demo
👉 [View App](https://amnaweatherstore123.z13.web.core.windows.net/)  

---

## ✨ Features
- 🌍 Search weather by **city name**
- 📍 Auto-detects your **current location** using browser geolocation
- 🌤️ Displays real-time **temperature, conditions, and weather icons**
- ⚠️ Clear error messages (e.g., “City not found”)
- ☁️ **Serverless backend** (Azure Functions)
- 🌐 **Frontend hosted on Azure Storage (Static Website)**

---

## 🛠️ Tech Stack
- **Backend:** Azure Functions (Python 3.10)
- **Frontend:** HTML, CSS, JavaScript
- **API:** [OpenWeather](https://openweathermap.org)
- **Hosting:** Azure Storage Static Website



## ⚙️ Setup & Run Locally

### 1. Clone Repo
```bash
git clone https://github.com/amna-hashim-tech/azure-weather-app.git
cd azure-weather-app
2. Backend Setup (Azure Function)
bash
Copy code
pip install -r requirements.txt
func start
Function runs locally at:

bash
Copy code
http://localhost:7071/api/weather?city=London
3. Frontend Setup
Simply open index.html in your browser,
or upload to Azure Static Website Hosting.

🚀 Deployment
Backend (Azure Functions)
bash
Copy code
func azure functionapp publish amnaweatherfunc123 --build remote
Frontend (Static Website)
bash
Copy code
az storage blob upload \
  --account-name amnaweatherstore123 \
  --container-name '$web' \
  --name index.html \
  --file index.html \
  --overwrite \
  --account-key "YOUR_STORAGE_KEY"
📌 Future Improvements
⏭️ Add 5-day weather forecast

🌈 Animated weather backgrounds

📱 Mobile responsive design

🔒 Secure API key with Azure Key Vault

🤖 Automate deployment with GitHub Actions

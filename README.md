
# 📘 Currency Converter - FastAPI Project

A simple **Currency Converter** web application built with **FastAPI** that allows you to:
- Convert currencies in real-time using a **free API**.
- View the **top 5 strongest** and **top 5 weakest** currencies against **USD**.
- Smooth and responsive **UI** with dropdowns for easy selection.

---

## 📌 Features
✅ Convert any currency to another in real-time.  
✅ Display **conversion result** instantly on the same page.  
✅ View the **Top 5 Strongest** and **Top 5 Weakest** currencies.  
✅ Handles **fallback API** if the primary API fails.  
✅ Fully responsive design using **HTML + CSS**.  
✅ Blazing fast with **Asynchronous HTTP requests** using `httpx`.

---

## 🛠️ Technologies Used
- **FastAPI** (Python Web Framework)
- **Jinja2** (Templating Engine)
- **httpx** (Async HTTP Requests)
- **HTML + CSS** (Frontend)
- **uvicorn** (ASGI Server)

---

## 📂 Project Structure
```
.
├── main.py                # FastAPI Application
├── static                 # Static Files (CSS, JS, Images)
│    └── styles.css        # Styling for the UI
└── templates              # HTML Templates
     └── index.html        # Main UI Template
```

---

## 🚀 Setup Instructions
1. **Clone the repository**:
```bash
git clone https://github.com/your-username/currency-converter-fastapi.git
cd currency-converter-fastapi
```

2. **Create a virtual environment** (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**:
```bash
pip install fastapi[all] httpx
```

4. **Run the FastAPI server**:
```bash
uvicorn main:app --reload
```

5. **Open the application**:  
Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📊 Usage
1. Select the **source currency** and **target currency** from the dropdown.
2. Enter the **amount** you want to convert.
3. Click on **Convert** and view the result instantly.
4. View **Top 5 Strongest** and **Top 5 Weakest** currencies against **USD**.

---

## 🔍 Example
- **Input**: 100 INR to USD  
- **Output**: `100 INR = 1.20 USD` (approx)

---

## 🧰 API Reference
This project uses the **Currency API** from `@fawazahmed0`:
- API Base URL:  
  - `https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1`
  - Fallback: `https://latest.currency-api.pages.dev/v1`

Example API Endpoints:
- Get all currencies:  
  `/currencies.json`
- Convert currency:  
  `/currencies/{currency_code}.json`

---

## 🤝 Contributing
1. **Fork** the repository.  
2. **Create** a new branch.  
3. **Commit** your changes.  
4. **Push** to your branch.  
5. Open a **Pull Request**.

---

## 📜 License
This project is licensed under the **MIT License**.  

---

## 🌟 Acknowledgements
Special thanks to:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Currency API](https://github.com/fawazahmed0/exchange-api)
- The open-source community! 💙

---

If you enjoy the project, give it a ⭐ on [GitHub](https://github.com/shubham31121999/Currency-Exchange)!

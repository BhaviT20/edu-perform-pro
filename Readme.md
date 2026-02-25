[🔗EduPerform Pro Dashboard](https://edu-perform-pro-gezd3swmj59sih5hblyhti.streamlit.app/)

# ⚡ EduPerform Pro | Intelligence Suite

**EduPerform Pro** is a high-end, glassmorphic educational dashboard designed for institutional administrators. It moves beyond traditional tracking by using predictive analytics and a modern "Deep Space" aesthetic to monitor faculty performance, task completion, and attrition risks.

---

## 🚀 Key Features

* **Executive Dashboard:** Real-time tracking of Staff Strength (62 members), Retention Risk, and Efficiency Indices.
* **Faculty Analytics:** Individual profiles with automated avatar generation and pedagogical competency radar charts.
* **Operational Pulse:** Interactive donut charts for real-time task completion monitoring.
* **Risk & Attrition Analysis:** A dedicated suite with sensitivity sliders to identify "at-risk" staff based on lateness and performance correlation.

---

## 🛠️ Technical Stack

### 🔹 Python (The Engine)
The core logic is built with **Streamlit**. It handles session state for secure authentication, routes navigation between modules, and processes data using **Pandas** and **NumPy**.
* **Predictive Logic:** Uses OLS Trendlines to correlate lateness with performance scores.
* **Authentication:** Integrated login system with session-based access control.

### 🔹 UI/UX Design (CSS & HTML)
This project features a complete visual overhaul that separates design from logic:
* **Glassmorphism:** A custom-built CSS suite utilizing `backdrop-filter: blur(15px)` and semi-transparent indigo surfaces.
* **Animations:** Implemented staggered "Slide-Up" entrance animations for a smooth, app-like experience.
* **Custom Components:** Re-engineered Streamlit containers to act as glowing "glass" modules.

### 🔹 Data Engineering
* **`academic_data.csv`:** The primary database containing teacher metrics, departmental scores, and incident logs.
* **`python_generate_data.py`:** A custom synthetic data engine created to simulate realistic variations in institutional performance (over 20% variation from standard templates).

---

## 📂 File Structure

| File | Description |
| :--- | :--- |
| **`app.py`** | The main application entry point and logic. |
| **`style.css`** | Custom design tokens and glassmorphic UI styling. |
| **`login_header.html`** | Custom HTML structure for the authentication portal. |
| **`academic_data.csv`** | The dataset fueling the visualizations. |
| **`python_generate_data.py`** | Script to generate or refresh synthetic faculty data. |
| **`requirements.txt`** | Dependency list (Streamlit, Pandas, Plotly, etc.). |

---

## 🔗 Access & Deployment

### **🌍 Live Demo**
> **URL:** [ https://share.streamlit.io/ ]  
> *The dashboard is hosted on Streamlit Cloud for real-time interaction.*

### **💻 Local Access**
If you are running the project on your machine:
1.  **Launch the app:** `streamlit run app.py`
2.  **Access URL:** [http://localhost:8501](http://localhost:8501)

### **🔐 Authentication Credentials**
To enter the Intelligence Suite, use the following administrative credentials:
* **Username:** `admin`
* **Password:** `admin`

---

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/BhaviT20/edu-perform-pro.git](https://github.com/BhaviT20/edu-perform-pro.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```


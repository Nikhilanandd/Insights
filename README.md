# 📊 Insights — Automated Insights & Data Visualizations

**Insights** is a Python-based web application that allows users to upload datasets (CSV/Excel) and automatically generates valuable insights and interactive visualizations. Built with **Flask** (for backend API) and **Streamlit** (for frontend UI), it leverages powerful open-source libraries like **Pandas**, **Plotly**, and **Seaborn** for seamless data processing and storytelling.

---
🔗 **[Live App on Streamlit](https://<your-app-URL>.streamlit.app)**  

---

## 🚀 Features

- Upload `.csv` or `.xlsx` datasets  
- Instantly generate:
  - Bar Charts  
  - Pie Charts  
  - Histograms  
- Enable optional charts with toggles:
  - Line Chart  
  - Box Plot  
  - Violin Plot  
  - Treemap  
  - Sunburst Chart  
  - Sankey Diagram  
  - Area Chart  
  - Scatter Plot  
  - Correlation Heatmap  
- Automatic dataset validation with user-friendly guidance  
- Generate and download PDF reports based on active visualizations  
- Clean, responsive multi-page interface

---

## 📂 Project Structure

```
InsightForge/
├── main.py                  # Entry point for Streamlit app
├── requirements.txt         # Required dependencies
├── uploads/                 # Uploaded dataset storage
├── visualizations/          # Saved chart images (optional)
├── src/
│   ├── app.py               # Flask backend (optional for API upload)
│   ├── data_processing/
│   │   └── analyze.py       # Core data reading and analysis functions
│   └── pages/
│       ├── Dashboard.py         # Main dashboard with visualizations
│       └── Generate_report.py   # PDF generation page
```

---

## 🛠️ Installation

### 🔗 Clone the Repository

```bash
git clone https://github.com/yourusername/insightforge.git
cd insightforge
```

### 📦 Install Dependencies

Using pip:

```bash
pip install -r requirements.txt
```

Or using [uv](https://github.com/astral-sh/uv):

```bash
uv pip install -r requirements.txt
```

---

## ▶️ Running the App

### Option 1: With Streamlit only

```bash
streamlit run main.py
```

### Option 2: Flask + Streamlit hybrid (if using backend API)

In separate terminals:

```bash
# Terminal 1
python src/app.py

# Terminal 2
streamlit run main.py
```

---

## 🧪 Sample Dataset

You can upload your own `.csv` or `.xlsx` files, or try any sample datasets from:

- [Kaggle Datasets](https://www.kaggle.com/datasets)  
- [Data.gov.in](https://data.gov.in)

---

## 📤 Export & Reports

- Navigate to the **Generate Report** page to export the visual dashboard as a clean PDF report.  
- Only charts currently displayed will be included in the exported report.

---

## 🤝 Contributing

We welcome contributions from the community!  
Feel free to fork the repo and open pull requests for:

- New visualizations  
- Performance improvements  
- UX/UI enhancements  
- Dataset compatibility fixes

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io) — UI Framework  
- [Flask](https://flask.palletsprojects.com/) — Backend Service  
- [Plotly](https://plotly.com/python/) — Interactive Visualizations  
- [Pandas](https://pandas.pydata.org/) — Data Analysis  
- [Seaborn](https://seaborn.pydata.org/) — Statistical Plots  
- [Kaleido](https://github.com/plotly/Kaleido) — Chart export engine

---

> Built with ❤️ to empower non-technical users to explore data visually and intuitively.

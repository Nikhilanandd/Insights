import pandas as pd
import matplotlib.pyplot as plt
import os

VISUALIZATION_FOLDER = "visualizations"
os.makedirs(VISUALIZATION_FOLDER, exist_ok=True)

def analyze_data(filepath):
    # Basic analysis
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)

    summary = df.describe().to_dict()
    return summary

def generate_visualizations(filepath):
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)

    filename = os.path.splitext(os.path.basename(filepath))[0]
    chart_filename = f"{filename}_chart.png"
    chart_path = os.path.join(VISUALIZATION_FOLDER, chart_filename)

    # Simple visualization (first two columns)
    if len(df.columns) >= 2:
        df.plot(x=df.columns[0], y=df.columns[1], kind='scatter')
        plt.title("Scatter Plot")
    else:
        df[df.columns[0]].value_counts().plot(kind='bar')
        plt.title("Bar Plot")

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path

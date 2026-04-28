# Sales Analysis Project

This project uses Python to analyze sales data and generate visual charts using machine learning.

## 🚀 Getting Started

### 1. Local Development (Virtual Environment)
If you want to run the code directly on your machine:

# Create the environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Install libraries
pip install -r requirements.txt

# Run the script
python src/main.py

---

### 2. Running with Docker
Use Docker to run the project in a locked, stable container.

# Build the image
docker build -t sales-analysis .

# Run the analysis and see the output files on your computer
docker run -v ${PWD}:/app sales-analysis

---

## 📦 Tech Stack
* **Python 3.10**
* **Pandas**: For data manipulation.
* **NumPy**: For numerical calculations.
* **Matplotlib**: For generating sales charts.
* **Scikit-learn**: For predictive analysis.

## 📊 Outputs
* The console will print the analysis summary.
* A file named `my_chart.png` (or your specific filename) will be generated in the root folder.
*
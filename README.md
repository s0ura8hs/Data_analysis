# Understanding the Basics of Data Analysis with Existing Datasets

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge\&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge\&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-teal?style=for-the-badge)

</div>

📌 Project Overview

This project focuses on understanding the fundamentals of **Data Analysis**, **Data Preprocessing**, and **Exploratory Data Analysis (EDA)** using two real-world datasets:

 Zomato Bengaluru Restaurant Dataset
 Delhi AQI (Air Quality Index) Dataset

The objective of this project is to apply practical data analysis techniques such as:

* Data Cleaning
* Handling Missing Values
* Feature Engineering
* Natural Language Processing (NLP)
* Statistical Analysis
* Data Visualization
* Correlation Analysis

The project was completed as part of the **IAPC Project (Semester IV)** at the **Cluster Innovation Centre, University of Delhi**. 

---

# 📂 Datasets Used

## 1️⃣ Zomato Bengaluru Restaurant Dataset

This dataset contains information about restaurants in Bengaluru including:

* Restaurant names
* Ratings
* Votes
* Cuisines
* Restaurant types
* Online ordering availability
* Table booking facilities
* Approximate cost
* Customer reviews

### Key Objectives

* Understand restaurant trends
* Analyze customer engagement
* Study relationship between ratings, votes, and pricing
* Identify top-performing restaurant types and locations

---

## 2️⃣ Delhi AQI Dataset (2020–2025)

This dataset contains environmental and atmospheric data such as:

* AQI
* PM2.5
* PM10
* NO₂
* SO₂
* CO
* O₃
* Temperature
* Humidity
* Wind Speed
* Visibility

### Key Objectives

* Analyze pollution trends
* Study relationships between pollutants
* Understand seasonal pollution behavior
* Explore meteorological impacts on AQI

---

# 🛠️ Technologies & Libraries Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Core programming language      |
| Pandas       | Data cleaning & manipulation   |
| NumPy        | Numerical computations         |
| Matplotlib   | Data visualization             |
| Seaborn      | Statistical plotting           |
| Scikit-learn | KNN Imputation & preprocessing |
| NLTK         | Natural Language Processing    |

---

# 🔍 Data Preprocessing Techniques

## ✔️ Data Cleaning

* Removed duplicate records
* Handled inconsistent formatting
* Removed unnecessary columns
* Cleaned textual data using regex

## ✔️ Missing Value Handling

* Mean/Median based filling
* KNN Imputation for numerical features

## ✔️ Feature Engineering

* Weighted rating score generation
* Numerical transformation of categorical data

## ✔️ NLP Processing

* Tokenization
* Stopword removal
* Lemmatization
* TF-IDF Vectorization

---

# 📊 Exploratory Data Analysis (EDA)

The project includes:

## 📈 Univariate Analysis

* Histograms
* Box plots

## 📉 Bivariate Analysis

* Scatter plots
* Relationship analysis

## 🔥 Multivariate Analysis

* Correlation heatmaps
* Feature relationship study

---

# 🍽️ Zomato Dataset Insights

## Key Findings

* Around **58%** of restaurants offer online ordering
* Only **11%** provide table booking
* **Microbreweries** had the highest average ratings
* Restaurants with higher ratings generally received more votes
* Most restaurants fall in the ₹300–₹500 price range
* **Lavelle Road** emerged as the top-rated location

## Important Observations

### ✔️ Online Ordering vs Customer Engagement

Restaurants offering online ordering generally received higher customer engagement and votes.

### ✔️ Table Booking vs Ratings

Restaurants with table booking facilities maintained higher average ratings.

### ✔️ Cost vs Votes

Mid-range restaurants showed maximum customer interaction.

---

# 🌫️ AQI Dataset Insights

## Key Findings

* **PM2.5** and **PM10** are the strongest contributors to AQI
* Visibility decreases as pollution increases
* Pollution peaks during winter and post-monsoon seasons
* Wind speed negatively correlates with AQI
* Ozone behaves differently compared to other pollutants

## Important Observations

### ✔️ AQI vs PM2.5 / PM10

Strong positive correlation observed between particulate matter and AQI.

### ✔️ Visibility vs Pollution

Visibility sharply decreases with increasing particulate concentration.

### ✔️ Pollutant Relationships

Most pollutants rise together due to common emission sources such as:

* Vehicular emissions
* Industrial activity
* Fossil fuel combustion

---

# 📷 Visualizations Included

The project contains multiple visualizations such as:

* Correlation Heatmaps
* Scatter Plots
* Histograms
* Box Plots
* Bar Charts

Examples:

* AQI vs PM2.5
* AQI vs PM10
* Visibility vs PM2.5
* Votes vs Ratings
* Restaurant Type vs Ratings
* Cost vs Customer Engagement

---

# 📚 Concepts Learned

Through this project, the following concepts were explored practically:

* Data Analysis Workflow
* Data Preprocessing
* Statistical Analysis
* Correlation Analysis
* Exploratory Data Analysis
* Feature Engineering
* Natural Language Processing
* Data Visualization

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Data_analysis.git
cd Data_analysis
```

## 2️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk
```

## 3️⃣ Run the Notebook / Python Files

```bash
python main.py
```

or open the Jupyter Notebook:

```bash
jupyter notebook
```

---

# 📁 Project Structure

```bash
Data_analysis/
│
├── datasets/
│   ├── zomato.txt
│   └── delhi_aqi.txt
│
├── notebooks/
│   ├── zomato_analysis.py
│   └── aqi_analysis.py
│
├── visualizations
│
├── README.md
└── requirements.txt
```

---

# 🎯 Conclusion

This project successfully demonstrates how real-world datasets can be cleaned, processed, analyzed, and visualized to extract meaningful insights.

The Zomato dataset helped understand customer behavior and restaurant trends, while the AQI dataset provided insights into pollution patterns and environmental relationships.

The project also provided hands-on experience with:

* Python-based data analysis
* EDA techniques
* Visualization tools
* Data preprocessing methods
* Statistical interpretation

---

# 👨‍💻 Contributors

* Chitranshi Kumre
* Sanskar Dwivedi
* Abhinav Saini
* Sourabh
* Uday Khichar

Mentor: **Prof. Shobha Bagai**

Cluster Innovation Centre, University of Delhi

---

# 📖 References

* Kaggle Datasets
* Pandas Documentation
* NumPy Documentation
* Matplotlib Documentation
* Scikit-learn Documentation
* NLTK Documentation

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!

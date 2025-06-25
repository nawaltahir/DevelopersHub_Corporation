# DevelopersHub_Corporation
AI/ML Internship tasks
# Task 1: Iris Dataset Exploration and Classification

## Task Objective
This project aims to explore the Iris dataset, visualize feature distributions and relationships, and apply basic machine learning models to classify iris flower species based on their sepal and petal measurements.

---

## Dataset Used
- **Name**: Iris Dataset
- **Source**: Built-in dataset from Seaborn or available via UCI Machine Learning Repository
- **Features**:
  - `sepal_length` (cm)
  - `sepal_width` (cm)
  - `petal_length` (cm)
  - `petal_width` (cm)
  - `species` (target variable with 3 classes: *setosa*, *versicolor*, *virginica*)

---

## Data Exploration
- Inspected data with `.head()`, `.info()`, and `.describe()`
- Visualizations created:
  - Pair plot (species clusters)
  - Correlation heatmap (strong correlation between petal features)
  - Box plots and violin plots (outliers and distribution shapes)
  - Andrews curves (high-dimensional visualization)
  - Scatter plots for sepal and petal dimensions

---

## Models Applied
- **K-Nearest Neighbors (k-NN)** for classification
  - Visualized decision boundaries using 2D features (`petal_length`, `petal_width`)
- (Optional) Logistic Regression or SVM can also be applied for boundary comparison

---

## Key Results and Findings
- **Setosa** is separable from the other species using both sepal and petal features.
- **Petal length and width** are the most informative features for classification.
- **Versicolor and Virginica** show partial overlap, especially when using only sepal dimensions.
- k-NN model with `petal_length` and `petal_width` achieves clear class boundaries with minimal overlap.

---


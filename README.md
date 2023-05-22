# User Keystroke Classification

User Keystroke Classification is a Python package that leverages machine learning to distinguish users based on their keystroke patterns.

## Description

User Keystroke Classification is a project that classifies users based on their typing behavior. By collecting and analyzing keystroke dynamics, such as key press durations, intervals, and key combinations, the project builds a machine learning model using XGBoost to classify if two keystroke patterns are from the same user or different users.

This repository contains the source code, example notebooks, and utilities for the User Keystroke Classification project.

## Docker Setup

To run the project inside a Docker container, follow these steps:

1. Make sure you have Docker installed on your machine. If not, you can download and install it from the official website: [https://www.docker.com/](https://www.docker.com/)

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/trabbani/user-keystroke-classification.git
   ```

3. Navigate to the project directory:

   ```bash
   cd user-keystroke-classification
   ```

4. Build the Docker image:

   ```bash
   docker build -t user-keystroke-classification -f docker/Dockerfile .
   ```

5. Run a Docker container from the image:

   ```bash
   docker run -p 8888:8888 user-keystroke-classification
   ```

6. Access the Jupyter notebook server by opening your web browser and navigating to `http://localhost:8888/?token=demo`. The notebooks can be found in the `notebooks/demo` directory.

## Local Installation

To install the User Keystroke Classification package in a virtual environment, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/trabbani/user-keystroke-classification.git
   ```

2. Navigate to the project directory:

   ```bash
   cd user-keystroke-classification
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Linux/Mac:

     ```bash
     source venv/bin/activate
     ```


5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   pip install .
   ```

6. You can now use the User Keystroke Classification package in your Python environment.

## Notebooks

The following notebooks are available in the `notebooks/demo` directory:

- **Data Demo**: [demo_data.ipynb](notebooks/demo/demo_data.ipynb)
  This notebook provides a demonstration of the data loading and viewing steps.

- **Training**: [demo_training.ipynb](notebooks/demo/demo_training.ipynb)
  This notebook demonstrates how to train the XGBoost model using the raw keystroke data.

- **Metrics for Balanced Data**: [demo_balanced_metrics.ipynb](notebooks/demo/demo_balanced_metrics.ipynb)
  This notebook showcases the evaluation metrics and performance analysis for the model trained on balanced data.

- **Metrics for Rare Positive Instances**: [demo_minority_metrics.ipynb](notebooks/demo/demo_minority_metrics.ipynb)
  This notebook focuses on the evaluation metrics and performance analysis for the model trained on imbalanced data with rare positive instances.

It is suggested to follow the order mentioned above when browsing the notebooks to understand the workflow and the analyses performed.


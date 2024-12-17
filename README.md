# House Price Prediction and Classification Project

## Project Overview
This project aims to develop two machine learning models:

### 1. **Feature Engineering**:
   - **File**: `House_Project_Feature_Engineering.ipynb`
   - **Description**: In this file, I performed a variety of feature engineering actions including dropping columns, filling null values, and transforming data into a suitable format. The preprocessing step was crucial in preparing the data for further analysis and model training. This file serves as a foundation for the data cleaning and transformation processes.

### 2. **Regression Model Training**:
   - **File**: `House_Project_Regression_Model_Training.ipynb`
   - **Algorithms**: Utilized various algorithms such as Linear Regression, regularization techniques including L1, L2, and Elastic Net, K-Nearest Neighbors, Decision Trees, Random Forests, Support Vector Machines, Gradient Boosting, and AdaBoost.
   - **Process**:
     - **Data Scaling**: Implemented `StandardScaler` to train models with scaled training data.
     - **Hyperparameter Tuning**: Used cross-validation to find the best hyperparameters for each algorithm.
     - **Evaluation Metrics**: Measured performance using Mean Absolute Error and Root Mean Squared Error. Visualizations were used to compare and select the best-performing model.
     - **Outcome**: The best-performing model was fine-tuned and saved as `final_regression_model.joblib`.

### 3. **Classification Model Training**:
   - **File**: `House_Project_Classification_Model_Training.ipynb`
   - **Algorithms**: Implemented algorithms such as Logistic Regression, Support Vector Machines, K-Nearest Neighbors, Decision Trees, Random Forests, Gradient Boosting, and AdaBoost.
   - **Process**:
     - **Data Scaling**: Applied `StandardScaler` to train models with scaled training data.
     - **Hyperparameter Tuning**: Used cross-validation to determine the best hyperparameters for each algorithm.
     - **Evaluation Metrics**: Performance was measured using Accuracy Score, Precision Score, Recall Score, F1 Score. Results were visually represented using the Classification Report and Confusion Matrix.
     - **Outcome**: The top-performing model was selected, tuned, and saved as `final_classification_model.joblib`.

### 4. **Models Tester**:
   - **File**: `models-tester.ipynb`
   - **Description**: This file includes two converters, `converter_regression.py` and `converter_classification.py`, which transform user input into a format that the models can understand. More details about these converters can be found in the `models-tester.ipynb` file.
   - **Testing**: I created a few test samples, converted them using the converters, and used the models to make predictions based on the input.

## Organization
   - **Models Folder**: Contains the machine learning models (`final_regression_model.joblib` and `final_classification_model.joblib`).
   - **Data Folder**: Includes all datasets and relevant files. For a better understanding of the dataset, it is recommended to read the `Housing_Feature_Description.txt` file.

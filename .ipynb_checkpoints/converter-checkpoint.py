import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dummies_converter(my_value):
    df = pd.read_csv('C:\\Users\\jovan\\Desktop\\HouseProject\\House_Price_Prediction_-_Classification\\Data\\Housing_Data_Helper_Function.csv')
    df = df.drop('Unnamed: 0', axis=1)
    
    # If the dataset has a 'SalePrice' column, we drop it from the input row
    if 'SalePrice' in df.columns:
        df = df.drop('SalePrice', axis=1)

    # Add the new input row (without SalePrice)
    df.loc[len(df)] = my_value

    # Handling missing values for string and numeric columns
    str_cols_bsmt = ['Bsmt Qual', 'Bsmt Cond', 'BsmtFin Type 1', 'BsmtFin Type 2', 'Bsmt Exposure']
    str_cols_gar = ['Garage Type', 'Garage Cond', 'Garage Qual', 'Garage Finish']
    df[str_cols_bsmt] = df[str_cols_bsmt].fillna('None')
    df[str_cols_gar] = df[str_cols_gar].fillna('None')
    
    num_cols = ['Garage Yr Blt']
    df[num_cols] = df[num_cols].fillna(0)
    df['Fireplace Qu'] = df['Fireplace Qu'].fillna('None')

    # Generate dummy variables
    dummies = pd.get_dummies(data=df, drop_first=True)

    # Drop specific columns if needed
    dummies = dummies.drop('Neighborhood_Blmngtn', axis=1)
    dummies = dummies.drop('Sale Type_WD', axis=1)

    # Convert the last row (newly added) to an array
    my_row = dummies.iloc[-1]
    my_row_converted = my_row.values
    my_row_converted = my_row_converted.reshape(1, -1)

    # Return the transformed row
    return my_row_converted
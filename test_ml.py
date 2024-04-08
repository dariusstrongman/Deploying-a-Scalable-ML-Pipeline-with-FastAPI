import pytest
import pandas as pd
from ml.data import process_data
from ml.model import train_model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_Random_Forest_model_verification():
    
    """
    Verfies that model type returned from pipeline is a Random Forest
    """
    path = './data/census.csv'
    data = pd.read_csv(path)
    
    train, test = train_test_split(data,
                              test_size = 0.20,
                              random_state= 42)
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    
    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features = cat_features,
        label = 'salary',
        training = True
        )
    
    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )
    model = train_model(X_train,y_train)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_input_data_length():
    """
    Checks that input length is greater than 3,000
    """
    path = './data/census.csv'
    input = pd.read_csv(path)
    
    assert len(input) > 3000
    


# TODO: implement the third test. Change the function name and input as needed
def test_precision_output():
    """
    Ensure precision output to slice_ouput was excuted sucessfully
    """
    with open('slice_output.txt','r') as f:
        text = f.read()
    assert len(text) > 0
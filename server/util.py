import json
import pickle
import numpy as np

__data_columns=None
__model=None

def load_saved_artifacts():
    print("Loading saved artifacts...")

    global __data_columns
    global __model

    with open("artifacts/rent_columns.json", "r") as f:
        __data_columns=json.load(f)['data_columns']

    with open("artifacts/rent_random_forest_model.pickle", "rb") as f:
        __model=pickle.load(f)

    print("Artifacts loaded successfully!")  

def get_city_names():
    return __data_columns[4:]  

def get_estimated_rent(city, area, beds, bathrooms, furnishing):
    try:
        city_index = __data_columns.index(city) 

    except:
        city_index=-1

    x=np.zeros(len(__data_columns))         

    x[0] =area
    x[1] =beds
    x[2]=bathrooms
    x[3]=furnishing


    if city_index >= 0:
        x[city_index] = 1

    return round(float(__model.predict([x])[0]), 2)
#here 2 is to convert the float value upto 2 decimal
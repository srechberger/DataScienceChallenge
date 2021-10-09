import pandas as pd

def load_data():
 
    """Filepaths"""
    data_file_path = "data/ntuity_datascience_challenge.csv"
    
    """Load data"""
    data = pd.read_csv(data_file_path)

    return data
    
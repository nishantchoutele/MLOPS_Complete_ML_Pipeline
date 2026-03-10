import pandas as pd
import os 
from sklearn.model_selection import train_test_split
import logging

#Ensures the "logs" directories exists
log_dir = 'logs'
os.makedirs (log_dir, exist_ok=True)

#logging configuration
logger = logging.getLogger('data_injestion')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_injestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_data(data_url: str) -> pd.DataFrame:
    """Load data from data frame"""
    try:
        df = pd.read_csv(data_url)
        logger.debug('Data loaded from %s', data_url)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the csv file: %s',e)
        raise
    except Exception as e :
        logger.error('Unexpected error occured while loading the data: %s', e)
        raise
#PREPROCESSING 46:41

    
import os
import json
import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
date_format = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt=date_format)
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
LOGGER.addHandler(ch)

def main():
    
    LOGGER.info('Loading Kaggle API Key')
    kaggle_api_key = os.environ.get('KAGGLE_API_KEY')
    if not kaggle_api_key:
        raise Exception('Could not find Kaggle API Key. Please make sure that the key is provided as a GitHub secret under the name "KAGGLE_API_KEY"')
        
    LOGGER.info('Reading Kaggle API Key as json')
    try:
        kaggle_json = json.loads(kaggle_api_key)
    except json.decoder.JSONDecodeError as e:
        raise Exception('Failed to read API key as JSON.')
        
    LOGGER.info('Writing Kaggle API Key into json')
    try:
        with open('.kaggle/kaggle.json', 'w') as f:
            json.dump(kaggle_json, f)
    except Exception as e:
        raise Exception('Could not write API key to file')
    
if __name__ == '__main__':
  main()

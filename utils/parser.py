import json

def parse_kaggle_output(filename):
    output_str = ''
    with open(f'{filename}.log', 'r') as f:
        json_output = json.load(f)
        for line in json_output:

            output_str += line.get('data')

import os
import json

GIT_USERNAME, GIT_REPO_NAME = os.environ.get('REPO_NAME').split('/')
GIT_ACCESS_TOKEN = os.environ.get('GIT_ACCESS_TOKEN')
TEST_FOLDER = os.environ.get('TEST_FOLDER')

JOB_FILE_NAME = 'job.py'

# need to think of a better way of doing this... you are showing the key within Kaggle this way. Maybe better to push a dataset of the tests?
JOB_LINES = [
  'import os',
  'import subprocess',
  #f'!git clone https://{GIT_ACCESS_TOKEN}@github.com/{GIT_USERNAME}/{GIT_REPO_NAME}',
  #'!pip install .',
  #f'!pytest {GIT_REPO_NAME}/{TEST_FOLDER}'
  f'os.system("git clone https://{GIT_ACCESS_TOKEN}@github.com/{GIT_USERNAME}/{GIT_REPO_NAME}")',
  f'os.chdir("{GIT_REPO_NAME}")',
  'os.system("pip install .")',
  f'return_code = os.system("pytest {TEST_FOLDER}")',
  'if return_code: raise Exception("tests failed.")'
]

def prepare_metadata_file():
  
  with open('kernel-metadata.json', 'r') as f:
    metadata_file = json.load(f)
    
  metadata_file['id'] = '/'.join([metadata_file['id'].split('/')[0], GIT_REPO_NAME])
  metadata_file['title'] = GIT_REPO_NAME
  metadata_file['code_file'] = JOB_FILE_NAME
  metadata_file['language'] = 'python'
  metadata_file['kernel_type'] = 'script'
  metadata_file['enable_gpu'] = True
  
  with open('kernel-metadata.json', 'w') as f:
    json.dump(metadata_file, f)

def prepare_job_file():
  with open(JOB_FILE_NAME, 'w') as f:
    f.write('\n'.join(JOB_LINES))

    
def main():
  prepare_metadata_file()
  prepare_job_file()  
  
  
if __name__ == '__main__':
  main()

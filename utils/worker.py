import os
import time
import subprocess
from utils

SLEEP_TIME = 5
GIT_REPO_NAME = os.environ.get('REPO_NAME').split('/')[-1]

def main():
  while True:
    
    output = subprocess.check_output(['kaggle', 'kernels', 'status', GIT_REPO_NAME])
    output = output.decode("utf-8")
    print(output)
    if 'error' in output:
      print('Test failed. Full logs below:')
      # download outputs in log file
      
      output = subprocess.check_output(['kaggle', 'kernels', 'output'])
      # raise an exception (make sure the logs show)
      break
    elif 'success':
      print('Kaggle Integration Test SUCCESS')
      break
    else:
      time.sleep(SLEEP_TIME)

if __name__ == '__main__':
  main()

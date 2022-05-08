import os
import time
import subprocess
from parser import parse_kaggle_output

SLEEP_TIME = 5
GIT_REPO_NAME = os.environ.get('REPO_NAME').split('/')[-1]

def main():
  while True:
    
    output = subprocess.check_output(['kaggle', 'kernels', 'status', GIT_REPO_NAME])
    output = output.decode("utf-8")
    if 'error' in output:
      print('FAIL: Test(s) failed. Full logs below:')
      # download outputs in log file
      output = subprocess.check_output(['kaggle', 'kernels', 'output'])
      parse_kaggle_output(GIT_REPO_NAME)
      break
    elif 'success':
      print('SUCCESS: Kaggle Integration Tests')
      break
    else:
      time.sleep(SLEEP_TIME)

if __name__ == '__main__':
  main()

import os
import time
import subprocess

SLEEP_TIME = 5
GIT_REPO_NAME = os.environ.get('REPO_NAME').split('/')[-1]

def main():
  while True:
    
    output = subprocess.check_output([f'kaggle kernels status {GIT_REPO_NAME}'])
    if 'error' in output:
      # get logs
      # output the logs
      # raise an exception (make sure the logs show)
      break
    elif 'success':
      # double check this
      # but if success write message and then end the loop
      break
    else:
      time.sleep(SLEEP_TIME)

if __name__ == '__main__':
  main()

import os
GIT_REPO_NAME = os.environ.get('REPO_NAME').split('/')[-1]

def main():
  while True:
    
    output = subprocess.check_output([f'kaggle kernels status {GIT_REPO_NAME}'])
    break
  print(output)

if __name__ == '__main__':
  pass

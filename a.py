import random
def main()->None:
  with open('out','w') as f:
    f.write(str(random.random()))
if __name__=='__main__':
  main()

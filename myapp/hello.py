import fire
import time

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
  for i in range(5):
    print(i)
    time.sleep(2)

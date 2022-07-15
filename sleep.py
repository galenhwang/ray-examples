import ray
import time


@ray.remote
def hello_world():
    time.sleep(120) # 2 min
    return "Hello World!"


result = ray.get(hello_world.remote())
print(result)

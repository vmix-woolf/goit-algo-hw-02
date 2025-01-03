from queue import Queue
import time, random

q = Queue()

def generate_request():
    request_id = random.randint(1, 100)
    print(f"Request {request_id} is created")
    q.put(request_id)

def process_request():
    if not q.empty():
        request_id = q.get()
        print(f"Request {request_id} is processing...")
        time.sleep(1)
        print(f"Request {request_id} is processed")
    else:
        print("Queue is empty")


if __name__ == "__main__":
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(random.uniform(0.5, 2))
    except KeyboardInterrupt: # Ctrl + C for exiting
        print("Handling interrupted by user")

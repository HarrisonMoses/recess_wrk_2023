"""
Context managers,  Multithreading and Multiprocessing

a) Show a context manager for file handling that automatically opens and closes a file.
b) Shows a context manager for managing a database connection.
c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time


"""
# Context manager: Context Managers: Context managers in Python are objects that define the methods __enter__() and 
#  __exit__() which enable them to be used with the with statement.

# Multithreading is a programming technique that allows multiple threads of execution to run concurrently within a single process
# Multiprocessing is a programming technique that allows multiple processes to run concurrently on a computer.


#a) Show a context manager for file handling that automatically opens and closes a file.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage example
with FileManager("phones.json", "w") as file:
    file.write("Samsung, iPhone, Nokia")





#b) Show a context manager for managing a database connection.
from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()


with MongoDBManager("localhost", 27017, "mydatabase") as db:
    collection = db["mycollection"]
    document = {"name": "Byansi Anthony", "age": 30}
    result = collection.insert_one(document)
    print(f"Inserted document with ID: {result.inserted_id}")








# Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time

import time
import threading
from multiprocessing import Pool

def worker_function(seconds):
    print(f"Starting worker for {seconds} seconds")
    time.sleep(seconds)
    print(f"Worker finished after {seconds} seconds")


# Using multithreading
thread1 = threading.Thread(target=worker_function, args=(2,))
thread2 = threading.Thread(target=worker_function, args=(4,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


pool = Pool(processes=2)
pool.apply_async(worker_function, (2,))
pool.apply_async(worker_function, (4,))
pool.close()
pool.join()



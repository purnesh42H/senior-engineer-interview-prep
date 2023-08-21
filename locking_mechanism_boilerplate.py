'''
- There is critical resource which has to be accessed in a distributed environment
- System supports N concurrent request to access the resource but beyond N, caller have to wait
- There are M callers which can make any number of requests at any time
- Implemement a locking mechanism to handle this usecase
'''

import threading

class LockingMechanism(object):
    
    def __init__(self, max_concurrent_requests):
        self.semaphore = threading.Semaphore(max_concurrent_requests)

    def access_critical_resource(self, caller):
        self.semaphore.acquire()
        try:
            print("Critical resource accessed by caller " + str(caller))
        finally:
            self.semaphore.release()

def caller_function(locking_mechanism, caller):
    locking_mechanism.access_critical_resource(caller)


if __name__ == "__main__":
    max_concurrent_requests = 3
    num_callers = 10

    locking_mechanism = LockingMechanism(max_concurrent_requests=max_concurrent_requests)

    threads = []
    for i in range(num_callers):
        thread = threading.Thread(target=caller_function, args=(locking_mechanism, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


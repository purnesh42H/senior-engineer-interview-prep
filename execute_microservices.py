import time
import unittest
from collections import defaultdict
from queue import Queue

'''
There are some tasks/microservices n1, n2, n3, n4 etc. You will be given a dependency list
- [(n1, n2), (n2, n3)] signifying n1 depends on n2 and n2 depends on n3 and so on.
- Every task/microservice needs time to execute. The time for task/microservice is t1, t2, t3, t3 for n1, n2, n3 and n4 respectively.
- The task is to find the minimum time to complete all tasks.
'''

class Microservice(object):

    def __init__(self, id, t):
        self.id = id
        self.t = t
        self.finished = False

    def execute(self):
        self.finished = False
        time.sleep(self.t)
        print("Executed service " + self.id)
        self.finished = True

class MicroserviceExecutor(object):

    def __init__(self, microservices):
        self.microservices = defaultdict(Microservice)
        self.dependency_map = defaultdict(list)
        self.execution_queue = Queue()
        
        self._build_microservices(microservices)

    def get_minimum_time_execute(self, dependencies):
        self._build_dependency_map(dependencies)
        
        remaining_dependencies = self._get_remaining_dependencies_map()
        times = self._queue_services_ready_to_execute(remaining_dependencies)

        while self.execution_queue.qsize() > 0:
            executed_services = self._execute_services()
            self._queue_next_services_to_execute(remaining_dependencies, executed_services, times)

        return max(times.values())
    
    def _queue_next_services_to_execute(self, remaining_dependencies, executed_services, times):
        for cur_service_id in executed_services:
            if cur_service_id not in self.dependency_map:
                continue

            for dependent in self.dependency_map[cur_service_id]:
                remaining_dependencies[dependent] -= 1
                if remaining_dependencies[dependent] == 0:
                    if dependent not in times:
                        times[dependent] = times[cur_service_id] + self.microservices[dependent].t
                    else:
                        times[dependent] = max(times[dependent], times[cur_service_id] + self.microservices[dependent].t)
                    
                    self.execution_queue.put(dependent)
    
    def _execute_services(self):
        executed_services = []
        while self.execution_queue.qsize() > 0:
            cur_service_id = self.execution_queue.get()
            # async execute cur_serivce_id microservice
            executed_services.append(cur_service_id)

        return executed_services
    
    def _queue_services_ready_to_execute(self, remaining_dependencies):
        times = defaultdict(int)

        for service_id in remaining_dependencies:
            if remaining_dependencies[service_id] == 0:
                self.execution_queue.put(service_id)
                times[service_id] = self.microservices[service_id].t

        return times
    
    def _get_remaining_dependencies_map(self):
        remaining_dependencies = defaultdict(int)

        for microservice_id in self.microservices:
            remaining_dependencies[microservice_id] = 0
        
        for (_, dependents) in self.dependency_map.items():
            for dependent in dependents:
                remaining_dependencies[dependent] += 1

        return remaining_dependencies
    
    def _build_dependency_map(self, dependencies):
        self.dependency_map.clear()
        
        for (dependent, depenedent_on) in dependencies:
            self.dependency_map[depenedent_on].append(dependent)

    def _build_microservices(self, microservices):
        for (id, t) in microservices:
            self.microservices[id] = Microservice(id, t)

class MicroserviceExecutorTest(unittest.TestCase):

    def test_get_minimum_time_execute(self):
        executor = MicroserviceExecutor([["s1", 3], ["s2", 5], ["s3", 1], ["s4", 2]])

        dependencies = []
        self.assertEqual(5, executor.get_minimum_time_execute(dependencies=dependencies))

        dependencies = [["s1", "s3"], ["s1", "s4"], ["s3", "s2"]]
        self.assertEqual(9, executor.get_minimum_time_execute(dependencies=dependencies))

        dependencies = [["s1", "s4"], ["s3", "s2"]]
        self.assertEqual(6, executor.get_minimum_time_execute(dependencies=dependencies))

if __name__  == "__main__":
    unittest.main()
        
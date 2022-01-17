""" Day 7: The Sum of Its Parts.


"""
import sys

from collections import defaultdict

REQUIRED_IDX = 1
STEP_IDX = 7

def construct_dag():
    """ Translate textual input into dictionary with requirements
    as keys.

    """
    graph = defaultdict(list)
    vertices = set()

    instructions = sys.stdin.readlines()
    for instruction in instructions:
        required, step = tuple(instruction.split()[i] for i in [REQUIRED_IDX, STEP_IDX])

        graph[required].append(step)
        vertices.add(required)
        vertices.add(step)

    return graph, vertices

def initialize_sorting(graph, vertices):
    """ Getting the number of dependencies and initial queue ready
    for topological sorting. """
    dependencies = {v: 0 for v in vertices}
    for i in graph:
        for j in graph[i]:
            dependencies[j] += 1

    queue = [v for v in vertices if dependencies[v] == 0]
    queue.sort()
    return queue, dependencies

def update_queue(subtasks, queue, dependencies):
    """ Remove dependencies after task is sorted, and add to queue. """
    for step in subtasks:
        dependencies[step] -= 1
        if dependencies[step] == 0:
            queue.append(step)
    queue.sort()

def topological_sort(graph, queue, dependencies):
    """ Return the topological order from a graph with the
    initial queue and depencies provided.

    """
    topological_order = []
    while queue:
        task = queue.pop(0)
        topological_order.append(task)

        update_queue(graph[task], queue, dependencies)
    return topological_order

def get_instructions_order(graph, vertices):
    """ Lexicographical topological sort.

    """
    return "".join(topological_sort(graph, *initialize_sorting(graph, vertices)))

def find_idle(workers):
    """ Return the index of the first idle worker in list. """
    for i, worker in enumerate(workers):
        if not worker.task:
            return i
    return -1

def task_time(task):
    """ Return the amount of seconds needed to complete the task. """
    return ord(task) - 64 + BASETIME_PER_STEP

class Worker:
    def __init__(self):
        self.task = None
        self.time_left = 0

def assign_tasks(workers, queue):
    while queue:
        i = find_idle(workers)
        if i < 0:
            break

        task = queue.pop(0)
        workers[i].task = task
        workers[i].time_left = task_time(task)

def update_task_state(workers, queue, tasks_done, graph, dependencies):
    """ Housekeeping at end of time step:

    All working workers get their times updated.
    The queue is updated with the recently finished task's children.
    The count of finished tasks is increased.

    """
    for worker in workers:
        if worker.task:
            worker.time_left -= 1
            if worker.time_left == 0:
                update_queue(graph[worker.task], queue, dependencies)
                tasks_done += 1
                worker.task = None
    return tasks_done

def get_assembly_time(number_of_workers, graph, vertices):
    """ Return the assembly time needed with the number of workers given."""
    queue, dependencies = initialize_sorting(graph, vertices)
    workers = [Worker() for i in range(number_of_workers)]

    time = 0
    tasks_done = 0
    while True:
        assign_tasks(workers, queue)

        time += 1

        tasks_done = update_task_state(workers, queue, tasks_done, graph, dependencies)

        if tasks_done == len(vertices):
            return time

NUMBER_OF_WORKERS = 5
BASETIME_PER_STEP = 60
DAG = construct_dag()

# Part 1
print("Order of instructions:\n\t",
      get_instructions_order(*DAG))

# Part 2
print("Number of seconds for assembly:\n\t",
      get_assembly_time(NUMBER_OF_WORKERS, *DAG))

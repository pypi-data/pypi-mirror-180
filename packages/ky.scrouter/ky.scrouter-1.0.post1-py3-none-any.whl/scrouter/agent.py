from threading import Thread
from . import worker
from multiprocessing import cpu_count
import time
import sys
import os
from random import randint

_THREADS_MAX = cpu_count()

progress_counter = 0
last_processed = 'Unknown'


def threaded_worker(routing_graph, routing_queue, user_to):
    while True:
        try:
            found, queued = worker.explore_worker(routing_queue.pop(0))
        except IndexError:
            continue
        for new_node in found:
            if new_node not in routing_graph.keys():
                routing_graph[new_node] = queued
            routing_queue.append(new_node)
        global progress_counter, last_processed
        progress_counter += 1
        last_processed = queued
        if user_to in routing_graph.keys():
            break


def route(user_from: str, user_to: str) -> None:
    """Main function.

    Works as a direct executor, returns nothing."""

    print('Input validation...')
    if user_to == user_from:
        print(f'Traced route: {user_from} ↔ {user_to}')
    if not (worker.check_worker(user_from) or worker.check_worker(user_to)):
        print('ROUTING FAILED! Invalid one or both usernames.')

    # initial data
    routing_graph = {}
    routing_queue = [user_from]

    # create threaded workers
    threads = []
    for i in range(_THREADS_MAX - 1):
        threads.append(Thread(target=threaded_worker, args=(
            routing_graph, routing_queue, user_to)))
        threads[-1].start()

    # wait stable connections
    init_time = time.time_ns()
    print('Workers preparation...')
    while not progress_counter > 0:
        pass

    # progress output
    os.system('')  # enable ansi codes
    while not user_to in routing_graph.keys():
        time.sleep(0.2)
        uptime = round((time.time_ns() - init_time) / 1e9, 1)
        sys.stdout.write('\033[F\033[K' * 4)
        print(f'{len(routing_queue)} positions in queue...\n'
              f'{progress_counter} processed positions...\n'
              f'{round(progress_counter / uptime, 2)} positions per second...\n'
              f'{last_processed} is last processed...\n'
              f'Uptime {uptime} seconds...', end='')
    print('')

    # make list with a route based on routing_graph
    def recursively_disclose_route(sequent, rt=None) -> list:
        if rt is None:
            rt = []
        if not sequent == user_from:
            recursively_disclose_route(routing_graph[sequent], rt).append(sequent)
        else:
            rt.append(user_from)
        return rt

    print('Traced route:', ' >> '.join(recursively_disclose_route(user_to)))

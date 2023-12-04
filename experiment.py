import sys, threading
import time
from util import file_to_data
from memory_profiler import memory_usage
from greedy import set_cover
from branch_and_bound import BB


def experiment_cover(cover_func, data):
    memory_usages = memory_usage((time_experiment_cover, (cover_func, data)), max_iterations=1)
    print(f'{max(memory_usages)} MB')


def time_experiment_cover(cover_func, data):
    start_time = time.time()
    output = cover_func(data[0], data[1], data[2])
    end_time = time.time()
    print(f'cost = {output[1]}')
    print(f'{(end_time - start_time) * 1000} ms')


def main():
    sizes = ['small', 'medium', 'large']
    n_sets = [20, 25, 30]
    datasets = {}
    
    for size in sizes:
        for n in n_sets:
            datasets[f'{size}_{n}'] = file_to_data(f'./datasets/{size}_{n}.txt')
    
    for size in sizes:
        for n in n_sets:
            print(f'Greedy {size}_{n}')
            experiment_cover(set_cover, datasets[f'{size}_{n}'])
            print(f'Branch and Bound {size}_{n}')
            experiment_cover(BB, datasets[f'{size}_{n}'])


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()

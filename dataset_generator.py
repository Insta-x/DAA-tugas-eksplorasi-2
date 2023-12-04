from util import data_to_file
from random import randint

def random_set(size, low, high):
    return set([randint(low, high) for _ in range(size)])


def main():
    sizes = {
        'small' : 20,
        'medium' : 200,
        'large' : 2000,
    }
    
    for size in sizes:
        universe = set(range(1, sizes[size]+1))
        sets = []
        test_set = set()
        while test_set != universe:
            sets = []
            test_set = set()
            for i in range(20):
                x = random_set(randint(sizes[size] // 4, sizes[size] // 2), 1, sizes[size])
                sets.append(x)
                test_set |= x
        costs = [randint(1, 100) for _ in range(20)]
        data_to_file(f'./datasets/{size}.txt', sets, costs)


if __name__ == '__main__':
    main()
    print('Generated datasets')

def data_to_file(file_path, sets, costs):
    with open(file_path, 'w') as f:
        for i in range(len(sets)):
            for x in sets[i]:
                f.write(f'{x} ')
            f.write(f'{costs[i]}\n')


def file_to_data(file_path):
    universe = set()
    sets = []
    costs = []
    with open(file_path, 'r') as f:
        for line in f:
            A = [int(x) for x in line.split()]
            universe |= set(A[:-1])
            sets.append(set(A[:-1]))
            costs.append(A[-1])
    return universe, sets, costs
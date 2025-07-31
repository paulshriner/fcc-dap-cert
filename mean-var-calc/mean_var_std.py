import numpy as np

def calculate(list):
    # Check that list has 9 or more numbers
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 numpy array
    matrix = np.array(list).reshape(3,3)

    calculations = {}

    # mean
    calculations['mean'] = []
    # thanks https://stackoverflow.com/a/1966210 for tolist()
    calculations['mean'].append(matrix.mean(axis=0).tolist())
    calculations['mean'].append(matrix.mean(axis=1).tolist())
    calculations['mean'].append(matrix.mean())

    # variance
    calculations['variance'] = []
    calculations['variance'].append(matrix.var(axis=0).tolist())
    calculations['variance'].append(matrix.var(axis=1).tolist())
    calculations['variance'].append(matrix.var())

    # standard deviation
    calculations['standard deviation'] = []
    calculations['standard deviation'].append(matrix.std(axis=0).tolist())
    calculations['standard deviation'].append(matrix.std(axis=1).tolist())
    calculations['standard deviation'].append(matrix.std())

    # max
    calculations['max'] = []
    calculations['max'].append(matrix.max(axis=0).tolist())
    calculations['max'].append(matrix.max(axis=1).tolist())
    calculations['max'].append(matrix.max())

    # min
    calculations['min'] = []
    calculations['min'].append(matrix.min(axis=0).tolist())
    calculations['min'].append(matrix.min(axis=1).tolist())
    calculations['min'].append(matrix.min())

    # sum
    calculations['sum'] = []
    calculations['sum'].append(matrix.sum(axis=0).tolist())
    calculations['sum'].append(matrix.sum(axis=1).tolist())
    calculations['sum'].append(matrix.sum())

    return calculations
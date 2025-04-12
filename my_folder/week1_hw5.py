def iterate(lst):
    for i in range(len(lst)):
        yield lst[i]
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in iterate(animals):
    print(i)

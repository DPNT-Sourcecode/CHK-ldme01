

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = dict()
    for char in skus:
        counts[char] = counts.get(char, 0)+1
    print(set(counts.keys()))
    if not set(counts.keys()).issubset({'A', 'B', 'C', 'D'}):
        return -1
    counter = 0
    counter += counts.get('D', 0)*15
    counter += counts.get('C', 0)*20
    counter += counts.get('B', 0)//2*45 + counts.get('B', 0)%2*30
    counter += counts.get('A', 0)//3*130 + counts.get('A', 0)%3*50
    return counter




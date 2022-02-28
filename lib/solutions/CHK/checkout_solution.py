

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = dict()
    for char in skus:
        counts[char] = counts.get(char, 0)+1
    print(set(counts.keys()))
    if not set(counts.keys()).issubset({'A', 'B', 'C', 'D', 'E', 'F'}):
        return -1
    counter = 0
    counter += counts.get('E', 0)*40
    counts['B'] = counts.get('B', 0) - min(counts.get('E', 0)//2, counts.get('B', 0))
    counter += counts['B']//2*45 + counts['B']%2*30
    counter += counts.get('D', 0)*15
    counter += counts.get('C', 0)*20
    counter += counts.get('A', 0)//5*200 + counts.get('A', 0)%5//3*130 + counts.get('A', 0)%5%3*50
    counter += counts.get('F', 0)//3*20+counts.get('F', 0)%3*10
    return counter




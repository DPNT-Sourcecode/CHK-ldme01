price_mapping = {
        'A': {5: 200, 3: 130, 1: 50},
        'B': {2: 45, 1: 30},
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': {10: 80, 5: 45, 1: 10},
        'I': 35,
        'J': 60,
        'K': {2: 150, 1: 80},
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': {5: 200, 1: 50},
        'Q': {3: 80, 1: 30},
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': {3: 130, 2: 90, 1: 50},
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
}
freebies = {
        'E': (2, 'B'),
        'F': (2, 'F'),
        'N': (3, 'M'),
        'R': (3, 'Q'),
        'U': (3, 'U'),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = dict()
    for sku in skus:
        counts[sku] = counts.get(sku, 0)+1
    if not set(counts.keys()).issubset(set(price_mapping.keys())):
        return -1

    for sku in freebies:
        if sku not in counts:
            continue
        if sku == freebies[sku][1]:
            deal_count = freebies[sku][0]
            applicable_count = 1 + deal_count
            counts[sku] = counts[sku]//applicable_count*deal_count + counts[sku]%applicable_count
        else:
            counts[freebies[sku][1]] = counts.get(freebies[sku][1], 0) - min(counts.get(freebies[sku][1], 0), counts[sku]//freebies[sku][0])

    counter = 0
    for sku in counts:
        if isinstance(price_mapping[sku], int):
            counter += counts[sku]*price_mapping[sku]
        elif isinstance(price_mapping[sku], dict):
            curr_sku_count = counts[sku]
            deals_for_count = list(price_mapping[sku].keys())
            deals_for_count.sort(reverse=True)
            for curr_deal in deals_for_count:
                counter += curr_sku_count//curr_deal*price_mapping[sku][curr_deal]
                curr_sku_count = curr_sku_count%curr_deal

    return counter

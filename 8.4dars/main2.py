#       https://www.codewars.com/kata/56f399b59821793533000683/train/python


def sort_cards(cards):
    rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    sorted_cards = sorted(cards, key=lambda card: rank_order[card])

    return sorted_cards
print(sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']))


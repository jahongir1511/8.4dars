#       https://www.codewars.com/kata/5b538734beb8654d6b00016d/train/python


def queue(people, pos):
    time = 0
    while people[pos] > 0:
        for i in range(len(people)):
            if people[i] > 0:
                people[i] -= 1
                time += 1
            if people[pos] == 0:
                break
    return time

print(queue([2, 5, 3, 4, 6], 2))

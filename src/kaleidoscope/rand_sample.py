from random import random, choice


def convert(freq):
    N = sum(freq.values())
    F_i = 0
    dist = {"placeholder": 0}
    for i in freq.keys():
        F_i += freq[i] / N
        dist[i] = F_i
    dist[list(dist.keys())[-1]] = 1.0
    return dist


def rand_sample(samples, prob):
    root = random()
    left, right = 0, len(prob) - 1

    for i in samples:
        # "while loop" is not used here, to avoid enter an endless loop
        if right - left <= 1:
            return samples[right]
        else:
            middle = (left + right) // 2
            if prob[middle] <= root:
                left = middle
            else:
                right = middle

    return choice(samples)


from mingzi.mingzi import *

# print(convert(surname))
dist = convert(surname)
while True:
    print(rand_sample(dist))

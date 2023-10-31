
def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def collect_collatz(a, b):

    dict = {}

    for i in range(a,b):
        dict[i] = collatz_sequence(i)

    return dict
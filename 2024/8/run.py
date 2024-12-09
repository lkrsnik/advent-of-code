import copy


def read(path: str) -> str:
    with open(path, 'r') as fp:
        text = fp.read()
    return text

# input_path = 'input-example.txt'
input_path = 'input.txt'

text = read(input_path)
antennas = {}
j, i = 0, 0
for j, row in enumerate(text.strip().split('\n')):
    for i, el in enumerate(row):
        if el.isalnum():
            if el not in antennas:
                antennas[el] = []
            antennas[el].append((i, j))

l = i + 1
h = j + 1

def diff(a1: tuple[int, int], a2: tuple[int, int]) -> tuple[int, int]:
    """
    a1 - a2
    :param a1:
    :param a2:
    :return:
    """
    return a1[0] - a2[0], a1[1] - a2[1]

def check_signal(s: tuple[int, int]) -> bool:
    return 0 <= s[0] < l and 0 <= s[1] < h

def find_signal_p1(a1: tuple[int, int], a2: tuple[int, int]) -> set[tuple[int, int]]:
    signals = set()
    d1 = diff(a2, a1)
    s1 = diff(a1, d1)
    if check_signal(s1):
        signals.add(s1)
    d2 = diff(a1, a2)
    s2 = diff(a2, d2)
    if check_signal(s2):
        signals.add(s2)


    return signals


def find_signal_p2(a1: tuple[int, int], a2: tuple[int, int]) -> set[tuple[int, int]]:
    signals = {a1, a2}
    d1 = diff(a2, a1)
    s1 = diff(a1, d1)
    while check_signal(s1):
        signals.add(s1)
        s1 = diff(s1, d1)
    d2 = diff(a1, a2)
    s2 = diff(a2, d2)
    while check_signal(s2):
        signals.add(s2)
        s2 = diff(s2, d2)


    return signals

# p1
def find_signals(antenna_locations: list[tuple[int,int]]) -> set[tuple[int,int]]:
    signal_locations = set()
    for antenna1_i in range(len(antenna_locations)):
        antenna1 = antenna_locations[antenna1_i]
        for antenna2_i in range(antenna1_i + 1, len(antenna_locations)):
            antenna2 = antenna_locations[antenna2_i]
            # signal_locations = signal_locations.union(find_signal_p1(antenna1, antenna2))
            signal_locations = signal_locations.union(find_signal_p2(antenna1, antenna2))
    return signal_locations

signals = set()
for antenna_id, antenna_locations in antennas.items():
    signals = signals.union(find_signals(antenna_locations))

print(len(signals))

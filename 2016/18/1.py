import hashlib

def solve1():
    positions = '^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^.'
    # positions = '.^^.^.^^^^'
    rows = 400000
    traps = positions.count('.')
    positions = '.' + positions + '.'
    for j in range(rows - 1):
        npos = ''
        for i in range(len(positions) - 2):
            if positions[i:i+3] == '^^.' or positions[i:i+3] == '.^^' or positions[i:i+3] == '^..' or positions[i:i+3] == '..^':
                npos += '^'
            else:
                npos += '.'

        # print npos
        traps += npos.count('.')
        positions = '.' + npos + '.'

    print traps

solve1()
import copy


def read(path: str) -> str:
    with open(path, 'r') as fp:
        text = fp.read()
    return text

input_path = 'input-example.txt'
# input_path = 'input.txt'

text = read(input_path).strip()

disk_map = list(map(int, text))
checksum = 0.0
files = [n for n in disk_map[::2]]
files_len = sum(files)
files_num = len(files)
def generator(files, start_id, id_change):
    file_id = start_id
    for file in files:
        for el in range(file):
            yield file_id
        file_id += id_change

front_gen = generator(files, 0, 1)
back_gen = generator(files[::-1], files_num - 1, -1)

reading_files = True
checksum_pos = 0
break_loop = False
for val in disk_map:
    if reading_files:
        for i in range(val):
            mem_num = next(front_gen)
            checksum += mem_num * checksum_pos
            checksum_pos += 1
            reading_files = False
            if checksum_pos == files_len:
                break_loop = True
                break

    else:
        for i in range(val):
            mem_num = next(back_gen)
            checksum += float(mem_num) * float(checksum_pos)
            checksum_pos += 1
            reading_files = True
            if checksum_pos == files_len:
                break_loop = True
                break
    if break_loop:
        break





print(checksum)
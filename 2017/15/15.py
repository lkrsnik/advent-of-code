a = 512.0
b = 191.0

m_a = 16807.0
m_b = 48271.0

mod = 2147483647

def generator(s_value, m_val, multiplies):
    while True:
        s_value = (s_value * m_val) % mod
        if s_value % multiplies == 0:
            yield s_value % 65536
        # yield "{0:b}".format(int(s_value)).zfill(16)[-16:]

gen_a = generator(a, m_a, 4)
gen_b = generator(b, m_b, 8)

res_1 = 0
for i in range(5000000):
    if gen_a.next() == gen_b.next():
        res_1 += 1

print res_1

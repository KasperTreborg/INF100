xlo = float(input("x_lo = "))
xhi = float(input("x_hi = "))

n = int(input("n = "))

segment_length = (xhi - xlo) / n

for i in range(n):
    segment_start = xlo + i * segment_length
    segment_end = xlo + (i+1) * segment_length
    print(f'{segment_start} {segment_end}')
#Round number in default form (less than 0.5 is dropped)
def rnd(a):
    b = a % 1
    if b < 0.5:
        return int(a - b)
    else:
        return int(a + (1 - b))
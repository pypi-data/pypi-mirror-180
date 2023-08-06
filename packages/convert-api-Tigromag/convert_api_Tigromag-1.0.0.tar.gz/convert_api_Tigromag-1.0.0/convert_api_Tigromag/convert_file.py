def convert_base(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


def convert(num, to_base=10, from_base=10):
    if to_base == 10:
        return int(str(num), from_base)
    elif from_base == 10:
        return convert_base(num, to_base, from_base)
    else:
        num = int(str(num), from_base)
        return convert_base(num, to_base, from_base)


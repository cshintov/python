""" creates a histogram dict out of a list """


def histogram(lst):
    """ makes a histogram out of a list """
    hist = {}
    for itm in lst:
        hist[itm] = hist.get(itm, 0) + 1
    return hist


def inv_dict(dct):
    """ inverts the dict """
    inv = {}
    for key, val in dct.items():
        inv[val] = inv.get(val, [])
        inv[val].append(key)
    return inv


def most_freq(dct):
    """ returns the most frequent values """
    return dct[max(dct)]


def sort_dct(dct):
    """ sort dct based on the value and return as a list of (val, key)"""
    itms = dct.items()
    itms.sort(key=lambda itm: itm[1], reverse=True)
    return itms

def main():
    """ main function """
    scr_name = ['a','a','b','c','c']
    hist = histogram(scr_name)
    print hist
    freq = inv_dict(hist)
    print most_freq(freq)


if  __name__ == '__main__':
    main()

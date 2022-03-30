def symbol_exists(symbol):
    """
    check if the queried symbol is in the existing symbols list
    :param symbol:
    :return:
    """
    file = open('data/symbols.txt', 'r')
    symbols = set(file.read().splitlines())
    file.close()
    if symbol in symbols:
        return True
    else:
        return False

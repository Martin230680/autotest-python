def proverka_skidki(flag, price, total_price):
    price1 = (price[:-1])
    price1 = price1.replace(',', '.')
    total_price1 = (total_price[:-1])
    total_price1 = total_price1.replace(',', '.')
    print(price1, total_price1)
    if flag == 1:
        assert float(price1) - float(price1) * 0.1 == float(total_price1)
    elif flag == 2:
        assert float(price1) == float(total_price1)
    else:
        assert float(price1) - float(price1) * 0.15 == float(total_price1)

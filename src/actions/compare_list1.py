import logging


def compare_list1(elem, order_list, sum, total):
    text = elem.text
    elem_list = text.split('\n')
    order_list[0: 2] = [' '.join(order_list[0: 2])]
    logging.info('Вывод личных данные в листе заказа:')
    print(elem_list)
    logging.info('Вывод личных данные в эталлоном списке:')
    print(order_list)
    logging.info('Вывод общей суммы заказа в корзине')
    print(sum)
    logging.info('Вывод итоговой суммы из листе заказа')
    print(total)
    assert elem_list == order_list
    assert sum == total

import logging


def compare_list(test, list, etalon):
    logging.info('START compere list')
    new_list = []
    if test == 1:
        for i in list:
            new_list.append(i.text)
    elif test == 0:
        for i in list:
            new_list.append(i.text.upper())
    else:
        new_list = list[:]
    assert new_list == etalon
    logging.info(f"Cравниваемый список {new_list}")
    logging.info(f"Эталонный список {etalon}")
    logging.info('END compere list')

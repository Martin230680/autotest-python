def get_attr(count_list):
    count1_list = []
    for value in count_list:
        x = value.get_attribute("value")
        count1_list.append(x)
    return count1_list

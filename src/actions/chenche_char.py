def chenche_char(item, char_remove):
    item_text = item.text
    for char in char_remove:
        item_text = item_text.replace(char, '"')
    return item_text

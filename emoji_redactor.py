from emoji_pack import emojies


def emoji_add(text, emojies_count=1):
    response = []
    for word in text.split():
        response.append(word)
        for spell in emojies:
            if word.startswith(spell):
                response.append(emojies[spell] * emojies_count)
    return response


if __name__ == '__main__':
    text = input('Введите текст: ')
    emojies_count = int(input('Количество повторений эмоджи: '))
    print(*emoji_add(text, emojies_count))

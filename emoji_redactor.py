from emoji_pack import emojies


def emoji_add(text):
    response = []
    for word in text.split():
        response.append(word)
        for spell in emojies:
            if word.startswith(spell):
                response.append(emojies[spell] * 3)
    return response


if __name__ == '__main__':
    text = 'инопланетянин'
    print(*emoji_add(text))

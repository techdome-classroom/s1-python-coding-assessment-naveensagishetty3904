def decode_message(message, key):
    i = 0
    j = 0
    while i < len(message) and j < len(key):
        if key[j] == '*':
            while i < len(message) and j < len(key) - 1 and key[j + 1] != '*':
                i += 1
            j += 1
        elif key[j] == '?' or message[i] == key[j]:
            i += 1
            j += 1
        else:
            return False
    return i == len(message) and j == len(key)

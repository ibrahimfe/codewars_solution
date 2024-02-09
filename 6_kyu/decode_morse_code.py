from preloaded import MORSE_CODE

def decode_morse(morse_code):
    message = []
    morse_code = morse_code.strip()
    list_morse_code = morse_code.split(' ')
    for i, code in enumerate(list_morse_code):
        if code:
            message.append(MORSE_CODE[code])
        else:
            if i < len(list_morse_code) - 1 and list_morse_code[i + 1] == '':
                message.append(' ')
    return ''.join(message)

def caesar_cipher(message):
    """
    Turned Cracking the Code With Python's solution into a function. The Caesar cipher uses a key and shifts the encoded letters over according to the key.
    """
    key = 13
    
    mode = 'encrypt'

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_idx = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                translated_idx = symbol_idx + key

            elif mode == 'decrypt':
                translated_idx = symbol_idx - key

            if translated_idx >= len(SYMBOLS):
                translated_idx -= len(SYMBOLS)

            elif translated_idx < 0:
                translated_idx += len(SYMBOLS)


            translated += SYMBOLS[translated_idx]

        else:
            translated += symbol
    
    return translated


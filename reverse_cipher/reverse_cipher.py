def reverse_cipher_slice(message):
    """
    reverses the message by returning a reference to the string starting from the end of the message.
    """
    return message[::-1]

def reverse_cipher_iterative(message):
    """
    reverses the message by extracting each letter, and placing it into a new string
    """

    ciphered = ''
    i = len(message) -1
    while i >= 0:
        ciphered += message[i]
        i -= 1
    return ciphered

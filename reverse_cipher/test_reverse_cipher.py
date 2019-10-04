import pytest
from reverse_cipher import reverse_cipher_slice, reverse_cipher_iterative

def test_reverse_cipher_slice():
    message = 'Three can keep a secret, if two of them are dead.'
    expected = '.daed era meht fo owt fi ,terces a peek nac eerhT'

    assert expected == reverse_cipher_slice(message)

def test_reverse_cipher_iterative():
    message = 'Three can keep a secret, if two of them are dead.'
    expected = '.daed era meht fo owt fi ,terces a peek nac eerhT'

    assert expected == reverse_cipher_iterative(message)
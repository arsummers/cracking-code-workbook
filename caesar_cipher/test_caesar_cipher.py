import pytest
from caesar_cipher import caesar_cipher

def test_caesar_cipher():
    message = 'This is my secret message.'
    expected = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

    assert expected == caesar_cipher(message)
import pytest
from HW_two import plugboard, rotor, enigma_encrypt, enigma_decrypt

plugboard_position = [{'a', 'c'}, {'t', 'z'}]
rotor_position = {'v': 'd', 'd': 'v', 'y': 'u', 'n': 'n', 'i': 'w', 'z': 'p',
                  's': 'e', 'x': 's', 'h': 'f', 'b': 'x', 'u': 'c', 'p': 'q',
                  'r': 'g', 'q': 'j', 'e': 't', 'l': 'y', 'o': 'z', 'g': 'o',
                  'k': 'b', 't': 'h', 'j': 'm', 'a': 'a', 'w': 'i', 'f': 'l',
                  'm': 'r', 'c': 'k'}


@enigma_encrypt(plugboard_position, rotor_position)
def encrypt_decorated(text):
    """Helper to test the encryption decorator."""
    return text


@enigma_decrypt(plugboard_position, rotor_position)
def decrypt_decorated(text):
    """Helper to test the decryption decorator."""
    return text


def test_plugboard():
    """Tests the plugboard function."""
    assert(plugboard("enigma", plugboard_position)) == "enigmc"
    assert(plugboard("aarcetzot", plugboard_position)) == "ccraeztoz"
    assert(plugboard("", plugboard_position)) == ""
    assert(plugboard(" ", plugboard_position)) == " "
    assert(plugboard("t", plugboard_position)) == "z"
    assert(plugboard("c", plugboard_position)) == "a"
    assert(plugboard("tctatctzac", plugboard_position)) == "zazczaztca"
    assert(plugboard("a t", plugboard_position)) == "c z"
    assert(plugboard(" a t ", plugboard_position)) == " c z "


def test_rotor():
    """Tests the rotor function."""
    assert(rotor("enigmc", rotor_position)) == "tnwork"
    assert(rotor("e", rotor_position)) == "t"
    assert(rotor("e c", rotor_position)) == "t k"
    assert(rotor("", rotor_position)) == ""
    assert(rotor(" ", rotor_position)) == " "
    assert(rotor("eeee", rotor_position)) == "tttt"
    assert(rotor("abcdefghijklmopqrstuvwxyz", rotor_position)) == "axkvtlofwmbyrzqjgehcdisup"


def test_enigma_encrypt():
    """Tests the enigma_encrypt decorator."""
    assert(encrypt_decorated("enigma")) == "tnwork"
    assert(encrypt_decorated("abcdefghijklmopqrstuvwxyz")) == "kxavtlofwmbyrzqjgepcdisuh"
    assert(encrypt_decorated("a")) == "k"
    assert(encrypt_decorated("")) == ""
    assert(encrypt_decorated(" ")) == " "
    assert(encrypt_decorated("cat")) == "akp"
    assert(encrypt_decorated(" c a t")) == " a k p"



def test_enigma_decrypt():
    """Tests the enigma_decrypt decorator."""
    assert(decrypt_decorated("tnwork")) == "enigma"
    assert(decrypt_decorated("kxavtlofwmbyrzqjgepcdisuh")) == "abcdefghijklmopqrstuvwxyz"
    assert(decrypt_decorated("k")) == "a"
    assert(decrypt_decorated("")) == ""
    assert(decrypt_decorated(" ")) == " "
    assert(decrypt_decorated("akp")) == "cat"
    assert(decrypt_decorated(" a k p ")) == " c a t "

plugboard_position = [{'a', 'c'}, {'t', 'z'}]
rotor_position = {'v': 'd', 'd': 'v', 'y': 'u', 'n': 'n', 'i': 'w', 'z': 'p',
                  's': 'e', 'x': 's', 'h': 'f', 'b': 'x', 'u': 'c', 'p': 'q',
                  'r': 'g', 'q': 'j', 'e': 't', 'l': 'y', 'o': 'z', 'g': 'o',
                  'k': 'b', 't': 'h', 'j': 'm', 'a': 'a', 'w': 'i', 'f': 'l',
                  'm': 'r', 'c': 'k'}


def plugboard(text, list_of_rules):
    changed_word = ""

    for letter in text:
        for set_of_letters in list_of_rules:
            if letter in set_of_letters:
                letter = set_of_letters.difference({letter}).pop()

        changed_word += letter

    return changed_word

def rotor(text, dict_of_rules):
    changed_text = ""

    for letter in text:
        changed_text += dict_of_rules.get(letter, " ")

    return changed_text

def enigma_encrypt(plugboard_position, rotor_position):
    def decorator(func):
        def crypting(text):
            crypted_text = plugboard(text, plugboard_position)
            crypted_text = rotor(crypted_text, rotor_position)
            return func(crypted_text)
        return crypting
    return decorator
    
@enigma_encrypt(plugboard_position, rotor_position)
def encrypt_decorated(text):
    return text

def enigma_decrypt(plugboard_position, rotor_position):
    def decorator(func):
        def decrypting(text):
            rotor_position_reversed = {y: x for x, y in rotor_position.items()}
            decrypted_text = rotor(text, rotor_position_reversed)
            decrypted_text = plugboard(decrypted_text, plugboard_position)

            return func(decrypted_text)
        return decrypting
    return decorator
    
@enigma_decrypt(plugboard_position, rotor_position)
def decrypt_decorated(text):
    return text
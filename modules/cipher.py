import string
import random

def generate_cipher(cipher):
    '''
    This function generate a proposed cipher from a given cipher by inverting two letters randomly choosen
    '''
    pos1 = random.randint(0, len(list(cipher))-1)
    pos2 = random.randint(0, len(list(cipher))-1)
    if pos1 == pos2:
        return generate_cipher(cipher)
    else:
        cipher = list(cipher)
        pos1_alpha = cipher[pos1]
        pos2_alpha = cipher[pos2]
        cipher[pos1] = pos2_alpha
        cipher[pos2] = pos1_alpha
        return "".join(cipher)


def apply_cipher_on_text(text,cipher):
    '''
    this function apply the cipher to the text using a json dictionary 
        generated by the function “create_cipher_dict“
    '''
    cipher_dict = create_cipher_dict(cipher) 
    text = list(text)
    newtext = ""
    for elem in text:
        if elem.upper() in cipher_dict:
            newtext+=cipher_dict[elem.upper()]
        else:
            newtext+=" "
    return newtext

def create_cipher_dict(cipher):
    '''
    create a cipher dictiornary from the cipher string so we can apply it to a text
    '''
    cipher_dict = {}
    alphabet_list = list(string.ascii_uppercase)
    for i in range(len(cipher)):
        cipher_dict[alphabet_list[i]] = cipher[i]
    return cipher_dict




# def create_cipher_dict(cipher_string):
#     """
#     Create a cipher dictionary from a cipher string.

#     :param cipher_string: A string representing the cipher (e.g., "DGHJKL...")
#     :return: A dictionary representing the substitution cipher.
#     """
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     cipher_dict = dict(zip(alphabet, cipher_string.upper()))
#     return cipher_dict

# def apply_cipher_on_text(text, cipher_string):
#     """
#     Apply the substitution cipher to the given text.

#     :param text: The text to be encrypted or decrypted.
#     :param cipher_string: A string representing the cipher.
#     :return: The text transformed by the substitution cipher.
#     """
#     cipher_dict = create_cipher_dict(cipher_string)
#     text = text.upper()
#     ciphered_text = ''.join(cipher_dict.get(char, char) for char in text)

#     return ciphered_text

#Charles J. Lai
#crypto.py
#August 7, 2013

import random
import time
import mathlib.numbers.*

"""
This module contains various cryptographic implementations of different 
number theory tools defined in the numbers package and 3rd party modules. 
These include but are not limited to: RSA Encryption, One-Time-Pad 
Encryption, Ceaser Cipher, and various hashing algorithms. Part of the
MathLib/numbers package.
"""


def caeser(message, key):
	"""
	Returns: Ciphertext of message encrypted with a Caeser cipher. This
	encryption function preserves case, whitespace, and punctuation.
	"""
	#Raw Alphabets
	low_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
				 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

	cap_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
				 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

	#Dictionaries for each alphabet type
	low_dict = {}
	cap_dict = {}
	for i in range(26):
		low_dict[low_alpha[i]] = low_alpha[(i+key) % 26]
		cap_dict[cap_alpha[i]] = cap_alpha[(i+key) % 26]

	#Conversion of message to ciphertext
	ciphertext = ""
	for l in message:
		if l in low_dict:
			l = low_dict[l]
		if l in cap_dict:
			l = cap_dict[l]
		ciphertext += l

	return ciphertext


def RSA_encrpyt(public_key, private_key, message):
    pass

def RSA_decrypt(public_key, private_key, cipher):
    pass

def phi(number):
    pass
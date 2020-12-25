import sys
import re
import math
import operator
from collections import defaultdict
from functools import reduce

card_pub = 3418282
door_pub = 8719412

card_sn = 7
door_sn = 7


def get_loop_count(pub, sn):
    x = 1
    loops = 0
    while x != pub:
        loops += 1
        x = (x * sn) % 20201227
    return loops

def get_encryption_key(loop, other_pub):
    x = 1
    for _ in range(loop):
        x = (x * other_pub) % 20201227
    return x

def get_enc_key_from_pub_keys(pub1, sn1, pub2, sn2):
    loop1 = get_loop_count(pub1, sn1)
    # loop2 = get_loop_count(pub2, sn2)
    return get_encryption_key(loop1, pub2)


# print(f'Encryption key: {get_enc_key_from_pub_keys(17807724, 7, 5764801, 7)}')
print(f'Encryption key: {get_enc_key_from_pub_keys(card_pub, card_sn, door_pub, door_sn)}')

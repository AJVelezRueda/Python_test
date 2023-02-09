import sys, os, string
import pandas as pd

from random import randint

def generate_random_strings(string_length):
    return ''.join(random.choices(string.ascii_lowercase, k=string_length))

def generate_random_ints_as_string(amount_of_numbers):
    numbers_list = [randint(0, i) for i in range(0, amount_of_numbers)]

    return numbers_list
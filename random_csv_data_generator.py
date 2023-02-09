import sys, os, string, random
import pandas as pd

from random import randint

def generate_random_strings(string_length):
    return ''.join(random.choices(string.ascii_lowercase, k=string_length))

def generate_random_strings_list(string_length, amount_of_strings):
    return [generate_random_strings(string_length) for i in range(0, amount_of_strings)]

def generate_random_ints_as_string(amount_of_numbers):
    numbers_list = [randint(0, i) for i in range(0, amount_of_numbers)]
    return numbers_list

def generate_random_df(amount_of_numbers, string_length):
    df = pd.DataFrame()
    df["ints"] = generate_random_ints_as_string(amount_of_numbers)
    df["strings"] = generate_random_strings_list(string_length, amount_of_numbers)
    return df

def write_df_into_a_file(amount_of_numbers, string_length, file_name, mode):
    df = generate_random_df(amount_of_numbers, string_length)
    df.to_csv(file_name, index=False, header=False, mode=mode)


def write_df_in_chunks(amount_of_numbers, string_length, file_name):
    write_df_into_a_file(amount_of_numbers%10000, string_length, file_name, "w")
    
    for i in range(0, amount_of_numbers//10000):
        write_df_into_a_file(10000, string_length, file_name, "a")
    
    
if __name__ == "__main__":
    args = sys.argv
    write_df_in_chunks(int(args[1]), 8, args[2])
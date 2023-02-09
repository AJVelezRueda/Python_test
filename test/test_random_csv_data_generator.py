import pytest
import pandas as pd
from ..random_csv_data_generator import *

def test_can_generate_random_df():
    df = generate_random_df(8,20) 
    assert len(df) == 8
    assert len(df.columns) == 2

def test_can_write_a_small_random_df():
    write_df_in_chunks(8, 15, "./test/resources/sample.csv")
    df = pd.read_csv("./test/resources/sample.csv", header=None)
    assert len(df) == 8

def test_can_write_a_medium_random_df():
    write_df_in_chunks(1000, 15, "./test/resources/sample.csv")
    df = pd.read_csv("./test/resources/sample.csv", header=None)
    assert len(df) == 1000

def test_can_write_a_large_random_df():
    write_df_in_chunks(200008, 15, "./test/resources/sample.csv")
    df = pd.read_csv("./test/resources/sample.csv", header=None)
    assert len(df) == 200008
import os
import sys  
sys.path.append('/visual studio code/envs/develop/lib/python3.8.1/site-packages/')

# import tqdm
import pytest
import getpass
from contextlib import contextmanager
USER = getpass.getuser()

from covidify.data_prep import *

@contextmanager
def not_raises(exception): # Check if an exception was not raised
    try:
        yield
    except exception:
        raise pytest.fail("DID RAISE {0}".format(exception))
        

def test_clean_sheet_names():
    
    file_names = ['20200101.csv', 'abdc.csv', '20200102.txt', '__pycache__']
    expected_res = ['20200101.csv','20200102.txt']
    
    assert expected_res == clean_sheet_names(file_names)
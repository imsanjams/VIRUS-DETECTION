import os
import sys  
import pytest
import getpass
from contextlib import contextmanager
sys.path.append('/visual studio code/envs/develop/lib/python3.8.1/site-packages/')
USER = getpass.getuser()


from covidify.cli import *



@contextmanager
def not_raises(exception): # Check if an exception was not raised
    try:
        yield
    except exception:
        raise pytest.fail("DID RAISE {0}".format(exception))



def test_check_output_folder():
    msg = 'test message'
    
    #Check if error message doesn't occur with path
    with not_raises(SystemExit):
        check_output_folder('/home/user/tmp', msg)
        
    #Check folder name    
    assert '/home/user/tmp' == check_output_folder('/home/user/tmp', msg)
    
    # Assert default folder location if arg is None
    assert '/Users/'+ USER +'/Desktop/covidify-output/' == check_output_folder(None, msg)
    

def test_check_source_arg():
    msg = 'test message'
    
    #Check if error message doesn't occur with path
    with not_raises(SystemExit):
        check_source_arg(None, msg)
        
    #Invalid source raises a sys exit
    with pytest.raises(SystemExit):
        check_source_arg('abcd', msg)
        
    #Default to git datasource
    assert 'git' == check_source_arg(None, msg)
    
    #Return source if valid
    assert 'wiki' == check_source_arg('wiki', msg)
    assert 'git' == check_source_arg('git', msg)
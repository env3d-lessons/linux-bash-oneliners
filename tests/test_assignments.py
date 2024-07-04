import pathlib
import os

def file_basic_check(f):
    # Test file existence and not empty
    assert pathlib.Path(f).is_file()
    assert pathlib.Path(f).stat().st_size > 0

def test_download():    
    file_basic_check('tuition.csv')

def test_q1():
    file_basic_check('q1.txt')

def test_q2():
    file_basic_check('q2.txt')

def test_q3():
    file_basic_check('q3.txt')

def test_q4():
    file_basic_check('q4.txt')
    
def test_q5():
    file_basic_check('q5.txt')
    
def test_q6():
    file_basic_check('q6.txt')
    
def test_q7():
    file_basic_check('q7.txt')
    
def test_q8():
    file_basic_check('q8.txt')


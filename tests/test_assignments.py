import pathlib
import os
import csv

def file_basic_check(f):
    # Test file existence and not empty
    assert pathlib.Path(f).is_file()
    assert pathlib.Path(f).stat().st_size > 0

def test_download():    
    file_basic_check('tuition.csv')

def test_q1():
    file_basic_check('q1.txt')

def test_q1_content():
    expected = os.popen('wc -l tuition.csv').read().split()[0] + '\n'
    answer = os.popen('bash q1.txt').read()
    assert expected == answer

def test_q2():
    file_basic_check('q2.txt')

def test_q2_content():
    expected = ''.join(open('tuition.csv').readlines()[4:])
    answer = os.popen('bash q2.txt').read()
    assert expected == answer

def test_q3():
    file_basic_check('q3.txt')

def test_q3_content():
    data = open('tuition.csv').readlines()
    expected = ''.join(data[4]+data[-1])
    answer = os.popen('bash q3.txt').read()
    assert expected == answer
    
def test_q4():
    file_basic_check('q4.txt')
    
def test_q4_content():
    expected = set([l.split(',')[3] for l in open('tuition.csv').readlines()])
    answer = set(os.popen('bash q4.txt').read().split('\n'))
    assert expected == answer    
    
def test_q5():
    file_basic_check('q5.txt')
    
def test_q5_content():
    expected = ''.join([l for l in open('tuition.csv').readlines()
                        if 'Capilano University' in l or 'Langara College' in l])
    answer = os.popen('bash q5.txt').read()
    assert expected == answer    
    
def test_q6():
    file_basic_check('q6.txt')

def test_q6_content():
    expected = ''.join([ ','.join(l.split(',')[3:])
                         for l in open('tuition.csv').readlines()
                         if '2019/20' in l])
    answer = os.popen('bash q6.txt').read()
    assert expected == answer    
    
    
def test_q7():
    file_basic_check('q7.txt')
    
def test_q7_content():
    expected = ''.join(sorted([ ','.join(l.split(',')[3:])
                         for l in open('tuition.csv').readlines()
                         if '2019/20' in l]))
    answer = os.popen('bash q7.txt').read()
    assert expected == answer    
    
def test_q8():
    file_basic_check('q8.txt')
    
def test_q8_content():
    s = sorted( [ [r[3],r[4].replace('$','').replace(',','')]
                         for r in csv.reader([l for l in open('tuition.csv').readlines() if '2019/20' in l])],
                       key=lambda x: int(x[1]) )
    expected = '\n'.join([r[0] for r in s]) + '\n'
    answer = os.popen('bash q8.txt').read()
    assert expected == answer    


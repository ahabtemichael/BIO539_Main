from script1 import *

import pandas as pd

#The test for all possilbe kmers function 

def test_all_kmers_1():
  k=1
  seq='AGTT'
  actual_result= all_kmers(k, seq)
  expected_result= 4
  assert actual_result == expected_result
  
  
def test_all_kmers_2():
  k=7
  seq='AAGTTTGAGG'
  actual_result= all_kmers(k, seq)
  expected_result= 4
  assert actual_result == expected_result
  
  
def test_all_kmers_3():
  k=3
  seq='CCAGAT'
  actual_result= all_kmers(k, seq)
  expected_result= 4
  assert actual_result == expected_result
  
#The test for observed kmers function

def test_obs_kmers_1():
  k=3
  seq='AGTT'
  actual_result= all_kmers(k, seq)
  expected_result= 2
  assert actual_result == expected_result
  
  
def test_obs_kmers_2():
  k=2
  seq='CCAGAT'
  actual_result= all_kmers(k, seq)
  expected_result= 5
  assert actual_result == expected_result
  
  
def test_obs_kmers_3():
  k=8
  seq='AAGTTTGAGG'
  actual_result= all_kmers(k, seq)
  expected_result= 3
  assert actual_result == expected_result
  
#The test for making the table function

def test_table_1():
  data = [[3,4],[3,3],[2,2],[1,1], [9,10]] 
  expected = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4, 'total'])
  seq = 'AGTT'
  actual = table(seq)
  result = expected.equals(actual)
  assert result == True
  
  
def test_table_2():
  data = [[4,4],[5,5],[4,4],[3,3],[2,2],[1,1], [19,19]] 
  expected = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6, 'total'])
  seq = 'CCAGAT'
  actual = table(seq)
  result = expected.equals(actual)
  assert result == True
  
  
def test_table_3():
  data = [[3,4], [7,9],[8,8],[7,7],[6,6],[5,5],[4,4], [3,3], [2,2], [1,1],[46,49]] 
  expected = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6,7,8,9,10, 'total'])
  seq = 'AAGTTTGAGG'
  actual = table(seq)
  result = expected.equals(actual)
  assert result == True
  
#The test for the linguistic complexity function

def test_linguistic_complexity_1():
  data = [[3,4], [4,4], [3,3], [2,2], [12,13]] 
  df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4, 'total'])
  actual_result = linguistic_complexity(df)
  expected_result = 0.9230769230769231
  assert actual_result == expected_result

def test_linguistic_complexity_2():
  data = [[4,4], [6,6],[5,5],[4,4], [3,3], [2,2], [24,24]]
  df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6, 'total'])
  actual_result = linguistic_complexity(df)
  expected_result = 1.0
  assert actual_result == expected_result
  
def test_linguistic_complexity_3():
  data = [[3,4], [7,9],[8,8],[7,7],[6,6],[5,5],[4,4], [3,3], [2,2], [1,1],[46,49]]
  df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6,7,8,9,10, 'total'])
  actual_result = linguistic_complexity(df)
  expected_result = 0.9387755102040817
  assert actual_result == expected_result

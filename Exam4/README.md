# Sequence Data Linguistic Complexity #

Asta Habtemichael

BIO 539 

May 7, 2021

### Linguistic complexity script (script1.py) ###

Usage:
python3 *script1.py* 'filename.csv'

Functions: 
 
*all_kmers (k,seq):*  When we have a given k value and sequence string, returns all the possible number of kmers

*obs_kmers(k, seq):*  When we have a given k value and sequence string, returns the observed number of kmers

*table (seq):* Creates a data frame indexing k values, and columns of observed kmers and possible kmers 
    and calculates totals of the two variables in the final row. 

*linguistic_complexity(df):*  Takes data from a data frame(*table ()*) and calculates the linguistic complexity 

*main(args):*  Takes a data in .CSV format as an argument and outputs new data frame in a .CSV file 
  and prints in the command line the linguistic complexity.

### Test Script (test_script1.py) ###

Usage: 
py.test

Description:
This script tests each of the four functions in script1.py using three different sequences. 

### Sequence data file (sequence.csv) ###

Usage:
To run this data file using *script1.py:*

python3 *script1.py* sequences.csv
#!/usr/bin/env python3

# import required packages 
import pandas as pd
import argparse

def all_kmers (k,seq):
  
  '''
    Description:
    When we have a given k value & sequence string, returns all the possible number of kmers
    
    Parameters:
    k (int): The length of kmer we are considering
    seq (str): The string 
    
    Returns: 
    integer: the number of all the possible kmers 
    
    '''
  string = len(seq)  
  poss_val=[]#setting a data frame
  if k ==1:
    return 4;# for k value of 1 always the out put is 4 as 4**1=4
  else:
      for i in range (0,string-k+1):
        poss_val.append(seq[i:i+k])
      return len(poss_val)
  
        
def obs_kmers(k, seq): 
  
    ''' 
    Description:
    When we have a given k value & sequence string, returns the observed number of kmers
    
    Parameters:
    k (int): The length of kmer we are considering
    seq (str): The sequence string 
    
    Returns: 
    integer: the number of observed kmers 
    
    '''
    #creating empty data frames
    complete = [] # creating empty data frame to store the list of all kmers 
    unique= [] # creating empty data frame to store the unique kmers
    count = 0 # create empty counter 
    string = len(seq) # calculate length of the string 
    for i in range(1,string+1): # loop over the kmer start position
        kmer = seq[(i-1):(i-1+k)] # Slice the string to get the kmer 
        if len(kmer) == k: # picking kmers of the same length that we are interested in 
            complete.append(kmer) # adding all the resulting kmers to a df 
    for item in complete:
        if item not in unique: # Add the kmer to the df if it's not there 
            count += 1 # Increment of count for this kmer
            unique.append(item)
    return(count)#return the final counts

def table (seq):
  
    '''
    Description:
    Creates a dataframe to be populated with k values, observed kmers and possible kmers 
    and calculates totals
    
    Parameters:
    seq(str): The sequence line (string) of the argument from the input data 
    
    Returns: 
    dataframe: a dataframe that lists the possible and observed kmers
    
    '''
    
    data = [] # setting an empty data frame 
    string = len(seq) # Find the length of the string 
    for i in range(1, string+1): # loop over the kmer start position 
        k = i 
        data.append([obs_kmers(k, seq), all_kmers(k, seq)]) # add the calculated poss & obs kmers and add to the df 
    # compiling the df with respective column values and total row at the bottom    
    df = pd.DataFrame(data, index = range(1,string+1), columns = ['observed_kmers', 'possible_kmers'])  
    df.loc['total']= df.sum()
    return(df)

def linguistic_complexity(df):
  
    '''
    Description: 
    Takes data from a data frame and calculates the linguistic complexity 
    
    Parameters:
    Pd.dataframe: A table (data frame) created by the table function 
    
    Returns: 
    ling_com (int): the linguistic complexity of a string (sequence line)
    
    '''
    ling_comp = df.loc['total','observed_kmers'] / df.loc['total','possible_kmers'] # calculation of linguistic complexity 
    return(ling_comp)
  
def main(args): 
  
  '''
  Description: 
  Takes a data in .CSV format and outputs new data frame in a .CSV file 
  and prints in the command line the linguistic complexity.
  
  Parameters:
  In put data (.CSV): A data file that contains a list of sequences 
  
  Returns: 
  Dataframe (.CSV): creates a file for each sequence line and saves the respective computation in each file 
  Linguistic complexity (terminal message): Prints a message naming the sequence line and
  linguistic complexity of the string
  
  '''
  result = [] #set a new df 
  for i in args.sequence:
    string = i # writes each line as a string 
    b = string.rstrip() # removes the white space from the end of the string 
    df = table (b) # writes the dataframe 
    result = linguistic_complexity(df) # computing the linguistic complexity
    df.to_csv(i+'.csv') # creates csv file
    print("The linguistic compleixty of", b, "is", result) # prints a message on the linguistic complexity to command line 
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('sequence', type=argparse.FileType('r')) # reading file
  args = parser.parse_args()
  main(args)

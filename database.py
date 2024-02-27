import sqlalchemy
import sys
import os
import pandas as pd

def get_data(rank, loc, size):
    
    ranks = []
    for i in rank:
        a = [int(j) for j in i.split('-')][0]
        b = [int(j) for j in i.split('-')][1]
        ranks = ranks + list(range(a,b+1))

    df = pd.read_csv('df.csv')
    df_select = df[(df['US News Rank'].isin(ranks)) & (df['Location Setting'].isin(loc)) & (df['University Size'].isin(size))]
    
    return df_select

def get_merged():
    
    df = pd.read_csv('df.csv')
    df3 = pd.read_csv('df3.csv')

    df4 = pd.merge(df3, df, how = 'inner', on = 'ID').sort_values('US News Rank')
    df4 = df4[df4.Status != 0.5][['US News Rank','GPA','SAT','Status']]
    
    return df4

def get_student_info(rank, loc, size, gpa, sat):
    
    df_select = get_data(rank, loc, size)[['University Name','US News Rank']]
    df_select['gpa'] = gpa
    df_select['sat'] = sat
    
    return df_select

if __name__ == '__main__':
    rank = float(sys.argv[1])
    loc = sys.argv[2]
    size = sys.argv[3]
    gpa = float(sys.argv[4])
    sat = float(sys.argv[5])

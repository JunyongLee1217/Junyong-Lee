# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:57:34 2020

@author: junyo
"""

list1 = ['Hello World', 'This is Tuesday']
list2 = ['Hello world', 'This is tuesday']
Diff = ''


def oneTask():
    
    for i in range(len(list1)):
        
        print('File1: ', list1[i])
        print('File2: ', list2[i])
        
        if(list1[i] != list2[i]):
            
            print(' diff:  ', end='')
            
            # Compare each character
            for k in range(len(list1[i])):
                if(list1[i][k] != list2[i][k]):                  
                    print('x', end='')
                else:
                
                    print(' ', end='')
            print()
            
            
        else:
            print('diff: ')
            

        
        
        #if( list1[i] != list2[i]):
        #    print("x", end='')
        #else:
        #    print(' ', end='')
        

oneTask()
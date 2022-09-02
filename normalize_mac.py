#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:00:18 2019

@author: tushar2911@gmail.com
"""
import sys

def normalizeMAC(mac):
    '''Function to normalize mac-address
    
       Input : Any valid mac-address ( aa/bb/cc/dd/ee/ff or 
                                       aabb.ccdd.eeff    or 
                                       aabbcc.ddeeff     or 
                                       a:b:c:d:e:f       or
                                       aabbccddeeff       )
       
       Output: Mac-address in the format aa:bb:cc:dd:ee:ff
       
       Limitations : Mac-address should have the same or no separator
                     Blank sections should be between separators. e.g. 01::03:04:05:06
                         will be normalized to 01:00:03:04:05:06
    '''
    '''intialize variables'''
    import re
    newmac=''
    separator=''
    left=right=0
    
    ''' find separator'''
    for i in mac:
        if not i.isalnum():
            separator=i
            break

    '''parse the mac address step by step'''
    for i in mac:
        i=i.lower()
        if not i==separator and re.match('[^a-fA-F0-9]',i):
            print("#WRONG - Invalid Char :"+i)
            return -1
        if left==0 and right==0 and not i==separator:
            newmac+=i
            left+=1
        elif left==1 and right==0 and not i==separator:
            newmac+=i
            right+=1
        elif left==1 and right==1 and not i==separator:
            newmac+=':'+i
            right=0
        elif left==1 and right==1 and i==separator:
            newmac+=':'
            left=right=0
        elif left==1 and right==0 and i==separator:
            newmac=newmac[0:-1]+'0'+newmac[-1:newmac.__len__()]
            right=1
        elif left==0 and right==0 and i==separator:
            newmac+='00:'
    else:
        if left==1 and right==0:
            newmac=newmac[0:-1]+'0'+newmac[-1:newmac.__len__()]
    ''' if mac-address is not of correct length'''
    if not newmac.__len__()==17:
        print("#WRONG - Insufficient Characters")
        return -1
    
    '''return normalized mac-address'''
    print(newmac)
    return 0

if __name__=='__main__':
    if sys.argv.__len__()<2 or sys.argv[1]=='-h' or sys.argv[1]=='--help':
        print("""Help:
                Please enter mac-address as first argument to normalize it
                e.g. ./normalize_mac.py aa.bb.dd.ee.ff
                """)
    else:
        normalizeMAC(sys.argv[1])

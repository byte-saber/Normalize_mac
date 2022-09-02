# Normalize_mac
Standardize mac-address from various formats to lowercase, colon separated


                Please enter mac-address as first argument to normalize it
                e.g. ./normalize_mac.py aa.bb.dd.ee.ff

Sample outputs
```                
[user@vm1 MACaddress_normalize]$ ./normalize_mac.py "aa bb cc dd ee ff"
aa:bb:cc:dd:ee:ff
[user@vm1 MACaddress_normalize]$ ./normalize_mac.py AA-BB-CC-DD-EE-FF
aa:bb:cc:dd:ee:ff
[user@vm1 MACaddress_normalize]$ ./normalize_mac.py aabbcc-DDEEFF
aa:bb:cc:dd:ee:ff
[user@vm1 MACaddress_normalize]$ ./normalize_mac.py AA-BB--DD-EE-FF
aa:bb:00:dd:ee:ff
[user@vm1 MACaddress_normalize]$ ./normalize_mac.py AA-BB--DD-EE-Fk
#WRONG - Invalid Char :k
[user@vm1 MACaddress_normalize]$ ./normalize_mac.py AA-BB--DD-EE-FK
#WRONG - Invalid Char :k
```

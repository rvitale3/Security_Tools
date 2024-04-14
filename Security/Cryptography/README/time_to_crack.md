# Time to crack
Estimates the time to crack based on the concept of [password entropy](https://en.wikipedia.org/wiki/Password_strength).  
File: [time_to_crack.py](https://github.com/rvitale3/Tools/blob/main/Security/Cryptography/source/time_to_crack.py)  
# Notice
This program does not take into account cracking time for dictionary attacks, Mangling rules or any other advance techniques such as Probabilistic Context-Free Grammar (PCFGs), the Markov models, improved transformer or AI.  
The output provides only an estimate on how long it would take to crack a password by exhausting the maximum password search space.  
## Requirements
1. Python >= 3.6  
2. [PrettyTable](https://pypi.org/project/prettytable/)  
## Running the script
```bash
$ python time_to_crack.py

    Please select the password character composition:

    (1) Lower case only     [a-z]
    (2) Upper case only     [A-Z]
    (3) Numbers only        [0-9]
    (4) Lower/Upper         [a-zA-Z]
    (5) Lower/Numbers       [a-z0-9]
    (6) Upper/Numbers       [A-Z0-9]
    (7) Lower/Upper/Numbers [a-zA-Z0-9]
    (8) All and Special     [a-zA-Z0-9!@#$%^&*()+_~`-_=+[]{}\|;:'",.<>?/]

    Enter a number from the list: 8

    Please select the cracking speed:

    (1) 1   Mega Hertz (MHz)
    (2) 10  Mega Hertz (MHz)
    (3) 100 Mega Hertz (MHz)
    (4) 1   Giga Hertz (GHz)
    (5) 10  Giga Hertz (GHz)
    (6) 100 Giga Hertz (GHz)
    (7) 1   Tera Hertz (THz)
    (8) 10  Tera Hertz (THz)
    (9) 100 Tera Hertz (THz)

    Enter a number from the list: 9

    Please select the number of processing elements working in parallel:

    (1) 1
    (2) 10
    (3) 100
    (4) 1,000
    (5) 10,000
    (6) 100,000
    (7) 1,000,000   
    (8) 10,000,000
    (9) 100,000,000

    Enter a number from the list: 9
+-----------------+----------------+---------------------+--------------------+
| Password Length | Password Space | Time to Crack (max) | Key Entropy (bits) |
+-----------------+----------------+---------------------+--------------------+
|     5 digits    |   ~ 8.59E+09   |   ~ 8.59E-13 secs   |        33.0        |
|     6 digits    |   ~ 8.33E+11   |   ~ 8.33E-11 secs   |        39.6        |
|     7 digits    |   ~ 8.08E+13   |   ~ 8.08E-09 secs   |        46.2        |
|     8 digits    |   ~ 7.84E+15   |   ~ 7.84E-07 secs   |        52.8        |
|     9 digits    |   ~ 7.60E+17   |   ~ 7.60E-05 secs   |        59.4        |
|    10 digits    |   ~ 7.37E+19   |   ~ 7.37E-03 secs   |        66.0        |
|    11 digits    |   ~ 7.15E+21   |   ~ 7.15E-01 secs   |        72.6        |
|    12 digits    |   ~ 6.94E+23   |   ~ 1.16E+00 mins   |        79.2        |
|    13 digits    |   ~ 6.73E+25   |   ~ 1.87E+00 hours  |        85.8        |
|    14 digits    |   ~ 6.53E+27   |   ~ 7.56E+00 days   |        92.4        |
|    15 digits    |   ~ 6.33E+29   |   ~ 2.02E+00 years  |        99.0        |
|    16 digits    |   ~ 6.14E+31   |   ~ 1.96E+02 years  |       105.6        |
|    17 digits    |   ~ 5.96E+33   |   ~ 1.90E+04 years  |       112.2        |
|    18 digits    |   ~ 5.78E+35   |   ~ 1.84E+06 years  |       118.8        |
|    19 digits    |   ~ 5.61E+37   |   ~ 1.79E+08 years  |       125.4        |
|    20 digits    |   ~ 5.44E+39   |   ~ 1.73E+10 years  |       132.0        |
|    21 digits    |   ~ 5.27E+41   |   ~ 1.68E+12 years  |       138.6        |
|    22 digits    |   ~ 5.12E+43   |   ~ 1.63E+14 years  |       145.2        |
|    23 digits    |   ~ 4.96E+45   |   ~ 1.58E+16 years  |       151.8        |
|    24 digits    |   ~ 4.81E+47   |   ~ 1.54E+18 years  |       158.4        |
|    25 digits    |   ~ 4.67E+49   |   ~ 1.49E+20 years  |       165.0        |
|    26 digits    |   ~ 4.53E+51   |   ~ 1.44E+22 years  |       171.6        |
|    27 digits    |   ~ 4.39E+53   |   ~ 1.40E+24 years  |       178.2        |
|    28 digits    |   ~ 4.26E+55   |   ~ 1.36E+26 years  |       184.8        |
|    29 digits    |   ~ 4.13E+57   |   ~ 1.32E+28 years  |       191.4        |
|    30 digits    |   ~ 4.01E+59   |   ~ 1.28E+30 years  |       198.0        |
|    31 digits    |   ~ 3.89E+61   |   ~ 1.24E+32 years  |       204.6        |
|    32 digits    |   ~ 3.77E+63   |   ~ 1.20E+34 years  |       211.2        |
+-----------------+----------------+---------------------+--------------------+
The Table was generated based on a password composed by
Characters: [a-zA-Z0-9!@#$%^&*()+_~`-_=+[]{}|;:'",.<>?/]
Number of characters 97
The evaluated cracking speed: 100 THz
Elements working is parallel to crack the password: 100,000,000 station(s)
```

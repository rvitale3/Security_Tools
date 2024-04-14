# Password Cracking Time Estimator
Estimates the time to crack for a password based on the concept of [password entropy](https://en.wikipedia.org/wiki/Password_strength).  
File: [passwd_cracking_time.py](https://github.com/rvitale3/Tools/blob/main/Security/Cryptography/source/passwd_cracking_time.py)  
## Disclaimer
This program does not take into account cracking time for dictionary attacks, mangling rules or any other advanced techniques; such as Probabilistic Context-Free Grammar (PCFGs), Markov model, Improved Transformer, neither AI.  
The output only provides an estimate about how long it would take to crack a password by exhausting the password maximum search space.  
## Requirements
1. Python >= 3.6  
2. [PrettyTable](https://pypi.org/project/prettytable/)  
## Running the script
```bash
$ python passwd_cracking_time.py

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
|     5 digits    |   ~ 7.74E+09   |   ~ 7.74E-13 secs   |       32.85        |
|     6 digits    |   ~ 7.35E+11   |   ~ 7.35E-11 secs   |       39.42        |
|     7 digits    |   ~ 6.98E+13   |   ~ 6.98E-09 secs   |       45.99        |
|     8 digits    |   ~ 6.63E+15   |   ~ 6.63E-07 secs   |       52.56        |
|     9 digits    |   ~ 6.30E+17   |   ~ 6.30E-05 secs   |       59.13        |
|    10 digits    |   ~ 5.99E+19   |   ~ 5.99E-03 secs   |        65.7        |
|    11 digits    |   ~ 5.69E+21   |   ~ 5.69E-01 secs   |       72.27        |
|    12 digits    |   ~ 5.40E+23   |   ~ 5.40E+01 secs   |       78.84        |
|    13 digits    |   ~ 5.13E+25   |   ~ 1.43E+00 hours  |       85.41        |
|    14 digits    |   ~ 4.88E+27   |   ~ 5.64E+00 days   |       91.98        |
|    15 digits    |   ~ 4.63E+29   |   ~ 1.48E+00 years  |       98.55        |
|    16 digits    |   ~ 4.40E+31   |   ~ 1.40E+02 years  |       105.12       |
|    17 digits    |   ~ 4.18E+33   |   ~ 1.33E+04 years  |       111.69       |
|    18 digits    |   ~ 3.97E+35   |   ~ 1.27E+06 years  |       118.26       |
|    19 digits    |   ~ 3.77E+37   |   ~ 1.20E+08 years  |       124.83       |
|    20 digits    |   ~ 3.58E+39   |   ~ 1.14E+10 years  |       131.4        |
|    21 digits    |   ~ 3.41E+41   |   ~ 1.09E+12 years  |       137.97       |
|    22 digits    |   ~ 3.24E+43   |   ~ 1.03E+14 years  |       144.54       |
|    23 digits    |   ~ 3.07E+45   |   ~ 9.80E+15 years  |       151.11       |
|    24 digits    |   ~ 2.92E+47   |   ~ 9.31E+17 years  |       157.68       |
|    25 digits    |   ~ 2.77E+49   |   ~ 8.85E+19 years  |       164.25       |
|    26 digits    |   ~ 2.64E+51   |   ~ 8.40E+21 years  |       170.82       |
|    27 digits    |   ~ 2.50E+53   |   ~ 7.98E+23 years  |       177.39       |
|    28 digits    |   ~ 2.38E+55   |   ~ 7.58E+25 years  |       183.96       |
|    29 digits    |   ~ 2.26E+57   |   ~ 7.21E+27 years  |       190.53       |
|    30 digits    |   ~ 2.15E+59   |   ~ 6.85E+29 years  |       197.1        |
|    31 digits    |   ~ 2.04E+61   |   ~ 6.50E+31 years  |       203.67       |
|    32 digits    |   ~ 1.94E+63   |   ~ 6.18E+33 years  |       210.24       |
+-----------------+----------------+---------------------+--------------------+
The Table was generated based on a password composed by
Characters: [a-zA-Z0-9!@#$%^&*()+_~`-_=+[]{}|;:'",.<>?/]
Number of characters 95
Password cracking speed: 100 THz
Elements working is parallel cracking the password: 100,000,000 station(s)
```

#!/usr/bin/python3
#
import sys
import math
from prettytable import PrettyTable as ptable
from decimal import Decimal

def character_space():
    """
    Allows the user to select the character space the password will be composite from.
    ---------
    Arguments
    ---------
    No arguments are required to be parsed.
    ---------
    Returns
    ---------
    chars_space  :  based on the selected option by the user the 'chars_space' will be
    a list with the number of possible chars within that selection and the selection.
    e.g chars_space = [26,"[a-z]"]
    """
    try:
        chars_list = int(input("""
        Please select the password character composition:\n
        (1) Lower case only     [a-z]
        (2) Upper case only     [A-Z]
        (3) Numbers only        [0-9]
        (4) Lower/Upper         [a-zA-Z]
        (5) Lower/Numbers       [a-z0-9]
        (6) Upper/Numbers       [A-Z0-9]
        (7) Lower/Upper/Numbers [a-zA-Z0-9]
        (8) All and Special     [a-zA-Z0-9!@#$%^&*()+_~`-_=+[]{}\|;:\'",.<>?/]\n
        Enter a number from the list: """))
    except:
        print("\nInvalid option : Please try again and select a valid number from the list\n")
        sys.exit()
        
    if chars_list >=1 and chars_list <= 8:
        if chars_list == 1:
            chars_space = [26,"[a-z]"]
        elif chars_list == 2:
            chars_space = [26,"[A-Z]"]
        elif chars_list == 3:
            chars_space = [10,"[0-9]"]
        elif chars_list == 4:
            chars_space = [52,"[a-zA-Z]"]
        elif chars_list == 5:
            chars_space = [36,"[a-z0-9]"]
        elif chars_list == 6:
            chars_space = [36,"[A-Z0-9]"]
        elif chars_list == 7:
            chars_space = [62,"[a-zA-Z0-9]"]
        else:
            chars_space = [97,"[a-zA-Z0-9!@#$%^&*()+_~`-_=+[]{}|;:\'\",.<>?/]"]
            
    else:
        print("\nInvalid option : Please try again and select a valid number from the list\n")
        sys.exit()
        
    return chars_space

def cracking_speed():
    """
    Allows the user to select the cracking speed for a processing element.
    ---------
    Arguments
    ---------
    No arguments are required to be parsed.
    ---------
    Returns
    ---------
    crack_speed : the selected speed for the processing element as list with the
    selected option as string.
    e.g. crack_speed = [1e+6,"1 MHz"]
    """
    try:
        crack_list = int(input("""
        Please select the cracking speed:\n
        (1) 1   Mega Hertz (MHz)
        (2) 10  Mega Hertz (MHz)
        (3) 100 Mega Hertz (MHz)
        (4) 1   Giga Hertz (GHz)
        (5) 10  Giga Hertz (GHz)
        (6) 100 Giga Hertz (GHz)
        (7) 1   Tera Hertz (THz)
        (8) 10  Tera Hertz (THz)
        (9) 100 Tera Hertz (THz)\n
        Enter a number from the list: """))
    except:
        print("\nInvalid option : Please try again and select a valid number from the list\n")
        sys.exit()
    
    if crack_list >=1 and crack_list <= 9:
        if crack_list == 1:
            crack_speed = [1e+6,"1 MHz"]
        elif crack_list == 2:
            crack_speed = [10e+6,"10 MHz"]
        elif crack_list == 3:
            crack_speed = [100e+6,"100 MHz"]
        elif crack_list == 4:
            crack_speed = [1e+9,"1 GHz"]
        elif crack_list == 5:
            crack_speed = [10e+9,"10 GHz"]
        elif crack_list == 6:
            crack_speed = [100e+9,"100 GHz"]
        elif crack_list == 7:
            crack_speed = [1e+12,"1 THz"]
        elif crack_list == 8:
            crack_speed = [10e+12,"10 THz"]
        else:
            crack_speed = [100e+12,"100 THz"]
            
    else:
        print("\nInvalid option : Please try again and select a valid number from the list\n")
        sys.exit()
        
    return crack_speed

def processing_stations():
    """
    Allows the user to select the number of elements working in parallel to
    crack the password.
    ---------
    Arguments
    ---------
    No arguments are required to be parsed.
    ---------
    Returns
    ---------
    proc_stations  :  The number of processing elements.
    """
    try:
        proc_list = int(input("""
        Please select the number of processing elements working in parallel:\n
        (1) 1
        (2) 10
        (3) 100
        (4) 1,000
        (5) 10,000
        (6) 100,000
        (7) 1,000,000   
        (8) 10,000,000
        (9) 100,000,000\n
        Enter a number from the list: """))
    except:
        print("\nInvalid option : Please try again and select a valid number from the list\n")
        sys.exit()
    
    if proc_list >=1 and proc_list <= 9:
        if proc_list == 1:
            proc_stations = 1
        elif proc_list == 2:
            proc_stations = 10
        elif proc_list == 3:
            proc_stations = 100
        elif proc_list == 4:
            proc_stations = 1e+3
        elif proc_list == 5:
            proc_stations = 10e+3
        elif proc_list == 6:
            proc_stations = 100e+3
        elif proc_list == 7:
            proc_stations = 1e+6
        elif proc_list == 8:
            proc_stations = 10e+6
        else:
            proc_stations = 100e+6
            
    else:
        print("\nInvalid option : Please try again and select a valid number from the list\n")
        sys.exit()

    return proc_stations

def password_entropy(N,L):
    """
    Calculates the password entropy for the given character space and the
    length of the password.
    ---------
    Arguments
    ---------
    N   :   Character space.
    L   :   Password length.
    ---------
    Returns
    ---------
    entropy  :   Password entropy in bits.
    """
    entropy = math.log2(N**L)
    return entropy

def cracking_time(ent, speed, station):
    """
    Calculates the approximate time needed to crack a password by brute forcing
    the maximum password searching space.
    ---------
    Arguments
    ---------
    ent     :   password entropy.
    speed   :   The cracking speed per element.
    station :   The number of processing elements.
    ---------
    Returns
    ---------
    timing  :   Time to crack in seconds.
    """
    password_space = 2 ** ent
    timing = (password_space / (speed*station))
    return timing

def main():
    N = character_space()
    speed = cracking_speed()
    station = processing_stations()
    #
    # Defining the table instance
    table = ptable()
    #
    # Defining the Table headers
    table.field_names = [f"Password Length","Password Space","Time to Crack (max)", "Key Entropy (bits)"]
    #
    # Password length range; evaluating from 5 digits to 32 digits long.
    for L in range(5,33):
        ent = password_entropy(N[0],L)
        timing = cracking_time(ent, speed[0], station)
        # Time in seconds
        if timing <= 60:
            time_crack = str('%.2E' % Decimal(timing)) + " secs"
        # Time in minutes
        elif timing >= 60 and timing <= 3599:
            time_crack = str('%.2E' % Decimal(timing/60)) + " mins"
        # Time in hours
        elif timing >= 3_600 and timing <= 86_399:
            time_crack = str('%.2E' % Decimal(timing/3_600)) + " hours"
        # Time in days
        elif timing >= 86_400 and timing <= 31_535_999:
            time_crack = str('%.2E' % Decimal(timing/86_400)) + " days"
        else:
            # Time in years
            time_crack = str('%.2E' % Decimal(timing/31_356_000)) + " years"
        #
        # Adding rows to the table
        table.add_row([f"{L} digits" ,"~ " + '%.2E' % Decimal(2**ent) , "~ " + time_crack , round(ent,2)])
        
    # Printing the final Table
    print(table.get_string())
    print(f"The Table was generated based on a password composed by")
    print(f"Characters: {N[1]}")
    print(f"Number of characters {N[0]}")
    print(f"The evaluated cracking speed: {speed[1]}")
    print(f"Elements working is parallel to crack the password: {round(station):,} station(s)")

if __name__ == "__main__":
    main()

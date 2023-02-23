from sys import argv
import os
from colorama import Fore, init
from time import sleep


# initializing colorama
init(autoreset=True)

def clearConsole():
    """
    Clears the console display
    """
    if os.name == 'posix': # linux and unix-based oses.
        os.system("clear")
    elif os.name == 'nt': # windows nt
        os.system("cls")
    else:
        print(f"{Fore.RED}error: unsupported os type: {os.name}, will clear console using 'clear'")
        os.system("clear")
    return None


def printSensorsReading():
    print("Sensors available for this PC")
    print('', end='\n\n')
    print("ISA/PCI Bridges and CPU Temperatures (using lm_sensors):")
    os.system("sensors")
    print('', end='\n\n')
    print("Hard drive temperatures (using hddtemp):")
    os.system("hddtemp SATA:/dev/sda")
    os.system("hddtemp SATA:/dev/sdb")
    print('', end='\n\n')
    print(f"{Fore.YELLOW}info: this will return anything but real drive temperatures if your hard drive is unsupported or the module is not installed or if not running as sudo user")
    print('', end='\n\n')
    return None


if __name__ == '__main__':
    try:
        if len(argv) == 1:
            while True:
                clearConsole()
                printSensorsReading()
                sleep(2) # refresh rate is 2 seconds
        elif len(argv) == 2:
            try:
                refresh_rate_insecs = int(argv[1])
            except Exception:
                print(f"{Fore.RED}error: couldn't convert '{argv[1]}' to int for use with parameter 'refreshrateinsecs'")
                raise SystemExit(10)
            while True:
                clearConsole()
                printSensorsReading()
                sleep(refresh_rate_insecs)
        else:
            print(f"{Fore.RED}error: invalid command line usage, script only accepts 1 argument: refreshrateinsecs")
            raise SystemExit(20)
    except KeyboardInterrupt:
        raise SystemExit(0)
    
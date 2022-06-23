"""
Try to extend the check list script to handle more different checks, all reported as RocketNotReady exceptions.
Add your own checks for: batteries and circuits.

"""

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    global batteries
    try:
        if batteries < 100:
            x = 100/0

    except Exception as e:
        raise RocketNotReadyError('SoC low') from e


def circuits_check():
    # add your own implentation
    pass


crew = ['John', 'Mary', 'Mike']
fuel = 50
batteries = 50
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))



def oxygen_analyzer(oxygen):
    """
    oxygen: percentage of oxygen in blood (ex. 96 %)
    return: int - rate of dangerous (from 1 to 10)
            str - description of problem
    """
    if oxygen >= 95:
        dangerous = 1
        msg = 'oxygen level is normal'

    elif 65 <= oxygen < 95:
        dangerous = 5
        msg = 'low oxygen. Impaired mental function on average.'
    elif 40 <= oxygen < 65:
        dangerous = 8
        msg = 'Very low oxygen. Loss of consciousness on average.'
    elif oxygen < 40:
        dangerous = 10
        msg = 'Extremely low oxygen. Life threatening.'

    return dangerous, msg


def pulse_analyzer(pulse):
    """
    pulse: heart beats per second (ex. 70 bps)
    return int - rate of dangerous (from 1 to 10)
           str - description of problem
    """
    if 60 <= pulse < 80:
        dangerous = 1
        msg = 'Normal heart rate.'
    if 40 <= pulse < 60:
        dangerous = 4
        msg = 'Low heart rate. Body weakness.'
    if pulse < 40:
        dangerous = 7
        msg = 'Very low heart rate. Loss of consciousness.'
    if 80 <= pulse < 110:
        dangerous = 4
        msg = 'Slightly high heart rate'
    if 110 <= pulse < 150:
        dangerous = 6
        msg = 'High heart rate'
    if 150 <= pulse < 200:
        dangerous = 8
        msg = 'Extremely high heart rate.'
    if pulse >= 200:
        dangerous = 10
        msg = 'Extremely high heart rate. Life threatening.'

    return dangerous, msg


def pressure_analyzer(pressure):
    """
    pressure: tuple of sistolic and diastolic pressure (ex. 120 80)
    return int - rate of dangerous (from 1 to 10)
           str - description of problem
    """
    systolic = pressure[0]
    if pressure[0] < 50 or pressure[1] < 30:
        dangerous = 10
        msg = 'Extremely low blood preasure. Life threatening.'
    if 50 <= systolic < 120:
        dangerous = 4
        msg = 'Low blood preasure.'
    if 120 <= systolic < 140:
        dangerous = 1
        msg = 'Blood pressure is normal'
    if 140 <= systolic < 160:
        dangerous = 4
        msg = 'High blood pressure. Stage 1'
    if 160 <= systolic < 190:
        dangerous = 7
        msg = 'Very high blood pressure. Stage 2'
    if systolic >= 190:
        dangerous = 10
        msg = 'Extremely high blood preasure. Life threatening.'

    return dangerous, msg


def monitor(pulse, oxyge, pressure):
    """
    pulse: heart beats per second (ex. 70 bps)
    oxygen: percentage of oxygen in blood (ex. 96 %)
    pressure: tuple of sistolic and diastolic pressure (ex. 120 80)
    """
    minor = ''
    high_priority = ''
    results = [pulse_analyzer(pulse), oxygen_analyzer(oxygen), pressure_analyzer(pressure)]
    for result in results:
        if 3 <= result[0] <= 5:
            minor += ' - ' + result[1] + '\n'
        if result[0] > 5:
            high_priority += ' - ' + result[1] + '\n'
    if len(high_priority) == 0:
        high_priority = '-\n'
    if len(minor) == 0:
        minor = '-\n'
    return 'High priority problems:\n{}Low priority problems:\n{}'.format(high_priority, minor)


if __name__ == '__main__':
    # Open file with data
    with open(os.path.join(dir_path,'data.txt'), 'r') as file:
        for line in file:
            # Read record from file
            data = line.split()
            pulse = int(data[0])
            oxygen = int(data[1])
            pressure = ( int(data[2]), int(data[3]) )
            # Analyze record
            result = monitor(pulse, oxygen, pressure)

            # Print out result
            print('Pulse: {}\tOxygen: {}\tPressure: {}'.format(pulse, oxygen, pressure))
            print('-' * 20)
            print(result)
            print('-' * 20 + '\n')
            
            

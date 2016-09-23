AINPATH = "/sys/bus/iio/devices/iio:device0/"
resistors = {
        'VDD_5V':{'R1':988, 'R2':462},
        'SYS_5V':{'R1':975, 'R2':464}}

def read_value(ain):
        fh = open("%sin_voltage%d_raw" %(AINPATH, ain), 'r')
        return float(fh.read());

def ain2volts(ain, vsrc):
        VIN = read_value(ain)*1.800/4095
#       print VIN
#       print vsrc['R1']
#       print vsrc['R2']
        VSRC = (vsrc['R1']+vsrc['R2'])*VIN/vsrc['R2']
#       print VSRC
        return VSRC;

def getPower(ain_VDD, ain_SYS):
        R = .1
        VDD = ain2volts(ain_VDD, resistors['VDD_5V'])
        SYS = ain2volts(ain_SYS, resistors['SYS_5V'])
        I = (VDD-SYS)/R
        print ("VDD", VDD)
        print ("SYS", SYS)
        print ("Current", I)
        Power = SYS*I
        return Power;

print ("Power consumption [W]", getPower(6, 5))


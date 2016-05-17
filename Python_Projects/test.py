''' List all available com port by number '''

from serial.tools import list_ports
def serial_ports():

    available=[port[0] for port in list_ports.grep('COM')]
    ports=[int(port[3:])for port in available]
    return ports

if __name__ == '__main__':
    print sorted(serial_ports())


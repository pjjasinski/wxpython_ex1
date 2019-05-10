import serial


class SerialSender(object):
    def __init__(self):
        self.port = None

    def open_port(self, name):
        try:
            self.port = serial.Serial(name, 9600)
        except serial.serialutil.SerialException:
            print(' cannot open serial port: {}'.format(name))

    def close_port(self):
        if self.port is not None:
            self.port.close()

    def send(self, data):
        if self.port is not None:
            self.port.write(data)

    def get_available_com_ports(self):
        pass


# this section is where program starts
if __name__ == '__main__':
    sender = SerialSender()
    sender.open_port("COM3")
    sender.send('String to send over serial port')
    sender.close_port()


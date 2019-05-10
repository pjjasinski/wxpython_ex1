import time  # using time for delay
import threading  # threading import


class ExampleThread(threading.Thread):  # inherits Thread class
    def __init__(self, my_id):  # constructor
        threading.Thread.__init__(self)  # base class constructor
        self.alive_counter = 5  # running counter
        self.my_id = my_id  # id and delay value

    def run(self):  # override method
        while self.alive_counter is not 0:  # loop while running
            print('I am alive thread #{} for {}'.format(self.my_id, self.alive_counter))
            time.sleep(self.my_id)  # delay some time
            self.alive_counter = self.alive_counter - 1  # decrease alive counter

    def stop(self):  # stop method
        self.alive_counter = 0


# this section is where program starts
if __name__ == '__main__':
    app1 = ExampleThread(1)  # create example thread
    app1.start()  # starts thread
    app2 = ExampleThread(2)
    app2.start()



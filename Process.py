class Process:

    def __init__(self, id):
        self.ID = id
        self.Time = 0
        self.ReceivedMessages = []
    
    #Message must be a string
    def receive_message(self, message, time_stamp):
        timed_message = 'Message Time: ' + str(time_stamp) + ", Message: " + message
        self.ReceivedMessages.append(timed_message)
        self.Time = max (time_stamp, self.Time) + 1

    def parse_attributes(self):
        process_info = 'ID: ' + str(self.ID)
        process_info += ' - Time: ' + str(self.Time) + '\n'
        process_info += 'Received Messages:'
        for message in self.ReceivedMessages:
            process_info += ' { ' + message + ' } '
        return process_info 
from Message import Message
class Process:

    def __init__(self, id):
        self.ID = id
        self.Time = 0
        self.ReceivedMessages = []
    
    #Message must be a string
    def receive_message(self, message, time_stamp):
        timed_message = Message(message, time_stamp)
        self.ReceivedMessages.append(timed_message)
        self.Time = max (time_stamp, self.Time) + 1

    def parse_attributes(self):
        process_info = 'ID: ' + str(self.ID)
        process_info += ' - Time: ' + str(self.Time) + '\n'
        process_info += 'Received Messages:'
        for message in self.ReceivedMessages:
            process_info += ' { ' + 'Message time: ' + str(message.Time) + ' Message: ' + message.Text + ' } '
        return process_info 
from Process import Process
import cmd

Processes = []

class PoorLamportCLI(cmd.Cmd):
    intro = 'PoorLamport.   Type help or ? to list commands.\n'
    prompt = 'Lamport> '
    global Processes

    def do_add_process(self, arg):
        new_process = Process(len(Processes))
        Processes.append(new_process)
        print('Process %d created!\n' % len(Processes))

    def do_log(self, process_number):
        if int(process_number) < len(Processes):
            print(Processes[int(process_number)].parse_attributes() + '\n')
        else:
            print('Error. The process ID does not exist.\n')
    
    def do_log_all(self, arg):
        for actual_process in Processes:
            separator_string = '-' * 40
            print(separator_string)
            print(actual_process.parse_attributes())
        
        print(separator_string)

    def do_send_message(self, args):
        args = args.split()
        sender_id = args[0]
        receiver_id = args[1]
        message = args[2]

        if int(sender_id) < len(Processes) and int(receiver_id) < len(Processes):
            Processes[int(sender_id)].Time += 1
            sender_timestamp = Processes[int(sender_id)].Time
            Processes[int(receiver_id)].receive_message(message, sender_timestamp)
            print ('Message sended from process %s to process %s.\n' % (sender_id, receiver_id))
        else:
            print('Error. The process ID does not exist.\n')

    def do_exit(self, arg):
        return True

   


    def help_add_process(self):
        print('Adds a process to the list, doesnt need parameters')

    def help_log(self):
        print('Shows process information (time, messages with time).\n Syntax = log [process id] \n Process id: starts with 0 and cannot be more than total processes.')

    def help_log_all(self):
        print('Shows all processes information (time, messages with time) \n Syntax = log_all\n Does not need parameters')

    def help_send_message(self):
        print('Sends a message from x process to y process.\n Syntax = send_message [sender_id] [receiver_id] [message] \n sender_id = Sender process ID\nreceiver_id = Receiver process ID\nmessage = String to send\nExample: send_message 0 1 hi')
    
    def help_exit(self):
        print('Exits program.')

if __name__ == '__main__':
    PoorLamportCLI().cmdloop()
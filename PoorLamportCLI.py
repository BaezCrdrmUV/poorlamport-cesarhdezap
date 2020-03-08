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
        print('Adds a process to the list')

if __name__ == '__main__':
    PoorLamportCLI().cmdloop()
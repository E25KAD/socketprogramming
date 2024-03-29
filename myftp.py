import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import ftplib  

SERVER_ADDRESS = ('127.0.0.1', 21)
FTP_ROOT = "ftp_folder"  # แก้เป็น path ของ ftp_folder ของคุณ

def connect_to_server():
    ftp = ftplib.FTP()
    ftp.connect(*SERVER_ADDRESS)
    welcome_message = ftp.getwelcome()
    print(welcome_message)
    return ftp

def send_command(ftp, command):
    response = ftp.sendcmd(command)
    print(response)

def setup_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("root", "root", FTP_ROOT, perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer

    server = ThreadedFTPServer(SERVER_ADDRESS, handler)
    server.serve_forever()

def ftp_repl():
    ftp = connect_to_server()
    while True:
        user_input = input('ftp> ').strip()
        command, *args = user_input.split()
        if command == 'quit':
            send_command(ftp, 'QUIT')
            break
        elif command == 'open':
            if len(args) != 1:
                print("Usage: open <hostname>")
                continue
            global SERVER_ADDRESS
            SERVER_ADDRESS = (args[0], 21)
            print("Server address updated.")
            ftp = connect_to_server()
        elif command == 'bye':
            send_command(ftp, 'BYE')
        elif command == 'ascii':
            send_command(ftp, 'TYPE A')
        elif command == 'binary':
            send_command(ftp, 'TYPE I')
        elif command == 'cd':
            if len(args) != 1:
                print("Usage: cd <directory>")
                continue
            send_command(ftp, 'CWD {}'.format(args[0]))
        elif command == 'close':
            send_command(ftp, 'QUIT')
            ftp.quit()
            break
        elif command == 'delete':
            if len(args) != 1:
                print("Usage: delete <filename>")
                continue
            send_command(ftp, 'DELE {}'.format(args[0]))
        elif command == 'disconnect':
            send_command(ftp, 'QUIT')
            ftp.quit()
            break
        elif command == 'get':
            if len(args) != 1:
                print("Usage: get <filename>")
                continue
            send_command(ftp, 'RETR {}'.format(args[0]))
        elif command == 'ls':
            send_command(ftp, 'LIST')
        elif command == 'put':
            if len(args) != 1:
                print("Usage: put <filename>")
                continue
            send_command(ftp, 'STOR {}'.format(args[0]))
        elif command == 'pwd':
            send_command(ftp, 'PWD')
        elif command == 'rename':
            if len(args) != 2:
                print("Usage: rename <oldname> <newname>")
                continue
            send_command(ftp, 'RNFR {}'.format(args[0]))
            response = ftp.getresp()
            print(response)
            if response.startswith('350'):
                send_command(ftp, 'RNTO {}'.format(args[1]))
        elif command == 'user':
            if len(args) != 1:
                print("Usage: user <username>")
                continue
            send_command(ftp, 'USER {}'.format(args[0]))
        else:
            print("Invalid command")

if __name__ == "__main__":
    setup_ftp_server()

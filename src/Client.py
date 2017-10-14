"""
Homework 2 Client
Cameron Sprowls
"""

# Imports
import socket

import os


class Client:
    @staticmethod
    def main():
        """
        Connects to a server and retrieves a file that is requested through a directory
        """

        # Prompt the user for the IP and the port of the server they wish to connect
        # Then prompt them for the message they with to send
        # ip = input("Enter IP address: ")
        # port = int(input("Enter port: "))
        print("Type the name of the file you want, type 'help' if you want a list of available files.")
        file_name_to_server = str(input("Name of the file you want (include extension):  "))
        ip = "35.40.114.88"
        port = 5001
        buf = 4096

        # Instantiate socket in case the user exits on first run through
        s = socket

        while True:
            # If they want a list of the files, don't add the directory onto their input
            if file_name_to_server.lower() == "exit":
                print("User controlled exit. Closing program.")
                s.close()
                return
            if file_name_to_server.lower() != "help":
                file_name_to_server = "C:\\Users\\Doomninja\\PycharmProject\\FileTransfer\\Data\\" + file_name_to_server

            extension = os.path.splitext(file_name_to_server)[1]

            # Connect to the server and send the file directory
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendall(file_name_to_server.encode())

            # Callback at this point, wait for the server to start sending the data
            data_from_server = s.recv(buf)

            # Make sure the server found the file data to send
            if data_from_server.decode() != "File not found \n ENDD":

                if data_from_server.decode().endswith('LISTT'):
                    print("Files that you can pull:")
                    print(data_from_server.decode('utf16')[:-5])
                    file_name_to_server = str(input("Name of the file you want (include extension): "))
                    continue

                file = open("newFile" + extension, 'rb')
                while data_from_server:
                    if data_from_server.endswith('ENDD'.encode()):
                        u = data_from_server[:-4]
                        file.write(u)
                        break
                    else:
                        file.write(data_from_server)
                        data_from_server = s.recv(buf)

                # Close the file that we're writing to
                file.close()
                file_name_to_server = str(input("File Received. Enter the name of the file you want. "
                                                "Or type help or exit: "))

            else:
                # Print error if the file wasn't found. Close the socket and return
                file_name_to_server = str(input("File not found, check your input and try again: "))
                continue


Client.main()

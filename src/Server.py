"""
Homework 2 Server
Cameron Sprowls
"""

# Imports
import socket
import threading
import os


class Server:

    @staticmethod
    def main():
        """
        Allows clients to connect and sends files back that they request
        """

        # Prompt the user for the port from which the server will run
        ip = "35.40.114.88"
        # port = int(input("Enter port: "))
        port = 5001
        buf = 4096

        # Wait for data in a loop until data is received
        # Send the data back to the client
        while True:
            # Connect to the server and listen for data
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            s.listen(1)
            connection = s.accept()
            # looks like the threading goes here
            threading.Thread(target=Server.multi_thread(connection, s, buf), args=(connection, connection)).start()

    @staticmethod
    def multi_thread(connection, s, buf):
        # Print the a client has been connected
        print("Client has been connected.")

        # Get the file name from the client, and decode it from bytes
        file_name = connection[0].recv(buf)
        file_name = file_name.decode()

        # If they asked, send a list of the files they wanted
        if file_name == "help":
            print("Client  wanted list of files. Sending...")
            data = os.listdir("C:\\Users\\Doomninja\\PycharmProject\\FileTransfer\\Data")
            data = str(data) + "LISTT"
            connection[0].send(data.encode())

        # Send find and send the file
        elif os.path.isfile(file_name):
            file = open(file_name, 'rb')

            # Loop to iterate through the file and send it to the cleint
            while True:
                data = file.read()

                # Check if all of the file has been looked through
                if not data:
                    break

                # Send the data to the client
                connection[0].send(data)

            # Close file and send final "ENDD" note to signify that the file is done
            file.close()
            connection[0].send("ENDD".encode())

        # File not found exception, lazy exception handling. I love python.
        else:
            connection[0].send("File not found \n ENDD".encode())

        # Close socket connection
        s.close()


Server.main()

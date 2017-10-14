"""
Homework 2 Client
Cameron Sprowls
"""

# Imports
import socket


class Client:
    @staticmethod
    def main():
        """
        Does the normal function of the program
        """

        # Prompt the user for the IP and the port of the server they wish to connect
        # Then prompt them for the message they with to send
        # ip = input("Enter IP address: ")
        ip = "35.40.114.88"
        # port = int(input("Enter port: "))
        port = 5000
        buf = 1024

        # Connect to the server and send the message
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            message = input("File to request (or /exit to exit): ")

            if message == "/exit":
                s.close()
                print("Disconnected from the server")
                return

            message = "C:\\Users\\Doomninja\\PycharmProject\\FileTransfer\\Data\\" + message

            # Send the file name that the client wants to the server
            s.sendto(message.encode(), (ip, port))

            file = open("newfile.txt", 'w')

            data_from_server = s.recvfrom(buf)
            got_packets = []

            count = 0

            # Receive data, print, and save the file
            while data_from_server:
                print(data_from_server[0].decode())
                file.write(data_from_server[0].decode())
                # got_packets.append(data_from_server[0][1])
                # s.sendto(bytearray(got_packets), (ip, port))
                data_from_server = s.recvfrom(buf)
                print(count)
                count += 1
                if count > 4:
                    s.sendto(3, (ip, port))
            print("out")
            file.close()


Client.main()

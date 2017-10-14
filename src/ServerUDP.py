"""
Homework 2 Server
Cameron Sprowls
"""

# Imports
import socket

import os


class Server:

    @staticmethod
    def main():
        """
        Does the normal function of the program
        """

        # Prompt the user for the port from which the server will run
        ip = '35.40.114.88'
        port = 5000
        buf = 1024
        packets = {}
        window = 0

        # Wait for data in a loop until data is received
        # Send the data back to the client
        while True:
            # Connect to the server and listen for data
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((ip, port))

            while True:
                data = s.recvfrom(buf)
                print("message: " + str(data[0].decode()))
                if os.path.isfile(str(data[0].decode())):
                    file = open(data[0].decode(), 'rb')

                    # Loop through file and send all of it in small packets
                    while True:
                        # Store window of packets into a dictionary for easy access
                        while window < 5:
                            packets[window] = file.readline(buf)
                            print(packets)
                            s.sendto(bytearray(packets), (data[1][0], data)[1][1])
                            packets.clear()
                            window += 1

                        # Get back acknowledgements, move window accordingly
                        # Get a list of the packets that weren't sent, as well as the smallest one?
                        max_packet_sent = s.recvfrom(buf)[len(s.recvfrom(buf)) - 1]
                        print(max_packet_sent)
                        for key in packets:
                            if int(key) + max_packet_sent > 4:
                                packets[key] = []
                            else:
                                packets[key] = packets[int(key) + max_packet_sent]

                        window = max_packet_sent


Server.main()

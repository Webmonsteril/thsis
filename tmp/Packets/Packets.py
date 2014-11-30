global DIR 
DIR = str('InputDog/')
import imp
Packet = imp.load_source('Packet', '/home/ubuntu/workspace/thsisWord/Packet/Packet.py')


import os
import fnmatch
import Packet
import Chunks


class Packets():
    def __init__(self):
        self.list_of_packets = []
        pass
    def loop_over_all_files(self):
        for file_name in os.listdir(DIR):
            if fnmatch.fnmatch(file_name, '*_s.txt*'):
                current_packet = Packet.Packet()
                current_packet.set_path(DIR)
                current_packet.set_file(file_name)
                current_packet.read_content()
                self.list_of_packets.append(current_packet)
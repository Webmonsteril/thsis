import imp
Chunk = imp.load_source('Chunk', '/home/ubuntu/workspace/thsisWord/Chunk/Chunk.py')
import Chunk


class Chunks():
    def __init__(self):
        self.List_of_chunks = list()
    def make_chunks(self, packet_data, num_of_n):
        list_of_data = list(packet_data)
        for i in range(len(packet_data) - num_of_n + 1):
            self.List_of_chunks.append( Chunk.Chunk(''.join(list_of_data[ i : i + num_of_n]), i) )

__author__ = 'Alex'
import struct
from itertools import islice
import os
import fnmatch
import os

def split_by_n(seq, n):
    """A generator to divide a sequence into chunks of n units.
    :rtype : object
    """
    while seq:
        yield seq[:n]
        seq = seq[n:]


class Reader():
    def __init__(self):
        self.path = ""
        self.filename = ""
        pass

    def set_path(self, path):
        self.path = path

    def set_file(self, filename):
        self.filename = filename

    def read_content(self):
        f = open(self.path + "/" + self.filename, 'rb')
        string = f.read()
        split = string.split("\r\n\r\n")
        raw_data = split[1]
        # p = list(split_by_n(raw_data, n))
        return raw_data
        
    def loop_over_all_files(self):
        l = []
        # return test_module("../Input/001_s.txt")
        for file_name in os.listdir('InputDog/'):
            if fnmatch.fnmatch(file_name, '*_s.txt*'):
                l.append(test_module("InputDog/"+file_name))
        return ''.join(l)



def test_module(filename):
    read = Reader()
    read.set_path(os.getcwd())
    read.set_file(filename)
    return read.read_content()
    



if __name__ == "__main__":
    pass
    # print loop_over_all_files()
    # test_module()
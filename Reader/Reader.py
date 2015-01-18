__author__ = 'Alex'
import struct
from itertools import islice
import os
import fnmatch
import zlib

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
        if ("HTTP/1.1 200 OK" in string):
            split = string.split("\r\n\r\n")
            raw_data = split[1]
            # print self.filename
            # # p = list(split_by_n(raw_data, n))
            # print split[0]
            # print "alex"
            # print split[1]
            # print "igor"
            # print len(raw_data)
            if( "gzip" in split[0]):
                try:
                    decompressed = zlib.decompress(raw_data, 16+zlib.MAX_WBITS)
                except Exception, e:
                    print e
                    decompressed = raw_data
            else:
                decompressed = raw_data
            return decompressed
        else:
            print "skip ", self.filename
            return ""
        
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
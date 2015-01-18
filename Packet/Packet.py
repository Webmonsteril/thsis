__author__ = 'Alex'
import zlib
import imp
Chunks = imp.load_source('Chunks', '/home/ubuntu/workspace/thsisWord/Chunks/Chunks.py')
import Chunks

class Packet():
    def __init__(self):
        self.path = ""
        self.filename = ""
        self.data = ""
        self.chunks = Chunks.Chunks()
        pass

    def set_path(self, path):
        self.path = path

    def set_file(self, filename):
        self.filename = filename

    def read_content(self):
        f = open(self.path + "/" + self.filename, 'rb')
        string = f.read()
        #take only 200 OK
        if ("HTTP/1.1 200 OK" in string):
            #split /r/n/r/n
            split = string.split("\r\n\r\n")
            raw_data = split[1]
            if( "gzip" in split[0]):
                try:
                    #ungzip
                    self.data = zlib.decompress(raw_data, 16+zlib.MAX_WBITS)
                except Exception, e:
                    print e
                    self.data = raw_data
            else:
                self.data = raw_data
        else:
            print "skip ", self.filename

















'''




def test_module(filename):
    read = Reader()
    read.set_path(os.getcwd())
    read.set_file(filename)
    return read.read_content()
    

'''


if __name__ == "__main__":
    pass
    # print loop_over_all_files()
    # test_module()

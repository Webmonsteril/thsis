#!/usr/bin/python
#import all in-app modules
import imp
Reader = imp.load_source('Reader', '/home/ubuntu/workspace/thsis/Reader/Reader.py')
Tokenaizer = imp.load_source('Tokenaizer', '/home/ubuntu/workspace/thsis/Tokenaizer/Tokenaizer.py')
Word = imp.load_source('Word', '/home/ubuntu/workspace/thsis/Word/Word.py')
PotintialSets = imp.load_source('PotintialSets', '/home/ubuntu/workspace/thsis/PotintialSets/PotintialSets.py')

#import out-app (system) module
import sys
import os
import sys
from collections import OrderedDict
import logging
logging.basicConfig(filename='log',level=logging.DEBUG)

import Reader
import Tokenaizer
import PotintialSets

class LossyCountingAlgorithm:
    input_list = []

    def __init__(self):
        """
        :rtype : object
        """
        self.D = {}
        self.B = 1
        self.N = 0
        self.w = 1024
        self.eps = 1 / self.w
        self.__read_dump_file()
        logging.debug("Lossy Counting Algorithm init")

    def __read_dump_file(self):
        read = Reader.Reader()
        input_as_string = read.loop_over_all_files()
        # read.set_path(os.getcwd())
        # read.set_file("154_Full.txt")
        # dump_file = file('dump.txt')
        # input_as_string = read.read_content()
        # print input_as_string
        
        subsets_of_input_as_string = Tokenaizer.subset(input_as_string, 6)
        for i in subsets_of_input_as_string:
            # print i
            self.input_list.append(i)
        # print self.input_list
        print len(self.input_list)
        self.all = len(self.input_list)
        # Tokenaizer.subset(self.input_list, 4)
        #self.input_list = [1, 2, 4, 3, 4, 3, 4, 5, 4, 6, 7, 3, 3, 6, 1, 1, 3, 2, 4, 7]
        pass

    def run(self):
        dtemp = {}
        i = 0
        try:
            for i in range(len(self.input_list)):
                x = self.input_list[i].encode("hex")
                self.N += 1
                if x in self.D:
                    self.D[x][0] += 1
                    # print "inc count by 1 to ", x
                else:
                    # print "add ", x, " to D"
                    self.D.update({x: [1, self.B - 1]})

                if self.N % self.w == 0:
                    # print "D before", self.D
                    #copy to temp if valied for next iteration
                    for key, value in self.D.iteritems():
                        # print "if ", value[0], "+", value[1], " <= ", self.B, "for key: ", key
                        if int(value[0] + value[1]) <= self.B:
                            pass
                            # del self.D[key]
                            # print "delete"
                        else:
                            dtemp.update({key: value})
                            # print "stay"
                    self.D = dtemp.copy()
                    dtemp.clear()
                    # print "D after", self.D
                    self.B += 1
                #i += 1
                if i % (self.all / 10) == 0:
                    print i, "/", self.all
        except IndexError:
            print "error at index ", i
            pass
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

        sorted_x = {}
        sorted_x = OrderedDict(sorted(self.D.items(), key=lambda(k, v): (v, k), reverse=True))
        for k, v in sorted_x.iteritems():
            if v[0] > 50:
                print "key hex: [", k, "] key ascii: [", k.decode("hex"), "] count: [", v[0], "] read from: [", v[1], "]."
        #print sorted_x
        listOfPotintial = set()
        for lword in sorted_x.keys():
            for rword in sorted_x.keys():
                PotintialSets.concatinateWords(lword, rword, listOfPotintial)
        for v in listOfPotintial:
            print "key hex: [", v.decode("ascii"), "] key ascii: [", v.decode("hex"), "]"
    

def main():
    lca = LossyCountingAlgorithm()
    lca.run()


if __name__ == "__main__":
    main()

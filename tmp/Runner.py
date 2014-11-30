#!/usr/bin/python
#import all in-app modules
import imp
# Reader = imp.load_source('Reader', '/home/ubuntu/workspace/thsisWord/Reader/Reader.py')
# Tokenaizer = imp.load_source('Tokenaizer', '/home/ubuntu/workspace/thsisWord/Tokenaizer/Tokenaizer.py')
# Word = imp.load_source('Word', '/home/ubuntu/workspace/thsisWord/Word/Word.py')
# PotintialSets = imp.load_source('PotintialSets', '/home/ubuntu/workspace/thsisWord/PotintialSets/PotintialSets.py')




Packets = imp.load_source('Packets', '/home/ubuntu/workspace/thsisWord/Packets/Packets.py')
Packet = imp.load_source('Packet', '/home/ubuntu/workspace/thsisWord/Packet/Packet.py')



#import out-app (system) module
import sys
import os
import sys
from collections import OrderedDict
import logging

sys.stdout = open('run.log', 'w+')

logging.basicConfig(filename='log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global logger
logger = logging.getLogger(__name__)

# import Reader
# import Word
# import PotintialSets

import Packets
import Packet

class LossyCountingAlgorithm:
    input_list = []

    def __init__(self, bucket_size):
        self.D = {}
        self.B = 1
        self.N = 0
        self.w = bucket_size
        self.eps = 1 / self.w
        # self.__read_dump_file(len_of_chunk)
        # logger.debug("Lossy Counting Algorithm init")

    # def __read_dump_file(self, len_of_chunk):
    #     #read all files in Input path
    #     read = Reader.Reader()
    #     input_as_string = read.loop_over_all_files()
    #     #split to chunks
    #     subsets_of_input_as_string = Word.subset(input_as_string, len_of_chunk)
    #     #TODO: optimize this section
    #     for i in subsets_of_input_as_string:
    #         self.input_list.append(i)
    #     self.num_of_words = len(self.input_list)
    #     #return void
    #     pass

    def run(self, list_of_chunks):
        #temp dictionary
        dtemp = {}
        current_index = 0
        try:
            self.num_of_words = len(list_of_chunks)
            for i in range(self.num_of_words):
                word_in_hex = list_of_chunks[i]
                self.N += 1
                if word_in_hex in self.D:
                    self.D[word_in_hex][0] += 1
                    logger.debug("word %s is in dictionary, increase counter by 1", word_in_hex)
                else:
                    self.D.update({word_in_hex: [1, self.B - 1]})
                    logger.debug("word %s is not in dictionary, adding to dictionary", word_in_hex)

                if self.N % self.w == 0:
                    #copy to temp if valied for next iteration
                    logger.info("end of iteration %d", self.B)
                    for key, value in self.D.iteritems():
                        # print "if ", value[0], "+", value[1], " <= ", self.B, "for key: ", key
                        if int(value[0] + value[1]) <= self.B:
                            pass
                            logger.debug("value: %d + delta: %d <= B: %d deleting", value[0], value[1], self.B)
                            #TODO: why can't delete while iterating
                        else:
                            dtemp.update({key: value})
                            logger.debug("value: %d + delta: %d <= B: %d keep in set", value[0], value[1], self.B)
                    #copy temp D to D
                    self.D = dtemp.copy()
                    #clear temp D for next iteration
                    dtemp.clear()
                    self.B += 1
                current_index += 1
                if current_index % (self.num_of_words / 10) == 0:
                    #TODO: update to something nice
                    print i, "/", self.num_of_words
        except IndexError:
            logger.error('Error: ', exc_info=True)
            print "error at index ", current_index
            pass
        except  Exception, e:
            logger.error('Error: ', exc_info=True)
            print "Unexpected error:", sys.exc_info()[0]
            raise
        # print self.D

        sorted_x = OrderedDict(sorted(self.D.items(), key=lambda(k, v): (v, k), reverse=True))
        for k, v in sorted_x.iteritems():
            if v[0] > 0:
                print "key hex: [", k.word, "] key ascii: [", k.word, "] position: [ ", k.position ," ] count: [", v[0], "] read from: [", v[1], "]."
        return sorted_x
    
def potential_next(input_dictionary_of_words):
    listOfPotintial = set()
    for lword in input_dictionary_of_words.keys():
        for rword in input_dictionary_of_words.keys():
            PotintialSets.concatinateWords(lword, rword, listOfPotintial)
    print "============ Potential next iteration words ============"
    for v in listOfPotintial:
        print "key hex: [", v.decode("ascii"), "] key ascii: [", v.decode("hex"), "]"
    return listOfPotintial
    



def main():
    p = Packets.Packets()
    p.loop_over_all_files()
    for packet in p.list_of_packets:
        packet.chunks.make_chunks(packet.data , 4)
        # print packet.data
        for i in packet.chunks.List_of_chunks:
            print i
    lca4 = LossyCountingAlgorithm(1024*10)
    sorted_x4 = lca4.run(packet.chunks.List_of_chunks)

if __name__ == "__main__":
    main()


class Word():
    word = ""
    position = 0
    def __init__(self, word, pos):
        self.word = word
        self.position = pos
    # def __cmp__(self, other):
    #     print "__cmp__()__ called"
    #     if( self.word == other.word and self.position == other.position ):
    #         return 0
    #     else:
    #         return -1
    # def __contains__(self, other):
    #     print "__contains__ called"
    #     if( self.word == other.word and self.position == other.position ):
    #         return True
    #     else:
    #         return False
    def __iter__(self):
        print "__iter__ called"
    # def __getattr__(self, attr):
    #     print "__getattr__ called"
    #     return self
    def __hash__(self):
        # print "__hash__ called"
        return hash(self.word) ^ hash(self.position)
    def __eq__(self, other):
        if( self.word == other.word and self.position == other.position ):
            return True
        else:
            return False
    def __str__(self):
        return self.word
    def __repr__(self):
        return self.word + "@" + str(self.position)
        
        
def subset(a, num_of_n):
    """

    :rtype : object
    """
    listofa = list(a)
    for i in range(len(listofa) - num_of_n + 1):
        yield Word(''.join(listofa[i:i+num_of_n]),i)
        
if __name__ == "__main__":
    pos = 0
    f = open("../Input/001_s.txt", 'rb')
    string = f.read()
    split = string.split("\r\n\r\n")
    raw_data = split[1]
    subset_of_raw_data = subset(raw_data, 4)
    for i in subset_of_raw_data:
        print i.word.encode("hex"), i.position
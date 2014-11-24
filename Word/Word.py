
class Word():
    word = ""
    position = 0
    def __init__(self, word, pos):
        self.word = word
        self.position = pos
        
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
    subset_of_raw_data = subset(raw_data, 20)
    for i in subset_of_raw_data:
        print i.word.encode("hex"), i.position
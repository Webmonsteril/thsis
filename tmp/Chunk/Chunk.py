class Chunk():
    word = ""
    position = 0
    def __init__(self, word, pos):
        self.word = word
        self.position = pos
    def __iter__(self):
        print "__iter__ called"
    def __hash__(self):
        return hash(self.word) ^ hash(self.position)
    def __eq__(self, other):
        if( self.word == other.word and self.position == other.position ):
            return True
        else:
            return False
    def __str__(self):
        return self.word + "@" + str(self.position)
    def __repr__(self):
        return self.word + "@" + str(self.position)
#!/usr/bin/python
__author__ = 'Alex'


def subset(a, num_of_n):
    """

    :rtype : object
    """
    listofa = list(a)
    for i in range(len(listofa) - num_of_n + 1):
        # print listofa[i:i+num_of_n]
        yield ''.join(listofa[i:i+num_of_n])


def main():
    teststring = "1234567890"
    subsets_of_a = subset(teststring, 5)
    for i in subsets_of_a:
        print i

    # set_a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # subsets_of_a = subset(set_a, 8)
    # for i in subsets_of_a:
    #     print i


if __name__=="__main__":
    main()
with open('mothersMilk/milk3.in', 'r') as infile:
    line = infile.readline()
    nums = line.split(" ")
    nums = [int(x) for x in nums]

global states
states = []

class state: # single state of a bucket config (ex, 0 0 10)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def edge(a, b, c, fromBucket, toBucket):
    ''' edge func moves through states tree with BFS, 
    adds states to the list
    in the end we will check list because it have all the states 
    we loop through all different permutations of from and to buckets later,
    and plug them into this function '''







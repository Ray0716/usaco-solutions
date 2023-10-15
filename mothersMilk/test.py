class state: # single state of a bucket config (ex, 0 0 10)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


test = []
test.append(state(0, 0, 0))

t = test[0]


print(t.a)
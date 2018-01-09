import numpy

class Labirynt:
    def __init__(self):
        with open("labirynt1.txt", "r") as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
        self.done = False
        self.start = "@"
        self.end = "$"
        self.height, self.width = self.lines[0].split(' ')
        self.height = int(self.height)
        self.width = int(self.width)

    def printuj(self):
        for c in self.lines[1:]:
            print c

    def findStart(self):
        tab = numpy.empty((self.height, self.width), dtype=object)
        for y in range(0, len(self.lines)-1):
            for x in range(len(self.lines[y+1])):
                if self.lines[y+1][x] == self.start:
                    sY, sX= y, x
                tab[y][x] = str(self.lines[y+1][x])
        self.lines = tab
        startCo = [sX,sY]
        return startCo

    def value(self, x, y):
        return self.lines[y][x]

    def listToString(self, list):
        tab=[]
        print tab
        for c in self.lines:
            tab.append("".join(c))
        # print 'Wykonuje?'
        return self.printuj2(tab)

    def printuj2(self,tab):
        for c in tab:
            print c


    def findEnd(self,cor=[],way=[]):
        if self.value(cor[0], cor[1]) == self.end:
            self.done = True
            return  self.listToString(self.lines)

        if self.value(cor[0], cor[1]) != '@':
            self.lines[cor[1]][cor[0]] = '.'
        # print 'cor',cor[0],cor[1]

        if (((self.value(cor[0]+1,cor[1])== ' ') or (self.value(cor[0]+1,cor[1]) == self.end))
            and (self.value(cor[0]+1,cor[1]) != self.start)
            and (self.value(cor[0]+1,cor[1]) != '#')
            and self.done == False) :
            way.append([cor[0] + 1, cor[1]])
            self.findEnd([cor[0] + 1, cor[1]])

        if (((self.value(cor[0], cor[1]+1) == ' ') or (self.value(cor[0] , cor[1]+ 1) == self.end))
            and (self.value(cor[0], cor[1]+1) != self.start)
            and (self.value(cor[0], cor[1]+1) != '#')
            and self.done == False):
            way.append([cor[0], cor[1]+1])
            self.findEnd([cor[0], cor[1]+1])

        if (((self.value(cor[0] - 1, cor[1]) == ' ') or (self.value(cor[0] - 1, cor[1]) == self.end))
            and (self.value(cor[0] - 1, cor[1]) != self.start)
            and (self.value(cor[0] - 1, cor[1]) != '#')
            and self.done == False):
            way.append([cor[0] - 1, cor[1]])
            self.findEnd([cor[0] - 1, cor[1]])

        if (((self.value(cor[0], cor[1] - 1) == ' ') or (self.value(cor[0] , cor[1]- 1) == self.end))
            and (self.value(cor[0], cor[1] - 1) != self.start)
            and (self.value(cor[0], cor[1] - 1) != '#')
            and self.done == False):
            way.append([cor[0], cor[1] - 1])
            self.findEnd([cor[0], cor[1] - 1])





Lab = Labirynt()

teab =Lab.findStart()
Lab.findEnd(teab)

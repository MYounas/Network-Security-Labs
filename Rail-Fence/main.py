from copy import deepcopy

class Main:

    def __init__(self):
        self.CT=""

    def main(self):
        self.PT=input("Enter Plain Text: ")
        self.key=int(input("Enter Key: "))

        self.col=len(self.PT)
        self.row=self.key

        self.railMat=[]
        for i in range(self.row):
            self.railMat.append([])

        #encryption start

        i=0
        while i < self.col:

            for j in range(self.row-1):
                if i<self.col:
                    self.railMat[j].append(self.PT[i])
                    i += 1

            for j in range(self.row-1,0,-1):
                if i<self.col:
                    self.railMat[j].append(self.PT[i])
                    i += 1

        for i in range(self.row):
            for j in range(len(self.railMat[i])):
                self.CT+=self.railMat[i][j]


        #encryption done


        #decryption

        self.decMat=[]
        for i in range(self.row):
            self.decMat.append([])

        i = 0
        while i < self.col:

            for j in range(self.row - 1):
                if i < self.col:
                    self.decMat[j].append("-")
                    i += 1

            for j in range(self.row - 1, 0, -1):
                if i < self.col:
                    self.decMat[j].append("-")
                    i += 1

        #replace dashes with cipher text

        k=0
        for i in range(self.row):
            for j in range(len(self.decMat[i])):
                self.decMat[i][j]=self.CT[k]
                k+=1


        self.dupDecMat=deepcopy(self.decMat)


        self.afterDec=""

        #read values from decryption matrix

        i = 0
        while i < self.col:

            for j in range(self.row - 1):
                if i < self.col:
                    self.afterDec +=self.decMat[j].pop(0)
                    i += 1

            for j in range(self.row - 1, 0, -1):
                if i < self.col:
                    self.afterDec +=self.decMat[j].pop(0)
                    i += 1






        print(self.railMat)
        print(self.dupDecMat)
        print(self.CT)
        print(self.afterDec)


Main().main()
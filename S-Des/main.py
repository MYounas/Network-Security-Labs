class Main:
    _IP = [2, 6, 3, 1, 4, 8, 5, 7]
    _EP = [4, 1, 2, 3, 2, 3, 4, 1]
    _P_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 7]
    _P_8 = [6, 3, 7, 4, 8, 5, 10, 9]
    _P_4 = [2, 4, 3, 1]
    _IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]
    _S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    _S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    def main(self):
        self.key = str(input("Key:"))
        self.PT = str(input("P.T:"))

        key1, key2 = self.keyMethod(self.key)

        print(key1,key2)

    def keyMethod(self, key):
        key1 = key2 = temp = ""

        for i in range(len(Main._P_10)):
            temp += key[Main._P_10[i] - 1]

        key=temp

        L, R = key[:5], key[5:]

        L, R = L[1:] + L[:1], R[1:] + R[:1]

        temp=L+R
        for i in range(len(Main._P_8)):
            key1+=temp[Main._P_8[i]-1]

        L, R= L[2:] + L[:2], R[2:] + R[:2]

        temp=L+R
        for i in range(len(Main._P_8)):
            key2+=temp[Main._P_8[i]-1]

        return key1, key2

obj=Main()
obj.main()
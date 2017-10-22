class Main:
    _IP = [2, 6, 3, 1, 4, 8, 5, 7]
    _EP = [4, 1, 2, 3, 2, 3, 4, 1]
    _P_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 7]
    _P_8 = [6, 3, 7, 4, 8, 5, 10, 9]
    _P_4 = [2, 4, 3, 1]
    _IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]
    _S0 = {"00": {"00": "01", "01": "00", "10": "11", "11": "10"},
           "01": {"00": "11", "01": "10", "10": "01", "11": "00"},
           "10": {"00": "00", "01": "10", "10": "01", "11": "11"},
           "11": {"00": "11", "01": "01", "10": "11", "11": "10"}}
    _S1 = {"00": {"00": "00", "01": "01", "10": "10", "11": "11"},
           "01": {"00": "10", "01": "00", "10": "01", "11": "11"},
           "10": {"00": "11", "01": "00", "10": "01", "11": "00"},
           "11": {"00": "10", "01": "01", "10": "00", "11": "11"}}

    def main(self):
        self.key = str(input("Key:"))
        self.PT = str(input("P.T:"))

        self.key1, self.key2 = self.keyMethod(self.key)

        afterIP = ""

        for i in range(len(Main._IP)):
            afterIP += self.PT[Main._IP[i] - 1]

        self.L,self.R=afterIP[:4],afterIP[4:]

        # encryption
        ansrLastXOR = self.Round(self.R, self.key1)
        afterRound1=self.R+ansrLastXOR
        self.L, self.R = afterRound1[:4], afterRound1[4:]
        round2EText = self.Round(self.R, self.key2)

        temp=round2EText+self.R

        self.CT=""
        for i in range(len(Main._IP_1)):
            self.CT+=temp[Main._IP_1[i]-1]

        afterIPD = ""

        for i in range(len(Main._IP)):
            afterIPD += self.CT[Main._IP[i] - 1]

        self.L, self.R = afterIPD[:4], afterIPD[4:]

        # decryption
        ansrLastXORD = self.Round(self.R, self.key2)
        afterRound1D=self.R+ansrLastXORD
        self.L, self.R = afterRound1D[:4], afterRound1D[4:]
        round2DText = self.Round(self.R, self.key1)

        temp=round2DText+self.R

        self.PTD=""
        for i in range(len(Main._IP_1)):
            self.PTD+=temp[Main._IP_1[i]-1]

        print(self.key1, self.key2, self.CT, self.PTD)

    def keyMethod(self, key):
        key1 = key2 = temp = ""

        for i in range(len(Main._P_10)):
            temp += key[Main._P_10[i] - 1]

        key = temp

        L, R = key[:5], key[5:]

        L, R = L[1:] + L[:1], R[1:] + R[:1]

        temp = L + R
        for i in range(len(Main._P_8)):
            key1 += temp[Main._P_8[i] - 1]

        L, R = L[2:] + L[:2], R[2:] + R[:2]

        temp = L + R
        for i in range(len(Main._P_8)):
            key2 += temp[Main._P_8[i] - 1]

        return key1, key2

    def Round(self, text, key):

        temp = ""
        for i in range(len(Main._EP)):
            temp += text[Main._EP[i] - 1]

        text = self.convertXOR(temp, key)

        s0, s1 = text[:4], text[4:]

        s0R, s0C = s0[0] + s0[3], s0[1] + s0[2]
        s1R, s1C = s1[0] + s1[3], s1[1] + s1[2]

        s0Text=Main._S0[s0R][s0C];
        s1Text=Main._S1[s1R][s1C];

        joinS=s0Text+s1Text

        temp=""
        for i in range(len(Main._P_4)):
            temp+=joinS[Main._P_4[i]-1]


        return self.convertXOR(temp,self.L)

    def convertXOR(self, t1, t2):
        ansr = ""
        for i in range(len(t1)):
            ansr += "0" if t1[i] == t2[i] else "1"

        return ansr


obj = Main()
obj.main()

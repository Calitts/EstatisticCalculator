import random


class calculate:
    def __init__(self):
        self.list_list = [1, 1, 1, 4, 4, 4]
        self.aprx = 2
        self.final = {}
        self.candidate = []

    def main(self, transform=True):
        acu = []
        fra = []

        for i, name in enumerate(set(self.list_list)):
            result = {}
            num = self.list_list.count(name)
            acu.append(num)

            result["Nome"] = name
            result["F"] = num
            result["Fa"] = sum(acu)

            if (num*100) % len(self.list_list)*100 == 0:
                freq = (num*100)//len(self.list_list)
            elif (num*100) % len(self.list_list)*100 > 0:
                freq = round((num*100)/len(self.list_list), self.aprx-1)
                self.candidate.append(i)

            fra.append(freq)

            result["Fr"] = freq
            result["Fra"] = round(sum(fra), self.aprx-1)

            if len(set(self.list_list)) == i+1:
                self.final["Last"] = result
            else:
                self.final[i] = result

        if transform:
            self.transform()

    def transform(self):
        perc = self.final["Last"]["Fra"]
        while perc != 100.0:
            if perc > 100:
                self.final[self.candidate[0]]["Fr"] = round(
                    self.final[self.candidate[0]]["Fr"] - 0.01, self.aprx)
                perc = round(perc - 0.01, self.aprx)
                self.update()

            if perc < 100:
                self.final[self.candidate[0]]["Fr"] = round(
                    self.final[self.candidate[0]]["Fr"] + 0.01, self.aprx)
                perc = round(perc + 0.01, self.aprx)
                self.update()

    def update(self):
        fra = []
        for index in self.final.keys():
            fra.append(float(self.final[index]["Fr"]))
            # print(self.final[index]["Fr"])
            # print(index)

        self.final["Last"]["Fra"] = round(sum(fra), self.aprx-1)
        #print(round(sum(fra), self.aprx-1))
        # print(self.final["Last"]["Fra"])

    def print(self):
        print(self.final)


cal = calculate()
cal.main()
cal.print()


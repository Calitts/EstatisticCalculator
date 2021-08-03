
class Calculate:  # The main class, reponsible for calculating and printing the values
    def __init__(self, list=[1, 1, 1, 3, 4, 4, 2, 2, 2], pre_cal=True):
        self.list_list = list
        self.aprx = 2
        self.final = {}
        self.candidate = []
        if pre_cal:  # If the program will calculate altomicaly the values
            self.run()

    def run(self, transform=True, show=False):  # Calculates the value and puts in a dict (self.final)
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
        
        if show:
            self.show()

    def give(self):  # Giev the value of the final in form of a dict
        return self.final

    def transform(self):  # Round the values to sum up to 100%
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

    def update(self):  # Update the value of the final dict
        fra = []
        for index in self.final.keys():
            fra.append(float(self.final[index]["Fr"]))
            # print(self.final[index]["Fr"]) - Debug
            # print(index) - Debug

        self.final["Last"]["Fra"] = round(sum(fra), self.aprx-1)
        # print(round(sum(fra), self.aprx-1)) - Debug
        # print(self.final["Last"]["Fra"]) - Debug

    def show(self):  # Print the value of the final dict
        print(self.final)


cal = Calculate()
cal.show()



class Weather:
    #Private city : str
    #Private temp : int
    #Private humid : int
    #Private raining : boolean

    def __init__(self,city, temp, humid, raining):
        self.__city = city
        self.__temp = temp
        self.__humid = humid
        self.__raining = raining

    def display(self):
        raining_status = "raining" if self.__raining else "not raining"
        print(f"{self.__city} has {self.__temp}°C, {self.__humid}% humidity and it is {raining_status}.")

wtrec = []

def RecToArray():
    global wtrec
    weather = ""
    num = int(input("Enter the Number of Data Entries : "))

    for x in range(0, num):
        city = str(input("Enter City :"))
        temp = int(input("Enter Temperature :"))
        humid = int(input("Enter Humidity :"))
        raining_input = input("Raining or Not Raining? (yes or no):").strip().lower()
        raining = True if raining_input == "yes" else False

        weather = Weather(city, temp, humid, raining)
        wtrec.append(weather)
        weather.display()
        print("--------------------------------------")

    print("Weather Records : ")
    for record in wtrec:
        record.display()

RecToArray()
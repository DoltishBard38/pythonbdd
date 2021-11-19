import datetime
import sys


class Retirement:
    birthYear = 0
    birthMonth = 0

    def retirement(self):
        while self.birthYear != "1":
            print('Social Security Full Retirement Age Calculator')
            self.birthYear = int(input("Enter the year of birth or to exit"))
            if self.birthYear == "1":
                sys.exit("Process finished with exit code 0")
            self.birthMonth = int(input("Enter the month of birth"))

            if self.birthYear <= 1937:
                print("Your full retirement age is 65 and 0 months")
            elif self.birthYear == 1938:
                print("Your full retirement age is 65 and 2 months")
            elif self.birthYear == 1939:
                print("Your full retirement age is 65 and 4 months")
            elif self.birthYear == 1940:
                print("Your full retirement age is 65 and 6 months")
            elif self.birthYear == 1941:
                print("Your full retirement age is 65 and 8 months")
            elif self.birthYear <= 1942:
                print("Your full retirement age is 65 and 10 months")
            elif 1943 <= self.birthYear <= 1954:
                print("Your full retirement age is 66 and 0 months")
            elif self.birthYear == 1955:
                print("Your full retirement age is 66 and 2 months")
            elif self.birthYear == 1956:
                print("Your full retirement age is 66 and 4 months")
            elif self.birthYear == 1957:
                print("Your full retirement age is 66 and 6 months")
            elif self.birthYear == 1958:
                print("Your full retirement age is 66 and 8 months")
            elif self.birthYear == 1959:
                print("Your full retirement age is 66 and 10 months")
            else:
                if self.birthYear == 1960 or self.birthYear > 1960:
                    print("Your full retirement age is 65 and 2 months")
            self.calculateRetirement()
    def calculateRetirement(self):

        dob = datetime.datetime(self.birthYear, self.birthMonth)


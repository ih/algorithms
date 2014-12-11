# Create a class DivisorDigits containing a method howMany which takes an 
# integer number and returns how many digits in number divide evenly into number
# itself

class DivisorDigits:
    def howMany(self, number):
        return len([digit for digit in str(number) if int(digit) != 0 and number % int(digit) == 0])


dd = DivisorDigits()
print dd.howMany(12345)
print dd.howMany(661232)
print dd.howMany(52527)
print dd.howMany(73000000)

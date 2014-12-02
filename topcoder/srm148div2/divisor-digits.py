# Create a class DivisorDigits containing a method howMany which takes an 
# integer number and returns how many digits in number divide evenly into number
# itself

class DivisorDigits:
    def howMany(self, number):
        divisor_count = 0
        digits = number
        while digits > 0:
            digit = digits % 10
            digits /= 10
            if digit == 0:
                continue

            if number / (digit * 1.0) == number / digit:
                divisor_count += 1
        return divisor_count

dd = DivisorDigits()
print dd.howMany(12345)
print dd.howMany(661232)
print dd.howMany(52527)
print dd.howMany(73000000)

#Implement an algorithm to determine if a string has all unique characters

def isAllUnique(string):
    seen_characters = {}
    for character in string:
        if character in seen_characters:
            return False
        else:
            seen_characters[character] = True
    return True

assert isAllUnique("")
assert isAllUnique("a")
assert not isAllUnique("aa")
assert isAllUnique("ab")
assert not isAllUnique("abcba")
print "all good!"

#What if you cannot use additional data structures?

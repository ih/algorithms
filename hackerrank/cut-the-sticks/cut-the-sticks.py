def printCuts(sticks):
    if len(sticks) == 0:
        return
    else:
        print len(sticks)
        smallest_stick = min(sticks)
        cut_sticks = [
            stick - smallest_stick
            for stick in sticks if stick - smallest_stick > 0]
        return printCuts(cut_sticks)

printCuts([5, 4, 4, 2, 2, 8])
printCuts([1, 2, 3, 4, 3, 3, 2, 1])

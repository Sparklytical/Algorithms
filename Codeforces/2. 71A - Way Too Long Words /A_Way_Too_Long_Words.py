tc = int(input())


for i in range(tc):
    val = str(input())
    length = len(val)

    def wayTooLong(val):
        if (length <= 10):
            return val
        else:
            return val[0] + str((length - 2)) + val[-1]
    print(wayTooLong(val))

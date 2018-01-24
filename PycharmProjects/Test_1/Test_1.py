
def nearest_square(limit):
    c = 1
    while (c * c) <= limit:
        c += 1
    return (c - 1) * (c - 1)

print("Enter limit==")
test1 = input()
test2 = int(test1)
test2=nearest_square(test2)
print("actual result: {}".format(test2))

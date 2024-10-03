def hello_world():
    print("hello world")

#funkce která vypíše požadovaný počet hvězd
def five_stars(limit):
    i = 0 
    while i < limit:
        print("*")
        i += 1




def in_range(number, minimum, maximum):
    if number > minimum and number < maximum:
        print("number", number, "is in range", minimum)
    else:print("out of range")     


in_range(1, 100, 1000)
"number 1 is out of range 100 = 10000"
in_range(500, 100, 1000)
"number 500 is in range 100 = 1000"


# funkce vrati nejvetsí cislo z a, b, c
def max_number(a, b, c):
    if a > b and a > c:
        return a
    if b > c and b > c:
        return b
    if c > b and c > a:
        return c
    print("m")



m = max_number(1, 2, 3)
3
m = max_number(100, 10, 1)
100
m = max_number(1.1, 1.3, 1.2)
1.3
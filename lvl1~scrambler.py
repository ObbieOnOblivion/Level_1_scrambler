import random

list_message = []
print('------------------------------############-----------------------------')
with open("day_codes", 'r') as codesheet:
    list1 = []
    r = codesheet.readlines()
    for i in r:
        i = i.strip("\n")
        list1.append(i)

    Rands = str(random.choice(list1))
    Rands = Rands.strip('(')
    Rands = Rands.strip(')')
    word = Rands.split(", ")
    code = None
    list2 = list()
    for i in word:
        i = int(i)
        list2.append(i)
        code = tuple(list2)

    print(code)
    R1, R2, R3 = code


print('------------------------------############-----------------------------')


with open('message_file', 'r') as message:
    R1 = 6  # i want to add a method in whixh i could ask the user for a number code
    read = message.read()
    read = read.lower()

    def get_letter(number):
        dict1 = dict()
        jeep = 'abcdefghijklmnopqrstuvwxyz'
        for letter in jeep:
            dict1[jeep.index(letter) + 1] = letter

        return dict1[number]


    def get_number(letter):
        dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
                 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                 's': 19, 't': 20, "u": 21, "v": 22, "w": 23, "x": 24,
                 'y': 25, 'z': 26}

        return dict1[letter]


    print(get_number("l"))

    print(get_letter(2))

    print('------------------------------############-----------------------------')
    """so with this section i will take this in a functional perspective, within the functions i will take care of the 
    cross wiring inside each rotor  """

    """before this i need to add a general position to find the offset and from there we chose the number
     to go into the rotor one """
    for qwert in read:
        if qwert not in 'qazwsxedcrfvtgbyhnujmikolp':

            list_message.append(qwert)
        if qwert in 'qazwsxedcrfvtgbyhnujmikolp':

            number101 = get_number(qwert)

            def letter_position():
                p1 = number101
                c1 = p1 + R1
                if c1 > 26:
                    c1 -= 26

                return c1


            james = letter_position()


            def rotor_position_1():
                key = letter_position()
                print(key, "first rotor position")
                cross_wiring = {'16': 13, '1': 26, '2': 17, '3': 19, '4': 5, '6': 21, '7': 24, '8': 22,
                                '9': 14, '10': 23, '11': 25, '12': 18, '15': 20}

                if str(key) in cross_wiring.keys():
                    return key, cross_wiring[str(key)]

                elif str(key) not in cross_wiring.keys():

                    if key in cross_wiring.values():

                        list101 = list()
                        for items in cross_wiring.values():
                            list101.append(items)

                        jin = int(list101.index(key))
                        list3 = []
                        for item in cross_wiring.keys():
                            list3.append(item)
                        inta = list3[jin]
                        inta = int(inta)

                        return key, inta

                else:
                    return None


            rotor1 = rotor_position_1

            def rotor_position_2():
                key = rotor1()[1]
                print(key, "second rotor key")
                cross_wiring = {'1': 19, '2': 7, '3': 23, '4': 16, '5': 25, '6': 9, '8': 15, '10': 11,
                                '12': 22, '13': 26, '14': 17, '18': 20, '21': 24}
                if str(key) in cross_wiring.keys():
                    return key, cross_wiring[str(key)]

                elif str(key) not in cross_wiring.keys():

                    if key in cross_wiring.values():

                        list101 = list()
                        for items in cross_wiring.values():
                            list101.append(items)

                        jin = int(list101.index(key))
                        list3 = []
                        for item in cross_wiring.keys():
                            list3.append(item)
                        inta = list3[jin]
                        inta = int(inta)

                        return key, inta

                else:
                    return None


            rotor2 = rotor_position_2


            def rotor_position_3():
                key = rotor2()[1]
                cross_wiring = {'1': 17, '2': 24, '3': 6, '4': 9, '5': 11, '7': 8, '10': 21, '12': 16,
                                '13': 23, '14': 19, '15': 18, '20': 22, '25': 26}

                if str(key) in cross_wiring.keys():
                    return key, cross_wiring[str(key)]

                elif str(key) not in cross_wiring.keys():

                    if key in cross_wiring.values():

                        list101 = list()
                        for items in cross_wiring.values():
                            list101.append(items)

                        jin = int(list101.index(key))
                        list3 = []
                        for item in cross_wiring.keys():
                            list3.append(item)
                        inta = list3[jin]
                        inta = int(inta)

                        return key, inta

                else:
                    return None


            rotor3 = rotor_position_3
            print(rotor3()[1])


            def output_1():
                number = rotor3()[1]
                return get_letter(number)

            if qwert in "qazwsxedcrfvtgbyhnujmikolp":
                list_message.append(output_1())
            else:
                if qwert in "!@#$%^&*()_+=-|}{`\][';/.,?><:`~ \'\"12334567890":
                    list_message.append(qwert)

        if R1 > 26:
            R1 = 1
        else:
            R1 += 1


stringvar = ''
with open('output_message', 'w') as killer:
    def print_job():
        for var in list_message:
            yield var

    stageVar = 0

    for inti in print_job():
        if inti != '\n':
            stageVar += 1
            killer.write(inti)
            if stageVar == 80:
                killer.write("\n")

                stageVar = 0
            next(print_job())


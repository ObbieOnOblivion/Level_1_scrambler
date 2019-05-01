import random
with open("day_codes", 'r') as codesheet:
    # The three rotors and the days of the week
    # this is the secret the rotor positions
    # this would be 26 X 26 X 26 ways
    list1 = []
    r = codesheet.readlines()
    for i in r:
        i = i.strip('\n')
        list1.append(i)

    Rands = str(random.choice(list1))
    # print(Rands)
    Rands = Rands.strip('(')
    Rands = Rands.strip(')')
    word = Rands.split(", ")
    # print(word)
    code = None
    list2 = list()
    for i in word:
        i = int(i)
        list2.append(i)
        code = tuple(list2)

    print(code)
    R1, R2, R3 = code


with open('message_file', 'r') as message:
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
        # dict1 = dict([2, l] if 'a' in "abcdefghijklmnopqrstuvwxyz" else [2,22] for l in range(1, 33))
        # figure out how to use to for loops at the same time to make full dict items

        return dict1[letter]

    for qwert in read:
        if qwert:
            number101 = get_number('j')

            def letter_position():
                p1 = number101
                c1 = p1 + R1
                if c1 > 26:
                    c1 -= 26

                return c1


            james = letter_position()
            # print(james)


            def rotor_position_1():
                key = letter_position()
                cross_wiring = {'16': 13, '1': 26, '2': 17, '3': 19, '4': 5, '6': 21, '7': 24, '8': 22,
                                '9': 14, '10': 23, '11': 25, '12': 18, '15': 20}

                if str(key) in cross_wiring.keys():
                    return key, cross_wiring[str(key)]

                elif str(key) not in cross_wiring.keys():

                    # print("its in the second round")
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
                cross_wiring = {'1': 19, '2': 7, '3': 23, '4': 16, '5': 25, '6': 9, '8': 15, '10': 11,
                                '12': 22, '13': 26, '14': 17, '18': 20, '21': 24}
                if str(key) in cross_wiring.keys():
                    # print('first round pics')
                    return key, cross_wiring[str(key)]

                elif str(key) not in cross_wiring.keys():

                    # print("its in the second round")
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

            def rotor_position_3(): # we need to incorporate R1 and R2 and R3 we need relative positions for eac one
                key3 = None
                key = rotor2()[1]
                cross_wiring = {'1': 17, '2': 24, '3': 6, '4': 9, '5': 11, '7': 8, '10': 21, '12': 16,
                                '13': 23, '14': 19, '15': 18, '20': 22, '25': 26}

                if str(key) in cross_wiring.keys():
                    # print('first round pics - 3rd')
                    return key, cross_wiring[str(key)]

                elif str(key) not in cross_wiring.keys():

                    # print("its in the second round")
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


            def output_1():
                number = rotor3()[1]
                return get_letter(number)

            # print(rotor1())
            # print(rotor2())
            # print(rotor3())
            # print(output_1())
            with open('output_message', 'a') as killer:
                if qwert in "qazwsxedcrfvtgbyhnujmikolp":
                    print(output_1(), file=killer)
                else:
                    if qwert in "!@#$%^&*()_+=-|}{\][';/.,?><:`~ \'\"12334567890":
                        print(qwert, file=killer)

        if R1 > 26:
            R1 = 1
        else:
            R1 += 1




import sys
import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def greet(input):
    if input == None or len(input) == 0:
        return "Hello, my friend."
    if isinstance(input, str):
        s = input.split("\\\"")
        lowerRes = []
        upperRes = []
        for i in s:
            if i.isupper():
                upperRes.append(i)
            else:
                lowerRes.append(i)
        if len(lowerRes) == 2:
            lowerRes = ' and '.join(lowerRes)
        if len(upperRes) == 2:
            upperRes = ' AND '.join(lowerRes)
        lowerResult = ', '.join(lowerRes)
        upperResult = ", ".join(upperRes)
        if len(upperResult) == 0:
            return "Hello, " + lowerResult + "."
        elif len(lowerResult) == 0:
            return "HELLO " + upperResult + "!"
        else:
            return "Hello " + lowerResult + ". AND HELLO " + upperResult + "!"
    else:
        lowerRes = []
        upperRes = []
        for i in input:
            if "\"" not in i:
                if i.isupper():
                    if isinstance(i, str):
                        if ',' in i:
                            print(i + " " + str(lineno()))
                            upperRes += [x for x in i.split(", ")]
                        else:
                            print(i + " " + str(lineno()))
                            upperRes.append(i)
                    else:
                        print(i + " " + str(lineno()))
                        upperRes += [x for x in i.split(", ")]
                else:
                    if isinstance(i, str):
                        if ',' in i:
                            print(i + " " + str(lineno()))
                            lowerRes += [x for x in i.split(", ")]
                        else:
                            print(i + " " + str(lineno()))
                            lowerRes.append(i)
                    else:
                        print(i + " " + str(lineno()))
                        lowerRes += [x for x in i.split(", ")]
            else:
                 if i.isupper():
                    upperRes.append(i.replace('""', '"').replace("\\", ""))
                 else:
                    lowerRes.append(i.replace('"', '').replace("\\", ""))
        lowerResult = ''
        if len(lowerRes) == 2:
            lowerResult = ' and '.join(lowerRes)
        elif len(lowerRes) > 2:
            lowerRes = lowerRes[:-2] + [lowerRes[-2] + ", and " + lowerRes[-1]]
            lowerResult = ', '.join(lowerRes)
        elif len(lowerRes) == 1:
            lowerResult = lowerRes[0]

        upperResult = ''
        if len(upperRes) == 2:
            upperResult = ' AND '.join(lowerRes)
        elif len(upperRes) > 2:
            upperRes = upperRes[:-2] + [upperRes[-2] + ", AND " + upperRes[-1]]
            upperResult = ", ".join(upperRes)
        elif len(upperRes) == 1:
            upperResult = upperRes[0]

        print(upperResult)
        print(lowerResult)
        if len(upperResult) == 0:
            return "Hello, " + lowerResult + "."
        elif len(lowerResult) == 0:
            return "HELLO " + upperResult + "!"
        else:
            return "Hello, " + lowerResult + ". AND HELLO " + upperResult + "!"

if __name__ == "__main__":
    name = ""
    try:
        name = sys.argv[1]
    except IndexError:
        pass
    print(greet(name))
from collections import OrderedDict

def removeDupWithoutOrder(str):

    str = ''.join(str.split())
    str= "".join(set(str))
    #str= ''.join(sorted(str))

    return ''.join(sorted(str))


def listreverse(str):
    return str.split(' ')[::-1]


if __name__ == "__main__":
    str = 'monty pythons flying circus'
    print("With Order = ", removeDupWithoutOrder(str))
    print("Reverse List  = ", listreverse(str))
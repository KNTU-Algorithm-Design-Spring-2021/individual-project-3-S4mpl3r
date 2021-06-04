def readFile(dictionary, filename='./The_Oxford_3000.txt'):
    file = open(filename, 'r')
    text = file.readlines()
    for line in text:
        dictionary[line.strip().lower()] = line.strip().lower()
    file.close()


def wordIsInDictionary(word, dictionary):
    return word in dictionary


def findAllSolutions(string, dictionary):
    breakTheSentence(string.lower(), len(string), "", dictionary)


def breakTheSentence(string, n, result, dictionary):

    for i in range(1, n + 1):
        prefix = string[:i]
        if wordIsInDictionary(prefix, dictionary):
            if i == n:
                # Add this element to previous prefix
                result += prefix
                print(result)
                return

            breakTheSentence(string[i:], n - i,
                             result + prefix + " ", dictionary)


def main():
    dictionary = {}
    readFile(dictionary)

    findAllSolutions(
        "CALLSECURITYATMIAMIAIRPORTBECAUSEITHINKABOMBISABOUTTOGOOFF", dictionary)
    findAllSolutions("ABORTTHEPLANMEETATTHEDARKCABIN", dictionary)
    findAllSolutions("ILOVEYOUSOMUCH", dictionary)


if __name__ == "__main__":
    main()

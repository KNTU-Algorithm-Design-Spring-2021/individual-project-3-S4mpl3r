import random


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


def estimateComplexity(runs, sentence, dictionary):
    sum = 0
    for _ in range(runs):
        sum += estimate(sentence, dictionary)

    return sum / runs


def estimate(sentence, dictionary):
    v = sentence
    numnodes, m, mprod = 1, 1, 1
    while m != 0:
        t = len(v)
        mprod = mprod * m
        numnodes = numnodes + mprod*t
        promisings = []
        for i in range(1, len(v) + 1):
            prefix = v[:i]
            if wordIsInDictionary(prefix, dictionary) and i != len(v):
                promisings.append(i)

        m = len(promisings)
        if m != 0:
            v = v[promisings[int(random.random() *
                                 len(promisings))]:]

    return numnodes


def main():
    dictionary = {}
    readFile(dictionary)

    findAllSolutions(
        "CALLSECURITYATMIAMIAIRPORTBECAUSEITHINKABOMBISABOUTTOGOOFF", dictionary)
    findAllSolutions("ABORTTHEPLANMEETATTHEDARKCABIN", dictionary)
    findAllSolutions("ILOVEYOUSOMUCH", dictionary)
    # print(
    #     f'estimate: {estimateComplexity(10000, "CALLSECURITYATMIAMIAIRPORTBECAUSEITHINKABOMBISABOUTTOGOOFF".lower(), dictionary)}')


if __name__ == "__main__":
    main()

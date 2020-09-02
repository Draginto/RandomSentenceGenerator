from random import randint

def readFromFile(filename):
    wordList = []
    with open(filename, 'r') as wordfile:
        for word in wordfile:
            wordList.append(word.strip('\n'))  # Strip new line from words then append it to the list.
    return wordList


def generateWord(numberOfWords, setOfWords):
    count = 0
    joinDelimeter = ' '
    randomSentence = []
    while count < numberOfWords:
        getWordLoc = randint(0, 480001)  # the amount of words in list.
        word = setOfWords[getWordLoc]  # Get A random word from the list.
        randomSentence.append(word)  # Add the word to the sentence.
        count += 1
    print(joinDelimeter.join(randomSentence))  # Join the sequence of words together.


def main():
    print("Generate a random sentence!")
    getWords = readFromFile('words.txt')
    totalWords = int(input("How many words do you want to randomly generate?"))
    generateWord(totalWords, getWords)


if __name__ == '__main__':
    main()

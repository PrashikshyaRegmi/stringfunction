def word(string):
    inputWords=string.split(" ") ##spliting the words
    inputWords=inputWords[::-1] ##reversing the list word
    output=' '.join(inputWords) ##join words
    return output
if __name__=="__main__":
    string = 'I type the string here'
    print (word(string))

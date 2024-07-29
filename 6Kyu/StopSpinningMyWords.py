def spin_words(sentence):
    splits = sentence.split(" ")
    splitss = []
    for word in splits:
        if len(word) >= 5:
            reversed = word[::-1]
            splitss.append(reversed)
        else:
            splitss.append(word)
            
    return " ".join(splitss)

def words(words):
    words=[item for item in Word.split("-")]
    words.sort()
    return words
Word=input("Enter a hypen seperated word:")
print('-'.join(words(Word)))
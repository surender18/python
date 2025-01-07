# from PyDictionary import PyDictionary
# dictionary = PyDictionary()
# print(dictionary.meaning("hello"))

from textblob import Word
word = Word("improve")
print(word.definitions)  

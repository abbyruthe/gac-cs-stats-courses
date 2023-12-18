#string, string -> boolean
def same_length(encoded, word):
    """Takes two strings, and returns True if they are the same length, and False if they are not."""
    if len(encoded) == len(word):
        return True
    else:
        return False

# string, string => boolean
def space_location (encoded, word):
     location1 = ""
     for space1 in encoded:
          if space1 == " ":
               location1 += str(encoded.find(space1))
     location2 = ""
     for space2 in word:
          if space2 == " ":
               location2 += str(word.find(space2))
     if location1 == location2:
         return True
     else:
         return False

# string, string => boolean
def is_valid(encoded, word):
     """ take an encoded string and a decoded string, returns True if the two strings have the same number of letters, the length of words and the space in the two strings match up, if not return False"""
     new_encoded = ""
     new_word = ""
     if same_length(encoded, word) and space_location(encoded, word):
         for i in encoded:
             if not (i in new_encoded):
                 new_encoded += i
         for j in word:
             if not (j in new_word):
                 new_word += j
         if len(new_encoded) == len(new_word):
             return True
         else:
             return False
     else:
         return False
        
# string, string, string => void
def substitute(cipher_text, encoded, word):
    if not is_valid(encoded, word):
        return "Substitution is invalid"
    for j in range(len(word)):
        cipher_text = cipher_text.replace(encoded[j], word[j])
    return cipher_text

# string => void
def suggest_substitutions (ciphertext):
     """takes in a string of words, identifies 1, 2, and 3 letter word, and print suggestions"""
     word = []
     word += ciphertext.split()
     print ("One letter words:")
     for i in range (len(word)):
          if len(word[i]) ==1:
               print (word[i])
     print ("Suggestions for one letter words: a, i")
     print ("Two letter words:")
     for i in range (len(word)):
          if len(word[i]) ==2:
               print(word[i])
     print ("Suggestions for two letter words:  of, to, in, it, is, be, as, at, so, we, he, by, or, on, do, if, me, my, up, an, go, no, us, am")
     print ("Three letter words:")
     for i in range (len(word)):
          if len(word[i]) ==3:
               print (word[i])
     print ("Suggestions for three letter words: the, and, for, are, but, not, you, all, any, can, had, her, was, one, our, out, day, get, has, him, his, how, man, new, now, old, see, two, way, who, boy, did, its, let, put, say, she, too, use")



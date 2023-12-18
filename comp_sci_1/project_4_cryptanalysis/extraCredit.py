#string => void
def print_frequencies (ciphertext):
     """ takes the ciphertext, and prints the frequencies of each letter in the string"""
     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     for i in alphabet:
          returnValue = ciphertext.count(i)
          print (str(i) + ":" + str(returnValue))

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

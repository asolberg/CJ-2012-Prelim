# Problem
# 
# We have come up with the best possible language here at Google, called Googlerese. To
# translate text into Googlerese, we take any message and replace each English letter with
# another English letter. This mapping is one-to-one and onto, which means that the same
# input letter always gets replaced with the same output letter, and different input letters
# always get replaced with different output letters. A letter may be replaced by itself.
# Spaces are left as-is.
# 
# For example (and here is a hint!), our awesome translation algorithm includes the
# following three mappings: 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. This means that "a zoo"
# will become "y qee".
# 
# Googlerese is based on the best possible replacement mapping, and we will never change it.
# It will always be the same. In every test case. We will not tell you the rest of our
# mapping because that would make the problem too easy, but there are a few examples below
# that may help.
# 
# Given some text in Googlerese, can you translate it to back to normal text?


def translate(string):
    code_dict = {}
    translation = []
    strings_coded = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    strings_decoded = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]
    for i in range(len(strings_coded)):
        for j in range(len(strings_coded[i])):
            code_dict[strings_coded[i][j]] = strings_decoded[i][j]
    code_dict['z'] = 'q'
    code_dict['q'] = 'z'
    for letter in string:
#        print("trying letter: %s" % letter)
        translation.append(code_dict[letter])
    return "".join(translation)

filePrefix = 'A-small-attempt0'
fin = open(filePrefix + '.in', 'r')
fout = open(filePrefix + '.out', 'w')
T = int(fin.readline())
#print(code_dict)
for i in range(T):
    line = fin.readline().strip()
    fout.write("Case #%d: %s\n" % ((i+1), translate(line)))
#print(sorted(list(code_dict.values())))
# Given a list of words, find the longest word in the list made up of other
# words in the list.
#
# This is quadratic time (n^2), and seems necessary because we are essentially
# asked to compare each word against all other words, which requires checking n
# words for each of the n words (hence, n^2).

def LongestWord(arr):
    words = []
    for word in arr:
        for compare in arr:
            if word == compare or len(compare) > len(word):
                continue
            elif compare in word and word not in words:
                words.append(word)

    return max(words, key=len)

if __name__ == '__main__':
    arr = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']

    word = LongestWord(arr)

    print word


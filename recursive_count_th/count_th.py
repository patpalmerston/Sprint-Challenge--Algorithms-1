'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # if there length of word is less than one return a zero value
    if len(word) <= 1:
        return 0
    # every time the first two indexes equal th
    if word[0] + word[1] == 'th':
        # recursively remove the first two indexes and add 1 value every time a new list is returned
        return count_th(word[1:]) + 1
    else:
        # otherwise return the list
        return count_th(word[1:])

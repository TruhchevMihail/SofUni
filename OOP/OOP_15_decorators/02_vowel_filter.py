def vowel_filter(function):
    def wrapper():
        vowels = {'a', 'e', 'i', 'o', 'u'}
        letters = function()
        return [x for x in letters if x.lower() in vowels]
    return wrapper
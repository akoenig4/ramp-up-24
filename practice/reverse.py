def reverse(word:str):
    reversedWord = word[::-1]
    print(reversedWord)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowelCount = 0
    for letter in reversedWord:
        if letter in vowels:
            vowelCount += 1
    print('the number of vowels is ' + str(vowelCount))
    

reverse('AEIOUaeiouAEIOU and bingo was his name-o')
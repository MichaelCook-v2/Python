Print(input("Please enter a sentence:")
count = []
    for letter in word:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    return count
print(count)5rf
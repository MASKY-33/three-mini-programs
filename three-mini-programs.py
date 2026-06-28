### Input & Output


## First Program:
# - counts from (1 - 10)

## Second Program:
# - asks for a word and gives it back with the letters in reverse

## Third Program:
# - keeps asking for words until the user types "stop"
# - saves all words except "stop" after each other in a list
# - prints out the list of saved words


count = 0

for numbers in range(1, 11):
    count += 1
    print(numbers)




word = input("Give a word: ")

print(f"Word in reverse: {word[::-1]}")




words_list = []

while True:
    user_input = input("Give more words, or (type 'stop' to stop): ")

    if user_input.lower() == 'stop':
        break

    words_list.append(user_input)

print("Your saved words:", words_list)

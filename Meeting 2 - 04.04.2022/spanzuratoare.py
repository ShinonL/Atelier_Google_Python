word = 'alfabet'

# word = 'a _ _ a _ _ t'
hidden = []

for i in word:
    # print(word[0], word[-1])
    if word[0] != i and word[-1] != i:
        hidden.append('_')
    else: 
        hidden.append(i)

print(" ".join(hidden))

attempts = 1
tried_letters = set()
while attempts <= len(word):
    input_letter = input("Enter a letter: ")

    if input_letter == "" or len(input_letter) > 1:
        print("Please enter a single letter.")
        continue

    if input_letter in tried_letters:
        print("Letter already used.")
        continue
    
    if input_letter in word:
        for iterator, value in enumerate(word):
            if word[iterator] == input_letter:
                hidden[iterator] = input_letter
        print(" ".join(hidden))
    else:
        attempts += 1

    if '_' not in hidden:
        print("You won.")
        break
    elif attempts > len(word):
        print(f"You lost! The word was {word}")
    tried_letters.add(input_letter)

    # break
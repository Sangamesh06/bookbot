def count_words(f) :
 ans=f.split()
 return len(ans)



def count_letters(text):
    # Remove punctuation and whitespace
    text = ''.join(ch for ch in text if ch.isalpha())

    # Convert to lowercase
    text = text.lower()

    letter_counts = {}
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    return letter_counts
 

with open("./books/frankenstein.txt") as f:
 file_contents = f.read()
 file_contents.lower()

print("--- Begin report of books/frankenstein.txt ---")
print(f"{cwords(file_contents)} words found in the document")

# cletter(file_contents)
ans = count_letters(file_contents)
for char in ans:
    print(f"The {char} charecter was found {ans[char]} times ")


print("--End report--")


 


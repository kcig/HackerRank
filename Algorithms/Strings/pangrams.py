import string
text = raw_input().strip().lower()

is_pangram = 'pangram'
for letter in string.lowercase:
    if letter not in text:
        is_pangram = 'not pangram'
        break
        
print is_pangram
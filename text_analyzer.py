text = input("Enter the text: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count= 0
digit_count = 0
space_count = 0
special_character = 0

for i in text:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        space_count += 1
    else:
        special_character += 1

print("\n----Text Analysis----")
print(f"vowels            : {vowel_count}") 
print(f"consonants        : {consonant_count}") 
print(f"digit             : {digit_count}")
print(f"spaces            : {space_count}")
print(f"special_character : {special_character}")
              


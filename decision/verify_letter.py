letter = input('Give a letter')

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"];
consonants = [
    "B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z",
    "b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"
];

if(letter in vowels):
    print("Vowel")
elif(letter in consonants):
    print('Consonant')
else:
    print('Not letter')
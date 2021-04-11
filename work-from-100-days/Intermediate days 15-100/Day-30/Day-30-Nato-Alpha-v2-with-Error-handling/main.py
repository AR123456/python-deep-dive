import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    #put this line behind try block since this were someone may put in a number by mistake
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        # repeat the function call to generate phonetic to give user another try
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
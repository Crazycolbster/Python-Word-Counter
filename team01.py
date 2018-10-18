def prompt_for_name():
    print("Pride dection tool. Copyright 2018 Teamname LLC.\nThis work is licenced under the GNU General Public Licence")
    name = input("Input file name (Please):")
    print("Opening file... (or is it?)")
    return name

def open_file_count_word(name,word):
    pride_count = 0
    with open(name, "r") as file_in:
        for line in file_in:
            words = line.split()
            for i in words:
                if (i == word):
                    pride_count  = pride_count + 1
    return pride_count

def prompt_for_word():
    word = input("What word do you seek? ")
    return word
def display_word_count(word, word_count):
    print("There are ", word_count, " instances of the word '", word, "' in the document.", sep ='')

def main():
    name = prompt_for_name()
    word = prompt_for_word()
    word_count = open_file_count_word(name,word)
    display_word_count(word,word_count)#Ugh, now "Word" is starting to sound weird.
    
if __name__ == "__main__":
    main()
# python-word-counter
Python-Word-Counter

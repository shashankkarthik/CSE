
import string
from operator import itemgetter


def add_word( word_map, word ):
    '''
    Takes dictionary and word as input
    Check if word is not in dictionary.
    If not, adds word to dictionary
    Increases value of word in the dictionary by 1
    '''

    # Adds word in dictionary if word doesn't already exists
    if word not in word_map:
        word_map[ word ] = 0

    # Increases the count of the word by 1
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    '''
    Takes file and empty dictionary as input
    Creates list for each line containing each word in that line
    Removes punction from each word.
    Adds word to dictionary    
    '''

    for line in in_file:

        # Creates a list of words for each line
        word_list = line.split()

        for word in word_list:

            # Removes punctuation from the begining and ends of each word.
            word = word.strip(string.punctuation)
            word = word.lower()
            if len(word)>0:
                add_word( word_map, word )
        

def display_map( word_map ):
    '''
    Takes dictionary containing words and their counts as input
    Creates a list of tuples containing words and their counts
    Sorts the list of tuples by the frequency and then alphabetically
    Prints out the words and their counts in the right format.
    '''
    word_list = list()

    # Creates a list of tuples containing the word and it's count.
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # Sort by frequency and then sort alphabetically.
    freq_list = sorted( word_list, key=itemgetter(0) )
    freq_list = sorted( word_list, key=itemgetter(1),reverse = True )
    
    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    '''
    Tries to open file.
    If unable, prints appropriate message
    '''

    try:
        in_file = open( input("Enter file name: "), "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


def main():
    '''
    opens file
    builds dictionary containing words and their counts from file.
    prints words and counts ordered by frequency first and then alphabetically
    '''
    word_map = dict()
    in_file = open_file()

    if in_file != None:

        build_map( in_file, word_map )
        display_map( word_map )
        in_file.close()


main()

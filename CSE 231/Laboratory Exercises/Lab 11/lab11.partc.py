
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        #removes any white spaces and creates a list of words.
        word_lst = line.strip().split()

        #Creates a new list with punctuation removed and all words in lower case
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                #
                word_set.add( word )
                
    return word_set


#def compare_files( file1, file2 ):

    # Build two sets:
    #   all of the unique words in file1
    #   all of the unique words in file2

    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.

    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.

  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

#compare_files( f1, f2 )
x = build_word_set(f1)
print(x)
f1.close()
f2.close()


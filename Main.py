from Organizer import Organizer
from Scraping import Scraping
from Sorting import Sorting
from Statistical import statistical
from WordSearch import WordSearch
import sys  # sys.exit command to quit/logout of the application


# Menu system
def main_menu():
    clear()
    print("************Python Twitter Scraper v1.3**************")

    choice = input("""
1: Scrape live data
2: Analyze existing data
Q: Quit

Please enter your choice: """)

    if choice == "1":
        scrape_menu()
    elif choice == "2":
        analyze_menu()
    elif choice == "Q":
        sys.exit
    else:
        print("You must only select either 1,2 or Q.")
        print("Please try again")
        main_menu()


def scrape_menu():
    twitterhandle = input("\nEnter account to scrape: ")
    tweetamount = input("Enter amount of tweets: ")
    tweetamountInt = int(tweetamount)

    newscrape = Scraping(twitterhandle, tweetamountInt) # Object of the user name and amounts of tweets to be scraped
    newscrape.scrape_data() # Scarping object
    allpost = newscrape.get_posts() # Returns list of posts


    Organizer.create_project(twitterhandle)
    Organizer.write_file_json(allpost, twitterhandle)
    main_menu()


def analyze_menu():
    clear()
    postlist, path = Organizer.getpostList_Json()





    clear()
    print("************Analyze menu**************")

    choice = input("""
    1: Statistical operation
    2: Word correlations
    M: Back to main menu
    Q: Quit

    Please enter your choice: """)

    if choice == "1":
        statistical_menu(postlist, path)
    elif choice == "2":
        wordsearch_menu(postlist, path)
    elif choice == "M" or "m":
        main_menu()
    elif choice == "Q" or "q":
        sys.exit
    else:
        print("You must only select either 1,2, 3, M or Q.")
        print("Please try again")
        analyze_menu()


def wordsearch_menu(listofpost, path):


    clear()
    print("************Wordsearch menu**************")

    choice = input("""
        1: Search for specific word \n
        2: get the most common words\n
        3. Check if containing certain words make a post more or less popular\n  
        Q: Quit
        \n
        Please enter your choice: """)

    if choice == "1":
        word_searching(listofpost, path)
    if choice == "2":
        word_counting(listofpost, path)
    if choice == "3":
        word_correlate(listofpost, path)
    elif choice == "Q" or "q":
        sys.exit



def statistical_menu(listofpost, path):

    clear()
    print("************Statistical menu**************")

    choice = input("""
    1: Sort from high to low
    2: Get calculated average for all attributes
    Q: Quit

    Please enter your choice: """)

    if choice == "1":
        sort_highlow(listofpost, path)
    elif choice == "2":
        get_average(listofpost, path)
    elif choice == "Q" or "q":
        sys.exit
    else:
        print("You must only select either 1,2, 3, M or Q.")
        print("Please try again")
        statistical_menu()


def clear():
    print("\n" * 50)


def sort_highlow(listofpost, path):
    # Quick_sort returns a sorted list on attribute high
    attribute = ""
    choice = input("which attribute would you like to sort the list on?: \n "
                   "1. likes \n "
                   "2. replys \n"
                   " 3. retweets \n"
                   " 4. length of message")
    if choice == "1":
        attribute = 'likes'
    elif choice == '2':
        attribute = 'replys'
    elif choice == "3":
        attribute = "retweets"
    elif choice == "4":
        attribute = 'lenMessage'
    lenlist = len(listofpost)



    Sorting.quick_sort(listofpost, 0, lenlist, attribute)
    Organizer.overwrite_file(path,listofpost)

    print("sorting done. json-file overwritten with sorted dataset")


    for posts in listofpost:
        posts.print_all()

    end_operation(listofpost, path)

def word_searching(listofpost, path):

    searchword = input("\n which word would you like to search for?: ")
    occurences = WordSearch.search_word(listofpost, searchword)

    Organizer.analysis_file(occurences, "occurences of word: "+searchword, path)

    print("The word " + "'" + searchword + "'" + " appears " + str(occurences) + " times in the posts scraped \n")
    print("wordsearch data dumped to analysisfile")

    end_operation(listofpost, path)

def word_counting(listofpost, path):
    result = WordSearch.word_counter(listofpost)

    for r in result:
        Organizer.analysis_file(r[0], "There are " + str(r[1]) + " occurences of: ", path)
        print("there are " , str(r[1]) , "occurences of the word " , str(r[0]))

    print("this data has been dumped to json analysisfile")

def word_correlate(List, path):

    print("type a certain word that you would like to see correlated with a tweets totalt impact (likes+replys+ retweet)\n"
          "This function will compare the total impact the tweets containing this word has, compared to the 'regular' impact \n \n")
    choiceword = input("type here: ")

    difference = WordSearch.word_correlation(List, choiceword)
    if difference == None:
        print("\n that word is nowhere to be found in the posts that you are analysing")
        word_correlate(List, path)

    if difference>0:
        print("posts containing the word " , choiceword, " have generally ", str(difference), " more reactions")
        Organizer.analysis_file("posts with the word " + choiceword + " has following amount more reactions than average: ", difference, path)
    if difference<0:
        print("posts containing the word " , choiceword, " have generally ", str(difference), " fewer reactions")
        Organizer.analysis_file( difference, "posts with the word " + choiceword + " has following amount fewer reactions than average: ",path)






def get_average(listofpost, path):
    Average_likes = statistical.get_average(listofpost, 'likes')

    Organizer.analysis_file(Average_likes, 'average amount of likes', path)

    print("average aomount of likes: " + str(Average_likes))

    Average_replys = statistical.get_average(listofpost, 'replys')

    Organizer.analysis_file(Average_replys, 'average amount of replys', path)

    print("average amount of replys: " + str(Average_replys))

    Average_lenofmessage = statistical.get_average(listofpost, 'lenMessage')

    Organizer.analysis_file(Average_lenofmessage, 'average lengnth of messages', path)


    print("average lenght of messages: " + str(Average_lenofmessage))

    end_operation(listofpost, path)

def end_operation(listofpost, path):
    print("Want to return to statistical menu?")
    choice = input("""
      1. Yes
      2. No
      Please enter your choice: """)

    if choice == "1":
        statistical_menu(listofpost, path)
    elif choice == "2":
        sys.exit()

main_menu()


"""
Iterating through all attributes
and returning each
"""
#for u in allpost:
 #   u.print_all()


"""
Reversesort_replys is returning the sorted list reversed 
"""
#reversesort_replys = newscrape.bubble_sort_reverse('replys')

"""
Averagelikes returns the average of Eg. 'likes
"""
#averagelikes = statistical.get_average(sortedList_likes, 'likes')

"""
Medianlikes returns the the median of a sorted list
"""
#medianlikes = statistical.get_median(sortedList_likes, 'likes')

"""
Reply_frequence returns the frequency of chosen groupings
"""
#Reply_frequence = statistical.frequency_grouping(sortedList_likes, 'replys', 1000, 5000, 10000,20000, 50000)

"""
Deviation returns the deviation of a chosen attribute
"""
#deviation = statistical.standard_deviation(allpost, 'likes')

"""
WordSearch searches how many time a word appears in the scraped list
"""
#WordSearch.search_word(sortedList_likes, "Mexico")
#WordSearch.word_counter(sortedList_likes)
#WordSearch.word_counter2(sortedList_likes)

#listOfwords = WordSearch.word_correlation(sortedList_likes, 'likes', 'Citizenship')
#for searchWord in listOfwords:
    #searchWord.print_all()

"""
Creates a project directory and writes data to a Json file
"""
#Organizer.create_project(twitterhandle)
#Organizer.write_file_json(allpost, twitterhandle)
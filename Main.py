from Organizer import Organizer
from Scraping import Scraping
from Sorting import Sorting
from Statistical import statistical
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
    postlist, Name = Organizer.getpostList_Json()




    clear()
    print("************Analyze menu**************")

    choice = input("""
    1: Statistical operation
    2: Word correlations
    M: Back to main menu
    Q: Quit

    Please enter your choice: """)

    if choice == "1":
        statistical_menu(postlist)
    elif choice == "2":
        wordsearch_menu()
    elif choice == "M" or "m":
        main_menu()
    elif choice == "Q" or "q":
        sys.exit
    else:
        print("You must only select either 1,2, 3, M or Q.")
        print("Please try again")
        analyze_menu()


def wordsearch_menu():
    pass


def statistical_menu(listofpost):

    clear()
    print("************Statistical menu**************")

    choice = input("""
    1: Sort from high to low
    2: Sort from low to high
    3: Get calculated average for all attributes
    M: Back to main menu
    Q: Quit

    Please enter your choice: """)

    if choice == "1":

        sort_highlow(listofpost)

    elif choice == "2":
        sort_lowhigh()
    elif choice == "3":
        get_average(listofpost)
    elif choice == "M" or "m":
        main_menu()
    elif choice == "Q" or "q":
        sys.exit
    else:
        print("You must only select either 1,2, 3, M or Q.")
        print("Please try again")
        statistical_menu()


def clear():
    print("\n" * 50)


def sort_highlow(listofpost):
    # Quick_sort returns a sorted list on attribute high
    lenlist = len(listofpost)

    Sorting.quick_sort(listofpost, 0, lenlist, 'likes')


    for posts in listofpost:
        posts.print_all()

    print("Want to return to statistical menu?")
    choice = input("""
    1. Yes
    2. No
    Please enter your choice: """)

    if choice == "1":
        statistical_menu(listofpost)
    elif choice == "2":
        sys.exit()


def sort_lowhigh():
    pass


def get_average():
    Average_likes = statistical.get_average(postlist, 'likes')

    Organizer.analysis_file(Average_likes, 'likes', Name)

    print("average aomount of likes: " + str(Average_likes))

    Average_replys = statistical.get_average(postlist, 'replys')

    print("average amount of replys: " + str(Average_replys))

    Average_lenofmessage = statistical.get_average(postlist, 'lenMessage')

    print("average lenght of messages: " + str(Average_lenofmessage))


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
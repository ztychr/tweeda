from Organizer import Organizer
from Scraping import Scraping
from Post import tweet
from Sorting import Sorting
from Statistical import statistical
from WordSearch import WordSearch
from Probability import Probalility
import sys  # sys.exit command to quit/logout of the application


# Menu system
def main_menu():
    print(30 * '-')
    print("   M A I N - M E N U")
    print(30 * '-')

    print("""
1: Collect new data
2: Analyze existing data
Q: Quit """)

    print(30 * '-')
    choice = input('Enter your choice : ')

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
    twitterhandle = input("\nEnter account to collect data from: ")
    tweetamount = input("Enter amount of tweets: ")
    try:
        tweetamountInt = int(tweetamount)
    except:
        print("you have to provide a number as amount, and not letters. try again")
        scrape_menu()

    newscrape = Scraping(twitterhandle, tweetamountInt) # Object of the user name and amounts of tweets to be scraped
    newscrape.scrape_data() # Scarping object



    allpost = newscrape.get_posts() # Returns list of posts
    if newscrape.r.status_code == 200:

        Organizer.create_project(twitterhandle)
        Organizer.write_file_json(allpost, twitterhandle)
        main_menu()


    else:
        print("The data can not be saved. Are you sure that you provided valid input?")
        scrape_menu()




def analyze_menu():
    postlist, path = Organizer.getpostList_Json()

    print(30 * '-')
    print("   A N A L Y Z E - M E N U")
    print(30 * '-')

    print("""
1: Go to Statistical and sorting menu
2: Go to Word searching menu
M: Back to main menu
Q: Quit """)

    print(30 * '-')
    choice = input('Enter your choice : ')

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

    print(30 * '-')
    print("   S E A R C H  - M E N U")
    print(30 * '-')

    print("""
1: Search for specific word 
2: Get the most common words
3. Check if containing certain words make a post more or less popular
4. Check the probability of a post containing a certain word
Q: Quit """)

    print(30 * '-')
    choice = input('Enter your choice : ')

    if choice == "1":
        word_searching(listofpost, path)
    if choice == "2":
        word_counting(listofpost, path)
    if choice == "3":
        word_correlate(listofpost, path)
    if choice == "4":
        word_prob(listofpost, path)
    elif choice == "Q" or "q":
        sys.exit


def statistical_menu(listofpost, path):
    print(30 * '-')
    print("   S T A T I S T I C S  - M E N U")
    print(30 * '-')

    print("""
1: Sort from high to low, and get median
2: Get calculated average for all attributes
3: Get Standard deviation
4. Get frequency groupings
Q: Quit """)

    print(30 * '-')
    choice = input('Enter your choice : ')

    if choice == "1":
        sort_highlow(listofpost, path)
    elif choice == "2":
        get_average(listofpost, path)
    elif choice == "3":
        get_standarddev(listofpost, path)
    elif choice == "4":
        freq_grouping(listofpost, path)
    elif choice == "Q" or "q":
        sys.exit
    else:
        print("You must only select either 1,2, 3, M or Q.")
        print("Please try again")
        statistical_menu(listofpost, path)


def clear():
    print("\n" * 50)


def sort_highlow(listofpost, path):
    # Quick_sort returns a sorted list on attribute high
    attribute = ""
    print(30 * '-')
    print("   S O R T I N G - M E N U")
    print(30 * '-')

    print("""Which attribute would you like to sort the list on?:
1. likes
2. replys
3. retweets
4. length of message
5. Total reactions""")

    print(30 * '-')
    choice = input('Enter your choice : ')
    if choice == "1":
        attribute = 'likes'
    elif choice == '2':
        attribute = 'replys'
    elif choice == "3":
        attribute = "retweets"
    elif choice == "4":
        attribute = 'lenMessage'
    elif choice == '5':
        attribute = 'reactions'
    lenlist = len(listofpost)

    # tweet.print_tweetlist(listofpost) just sorts in the JSON file

    Sorting.quick_sort(listofpost, 0, lenlist-1, attribute)
    Organizer.overwrite_file(path,listofpost)
    print(30 * '-')
    print("Sorting done. json-file overwritten with sorted dataset")
    print(30 * '-')
    print("Would you also like to get the median calculated on same " + attribute + "?"
                    "\n  1. Yes, calculate it and save in Json-analysisfile \n  2. no")

    print(30 * '-')
    medianpos = input('Enter your choice : ')

    if medianpos == "1":
        medianvalue = statistical.get_median(listofpost, attribute)
        print("the median value of the attribute " + attribute + " is " + str(medianvalue))
        Organizer.analysis_file(medianvalue, "the median of " + attribute + " is: ", path)

    end_operation(listofpost, path)


def word_prob(listofposts, path):
    searchword = input("\n which word would you like to get probalilities of occurence for?: ")
    prob = Probalility.prob_of_word(listofposts, searchword)
    print("The probability of the word: " + str(searchword) + " being in this users posts, is " + str(prob) + "% ")
    Organizer.analysis_file(str(prob) + "%", "The probability of the word " + str(searchword) + " being in this users posts, is this", path)
    end_operation(listofposts, path)


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
    end_operation(listofpost, path)


def word_correlate(List, path):

    print("type a certain word that you would like to see correlated with a tweets totalt impact (likes+replys+ retweet)\n"
          "This function will compare the total impact the tweets containing this word has, compared to the 'regular' impact \n \n")
    choiceword = input("type here: ")

    difference = WordSearch.word_correlation(List, choiceword)
    if difference == 0 or None:
        print("\n that word is nowhere to be found in the posts that you are analysing")
        word_correlate(List, path)

    if difference>0:
        print("posts containing the word " , choiceword, " have generally ", str(difference), " more reactions")
        Organizer.analysis_file("posts with the word " + choiceword + " has following amount more reactions than average: ", difference, path)

    if difference<0:
        print("posts containing the word " , choiceword, " have generally ", str(difference), " fewer reactions")
        Organizer.analysis_file( difference, "posts with the word " + choiceword + " has following amount fewer reactions than average: ",path)

    end_operation(list, path)


def get_standarddev(listofposts, path):
    print(30 * '-')
    print("""which attribute would you like to get the standard deviation of?:
1. likes
2. replys
3. retweets
4. length of message
5. Total reactions """)
    print(30 * '-')
    choice = input("Enter your choice : ")

    if choice == "1":
        attribute = 'likes'
    elif choice == '2':
        attribute = 'replys'
    elif choice == "3":
        attribute = "retweets"
    elif choice == "4":
        attribute = 'lenMessage'
    elif choice == "5":
        attribute = 'reactions'

    standard_dev = statistical.standard_deviation(listofposts, attribute)
    standard_dev_round = int(standard_dev)
    print(30 * '-')
    print("Standard deviation is:" +  str(standard_dev_round))

    Organizer.analysis_file(standard_dev_round, "standard deviation of "+ attribute +":", path)

    end_operation(listofposts, path)


def freq_grouping(listofpost, path):

    attribute = ""
    print(30 * '-')
    print("""Which attribute would you like to get the standard deviation of?:
1. likes
2. replys
3. retweets
4. length of message
5. Total reactions """)
    print(30 * '-')
    choice = input("Enter your choice : ")

    if choice == "1":
        attribute = 'likes'
    elif choice == '2':
        attribute = 'replys'
    elif choice == "3":
        attribute = "retweets"
    elif choice == "4":
        attribute = 'lenMessage'
    elif choice == "5":
        attribute = 'reactions'
    print(30 * '-')
    print("How would you like to group the data? \n"
                      "1. 5, 10, 20, 30, 40 \n"
                      "2. 50, 100, 150 \n"
                      "3. 100, 300, 500, 700, 1000 \n"
                      "4. 500, 1000, 3000, 5000, 8000 \n"
                      "5. 1500, 5000, 10000, 15.000, 20.000 \n")

    print(30 * '-')
    groupings = input("Enter your choice : ")
    if groupings == "1":
        one = 5
        two = 10
        three = 20
        four = 30
        five = 40
    if groupings == "2":
        one = 50
        two = 100
        three = 150
        four = 300
        five = 500
    if groupings == "3":
        one = 100
        two = 300
        three = 500
        four = 700
        five = 1000
    if groupings == "4":
        one = 500
        two = 10000
        three = 3000
        four = 5000
        five = 8000
    if groupings == "5":
        one = 1500
        two = 5000
        three = 10000
        four = 15000
        five = 20000

    freqs = statistical.frequency_grouping(listofpost, attribute, one, two, three, four, five)
    print(30 * '-')
    print("Size of list:" + str(len(listofpost)))
    print(30 * '-')

    print(str(freqs[0]) + " posts with " + attribute + " below " + str(one))
    print(str(freqs[1]) + " posts with " + attribute + " between " + str(one) + " and " + str(two))
    print(str(freqs[2]) + " posts with " + attribute + " between " + str(two) + " and " + str(three))
    print(str(freqs[3]) + " posts with " + attribute + " between " + str(three) + " and " + str(four))
    print(str(freqs[4]) + " posts with " + attribute + " between " + str(four) + " and " + str(five))
    print(str(freqs[5]) + " posts with " + attribute + " above " + str(five))

    Organizer.analysis_file(freqs[0], " amount of " + attribute + " below "+ str(one), path)
    Organizer.analysis_file(freqs[1], " amount of " + attribute + " between " + str(one) + " and " + str(two), path)
    Organizer.analysis_file(freqs[2], " amount of " + attribute + " between " + str(two) + " and " + str(three), path)
    Organizer.analysis_file(freqs[3], " amount of " + attribute + " between " + str(three) + " and " + str(four), path)
    Organizer.analysis_file(freqs[4], " amount of " + attribute + " between " + str(four) + " and " + str(five), path)
    Organizer.analysis_file(freqs[5], " amount of " + attribute + " above " + str(five), path)
    print(30 * '-')
    print("Would you also like get these groupings shown as percentages? \n 1. Yes \n 2. No")
    print(30 * '-')
    prob_choice = input("Enter your choice : ")
    if prob_choice == "1":
        freq_grouping_prob(listofpost, attribute, one, two, three, four, five, path)

    end_operation(listofpost, path)

def freq_grouping_prob(listofpost, attribute, one, two, three, four, five, path):

    freqs = Probalility.prob_of_groupings(listofpost, attribute, one, two, three, four, five)

    print("The percentage of the posts with "+attribute+ " below " + str(one) +" is "  + str(freqs[0]) + "%")
    print("The percentage of the posts with "+attribute+ " between " + str(one) +" and " + str(two) + " is " + str(freqs[1]) + "%")
    print("The percentage of the posts with " +attribute+" between " + str(two) +" and " + str(three) + " is " + str(freqs[2]) + "%")
    print("The percentage of the posts with "+attribute+ " between " + str(three)+ " and " + str(four) + " is " + str(freqs[3])  + "%")
    print("The percentage of the posts with "+attribute+ " between  " + str(four) +" and " + str(five)  + " is "  + str(freqs[4])  + "%")
    print("The percentage of the posts with "+attribute+  " over " + str(five) + " is "  + str(freqs[5]) + "%")

    Organizer.analysis_file(freqs[0], "The percentage of posts with " + attribute + " below " + str(one) + " is: ", path)
    Organizer.analysis_file(freqs[1], "The percentage of posts with " + attribute + " between " + str(one)+ "and" + str(two) + " is: ", path)
    Organizer.analysis_file(freqs[2], "The percentage of posts with " + attribute + " between " + str(two)+ "and" + str(three) + " is: ", path)
    Organizer.analysis_file(freqs[3], "The percentage of posts with " + attribute + " between " + str(three)+ "and" + str(four) + " is: ", path)
    Organizer.analysis_file(freqs[4], "The percentage of posts with " + attribute + " between " + str(four)+ "and" + str(five) + " is: ", path)
    Organizer.analysis_file(freqs[5], "The percentage of posts with " + attribute + " above " + str(five)+ "is ", path)


def get_average(listofpost, path):
    Average_likes = statistical.get_average(listofpost, 'likes' )

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
    print(30 * '-')
    print("Want to return to main menu?")
    print(30 * '-')
    print("""
1. Yes
2. No
3. Go to statistical menu
4. Go to wordsearch menu """)
    print(30 * '-')
    choice = input('Enter your choice : ')

    if choice == "1":
        main_menu()
    if choice == "2":
        sys.exit()
    if  choice == "3":
        statistical_menu(listofpost, path)
    if choice == "4":
        wordsearch_menu(listofpost, path)
    else:
        print("please enter one of the options \n")
        end_operation(listofpost, path)


main_menu()

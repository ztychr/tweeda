import os
import sys
import json
from Scraping import Scraping
import time
import datetime

# realdonaldtrump

def attributes_to_list(tweet):
    a0 = getattr(tweet, "userName")
    a1 = getattr(tweet, "likes")
    a2 = getattr(tweet, "replys")
    a3 = getattr(tweet, "retweets")
    a4 = getattr(tweet, "message")
    a5 = getattr(tweet, "ID")

    return a0, a1, a2, a3, a4, a5

class Organizer:

    @classmethod
    def create_project(self, twitterhandle):

        path = os.getcwd() + "/" + twitterhandle

        try:
            os.makedirs(path)
            print("new directory created. path:" + str(path))
        except OSError:
            print ("Directory %s was not created. \nDirectory probably exists. \n" % path)
        else:
            print ("Directory %s created. \n" % path)

        #if not os.path.exists(path):
            #os.makedirs(path)

    @classmethod
    def write_file_json(self, listofposts, twitterhandle):

        #C:\Users\Ejer\PycharmProjects\empty4git\tweeda\realdonaldtrump
        if os.path.isfile("realdonaldtrump.json"):
            print("file found")

        specpath = os.getcwd() + "\\" + twitterhandle + "\\" + twitterhandle + ".json"

        path = os.getcwd() + "\\" + twitterhandle
        templist = []


        if not os.path.isfile(specpath):
            print("making and writing file")

            outfile = os.path.join(path,  twitterhandle+".json")
            f = open(outfile, 'w')

            for item in listofposts:

                all_attr = attributes_to_list(item)
                dict = {
                'username': all_attr[0],
                'likes': all_attr[1],
                'replys': all_attr[2],
                'retweets': all_attr[3],
                'message': all_attr[4],
                'ID': all_attr[5]
                }

                templist.append(dict)

            json.dump(templist, f)
            f.close()

            print("Data dumped to " + twitterhandle + ".json \n")

        else:
            print("File called " + twitterhandle + ".json already exists. \n"
                                                   "appending new data to file")
            outfile = os.path.join(path, twitterhandle + ".json")


            with open(outfile) as f:
                listofdict = json.load(f)

            for item in listofposts:

                appendthis = True

                all_attr = attributes_to_list(item)
                dict = {
                    'username': all_attr[0],
                    'likes': all_attr[1],
                    'replys': all_attr[2],
                    'retweets': all_attr[3],
                    'message': all_attr[4],
                    'ID': all_attr[5]
                }
                for d in listofdict:
                    if d['ID'] == dict['ID']:
                        appendthis = False
                if appendthis == True:
                    listofdict.append(dict)

            with open(outfile, 'w') as f:
                json.dump(listofdict, f)












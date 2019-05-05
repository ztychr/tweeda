import json
import os
import Post

"""
The Organizer class creates a local directory
    and dumps data to a JSON file
"""

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
 #C:\Users\Ejer\PycharmProjects\empty4git\tweeda\Jsondata_files
        path = os.getcwd() + "/" +"Jsondata_files" + "/"+ twitterhandle

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


        specpath = os.getcwd() + "/" +"Jsondata_files" + "/"+ twitterhandle + "/" + twitterhandle + ".json"

        path = os.getcwd() + "/" +"Jsondata_files" + "/"+  twitterhandle
        templist = []

        print("specpath")
        print(specpath)
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

    @classmethod

    def getpostList_Json(self):

        print("\n you have the following Jsonfiles of data stored: \n")
        Jsonpath = os.getcwd() + "/" + "Jsondata_files"

        files = os.listdir(Jsonpath)
        print("which of these stored accounts would you like to run analysis on? \n")
        for index, file in enumerate(files):
            print(index, ".", file)

        choiceindx = input("\n pick the number of the file tht you would like to choose: ")

        choiceindxInt = int(choiceindx)

        choice = files[choiceindxInt]

        choicepath = Jsonpath + "/" + choice + "/" + choice + ".json"
        with open(choicepath, 'r') as f:
            datastore = json.load(f)

        postList = []

        for i in datastore:
            userName = i["username"]
            likes = i["likes"]
            replys = i["replys"]
            retweets = i["retweets"]
            message = i["message"]
            ID = i["ID"]
            temppost = Post.tweet(userName, likes, replys, retweets, message, ID)

            postList.append(temppost)

        return postList









import json
import os
import Post
from  Datastruct import AVL

"""
The Organizer class creates a local directory
    and dumps data to a JSON file
"""


class Organizer:

    @classmethod
    def attributes_to_list(cls, tweet):
        a0 = getattr(tweet, "userName")
        a1 = getattr(tweet, "likes")
        a2 = getattr(tweet, "replys")
        a3 = getattr(tweet, "retweets")
        a4 = getattr(tweet, "message")
        a5 = getattr(tweet, "ID")

        return a0, a1, a2, a3, a4, a5


    @classmethod
    def create_project(self, twitterhandle):
        path = os.getcwd() + "/" +"Jsondata_files" + "/"+ twitterhandle

        try:
            os.makedirs(path)
            print("new directory created. path:" + str(path))
        except OSError:
            print ("Directory %s was not created. \nDirectory probably exists. \n" % path)
        else:
            print ("Directory %s created. \n" % path)


    @classmethod
    def write_file_json(self, listofposts, twitterhandle):

        path = os.getcwd() + "/" +"Jsondata_files" + "/"+  twitterhandle

        specpath = os.getcwd() + "/" +"Jsondata_files" + "/"+ twitterhandle + "/" + twitterhandle + ".json"

        templist = []

        if not os.path.isfile(specpath):
            print("making and writing file")

            outfile = os.path.join(path,  twitterhandle+".json")
            f = open(outfile, 'w')

            for item in listofposts:

                all_attr = self.attributes_to_list(item)
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

            IDtree = AVL.AVLTree()
            IDtree.constructfromList(listofdict)

            for item in listofposts:

                appendthis = True

                all_attr = self.attributes_to_list(item)
                dict = {
                    'username': all_attr[0],
                    'likes': all_attr[1],
                    'replys': all_attr[2],
                    'retweets': all_attr[3],
                    'message': all_attr[4],
                    'ID': all_attr[5]
                }
                # if tree.search == TRUe:
                # BOOL = FALSE
                if IDtree.search(dict['ID']):
                    appendthis = False
                if appendthis == True:
                    listofdict.append(dict)

            with open(outfile, 'w') as f:
                json.dump(listofdict, f)

    @classmethod
    def getpostList_Json(self):
        print(30 * '-')
        print("   D A T A - S T O R E D")
        print(30 * '-')
        Jsonpath = os.getcwd() + "/" + "Jsondata_files"

        files = os.listdir(Jsonpath)
        for index, file in enumerate(files):
            print(index, ".", file)
        print(30 * '-')
        choiceindx = input("Enter your choice : ")

        choiceindxInt = int(choiceindx)

        choice = files[choiceindxInt]

        folder_path = Jsonpath + "/" + choice
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

        return postList, folder_path

    @classmethod
    def overwrite_file(self, path, list):
        filename = ""
        newdata = []

        files = os.listdir(path)
        for file in files:
            if file != "analysis.json":
                filename = file
        speecpath = path + "/"+ filename

        for item in list:
            all_attr = self.attributes_to_list(item)
            dict = {
                'username': all_attr[0],
                'likes': all_attr[1],
                'replys': all_attr[2],
                'retweets': all_attr[3],
                'message': all_attr[4],
                'ID': all_attr[5]
            }

            newdata.append(dict)

        with open(speecpath, "w") as f:
            json.dump(newdata, f)

    @classmethod
    def analysis_file(self, data, datatype, path):
        analysisdict = {}
        newpath = path + "/" + "analysis.json"


        if not os.path.isfile(newpath):
            with open(newpath, 'w') as outfile:
                analysisdict["anlaysed data for the file:"] = path
                analysisdict[datatype] = data
                json.dump(analysisdict, outfile)

        else:
            with open(newpath) as f:
                listofdict = json.load(f)

            with open(newpath, 'w') as f:
                listofdict[datatype] = data
                json.dump(listofdict, f)














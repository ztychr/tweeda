import os
import sys
import json
from Scraping import Scraping

class Organizer:

    @classmethod
    def create_project(self, twitterhandle):

        path = os.getcwd() + "/" + twitterhandle

        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed. Directory probably exists." % path)
        else:
            print ("Successfully created the directory %s " % path)

        #if not os.path.exists(path):
            #os.makedirs(path)

    @classmethod
    def write_file_json(self, twitterhandle):

        path = os.getcwd() + "/" + twitterhandle

        json_data = ['cat: grey', 'dog: brown', 'frog: green', 'mouse: white']
        #json_data = Scraping.get_posts()

        if not os.path.isfile(twitterhandle):

            outfile = os.path.join(path, twitterhandle+".json")
            f = open(outfile, 'w')
            json.dump(json_data, f)
            f.close()

        else:
            print("File called " + twitterhandle + ".json already exists.")

        #with open(path, twitterhandle + '.json', 'w') as f:
        #    json.dump(json_data, f)
        #    f.close()

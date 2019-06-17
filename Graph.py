import matplotlib.pyplot as plt
import pandas as pd
import os


def line_diagram(path):

    files = os.listdir(path)
    for i in files:
        if i == 'analysis.json':
            files.remove(i)

    str1 = ''.join(files)
    final = str(path + '/' + str1)

    user = final
    d = pd.read_json(user)
    likes = d['likes']
    plt.plot(likes)

    # Defining axes
    plt.xlabel("Posts")
    plt.ylabel("Likes")
    plt.title(str1)
    plt.show()

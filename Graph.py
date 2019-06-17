import matplotlib.pyplot as plt
import pandas as pd
import os


def line_diagram(path, attr):

    files = os.listdir(path)
    for i in files:
        if i == 'analysis.json':
            files.remove(i)

    str1 = ''.join(files)
    final = str(path + '/' + str1)

    user = final
    d = pd.read_json(user)
    attr = d[attr]
    plt.plot(attr)

    # Defining axes
    plt.xlabel("Posts")
    plt.ylabel("Attributes")
    plt.title(str1)
    plt.show()

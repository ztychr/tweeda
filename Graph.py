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
    attr_name = str(attr)
    attr = d[attr]
    plt.plot(attr)
    y_attr_name = ''.join([i for i in attr_name if not i.isdigit()])

    # Defining axes
    plt.xlabel("Posts")
    plt.ylabel(y_attr_name)
    plt.title(str1)
    plt.show()

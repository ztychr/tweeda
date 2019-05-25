import math
import statistics

"""
The statistical class sorts data upon different statistical parameters
"""

class statistical:

    """
    method for getting an average of a certain attribute
    @:param list. A list of tweet objects
    @:param attrs. The attribute that the method will calculate the average of
    @:returns The average value of the attribute in the list
    """
    @classmethod
    def get_average(self, list, attrs):
        sum = 0
        amount = len(list)
        for i in range(0, amount):
            attribute = getattr(list[i], attrs)
            sum = sum + attribute

        average = sum / amount

        averageround = int(average)

        return averageround
    """
    Getting the median of a list. Only works on sorted lists
    Used in both Quicksort and bubblesort
    @:param list. list of tweet-objects
    @:param attrs. attribute that is wanted a median on
    """

    @classmethod
    def get_median(self, list, attrs):
        # only works for lists that are sorted on the specific attribute that you want to get the median of
        median = 0
        lenght = len(list)

        half = lenght / 2

        if lenght == 2:
            median = list[0]

        elif lenght % 2 == 0:
            middle = int(half)
            middle1 = int(half + 1)
            print("middle1:" + str(middle1))
            attribute = getattr(list[middle], attrs)
            attribute1 = getattr(list[middle1], attrs)
            print("length= " + str(lenght))
            median = (attribute + attribute1) / 2

        if lenght % 2 != 0:
            halfIndex = int(half)
            attribute = getattr(list[halfIndex], attrs)
            median = attribute

        return median
    """
    method for getting amounts of different occurences of certain attributes
    @:param List. list of tweets
    @:param attrs. Attribute that is up for calculation
    @:param grouping1. The first groupof data
    @:param grouping2. The second group of data
    @:param grouping3. The third group of data
    @:param grouping4. The fourth group of data (overloaded, method can work without this one)
    @:param grouping5. The fifth group of data (overloaded, method can work without this one)
    @:returns 1. amounts of attribute below grouping1. 2. amounts of attributes over grouping1 and below grpuping2
    3. amounts of attributes over grouping2 and below grpuping3 4. amounts of attribute over grouping3 and below grpuping4
    5. amounts of attribute over grouping4 and below grpuping5 6. amounts of attribute over grouping 5

    """
    @classmethod
    def frequency_grouping(self, list, attrs, grouping1, grouping2, grouping3, grouping4=None, grouping5=None):
        # returns frequency of different groupings.
        # attrs is  chosen attribute
        # it is required to use at least 4 grouping, but grouping 4 and 5 are overloaded, and can discarded
        try:
            if (attrs != 'message' or attrs != 'userName'):
                frequency1 = 0
                frequency2 = 0
                frequency3 = 0
                lastgrouping = grouping3
                ceiling_break = 0

                if grouping4 != None:
                    frequency4 = 0
                    lastgrouping = grouping4
                if grouping5 != None:
                    frequency5 = 0
                    lastgrouping = grouping5

                for item in list:
                    attribute = getattr(item, attrs)

                    if attribute > 0 and attribute < grouping1:
                        frequency1 = frequency1 + 1
                    if attribute > grouping1 and attribute < grouping2:
                        frequency2 = frequency2 + 1
                    if attribute > grouping2 and attribute < grouping3:

                        frequency3 = frequency3 + 1

                    if grouping4 != None:
                        if attribute > grouping3 and attribute < grouping4:
                            frequency4 = frequency4 + 1
                            lastgrouping = grouping5

                    if grouping5 != None:
                        if attribute > grouping4 and attribute < grouping5:
                            lastgrouping = grouping5
                            frequency5 = frequency5 + 1

                    if (attribute > lastgrouping):
                        ceiling_break = ceiling_break + 1
                if grouping4 is None and grouping5 is None:
                    return frequency1, frequency2, frequency3, ceiling_break
                if grouping4 is not None and grouping5 is None:
                    return frequency1, frequency2, frequency3, frequency4, ceiling_break
                if grouping4 is not None and grouping5 is not None:
                    return frequency1, frequency2, frequency3, frequency4, frequency5, ceiling_break

            else:
                return print("you cant sort on message or username \n those are strings")
        except:
            return print("the attribute you typed is not available for posts \n maybe you typed wrong?")
    """

    @:param list. A list of tweet objects
    @:param attrs. The attribute that the method will calculate the average of
    @:returns The standard deviation of the attribute in the list
    """

    @classmethod
    def standard_deviation(self, List, attrs):
        # getting standard deviation of the dataset, uses get_average() from above.
        # standard deviation can later be used to provide further analysis
        listLen = len(List)
        # calc of mean
        # skal udskiftes med getAverage()
        average = self.get_average(List, attrs) # getting differences between data points and calculated average
        differences = []
        for i in range(0, listLen):
            attribute = getattr(List[i], attrs)
            diff = attribute - average
            differences.append(diff)

        Squaring = [] # squaring differences
        for i in range(0, listLen):
            square = differences[i] * differences[i]
            Squaring.append(square)

        sumofSquared = sum(Squaring)

        AverageSquare = sumofSquared/listLen
        deviation = math.sqrt(AverageSquare)
        rdeviation = round(deviation, 2)
        return rdeviation  # return deviation
        # get square root of squaredMean = standard_deviation

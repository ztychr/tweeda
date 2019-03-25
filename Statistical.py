import math
import statistics


class statistical:
    @classmethod
    # getting calculated average/mean, takes the list you want to get the average of as parameter
    # also takes the attribute 'attrs' as an argument, this is the attribute that you want to get the average of

    def get_average(self, list, attrs):  # only give list as parameter
        sum = 0
        amount = len(list)
        for i in range(0, amount):
            attribute = getattr(list[i], attrs)
            sum = sum + attribute

        average = sum / amount

        return average

    @classmethod
    # only works for lists that are sorted on the specific attribute that you want to get the median of

    def get_median(self, list, attrs):
        median = 0
        lenght = len(list)
        half = lenght / 2
        if lenght % 2 == 0:
            middle = int(half)
            print("middle" + str(middle))
            middle1 = int(half + 1)
            print("middle1" + str(middle1))
            attribute = getattr(list[middle], attrs)
            attribute1 = getattr(list[middle1], attrs)
            median = (attribute + attribute1) / 2

        if lenght % 2 != 0:
            halfIndex = int(half)
            attribute = getattr(list[halfIndex], attrs)
            median = attribute

        return median

    @classmethod
    # returns frequency of different groupings.
    # attrs is  chosen attribute
    # it is required to use at least 4 grouping, but grouping 4 and 5 are overloaded, and can discarded
    def frequency_grouping(self, list, attrs, grouping1, grouping2, grouping3, grouping4=None, grouping5=None):
        try:
            if (attrs != 'message' or attrs != 'userName'):
                frequency1 = 0
                frequency2 = 0
                frequency3 = 0
                lastgrouping = 0
                ceiling_break = 0
                if grouping4 != None:
                    frequency4 = 0
                if grouping5 != None:
                    frequency5 = 0
                for item in list:
                    attribute = getattr(item, attrs)

                    if attribute > 0 and attribute < grouping1:
                        frequency1 = frequency1 + 1
                    if attribute > grouping1 and attribute < grouping2:
                        frequency2 = frequency2 + 1
                    if attribute > grouping2 and attribute < grouping3:
                        lastgrouping = grouping5
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

                print("there are: " + str(frequency1) + " occurences of " + attrs + " below: " + str(grouping1))
                print("there are: " + str(frequency2) + " occurences of " + attrs + " below: " + str(grouping2))
                print("there are: " + str(frequency3) + " occurences of " + attrs + " below: " + str(grouping3))
                if (grouping4 != None):
                    print("there are: " + str(frequency4) + " occurences of " + attrs + " below: " + str(grouping4))

                if (grouping5 != None):
                    print("there are: " + str(frequency5) + " occurences of " + attrs + "below" + str(grouping5))

                print("there are: " + str(ceiling_break) + " ocurrences of " + attrs + " above your highest grouping")

                return grouping1, grouping2, grouping3, grouping4, grouping5
            else:
                return print("you cant sort on message or username \n those are strings")
        except:
            return print("the attribute you typed is not available for posts \n maybe you typed wrong?")

    @classmethod
    # getting standard deviation of the dataset, uses get_average() from above.
    # standard deviation can later be used to provide further analysis
    def standard_deviation(self, List, attrs):

        # average = self.get_average(List, 'likes')
        listLen = len(List)




        # calc of mean
        # skal udskiftes med getAverage()
        average = self.get_average(List, attrs)

        print("devagerage" + str(average))


        # getting differences between datapoints and calculated average
        #working
        differences = []
        for i in range(0, listLen):
            attribute = getattr(List[i], attrs)
            diff = attribute - average
            differences.append(diff)

        # squaring differences
        Squaring = []

        for i in range(0, listLen):
            square = differences[i] * differences[i]
            Squaring.append(square)

        sumofSquared = sum(Squaring)

        AverageSquare = sumofSquared/listLen
        print(AverageSquare)


        deviation = math.sqrt(AverageSquare)

        print("deviation: " + str(deviation))

        return deviation


        #  return deviation

        # get square root of squaredMean = standard_deviation

    # using an already defined standard deviationmeasurement
    # for testing my own method
    @classmethod

    def native_sd(self, List, attrs):

        tempList = []
        lenList = len(List)
        for i in range(0,lenList):
            attribute = getattr(List[i], attrs)
            tempList.append(attribute)



        stdev = statistics.pstdev(tempList)
        print("standard dev:" + str(stdev))

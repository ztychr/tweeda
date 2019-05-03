from Statistical import statistical

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


class Sorting:
    # bubblesort algorthm that sorts low-high. The attribute that you would like to sort is passed as parameter
    # takes list of posts as parameter

    @staticmethod
    def bubble_sort(List, attrs):
        bubbleruns = 0
        try:
            if attrs != 'message' and attrs != 'userName':
                for i in range(0, len(List) - 1):

                    for j in range(0, len(List) - 1 - i, 1):
                        attribute = getattr(List[j], attrs)
                        attribute1 = getattr(List[j + 1], attrs)

                        if attribute > attribute1:
                            swap(List, j, j + 1)
                return List
            else:
                return print("you cant sort on message or username \n those are strings")
        except:
            return print("the attribute you typed is not available for posts \n maybe you typed wrong?")

    # bubblesort algorithm that sorts high-low. the attribute that you would like to sort on is passed as parameter

    @staticmethod
    def bubble_sort_reverse(List, attrs):

        try:
            if attrs != 'message' and attrs != 'userName':
                for i in range(0, len(List) - 1):
                    for j in range(0, len(List) - 1 - i, 1):
                        attribute = getattr(List[j], attrs)
                        attribute1 = getattr(List[j + 1], attrs)
                        if attribute < attribute1:
                            swap(List, j, j + 1)
                return List
            else:
                return print("you cant sort on message or username \n those are strings")
        except:
            return print("the attribute you typed is not available for posts \n maybe you typed wrong?")

    @classmethod
    def partition(self, List, low, high, attrs):
        posPartitions = []

        middle = (low + high)// 2
        posPartitions.append(List[low])
        posPartitions.append(List[middle])
        posPartitions.append(List[high])
        self.bubble_sort(posPartitions, attrs)

        pivot_value = statistical.get_median(posPartitions, attrs)

        if getattr(List[low], attrs) == pivot_value:
            pivot_index = low
        elif getattr(List[middle], attrs) == pivot_value:
            pivot_index = middle
        elif getattr(List[high], attrs) == pivot_value:
            pivot_index = middle

        swap(List, pivot_index, high)
        i = low

        for j in range(low, high, 1):

            attr = getattr(List[j], attrs)
            attr2 = getattr(List[high], attrs)
            if attr <= attr2:
                swap(List, i, j)
                i = i + 1
        swap(List, i, high)
        return i

    @classmethod
    def quick_sort(self, List, low, high, attrs):
        high1 = high - 1
        if low >= high1:
            return List
        pivot_index = self.partition(List, low, high1, attrs)
        self.quick_sort(List, low, pivot_index - 1, attrs)
        self.quick_sort(List, pivot_index + 1, high, attrs)


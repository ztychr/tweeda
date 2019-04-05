

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


class Sorting:
    # bubblesort algorthm that sorts low-high. The attribute that you would like to sort is passed as parameter
    # takes list of posts as parameter

    @staticmethod
    def bubble_sort(List, attrs):
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




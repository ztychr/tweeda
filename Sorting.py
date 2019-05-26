from Statistical import statistical

"""
The Sorting class. Contains the Quicksort and the Bubblesort algorithm
"""
class Sorting:
    """
    method used for getting two indexes in a list, and swapping them.
    Used in both Quicksort and bubblesort
    @:param nums. list
    @:param i. the first index
    @:param j. the second index
    """
    @classmethod
    def swap(cls, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    """
    Bubblesort. The sorting algorithm which is not directly used in controller,
    but is used to secure a better perfomance for Quicksort.

    @:param List. List of tweet-objects
    @:param attrs. Attribute for sorting
    @:returns A sorted list.

    """
    @classmethod
    def bubble_sort(cls, List, attrs):
        try:
            if attrs != 'message' and attrs != 'userName':
                for i in range(0, len(List) - 1):

                    for j in range(0, len(List) - 1 - i, 1):
                        attribute = getattr(List[j], attrs)
                        attribute1 = getattr(List[j + 1], attrs)

                        if attribute > attribute1:
                            cls.swap(List, j, j + 1)
                return List
            else:
                return print("you cant sort on message or username \n those are strings")
        except:
            return print("the attribute you typed is not available for posts \n maybe you typed wrong?")

    """
    The partition method for quicksort. Partition puts all elements smaller than pivot to the left of it,
    and all others to the right
    Notice that bubblesort is called, and used here
    @:param List. the List of tweet-objects for sorting
    @:param low. the lowest index of the sublist. defines where the sublist starts
    @:param high.  The highest index of the sublist. defines where the sublist ends.
    @:param attrs. The attribute that is up for sorting
    @:returns The index that the pivot element is now placed in
    """
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
            pivot_index = high

        self.swap(List, pivot_index, high)
        i = low
        for j in range(low, high, 1):

            attr = getattr(List[j], attrs)
            attr2 = getattr(List[high], attrs)
            if attr <= attr2:
                self.swap(List, i, j)
                i = i + 1
        self.swap(List, i, high)
        return i

    """
    The quicksort algorithm with a base case, a call of partition to get sublists,
    and two recursive calls on the lowest and the highest end of the Lists
    @:param List. The list of tweet-objects
    @:param low. lowest index
    @:param high. the highest index
    @:param attrs. the attribute that is up for sorting
    """
    @classmethod
    def quick_sort(self, List, low, high, attrs):

        if low >= high:
            return List
        pivot_index = self.partition(List, low, high, attrs)
        self.quick_sort(List, low, pivot_index - 1, attrs)
        self.quick_sort(List, pivot_index + 1, high, attrs)

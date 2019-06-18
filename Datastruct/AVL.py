class Node:

    def __init__(self, ID):
        self.ID = ID
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.height = 1 # bliver som default altid sat til 1, fordi nye nodes altid er leaf


class AVLTree:

    def __init__(self, list = None):
        self.root = None
        if list != None:
            for i in list:
                self.insert(i)

    def __repr__(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '' + sep
                    next_row += '' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.ID != None:
                    buf = ' ' * int((5 - len(str(n.ID))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.ID), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.leftChild != None:
                    next_nodes.append(n.leftChild)
                    next_row += ' /' + sep
                else:
                    next_row += '' + sep
                    next_nodes.append(None)

                if n.rightChild != None:
                    next_nodes.append(n.rightChild)
                    next_row += '\ ' + sep
                else:
                    next_row += '' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def constructfromList(self, list):
        for i in list:
            ID = i['ID']
            self.insert(ID)



    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert(value, self.root)


    def __insert(self, ID, current):
        if ID < current.ID:
            if not current.leftChild:

                current.leftChild = Node(ID)
                current.leftChild.parent = current
                self._inspect_insertion(current.leftChild) #inspicerer højde, o0g tjekker om det skal roteres
            else:
                self.__insert(ID, current.leftChild)
        elif ID> current.ID:
            if not current.rightChild:
                current.rightChild = Node(ID)
                current.rightChild.parent = current
                self._inspect_insertion(current.rightChild)
            else:
                self.__insert(ID, current.rightChild)
        else:
            print("fail occurred, the same id is already twice en in structure")

    def _find(self, ID, current):
        if ID == current.ID:
            return current
        elif ID < current.ID and current.leftChild != None:
            return self._find(ID, current.leftChild)
        elif ID > current.ID and current.rightChild != None:
            return self._find(ID, current.rightChild)

    def print_tree(self):
        if  self.root is not None:
            self._print_tree(self.root)
        else:
            print("træet er tomt")

    def _print_tree(self, current):
        if current != None:
            self._print_tree(current.leftChild)
            print(str(current.ID))
            self._print_tree(current.rightChild)

    def _inspect_insertion(self, current, path=[]): # path er en liste af de nodes som vi har besøgt
        if current.parent==None: return #base case, hvis vi befinder os ved root, som ikke har en paremnt
        path = [current]+path # vi smider current node ind i toppen (ligeom push)

        leftHeight = self.get_height(current.parent.leftChild) # vi kigger på current node og dens søskende og tjeker deres højde fra bunden
        rightHeight = self.get_height(current.parent.rightChild)

        if abs(leftHeight - rightHeight)>1: # vi tjekker om der er balanceret
            path = [current.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return

        newHeight = 1 + current.height
        if newHeight > current.parent.height:
            current.parent.height = newHeight

        self._inspect_insertion(current.parent, path)

    # rebalance har 3 cases
    def _rebalance_node(self, z, y, x): # z is always the node that needs to be removed/moved around
        if y == z.leftChild and x == y.leftChild:
            self._rotate_right(z)
        elif y == z.leftChild and x == y.rightChild:
            self._rotate_left(y)
            self._rotate_right(z)
        elif y == z.rightChild and x == y.rightChild:
            self._rotate_left(z)
        elif y == z.rightChild and x == y.leftChild:
            self._rotate_right(y)
            self._rotate_left(z)

    def search(self, ID):
        if self.root != None:
            return self._search(ID, self.root)
        else:
            return False

    def _search(self, ID, current):
        if ID == current.ID:
            return True
        elif ID < current.ID and current.leftChild != None:
            return self._search(ID, current.leftChild)
        elif ID > current.ID and current.rightChild != None:
            return self._search(ID, current.rightChild)
        return False


    def _rotate_right(self, z):
        sub_root = z.parent
        y = z.leftChild
        t3 = y.rightChild
        y.rightChild = z
        z.parent = y
        z.leftChild = t3
        if t3 != None: t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.leftChild == z:
                y.parent.leftChild = y
            else:
                y.parent.righChild = y
        z.height = 1 + max(self.get_height(z.leftChild), self.get_height(z.rightChild))
        y.height = 1 + max(self.get_height(y.leftChild),self.get_height(y.rightChild))
    def _rotate_left(self, z):
        sub_root = z.parent
        y = z.rightChild
        t2 = y.leftChild
        y.leftChild = z
        z.parent = y
        z.rightChild = t2
        if t2 != None: t2.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.leftChild == z:
                y.parent.leftChild = y
            else:
                y.parent.rightChild = y
        z.height = 1 + max(self.get_height(z.leftChild),self.get_height(z.rightChild))
        y.height = 1 + max(self.get_height(y.leftChild),self.get_height(y.rightChild))
    def get_height(self, current):
        if current == None: return 0
        return current.height


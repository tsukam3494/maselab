import re
import copy


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    >>> values = DoublyLinkedList()
    >>> values.insert(5)
    >>> values.insert(2)
    >>> values.insert(3)
    >>> values.insert(1)
    >>> values.delete(3)
    >>> values.insert(6)
    >>> values.delete(5)
    >>> values.deletefirst()
    >>> values.deletelast()
    >>> print(values)
    1
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        if self.head is None:
            return result
        else:
            current_node = self.head
            while current_node is not None:
                if result != "":
                    result += ("," + str(current_node.key))
                else:
                    result += str(current_node.key)
                current_node = current_node.next
            return result

    def __len__(self):
        counter = 0
        if self.head is None:
            return counter
        else:
            current_node = self.head
            while current_node is not None:
                counter += 1
                current_node = current_node.next
            return counter

    def insert(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_list(self, values):
        for value in reversed(values):
            self.insert(value)

    def delete(self, key):
        if self.head is not None:
            current_node = self.head
            # current_nodeは先頭から末尾まで変わっていく
            while current_node is not None:
                if key == current_node.key:
                    # current_nodeが先頭出ない場合
                    if current_node.prev is not None:
                        current_node.prev.next = current_node.next
                    # current_nodeが先頭である場合
                    else:
                        self.head = current_node.next
                    # current_nodeが末端である場合
                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev
                    break
                current_node = current_node.next

    def deletefirst(self):
        # 先頭を二番目のノードに変え、二番目のノードのprevをNoneにする
        if self.head is not None:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next

    def deletelast(self):
        if self.head is not None:
            current_node = self.head
            # 要素が2つ以上だった場合
            if self.head.next is not None:
                while True:
                    if current_node.next is None:
                        current_node.prev.next = None
                        break
                    else:
                        current_node = current_node.next
            # 要素が1つだった場合
            else:
                self.head = None


def insertionsort(values, comp_func):
    """
    >>> values1 = [5,2,4,6,1,3]
    >>> insertionsort(values1, comp_func=lambda x, y: x < y)
    insertion sort
    >>> print(values1)
    [1, 2, 3, 4, 5, 6]
    >>> values2 = DoublyLinkedList()
    >>> values2.insert_list([5,2,4,6,1,3])
    >>> print(values2)
    5,2,4,6,1,3
    >>> insertionsort(values2, comp_func=lambda x, y: x < y)
    insertion sort
    >>> print(values2)
    1,2,3,4,5,6
    """
    if isinstance(values, list):
        print("insertion sort")
        for i in range(1, len(values)):
            v = values[i]
            j = i - 1
            while j >= 0 and comp_func(int(re.sub(r"\D", "", str(v))), int(re.sub(r"\D", "", str(values[j])))):
                values[j + 1] = values[j]
                j = j - 1
            values[j + 1] = v
    elif isinstance(values, DoublyLinkedList):
        print("insertion sort")
        if len(values) >= 2:
            v = values.head.next
            while v is not None:
                # v.keyはソート途中で変わってしまうため初期値をvkeyに保管
                vkey = v.key
                j = v.prev
                while j is not None \
                        and comp_func(int(re.sub(r"\D", "", str(vkey))), int(re.sub(r"\D", "", str(j.key)))):
                    j.next.key = j.key
                    j = j.prev
                if j is None:
                    values.head.key = vkey
                else:
                    j.next.key = vkey
                # vを更新
                v = v.next


def bubblesort(values, comp_func):
    """
    >>> values1 = [5,3,2,4,1]
    >>> bubblesort(values1, comp_func=lambda x, y: x < y)
    bubble sort
    >>> print(values1)
    [1, 2, 3, 4, 5]
    >>> values2 = DoublyLinkedList()
    >>> values2.insert_list([5,3,2,4,1])
    >>> print(values2)
    5,3,2,4,1
    >>> bubblesort(values2, comp_func=lambda x, y: x < y)
    bubble sort
    >>> print(values2)
    1,2,3,4,5
    """
    if isinstance(values, list):
        print("bubble sort")
        flag = 1
        while flag:
            flag = 0
            for j in reversed(range(1, len(values))):
                if comp_func(int(re.sub(r"\D", "", str(values[j]))), int(re.sub(r"\D", "", str(values[j - 1])))):
                    tmp = values[j]
                    values[j] = values[j - 1]
                    values[j - 1] = tmp
                    flag = 1
    elif isinstance(values, DoublyLinkedList):
        print("bubble sort")
        # リストが2以上の時ソートする
        if len(values) >= 2:
            # 更新が行われたかどうかのフラグを1に初期化
            flag = 1
            while flag:
                flag = 0
                v = values.head
                for i in range(1, len(values)):
                    v = v.next
                    if comp_func(int(re.sub(r"\D", "", str(v.key))), int(re.sub(r"\D", "", str(v.prev.key)))):
                        temp = v.key
                        v.key = v.prev.key
                        v.prev.key = temp
                        flag = 1


def selectionsort(values, comp_func):
    """
    >>> values1 = [5,6,4,2,1,3]
    >>> selectionsort(values1, comp_func=lambda x, y: x < y)
    selection sort
    >>> print(values1)
    [1, 2, 3, 4, 5, 6]
    >>> values2 = DoublyLinkedList()
    >>> values2.insert_list([5,6,4,2,1,3])
    >>> print(values2)
    5,6,4,2,1,3
    >>> selectionsort(values2, comp_func=lambda x, y: x < y)
    selection sort
    >>> print(values2)
    1,2,3,4,5,6
    """
    if isinstance(values, list):
        print("selection sort")
        for i in range(0, len(values) - 1):
            minj = i
            for j in range(i, len(values)):
                if comp_func(int(re.sub(r"\D", "", str(values[j]))), int(re.sub(r"\D", "", str(values[minj])))):
                    minj = j
            tmp = values[i]
            values[i] = values[minj]
            values[minj] = tmp
    elif isinstance(values, DoublyLinkedList):
        print("selection sort")
        # リストが2以上の時ソートする
        if len(values) >= 2:
            v = values.head
            for i in range(0, len(values) - 1):
                node_j = v
                minj = v
                for j in range(i, len(values)):
                    if comp_func(int(re.sub(r"\D", "", str(node_j.key))), int(re.sub(r"\D", "", str(minj.key)))):
                        minj = node_j
                    node_j = node_j.next
                tmp = v.key
                v.key = minj.key
                minj.key = tmp
                v = v.next


def stablesortcheck(values, func):
    """
    >>> values1 = ["H4", "C9", "S4", "D2", "C3"]
    >>> values2 = DoublyLinkedList()
    >>> values2.insert_list(values1)
    >>> stablesortcheck(values1,insertionsort)
    insertion sort
    ['D2', 'C3', 'H4', 'S4', 'C9']
    Stable
    >>> stablesortcheck(values2,bubblesort)
    bubble sort
    D2,C3,H4,S4,C9
    Stable
    >>> values3 = ["H4", "C9", "S4", "D2", "C3"]
    >>> stablesortcheck(values3,selectionsort)
    selection sort
    ['D2', 'C3', 'S4', 'H4', 'C9']
    Not Stable
    """
    values1 = copy.deepcopy(values)
    values2 = copy.deepcopy(values)
    func(values2, comp_func=lambda x, y: x < y)
    print(values2)
    if isinstance(values1, DoublyLinkedList):
        values1 = str(values1).split(",")
    if isinstance(values2, DoublyLinkedList):
        values2 = str(values2).split(",")
    for i in range(len(values1)):
        for j in range(i + 1, len(values1)):
            for k in range(len(values2)):
                for l in range(k + 1, len(values2)):
                    if (re.sub(r"\D", "", str(values1[i])) == re.sub(r"\D", "", str(values1[j]))
                            and values1[i] == values2[l]
                            and values1[j] == values2[k]):
                        print("Not Stable")
                        return
    print("Stable")
    return


values1 = [4, 7, 3, 8, 4, 23]
values2 = [4, 7, 3, 8, 4, 23]
values3 = [4, 7, 3, 8, 4, 23]
insertionsort(values1, comp_func=lambda x, y: x < y)
print(values1)
bubblesort(values2, comp_func=lambda x, y: x > y)
print(values2)
j = DoublyLinkedList()
j.insert_list(values3)
selectionsort(values3, comp_func=lambda x, y: True if ((x % 2 == 1 and y % 2 == 0)
                                                       or (x % 2 == y % 2 and x < y)) else False)
print(values3)

values4 = [4, 7, 3, 8, 4, 23]
d_list1 = DoublyLinkedList()
d_list1.insert_list(values4)
d_list2 = DoublyLinkedList()
d_list2.insert_list(values4)
d_list3 = DoublyLinkedList()
d_list3.insert_list(values4)
selectionsort(d_list1, comp_func=lambda x, y: x < y)
print(d_list1)
insertionsort(d_list2, comp_func=lambda x, y: x > y)
print(d_list2)
bubblesort(d_list3, comp_func=lambda x, y: True if ((x % 2 == 1 and y % 2 == 0)
                                                    or (x % 2 == y % 2 and x < y)) else False)
print(d_list3)

if __name__ == '__main__':
    import doctest

    doctest.testmod()

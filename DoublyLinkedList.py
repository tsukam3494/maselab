import re
import copy
from abc import abstractmethod


class Node:
    def __init__(self, key: "int or str"):
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

    def insert(self, key: "int or str"):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_list(self, values: "list"):
        for value in reversed(values):
            self.insert(value)

    def delete(self, key: "int or str"):
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


class AbstractSort:
    @abstractmethod
    def sort(self, values: "list or doublylinkedlist", comp_func: "lambda function"):
        raise NotImplementedError


class InsertionSort(AbstractSort):
    def sort(self, values: "int or str", comp_func: "lambda function"):
        """
        >>> values1 = [5,2,4,6,1,3]
        >>> _c = get_sort_instance("insertion")
        >>> _c.sort(values1, comp_func=lambda x, y: x < y)
        insertion sort
        >>> print(values1)
        [1, 2, 3, 4, 5, 6]
        >>> values2 = DoublyLinkedList()
        >>> values2.insert_list([5,2,4,6,1,3])
        >>> print(values2)
        5,2,4,6,1,3
        >>> _c.sort(values2, comp_func=lambda x, y: x < y)
        insertion sort
        >>> print(values2)
        1,2,3,4,5,6
        """
        # listが与えられた場合
        if isinstance(values, list):
            print("insertion sort")
            for i in range(1, len(values)):
                target_data = values[i]
                j = i - 1
                # target_data,value[j]を数字のみ抽出して比較
                while j >= 0 and comp_func(int(re.sub(r"\D", "", str(target_data))),
                                           int(re.sub(r"\D", "", str(values[j])))):
                    values[j + 1] = values[j]
                    j = j - 1
                values[j + 1] = target_data
        # 双方向リストが与えられたとき
        elif isinstance(values, DoublyLinkedList):
            print("insertion sort")
            if len(values) >= 2:
                target_node = values.head.next
                while target_node is not None:
                    # target_node.keyはソート途中で変わってしまうため初期値をtarget_node_keyに保管
                    target_node_key = target_node.key
                    compare_node = target_node.prev
                    # target_node_key,compare_node.keyを数字のみ抽出して比較
                    while compare_node is not None \
                            and comp_func(int(re.sub(r"\D", "", str(target_node_key))),
                                          int(re.sub(r"\D", "", str(compare_node.key)))):
                        compare_node.next.key = compare_node.key
                        compare_node = compare_node.prev
                    # target_nodeより大きい数字がそれより前に無かった時
                    if compare_node is None:
                        values.head.key = target_node_key
                    # target_nodeより大きい数字がそれより前にあった場合
                    else:
                        compare_node.next.key = target_node_key
                    # target_nodeを更新
                    target_node = target_node.next


class BubbleSort(AbstractSort):
    def sort(self, values: "int or str", comp_func: "lambda function"):
        """
        >>> values1 = [5,3,2,4,1]
        >>> _c = get_sort_instance("bubble")
        >>> _c.sort(values1, comp_func=lambda x, y: x < y)
        bubble sort
        >>> print(values1)
        [1, 2, 3, 4, 5]
        >>> values2 = DoublyLinkedList()
        >>> values2.insert_list([5,3,2,4,1])
        >>> print(values2)
        5,3,2,4,1
        >>> _c.sort(values2, comp_func=lambda x, y: x < y)
        bubble sort
        >>> print(values2)
        1,2,3,4,5
        """
        # listが与えられた場合
        if isinstance(values, list):
            print("bubble sort")
            exchange_flag = 1
            while exchange_flag:
                exchange_flag = 0
                for j in reversed(range(1, len(values))):
                    # values[j],values[j-1]を数字のみ抽出して比較
                    if comp_func(int(re.sub(r"\D", "", str(values[j]))),
                                 int(re.sub(r"\D", "", str(values[j - 1])))):
                        # 交換
                        tmp = values[j]
                        values[j] = values[j - 1]
                        values[j - 1] = tmp

                        exchange_flag = 1
        # 双方向リストが与えられた場合
        elif isinstance(values, DoublyLinkedList):
            print("bubble sort")
            if len(values) >= 2:
                exchange_flag = 1
                while exchange_flag:
                    exchange_flag = 0
                    target_node = values.head
                    for i in range(1, len(values)):
                        target_node = target_node.next
                        # target_node.key,target_node.prev.keyを数字のみ抽出して比較
                        if comp_func(int(re.sub(r"\D", "", str(target_node.key))),
                                     int(re.sub(r"\D", "", str(target_node.prev.key)))):
                            # 交換
                            tmp = target_node.key
                            target_node.key = target_node.prev.key
                            target_node.prev.key = tmp

                            exchange_flag = 1


class SelectionSort(AbstractSort):
    def sort(self, values: "int or str", comp_func: "lambda function"):
        """
        >>> values1 = [5,6,4,2,1,3]
        >>> _c = get_sort_instance("selection")
        >>> _c.sort(values1, comp_func=lambda x, y: x < y)
        selection sort
        >>> print(values1)
        [1, 2, 3, 4, 5, 6]
        >>> values2 = DoublyLinkedList()
        >>> values2.insert_list([5,6,4,2,1,3])
        >>> print(values2)
        5,6,4,2,1,3
        >>> _c.sort(values2, comp_func=lambda x, y: x < y)
        selection sort
        >>> print(values2)
        1,2,3,4,5,6
        """
        # listが与えられた場合
        if isinstance(values, list):
            print("selection sort")
            for i in range(0, len(values) - 1):
                min_value_index_after_target = i
                for j in range(i, len(values)):
                    # values[j],min_value_index_after_targetを数字のみ抽出して比較
                    if comp_func(int(re.sub(r"\D", "", str(values[j]))),
                                 int(re.sub(r"\D", "", str(values[min_value_index_after_target])))):
                        min_value_index_after_target = j
                tmp = values[i]
                values[i] = values[min_value_index_after_target]
                values[min_value_index_after_target] = tmp
        # 双方向リストが与えられた場合
        elif isinstance(values, DoublyLinkedList):
            print("selection sort")
            if len(values) >= 2:
                target_node = values.head
                for i in range(0, len(values) - 1):
                    compare_node = target_node
                    min_value_after_target = target_node
                    for j in range(i, len(values)):
                        # compare_node.key,target_node.prev.keyを数字のみ抽出して比較
                        if comp_func(int(re.sub(r"\D", "", str(compare_node.key))),
                                     int(re.sub(r"\D", "", str(min_value_after_target.key)))):
                            min_value_after_target = compare_node
                        compare_node = compare_node.next
                    # 交換
                    tmp = target_node.key
                    target_node.key = min_value_after_target.key
                    min_value_after_target.key = tmp

                    target_node = target_node.next


def get_sort_instance(algorithm_name: "str"):
    if algorithm_name == "insertion":
        return InsertionSort()
    elif algorithm_name == "bubble":
        return BubbleSort()
    elif algorithm_name == "selection":
        return SelectionSort()


def stablesortcheck(values: "list or doublylinkedlist", algorithm_name: "str"):
    """
    >>> values1 = ["H4", "C9", "S4", "D2", "C3"]
    >>> values2 = DoublyLinkedList()
    >>> values2.insert_list(values1)
    >>> stablesortcheck(values1,"insertion")
    insertion sort
    ['D2', 'C3', 'H4', 'S4', 'C9']
    Stable
    >>> stablesortcheck(values2,"bubble")
    bubble sort
    D2,C3,H4,S4,C9
    Stable
    >>> values3 = ["H4", "C9", "S4", "D2", "C3"]
    >>> stablesortcheck(values3,"selection")
    selection sort
    ['D2', 'C3', 'S4', 'H4', 'C9']
    Not Stable
    """
    # 与えられたリストを複製(values1は初期状態,values2はソート後を入れる)
    values1 = copy.deepcopy(values)
    values2 = copy.deepcopy(values)
    # 実体化しソートを使用
    _c = get_sort_instance(algorithm_name)
    _c.sort(values2, comp_func=lambda x, y: x < y)
    print(values2)
    # 双方向リストであれば、リストに変換
    if isinstance(values1, DoublyLinkedList):
        values1 = str(values1).split(",")
    if isinstance(values2, DoublyLinkedList):
        values2 = str(values2).split(",")

    for i in range(len(values1)):
        for j in range(i + 1, len(values1)):
            for k in range(len(values2)):
                for l in range(k + 1, len(values2)):
                    # 数字が一緒のペアで、ソート前と後で前後関係が入れ替わっている時
                    if (re.sub(r"\D", "", str(values1[i])) == re.sub(r"\D", "", str(values1[j]))
                            and values1[i] == values2[l]
                            and values1[j] == values2[k]):
                        print("Not Stable")
                        return
    print("Stable")
    return


# ラムダ関数使用例
values1 = [4, 7, 3, 8, 4, 23]
values2 = [4, 7, 3, 8, 4, 23]
values3 = [4, 7, 3, 8, 4, 23]
_c1 = get_sort_instance("insertion")
_c1.sort(values1, comp_func=lambda x, y: x < y)
print(values1)
_c2 = get_sort_instance("bubble")
_c2.sort(values2, comp_func=lambda x, y: x > y)
print(values2)
j = DoublyLinkedList()
j.insert_list(values3)
_c3 = get_sort_instance("selection")
_c3.sort(values3, comp_func=lambda x, y: True if ((x % 2 == 1 and y % 2 == 0)
                                                  or (x % 2 == y % 2 and x < y)) else False)
print(values3)

values4 = [4, 7, 3, 8, 4, 23]
d_list1 = DoublyLinkedList()
d_list1.insert_list(values4)
d_list2 = DoublyLinkedList()
d_list2.insert_list(values4)
d_list3 = DoublyLinkedList()
d_list3.insert_list(values4)
_c3.sort(d_list1, comp_func=lambda x, y: x < y)
print(d_list1)
_c1.sort(d_list2, comp_func=lambda x, y: x > y)
print(d_list2)
_c2.sort(d_list3, comp_func=lambda x, y: True if ((x % 2 == 1 and y % 2 == 0)
                                                  or (x % 2 == y % 2 and x < y)) else False)
print(d_list3)

if __name__ == '__main__':
    import doctest

    doctest.testmod()

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        if self.head is None:
            return result
        else:
            current_node = self.head
            while True:
                result += str(current_node.key)
                if current_node.next is None:
                    return result
                    break
                else:
                    current_node = current_node.next

    def __len__(self):
        counter = 0
        if self.head is None:
            return counter
        else:
            current_node = self.head
            while True:
                counter += 1
                if current_node.next is None:
                    return counter
                    break
                else:
                    current_node = current_node.next

    def insert(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        if not self.head is None:
            current_node = self.head
            while True:
                if key == current_node.key:
                    if current_node.prev is not None:
                        current_node.prev.next = current_node.next
                    else:
                        self.head = current_node.next
                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev
                    break
                else:
                    if current_node.next is None:
                        break
                    current_node = current_node.next

    def deletefirst(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next

    def deletelast(self):
        if self.head is not None:
            current_node = self.head
            if self.head.next is not None:
                while True:
                    if current_node.next is None:
                        current_node.prev.next = None
                        break
                    else:
                        current_node = current_node.next
            else:
                self.head = None



def insertionsort(arg):
    if isinstance(arg,list):
        for i in range(1, len(arg)):
            v = arg[i]
            j = i - 1
            while j >= 0 and arg[j] > v:
                arg[j + 1] = arg[j]
                j = j - 1
                arg[j + 1] = v
    elif isinstance(arg,DoublyLinkedList):
        print("insertion sort")
        if len(arg) >= 2:
            current_node = arg.head
            current_next_node = current_node.next
            for i in range(1, len(arg)):
                current_node = current_next_node
                current_next_node = current_node.next
                comparative_node = current_node.prev
                while True:
                    if comparative_node.key <= current_node.key:
                        # current_nodeを初期の位置からdelete
                        if current_node.prev is not None:
                            current_node.prev.next = current_node.next
                        else:
                            arg.head = current_node.next
                        if current_node.next is not None:
                            current_node.next.prev = current_node.prev
                        # current_nodeを挿入
                        current_node.prev = comparative_node
                        current_node.next = comparative_node.next
                        if comparative_node.next is not None:
                            comparative_node.next.prev = current_node
                        comparative_node.next = current_node
                        break
                    if comparative_node.prev is None:
                        # current_nodeを初期の位置からdelete
                        if current_node.prev is not None:
                            current_node.prev.next = current_node.next
                        else:
                            arg.head = current_node.next
                        if current_node.next is not None:
                            current_node.next.prev = current_node.prev
                        # current_nodeを先頭に挿入
                        arg.head.prev = current_node
                        current_node.next = arg.head
                        current_node.prev = None
                        arg.head = current_node
                        break
                    comparative_node = comparative_node.prev

def bubblesort(arg):
    if isinstance(arg,list):
        flag = 1
        while flag:
            flag = 0
            for j in reversed(range(1, len(arg))):
                if arg[j] < arg[j - 1]:
                    tmp = arg[j]
                    arg[j] = arg[j - 1]
                    arg[j - 1] = tmp
                    flag = 1
    elif isinstance(arg,DoublyLinkedList):
        print("bubble sort")
        # リストが2以上の時ソートする
        if len(arg) >= 2:
            # 更新が行われたかどうかのフラグを1に初期化
            flag = 1

            while flag:
                flag = 0
                current_node = arg.head
                for i in range(1, len(arg)):
                    current_node = current_node.next
                    if current_node.prev.key > current_node.key:
                        temp = current_node.key
                        current_node.key = current_node.prev.key
                        current_node.prev.key = temp
                        flag = 1

def selectionsort(arg):
    if isinstance(arg,list):
        for i in range(1, len(arg)):
            minj = i
            for j in range(i, len(arg)):
                if arg[j] < arg[minj]:
                    minj = j
            tmp = arg[i]
            arg[i] = arg[minj]
            arg[minj] = tmp
    elif isinstance(arg,DoublyLinkedList):
        print("selection sort")
        # リストが2以上の時ソートする
        if len(arg) >= 2:
            # serch_nodeは最小値を探すノード,min_nodeは暫定の最小値を入れる
            search_node = arg.head
            min_node = search_node
            # 一桁目はarg.headが変わるため,別個で探す
            for i in range(1, len(arg)):
                # serach_nodeを更新,2桁目からスタートし最終的に末桁まで更新される
                search_node = search_node.next
                # serach_nodeの方がmin_nodeより小さい場合,serach_nodeをmin_nodeにする
                if min_node.key > search_node.key:
                    min_node = search_node
            # min_nodeが決定されたため、min_nodeがarg.head出ないとき、一桁目に挿入する
            if not min_node == arg.head:
                # min_nodeを初期の位置からdelete
                min_node.prev.next = min_node.next
                if min_node.next is not None:
                    min_node.next.prev = min_node.prev
                # min_nodeを先頭に挿入
                arg.head.prev = min_node
                min_node.next = arg.head
                min_node.prev = None
                arg.head = min_node
            # 二桁目以降のソートを行う、代入する桁のノードは変わってしまうためcurrent_nodeは決定する桁の一つ前の桁を示す
            current_node = arg.head
            # 二桁目以降の桁数だけループする
            for j in range(2, len(arg)):
                # serch_node,min_nodeの初期状態は代入する桁のノード
                search_node = current_node.next
                min_node = search_node
                # 代入する桁より上の桁の数だけループする
                for k in range(j, len(arg)):
                    # serch_nodeを更新,代入する桁の一つ上の桁からスタートし最終的に末桁まで更新される
                    search_node = search_node.next
                    # serach_nodeの方がmin_nodeより小さい場合,serach_nodeをmin_nodeにする
                    if min_node.key > search_node.key:
                        min_node = search_node
                # min_nodeを初期の位置からdelete
                min_node.prev.next = min_node.next
                if min_node.next is not None:
                    min_node.next.prev = min_node.prev
                # min_nodeを挿入
                min_node.prev = current_node
                min_node.next = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = min_node
                current_node.next = min_node

                # 代入する桁を次の桁に進める
                current_node = current_node.next



alist = [3, 7, 4, 8, 67, 9]

i = DoublyLinkedList()
i.insert("7H")
i.insert("2D")
i.insert("3H")
i.insert("8S")
i.insert("9L")

print(i)
# i.insertionsort()
# i.bubblesort()
selectionsort(i)
print(i)

insertionsort(alist)
print(alist)
print(isinstance(i,DoublyLinkedList))
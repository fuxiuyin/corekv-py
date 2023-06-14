import os
import random

MAX_HEIGHT = 31


class Node:
    def __init__(self, key, value, height: int) -> None:
        self.next_nodes = [None] * (height + 1)
        self.key: str  = key
        self.value: any = value
        self.is_live: bool = True
        
    def __str__(self) -> str:
        if self.key is None:
            return "head"
        else:
            return self.key
    
    def __repr__(self) -> str:
        return self.__str__()


class SkipList:
    def __init__(self) -> None:
        self.randomer = random.Random(int.from_bytes(os.urandom(32), "big"))
        self.head = Node(None, None, MAX_HEIGHT)
        self.key_count = 0
        self.max_hight = 0
        
    def __get_item_height(self):
        height = 0
        while height < MAX_HEIGHT and self.randomer.randint(0, 99) > 49:
            height += 1
        return height
    
    def _get(self, key: str, p_nodes: list) -> Node:
        level = self.max_hight
        p: Node = self.head
        while level >= 0:
            n = None
            while p.next_nodes[level] != None:
                n = p.next_nodes[level]
                while n is not None and not n.is_live:
                    n = n.next_nodes[level]
                    p.next_nodes[level] = n
                if n is None:
                    break
                if n.key == key:
                    return n
                elif n.key < key:
                    p = n
                else:
                    break
            
            while p.next_nodes[level] == n and level >= 0:
                if p_nodes is not None:
                    p_nodes[level] = p
                level -= 1
        return None
        
        
    def set(self, key: str, value: any):
        p_nodes = [None] * (MAX_HEIGHT + 1)
        
        old_node = self._get(key, p_nodes)
        if old_node is not None:
            old_value = old_node.value            
            old_node.value = value
            return old_value
        
        new_node_height = self.__get_item_height()
        if new_node_height > self.max_hight:
            self.max_hight = new_node_height
        new_node = Node(key, value, new_node_height)
        
        self.key_count += 1
        level = new_node_height
        while level >= 0:
            p_node = p_nodes[level]
            if p_node is None:
                p_node = self.head
            new_node.next_nodes[level] = p_node.next_nodes[level]
            p_node.next_nodes[level] = new_node
            level -= 1
    
    def get(self, key: str):
        node = self._get(key, None)
        if node is None:
            return None
        else:
            return node.value        

    
    def remove(self, key: str):
        node = self._get(key, None)
        if node is None:
            return None
        else:
            node.is_live = False
    
    def draw(self, gep=4):
        lines = []
        
        line = []
        geps = []
        c = self.head
        while c is not None:
            line.append(str(c))            
            geps.append(gep)
            line.append('-' * gep)
            c = c.next_nodes[0]
        line.append("None")
        lines.append(line)
        
        level = 1
        while level <= MAX_HEIGHT:
            if self.head.next_nodes[level - 1] is None:
                break
            line = []
            n_geps = list(reversed(geps))
            geps = []
            c = self.head
            while c is not None:
                line.append(str(c))
                gep = n_geps.pop()
                n_c = c
                while n_c.next_nodes[level - 1] != c.next_nodes[level]:
                    gep += len(n_c.next_nodes[level - 1].key)
                    gep += n_geps.pop()
                    n_c = n_c.next_nodes[level - 1]
                line.append('-' * gep)
                c = c.next_nodes[level]
                geps.append(gep)
            line.append("None")
            lines.append(line)
            level += 1
        for line in reversed(lines):
            print("".join(line))
                

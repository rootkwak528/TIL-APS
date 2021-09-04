from functools import lru_cache

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [False] * len(parent)
        self.user = [None] * len(parent)
        
        self.children = collections.defaultdict(list)
        for i in range(1, len(parent)):
            self.children[parent[i]].append(i)
            
        self.locked_set = set()
            
        # parent set for every nodes
        self.parents_set = collections.defaultdict(set)
        for i in range(1, len(parent)):
            p_node = self.parent[i]
            while p_node >= 0:
                if p_node < i:
                    self.parents_set[i].add(p_node)
                    self.parents_set[i] |= self.parents_set[p_node]
                    break
                else:
                    self.parents_set[i].add(p_node)
                    p_node = self.parent[p_node]
                    
        # children set for every nodes
        self.children_set = collections.defaultdict(set)
        self.get_children_set(0)
        
        # print(self.parents_set)
    
    
    @lru_cache(None)
    def get_children_set(self, node):
        self.children_set[node] = set(self.children[node])
        
        for child in self.children[node]:
            self.children_set[node] |= self.get_children_set(child)
        
        return self.children_set[node]
        

    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num] = True
            self.user[num] = user
            self.locked_set.add(num)
            return True
        else:
            return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] and self.user[num] == user:
            self.locked[num] = False
            self.user[num] = None
            self.locked_set.remove(num)
            return True
        else:
            return False

        
    def upgrade(self, num: int, user: int) -> bool:
        
        # check first
        if self.locked[num]:
            return False
        
        # print(self.locked_set, self.children_set[num], self.parents_set[num])
        
        if not self.locked_set & self.children_set[num]:
            return False
        
        if self.locked_set & self.parents_set[num]:
            return False
        
#         locked_children = []
#         queue = self.children[num]
#         idx = 0
#         flag = False
#         while idx < len(queue):
#             node = queue[idx]
#             queue += self.children[node]
#             idx += 1
#             if self.locked[node]:
#                 locked_children.append(node)
#                 flag = True
#         if not flag:
#             return False
        
#         parent = self.parent[num]
#         while parent >= 0:
#             if self.locked[parent]:
#                 return False
#             parent = self.parent[parent]

        # update later
        self.locked[num] = True
        self.locked_set.add(num)
        
        locked_children = self.locked_set & self.children_set[num]
        for locked_child in locked_children:
            self.locked[locked_child] = False
            self.locked_set.remove(locked_child)
            
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
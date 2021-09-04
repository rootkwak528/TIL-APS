class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        ans = []
        flag = False
        
        for i in range(len(land)):
            for j in range(len(land[0])):
                
                if flag:
                    if land[i][j] == 0:
                        flag = False
                
                else:
                    if land[i][j] == 1:
                        land[i][j] = 2

                        new_i = i + 1
                        while new_i < len(land):
                            if land[new_i][j] == 1:
                                land[new_i][j] = 2
                                new_i += 1
                            else:
                                break

                        new_j = j + 1
                        while new_j < len(land[0]):
                            if land[i][new_j] == 1:
                                land[i][new_j] = 2
                                new_j += 1
                            else:
                                break
                                
                        ans += [[i, j, new_i-1, new_j-1]]
                        
                    elif land[i][j] == 2:
                        flag = True
                        
        return ans
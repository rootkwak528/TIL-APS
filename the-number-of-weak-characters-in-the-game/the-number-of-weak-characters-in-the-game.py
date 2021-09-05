class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(reverse=True)
        print(properties)
        
        ans = 0
        max_def = 0
        max_def_with_same_att = properties[0]
        
        for pro in properties[1:]:
            if pro[0] != max_def_with_same_att[0]:
                max_def = max(max_def, max_def_with_same_att[1])
                max_def_with_same_att = pro
                    
            if max_def and pro[1] < max_def:
                ans += 1
                    
        return ans
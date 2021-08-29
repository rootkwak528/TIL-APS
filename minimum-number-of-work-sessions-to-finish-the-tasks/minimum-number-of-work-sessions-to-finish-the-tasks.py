from functools import lru_cache

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        tasks = sorted(tasks, reverse=True)
        
        @lru_cache(None)
        def recursive(sessions, idx):
            if idx == len(tasks):
                return len(sessions)
            
            task = tasks[idx]
            rtn = len(sessions) + len(tasks) - idx
            
            for i in range(len(sessions)):
                if sum(sessions[i]) + task <= sessionTime:
                    new_session = tuple(list(sessions[i]) + [task])
                    new_sessions = sessions[:i] + (new_session,) + sessions[i+1:]
                    
                    rtn = min(rtn, recursive(new_sessions, idx+1))
                    
            new_sessions = sessions + ((task,),)
            rtn = min(rtn, recursive(new_sessions, idx+1))
            
            return rtn
        
        return recursive( (), 0 )
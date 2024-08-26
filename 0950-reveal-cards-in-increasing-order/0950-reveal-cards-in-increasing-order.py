class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        N = len(deck)
        
        q = deque()
        
        for i in range(N):
            q.append(i)
        
        deck.sort()
        
        res = [0]*N
        for card in deck:
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())
            
        
        return res
        
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if len(people)<=1:
            return len(people)
        lst_saved = []
        needed_boats = 0
        i = 0
        j = len(people)-1
        people = sorted(people,reverse=False)
        while(i<=j):
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            needed_boats+=1
            
            
        return needed_boats
        


        
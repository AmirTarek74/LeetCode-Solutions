class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)

        q = deque(range(len(recipes)))
        res = []
        last_size = -1
        while len(available) > last_size:
            last_size = len(available)
            q_size = len(q)
            while q_size > 0:
                q_size -= 1
                idx = q.popleft()
                if all(ing in available for ing in ingredients[idx]):
                    available.add(recipes[idx])
                    res.append(recipes[idx])
                else:
                    q.append(idx)
        return res
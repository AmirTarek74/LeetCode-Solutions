class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            final_local = ''
            for c in local:
                if c == '.':
                    continue
                elif c== '+':
                    break
                final_local += c
            res.add(final_local+'@'+domain)
        return len(res)
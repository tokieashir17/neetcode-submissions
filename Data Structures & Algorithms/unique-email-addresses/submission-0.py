class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            hashset.add((local,domain))
        return len(hashset)
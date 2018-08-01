class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        'Set to check all mails'
        all_mails = {}
        'List to save result'
        result = {}
        count = 0
        names = []
        for i in range(len(accounts)):
            mails = set()
            flag = False
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in all_mails:
                    if not flag:
                        repeated = all_mails[accounts[i][j]]
                    flag = True

                else:
                    mails.add(accounts[i][j])
            if flag:
                result[repeated].update(mails)
                for mail in mails:
                    all_mails[mail] = repeated
            else:
                for mail in mails:
                    all_mails[mail] = count
                result[count] = mails
                names.append(accounts[i][0])
                count += 1
        result2 = []
        for key, value in result.items():
            result2.append([names[key]] + sorted(list(value)))

        result2 = sorted(result2, key=lambda x: x[0])
        return result2


# accounts1 = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
accounts1 = [["David", "David0@m.co", "David0@m.co", "David1@m.co"],
             ["David", "David6@m.co", "David1@m.co", "David6@m.co"],
             ["David", "David3@m.co", "David8@m.co", "David0@m.co"],
             ["David", "David5@m.co", "David8@m.co", "David7@m.co"],
             ["David", "David5@m.co", "David2@m.co", "David1@m.co"],
             ["David", "David0@m.co", "David7@m.co", "David6@m.co"],
             ["David", "David0@m.co", "David1@m.co", "David4@m.co"],
             ["David", "David1@m.co", "David1@m.co", "David8@m.co"]]
# accounts1 = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
#              ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
#              ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
sol = Solution()
print(sol.accountsMerge(accounts1))

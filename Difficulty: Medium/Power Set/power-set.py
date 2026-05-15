class Solution:
    def AllPossibleStrings(self, s):

        ans = []

        def backtrack(index, path):

            if index == len(s):

                if path != "":
                    ans.append(path)

                return

            backtrack(index + 1, path + s[index])

            backtrack(index + 1, path)

        backtrack(0, "")

        ans.sort()

        return ans
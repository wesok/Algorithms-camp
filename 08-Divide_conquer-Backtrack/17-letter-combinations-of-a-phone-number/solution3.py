# 递归实现1：
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def search(s, digits, level, res, lookup):
            # terminator
            if level == n:
                res.append(s)
                return
            
            # 取出digits每层数字对应的str
            letters = lookup.get(digits[level])

            # 遍历str
            for i in range(len(letters)):
                # 下探到下一层
                search(s + letters[i], digits, level + 1, res, lookup)


        n = len(digits)
        if digits == None or n == 0: 
            return []

        lookup = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []
        search("", digits, 0, res, lookup)
        return res



# 简洁版递2：
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def helper(level, visited):
            if level == n:
                res.append(visited)
                return 
            for s in lookup[digits[level]]:
                helper(level + 1,visited + s)


        lookup = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        n = len(digits)
        if not digits: return []
        
        res = []
        helper(0,"")
        return res
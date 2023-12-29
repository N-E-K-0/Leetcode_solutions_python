def isValid(self, s: str) -> bool:
        a = 0
        while True:
            if '()' in s:
                s = s.replace('()','')
            elif '{}' in s:
                s = s.replace('{}','')
            elif '[]' in s:
                s = s.replace('[]','')
            else: 
                return not s
isValid('(){}[]')
# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text = text.split(' ')
#         text.sort(key = len)
#         text = [char.lower() for char in text]
#         text = ' '.join([text[0].capitalize()] + text[1:])
       

            
        
#         return text

class Solution:
    def firstUniqChar(self, s):
        d = {}
        seen = set()
        for index, c in enumerate(s):
            

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         size = len(s)

#         for i in s:
#             print(i)
#             for j in range(1,size):
#                 if i == s[j]:
#                     continue
#                 else:
#                     print(i, s[j])
#                     return s.index(i)

def main():
    # print(Solution.arrangeWords(Solution,"Leetcode is cool"))
    print(Solution.firstUniqChar(Solution, "loveleetcode"))

if __name__ == "__main__":
    main()
class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        
        n = max(len(a),len(b))
        carry = 0
        ans = ""
        for i in range(n):
            ca = a[-1 - i] if i < len(a) else '0'
            cb = b[-1 - i] if i < len(b) else '0'
            #print(ca,cb,carry)
            ans = (str((int(ca)+int(cb)+ carry)%2)) + ans #carry from previous iteration 
            carry = 1 if (int(ca) + int(cb)+carry) >=2 else 0 # update carry
        
        ans = str(carry) + ans if carry == 1 else ans 
            
        return ans

if __name__ == "__main__":
    s = Solution()

    print(s.addBinary("11","1")) #Expect "100"
    print(s.addBinary("1010","1011")) #Expect "10101"
    print(s.addBinary("0","0")) #Expect "0"
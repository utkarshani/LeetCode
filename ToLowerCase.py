#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#Example 1:
#Input: "Hello"
#Output: "hello"

#Example 2:
#Input: "here"
#Output: "here"

#Example 3:
#Input: "LOVELY"
#Output: "lovely"

#Runtime:20 ms
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        newstr=''
        for i in range(len(str)):
            if(str[i]>='A'):
                if (str[i] <='Z'):
                    newstr+=chr(ord(str[i]) + 32)
                else:
                    newstr+=chr(ord(str[i]))
            else:
                    newstr+=chr(ord(str[i]))       
        return newstr

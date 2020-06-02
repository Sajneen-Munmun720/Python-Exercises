def test_palindrome(string):
    def reverse(string):
        reversed_string = ""
        for i in string:
            reversed_string = i + reversed_string
            if string==reversed_string:
                print("string is palindrome")
        return reversed_string
    return reverse(string)
String=input("Enter a string:")
result=test_palindrome(String)
print(result)

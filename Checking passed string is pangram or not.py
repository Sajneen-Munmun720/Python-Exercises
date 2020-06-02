def test_pangram(passed_string):
    import string
    small=set(string.ascii_lowercase)
    return small<=set(passed_string.lower())
String=input("Enter a string: ")
if test_pangram(String):
    print("The string is a pangram")
else:
    print("The string is not a pangram")
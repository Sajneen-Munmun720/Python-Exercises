python_code_string='print("I am a pythonista")'
python_code="""
def sum(a,b):
    return a+b
print('Sum of a and b is:',sum(7,8))
"""
exec(python_code_string)
exec(python_code)
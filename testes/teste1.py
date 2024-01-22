import array

a = array.array('c', 'spam and eggs')
a[0] = ord('S')  # Use ord() to get the ASCII value of 'S'
a[-4:] = array.array('c', 'toast')  # Replace the last four characters with 'toast'

result = "".join(a)
print(result)

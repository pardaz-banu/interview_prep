#A string is said to be Pangram if it contains all the alphabets
from string import ascii_lowercase
st = input()
if set(ascii_lowercase) - set(st.lower()) == set([]):
    print("Pangram")
else:
    print("Not Pangram")

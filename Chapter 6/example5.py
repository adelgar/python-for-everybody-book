str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
print(colon)
number = float(str[colon+1:])
print(number)
digits = ['', 'one', 'two', 'three', 'four', 'five', 
          'six', 'seven', 'eight', 'nine', 'ten', 
          'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
          'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = 'hundred'

answer = 0

#1-19
answer = digits[1:]
#20-99
answer += [t + digits[j] for t in tens for j in range(10)]
first = [a for a in answer]

#100 - 999
for i in range(1, 10):
    answer += [digits[i] + hundred]
    answer += [digits[i] + hundred + 'and' + f for f in first]
answer += ['onethousand']
print len(''.join(answer))

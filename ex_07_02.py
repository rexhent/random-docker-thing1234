file = 'mbox-short.txt'
try:
    fhand = open(file)
except:
    print('Invalid filename:', file)
    quit()

#print(fhand.read())
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        colon = line.find(':')
        flt = float(line[colon + 2:])
        total += flt
        count += 1
average = total / count
print('Average spam confidence:', average)



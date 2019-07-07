import csv

file = 'Resources/election_data.csv'

total = 0
ktot = 0
kcan = []
Khan = 'Khan'
ccan = []
Correy = 'Correy'
lcan = []
Li = 'Li'
ocan = []
Otooley = 'O\'Tooley'

found = False

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headrow = next(csvreader)
    total = sum(1 for row in csvreader)
    
with open(file, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     for row in csvreader:
          if row[2] == Khan:
             kcan.append(row[2])
ktot = (len(kcan))
kp = ktot/total
kpf = ('{:.3%}'.format(kp))

with open(file, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     for row in csvreader:
          if row[2] == Correy:
             ccan.append(row[2])
ctot = (len(ccan))
cp = ctot/total
cpf = ('{:.3%}'.format(cp))

with open(file, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     for row in csvreader:
          if row[2] == Li:
             lcan.append(row[2])
ltot = (len(lcan))        
lp = ltot/total
lpf = ('{:.3%}'.format(lp))

with open(file, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     for row in csvreader:
          if row[2] == Otooley:
             ocan.append(row[2])
otot = (len(ocan))       
op = otot/total
opf = ('{:.3%}'.format(op))


# ['Voter ID', 'County', 'Candidate']
print('  Election Results  ')
print('--------------------')
print('Total Votes: ' + str(total))
print('--------------------')
print('Khan: ' + kpf  + ' (' + str(ktot) + ')')
print('Correy: ' + cpf + ' (' + str(ctot) + ')')
print('Li: ' + lpf + ' (' + str(ltot) + ')')
print('O\'Tooley: ' + opf + ' (' + str(otot) + ')')
print('--------------------')
print('Winner: Khan')
print('--------------------')


file = open('PyPoll.txt','w') 

file.write('  Election Results  \n')
file.write('--------------------\n')
file.write('Total Votes: ' + str(total)+'\n')
file.write('--------------------\n')
file.write('Khan: ' + kpf  + ' (' + str(ktot) + ')\n')
file.write('Correy: ' + cpf + ' (' + str(ctot) + ')\n')
file.write('Li: ' + lpf + ' (' + str(ltot) + ')\n')
file.write('O\'Tooley: ' + opf + ' (' + str(otot) + ')\n')
file.write('--------------------\n')
file.write('Winner: Khan\n')
file.write('--------------------\n')
file.close()  

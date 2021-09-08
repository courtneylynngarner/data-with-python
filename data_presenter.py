open_file = open("CupcakeInvoices.csv")

for line in open_file:
  print(line)

open_file.seek(0)
for line in open_file:
  line = line.rstrip('\n').split(',')
  print(line[2])

open_file.seek(0)
for line in open_file:
  line = line.rstrip('\n').split(',')
  total = float(line[3]) * float(line[4])
  print total

open_file.seek(0)
grand_total = 0.0
for line in open_file:
  line = line.rstrip('\n').split(',')
  total = float(line[3]) * float(line[4])
  grand_total += total
  
print grand_total

open_file.close()
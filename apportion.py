#!/usr/bin/env python

import csv
import math
import sys

populations = {}
f = open('2010.csv', 'rt')
try:
  reader = csv.reader(f)
  for row in reader:
    populations[row[0]] = int(row[1])
finally:
  f.close()

total_population = sum(v for v in populations.itervalues())
print total_population
total_seats = 435

# First give each state one seat
seats = dict((k,1) for (k,v) in populations.iteritems())
seat_count = len(seats)

# Then allocate seats using the method of equal proportions
while seat_count < total_seats:
  (max_priority, max_state) = (0, '')
  for (state, pop) in populations.iteritems():
    n = seats[state]
    A = pop / math.sqrt(n*(n+1))
    if (A > max_priority):
      (max_priority, max_state) = (A, state)
  seat_count += 1
  seats[max_state] +=1
  print "house seat: %s, priority: %.0f, state: %s, state seats: %s" % (seat_count, max_priority, max_state, seats[max_state])

# Show results
for k in sorted(seats.iterkeys()):
  quota = total_seats*populations[k]*1.0/total_population
  print k, seats[k], int(math.floor(quota)), int(math.ceil(quota)), quota, populations[k]/seats[k]

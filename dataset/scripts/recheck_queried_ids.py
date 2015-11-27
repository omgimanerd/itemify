#!/usr/bin/python
# This script rechecks all entries in queried_summoners and unqueried_summoners
# and removes any duplicates. It also makes sure that no entry in
# queried_summoners is in unqueried_summoners
# Author: Alvin Lin (alvin.lin@stuypulse.com)

def main():
  with open('../QUERIED_SUMMONERS', 'r') as queried_summoners_input:
    queried_summoners = map(lambda x: x.strip(), list(set(
        queried_summoners_input.readlines())))
  with open('../UNQUERIED_SUMMONERS', 'r') as unqueried_summoners_input:
    unqueried_summoners = map(lambda x: x.strip(), list(set(
        unqueried_summoners_input.readlines())))

  print 'Queried: %s' % ', '.join(queried_summoners)
  print 'Unqueried: %s' % ', '.join(unqueried_summoners)

  nonduplicate_unqueried_summoners = []
  for id in unqueried_summoners:
    if id in queried_summoners:
      print 'Found already queried summoner: %s' % id
    elif id.isspace():
      print 'Found empty summoner ID'
    else:
      nonduplicate_unqueried_summoners.append(id)

  with open('../UNQUERIED_SUMMONERS', 'w') as unqueried_summoners_output:
    for id in nonduplicate_unqueried_summoners:
      unqueried_summoners_output.write('%s\n' % id)

if __name__ == '__main__':
  main()

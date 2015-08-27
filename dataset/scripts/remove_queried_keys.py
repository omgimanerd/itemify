#!/usr/bin/python

def main():
  with open('../queried_summoners', 'r') as queried_summoners_input:
    queried_summoners = queried_summoners_input.read().split('\n')[:-1]
  with open('../unqueried_summoners', 'r') as unqueried_summoners_input:
    unqueried_summoners = unqueried_summoners_input.read().split('\n')[:-1]

  print 'Queried: %s' % ', '.join(queried_summoners)
  print 'Unqueried: %s' % ', '.join(unqueried_summoners)

  nonduplicate_unqueried_summoners = []
  for id in unqueried_summoners:
    if id in queried_summoners:
      print "Found already queried summoner: %s" % id
    else:
      nonduplicate_unqueried_summoners.append(id)

  with open('../unqueried_summoners', 'w') as unqueried_summoners_output:
    for id in nonduplicate_unqueried_summoners:
      unqueried_summoners_output.write('%s\n' % id)

if __name__ == '__main__':
  main()

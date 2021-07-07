import  collections

list1 = ["Rafsan","jani"]
list2 = ["home applicane","Build work","home work"]
list3 = ["Byzid","Chittagong"]

services = collections.defaultdict(list)

for service in list2:
     for name in list1:
          services[service].append(name)

for x in services.keys():
    print (x)
      



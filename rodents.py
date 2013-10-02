class Rodent:
    def __init__(self, tag_id):
        self.tag_id = tag_id
        self.weights = []
        
    def plot(self):
        return self.tag_id[0]
        
    def add_weight(self, weight):
        self.weights.append(weight)
        


from rodents import Rodent

rodents = {}
    
my_file='data.txt'

file=open(my_file)
for line in file:
    tag, weight=line.split(',')
    if tag in rodents:
        rodents[tag].add_weight(weight)
    else:
        rodents[tag]=Rodent(tag)
        rodents[tag].add_weight(weight)
        
print rodents
        

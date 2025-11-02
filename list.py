names=["alex",1,34.5,True]

print(type(names))
print(len(names))
print(names[0])

names[2]="sami"
print(names)

names=["alex","abel","hanna"]
first,second,*third =names

print(third)
print(names[-3:-1])
print(names.pop())


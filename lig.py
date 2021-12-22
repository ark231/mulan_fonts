#!/usr/bin/env python3
normal_vowels="iauoe"
semi_vowels="yw"
consonants="kgsztdnhmrpb"

Vs=[]
for V1 in normal_vowels+semi_vowels:
    if V1 in normal_vowels:
        Vs.append(V1)
    for V2 in normal_vowels:
        Vs.append(V1+V2)

result=[]
for C in consonants:
    for V in Vs:
        result.append(C+V)
#print(result)
for lig in result:
    print(lig)
print()
print(len(result))

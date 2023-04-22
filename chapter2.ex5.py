def maghsom(a):
    maghsom_list=[]
    i=1
    while i<=a:
        b=a%i
        if b==0:
            maghsom_list.append(b)
        i+=1
    return len(maghsom_list)
tedad_maghsom=[]
adad=[]
for i in range(20):
    number=int(input())
    adad.append(number)
    maghsom(number)
    tedad_maghsom.append(maghsom(number))

print(adad[tedad_maghsom.index(max(tedad_maghsom))],max(tedad_maghsom))

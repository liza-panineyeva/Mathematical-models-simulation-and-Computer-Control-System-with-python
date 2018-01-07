
list =[23,12,3,4,5,34,56]
#print(list[1::2])

def pokaz_argumenty(x, y, *args, **kwargs):
    print("x=%s, y=%s" % (x, y))
    print("Argumenty pozycyjne:", end=' ')
    for aa in args:
        print(aa, end=' ')
    print("\nArgumenty nazwane:", end=' ')
    for kk in kwargs:
        print("%s=%s" % (kk, kwargs[kk]), end=' ')


#pokaz_argumenty('abc', 123, 456, 'def','bgt',45, k=789, m='ghi')

gen_kwadratow = (i**2 for i in range(5))
for i in(gen_kwadratow):
    print (i)

v ="Hello,Liza"
r = input("enter a value:")
print(r)

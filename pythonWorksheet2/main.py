shoppingList = ['apple','egg','banana']

shoppingList.append('water') #sona ekleme
#print(shoppingList)

shoppingList.insert(2,'beef') #belirtilen indise ekleme
#print(shoppingList)

shoppingList.remove('beef') #belirtilen indisi çıkartma
#print(shoppingList)

shoppingList[1] = 'watermelon' #belirtilen indisi değiştirme
print(shoppingList)




sayilar = [1,2,3,4,5]

"""kareleri = []
for i in sayilar:
  kareleri.append(i**2)
print(kareleri)"""

kareleri = [i**2 for i in sayilar]
print(kareleri)




tuple = ('orange','letuce','tomato','watermelon') #tuple oluşturduk. tuple ın listeden farkı köşeli parantez yerine normal parantez kullanmamızdır.

item1,item2,item3,item4 = tuple
print(item1)
print(item2)
print(item3)
print(item4)

print(tuple[2])
print(tuple[1:3])




phoneBook = {'dilara': '+90 505 123 45 67','derya': '+90 505 123 54 67','yusuf': '+90 505 123 45 76'}
print(phoneBook)
print(phoneBook['dilara'])




stok = dict() #dict() fonksiyonu sözlük oluşturmamızı sağlar

stok['elma'] = 58
stok['armut'] = 245
stok['kavun'] = 96
stok['portakal'] = 19

print(stok)

print(stok.keys()) #sadece key kısmını bastırır.
print(stok.values()) #sadece value kısmını bastırır.
print(stok.items())# her değişkeni ayırarak yazdırır.
print("--------------------------------------------")

for i in stok:
  stok[i] += 100 # her birine 100 ekledik

print(stok)




messageFile = open("message.txt", "r")
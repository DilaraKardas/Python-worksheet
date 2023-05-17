import random
print(random.randint(1,10))



print(7//2) # integer bölmesi. Sonucun tam kısmını alır. Pythonda yuvarlama, küçük sayıya yapılır
print(7/2)
print(2**3) #üs alma
num1 = 5
num2 = 10
print(num1, ">", num2, "=", num1>num2) #false döndürecek. Karşılaştırma operatörleri böyle kullanılır



print("true and true = ", True and True)
print("true and false = ", True and False)
print("false and true = ", False and True)
print("false and false = ", False and False)



def greetings(firstName, lastName, autoCorrection):
  if autoCorrection == True:
    capitalFirstName = firstName.capitalize()
    capitalLastName = lastName.capitalize()
    print("Hello", capitalFirstName, capitalLastName)
  else:
    print("Hello", firtsName, lastName)
greetings('dilara','kardaŞ',True)



def athlete(name, major, nation):
  print("my favourite athlete is ",name, major, nation)
#athlete('Gabriella Guimaraes','Voleyball','Brezilian')
athlete(major= 'Voleyball', name= 'Yuji Nishida', nation= 'Japan')



import seaborn as sns
data = [1,5,8,4,9,6,10]
sns.lineplot(range(10))

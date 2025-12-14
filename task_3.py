import matplotlib.pyplot as plt


golosni_literi = "аеєиіїоуюя"


f = open('task3.txt', 'r', encoding='utf-8')
text = f.read()
f.close() 
text = text.lower()

spysok_liter = []
spysok_kilkosti = [] 


for litera in golosni_literi:
   
    kiltist = text.count(litera)
    
 
    spysok_liter.append(litera)
    spysok_kilkosti.append(kiltist)


plt.bar(spysok_liter, spysok_kilkosti, color='green')


plt.title('Голосні літери в тексті')
plt.xlabel('Літери')
plt.ylabel('Кількість')


plt.savefig('resultat.png')

print("Все готово! Графік збережено у файл resultat.png")
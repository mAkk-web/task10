import matplotlib.pyplot as plt

# 1. Створюємо рядок з усіма голосними, які будемо шукати
golosni_literi = "аеєиіїоуюя"

# 2. Відкриваємо файл і читаємо текст
# Використовуємо encoding='utf-8', щоб розуміло українські літери
f = open('task3.txt', 'r', encoding='utf-8')
text = f.read()
f.close() # Не забуваємо закрити файл

# Переводимо весь текст у малі літери, щоб 'А' і 'а' були однакові
text = text.lower()

# 3. Готуємо списки для графіка
spysok_liter = []  # Тут будуть літери (вісь X)
spysok_kilkosti = [] # Тут буде кількість (вісь Y)

# 4. Рахуємо кожну голосну
for litera in golosni_literi:
    # Метод count рахує, скільки разів літера зустрічається в тексті
    kiltist = text.count(litera)
    
    # Додаємо дані у списки
    spysok_liter.append(litera)
    spysok_kilkosti.append(kiltist)

# 5. Будуємо стовпчикову діаграму
plt.bar(spysok_liter, spysok_kilkosti, color='green')

# Підписуємо графік, щоб було зрозуміло, що це
plt.title('Голосні літери в тексті')
plt.xlabel('Літери')
plt.ylabel('Кількість')

# 6. Зберігаємо результат у картинку
plt.savefig('resultat.png')

print("Все готово! Графік збережено у файл resultat.png")
import numpy as np
mas_1 = np.array([60, 80, 90, 40, 30])
mas_2 = np.array([1, 4, 1, 8, 2])

print(f"Масив 1: {mas_1}")
print(f"Масив 2: {mas_2}")
print("-" * 30)


dodavannya = mas_1 + mas_2
print(f"Сума масивів: \n{dodavannya}")

vidnimannya = mas_1 - mas_2
print(f"Різниця масивів: \n{vidnimannya}")

mnozhennya = mas_1 * mas_2
print(f"Добуток масивів: \n{mnozhennya}")

dilennya = mas_1 / mas_2
print(f"Ділення масивів: \n{dilennya}")

print("-" * 30)

big_masiv = np.concatenate((mas_1, mas_2))
print(f"Об'єднаний масив: \n{big_masiv}")

print("-" * 30)

maksimumBig = big_masiv.max()
minimumBig = big_masiv.min()
sumaBig = big_masiv.sum()
dobutokBig = big_masiv.prod()

print(f"Max: {maksimumBig}")
print(f"Min: {minimumBig}")
print(f"Сума елементів об'єднаного масиву: {sumaBig}")
print(f"Добуток елементів об'єднаного масиву: {dobutokBig}")
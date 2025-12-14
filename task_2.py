with open("task2.txt", "w", encoding="utf-8") as file:

    for i in range(1, 10):
        
        file.write("a" * i + "\n")

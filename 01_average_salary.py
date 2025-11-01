def total_salary(path: str):
    sum = 0
    count = 0
    try: 
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                sum = sum + int(line.split(",")[1])
                count += 1
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")
    return sum, sum/count

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

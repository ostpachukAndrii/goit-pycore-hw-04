def get_cats_info(path):
    try:    
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",", 2)
                if len(parts) == 3:
                    cat_id, name, count = parts
                    yield {"id": cat_id, "name": name, "count": count}
                else:
                    print(f"Некоректний рядок: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка - бубомилка: {e}")

cats_info = list(get_cats_info("cats.txt"))
print(cats_info)
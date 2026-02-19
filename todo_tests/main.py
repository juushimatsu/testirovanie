import json 
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("not tasks")
        return
    for task in tasks:
        status = "+" if task.get("completed", False) else "-"
        print(f"{task["id"]}. {status} {task['description']}")
    print()

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(tasks):
    description = input("Описание задачи: ")

    if not description:
        print("Нет описания")
        return
    
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Задача {description} - добавлена")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Введите id задачи: "))
        task_to_remove = next((t for t in tasks if t["id"] == task_id), None)
        if task_to_remove:
            tasks.remove(task_to_remove)
            save_tasks(tasks)
            print(f"Задача {task_to_remove['description']} - удалена")
        else:
            print("Задача не найдена")

    except ValueError:
        print("id error")

def edit_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Введите id задачи: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            new_description = input(f"Новое описание (старое '{task['description']}')")
            if new_description:
                task["description"] = new_description
                save_tasks(tasks)
                print("Описание добавлено")
            else:
                print("Ошибка описания")
        else:
            print("Задача не найдена")
    except ValueError:
        print("id error")

def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Введите id задачи: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            task["completed"] = not task["completed"]
            status = "выполнена" if task["completed"] else "не выполнена"
            save_tasks(tasks)
            print(f"Задача {task['description']} - отмечена как {status}")
        else:
            print("Задача не найдена")
    except ValueError:
        print("id error")

def main():
    tasks = load_tasks()
    while True:
        print("1 - все задачи")
        print("2 - добавить")
        print("3 - редактировать")
        print("4 - отметить как выполненую")
        print("5 - удалить")
        print("6 - выход")
        choice = input("Действие: ").strip()

        if choice == "1":
            show_tasks(tasks)
        if choice == "2":
            add_task(tasks)
        if choice == "3":
            edit_task(tasks)
        if choice == "4":
            complete_task(tasks)
        if choice == "5":
            delete_task(tasks)
        elif choice == "6":
            break

        else:
            print("нет такого действия")

if __name__ == "__main__":
    main()
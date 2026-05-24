from queue import Queue


queue = Queue()

def generate_request(request):
    queue.put(request)
    print(f"Заявка '{request}' додана в чергу.")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Заявка '{request}' оброблена.")
    else:
        print("Немає заявок для обробки.")


def main():
    while True:
        print("\n1. Додати заявку")
        print("2. Обробити заявку")
        print("3. Вихід")
        choice = input("Виберіть дію: ")

        if choice == '1':
            request = input("Введіть заявку: ")
            generate_request(request)
        elif choice == '2':
            process_request()
        elif choice == '3':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
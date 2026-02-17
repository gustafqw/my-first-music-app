# Список, где будем хранить наши задачи
# enumerate = нумерация элементов списка
# index = индекс элемента в списке
# input = ввод данных
# append = добавление элемента в список
# len = длина списка

ru_music = [] # пустой список для хранения задач
eng_music = []


def show_all_music():
    all_music = ru_music + eng_music
    if not all_music:
        print ("\n--- All music list is emty: ---")
    else:
        print ("\n--- All list music: ---")
        for i, song in enumerate (all_music, start=1):
            print (f'{i}. {song}')


def show_ru_music ():
    if not ru_music:
        print("\n--- Russian music list is emty: ---")
    else:
        print ("\n--- list music Russian: ---")
        for index, task in enumerate (ru_music, start=1):
            print (f"{index}. {task}")
def show_eng_music ():
    if not eng_music:
        print ("\n--- English music list is emty: ---")
    else:
        print ("\n--- list music English: ---")
        for index, task in enumerate (eng_music, start=1):
            print (f"{index}. {task}")

def add_ru_music():
    new_ru_music = input ('Enter your music: ')
    ru_music.append (new_ru_music)
    print ('Your Russian music add!')
def add_eng_music():
    new_eng_music = input ('Enter your music: ')
    eng_music.append (new_eng_music)
    print ('Your English music add!')



def remove_ru_music():
    show_ru_music()
    if not ru_music: # Сначала проверяем, есть ли вообще что удалять
        return
    user_input = input('Enter number or name: ')
    if user_input.isdigit(): # ЕСЛИ ВВЕЛИ ЦИФРЫ
        num = int(user_input)
        if 1 <= num <= len(ru_music):
            removed = ru_music.pop(num - 1)
            print(f"Deleted by number: {removed}")
        else:
            print("Number not found.")
    else: # ЕСЛИ ВВЕЛИ ТЕКСТ (название)
        if user_input in ru_music:
            ru_music.remove(user_input)
            print(f"Removed by name: {user_input}")
        else:
            print("Song not found.")
def remove_eng_music():
    show_eng_music()
    if not eng_music: # Сначала проверяем, есть ли вообще что удалять
        return
    user_input = input('Enter number or name: ')
    if user_input.isdigit(): # ЕСЛИ ВВЕЛИ ЦИФРЫ
        num = int(user_input)
        if 1 <= num <= len(eng_music):
            removed = eng_music.pop(num - 1)
            print(f"Deleted by number: {removed}")
        else:
            print("Song not found.")
    else: # ЕСЛИ ВВЕЛИ ТЕКСТ (название)
        if user_input in eng_music:
            eng_music.remove(user_input)
            print(f"Removed by name: {user_input}")
        else:
            print("Song not found.")


def remove_music_smart():
    show_all_music() # Сначала показываем всё
    if not (ru_music + eng_music): # Если оба списка пусты
        return
    user_input = input('Enter the number or title to delete: ')
    # 1. Пытаемся удалить по номеру
    if user_input.isdigit():
        num = int(user_input)
        all_music = ru_music + eng_music # Склеиваем для поиска индекса
        if 1 <= num <= len(all_music):
            # Определяем, в какой список попал номер
            if num <= len(ru_music):
                removed = ru_music.pop(num - 1)
            else:
                removed = eng_music.pop(num - len(ru_music) - 1)
            print(f"Music '{removed}' delete for number.")
        else:
            print("Number not found.")
    # 2. Если ввели название (текст)
    else:
        if user_input in ru_music:
            ru_music.remove(user_input)
            print(f"'{user_input}' the song has been deleted from the Russian list.")
        elif user_input in eng_music:
            eng_music.remove(user_input)
            print(f"'{user_input}' the song has been deleted from the English list..")
        else:
            print("Song not found in any list.")



while True:
    print ('\nMenu:')
    print ('1. My favorite songs')
    print ('2. My favorite Russian songs.')
    print ('3. My favorite English songs.')
    print ('4. Add your favorite song on Russian.')
    print ('5. Add your favorite song on English.')
    print ('6. Delete favorite song.')
    print ('7. Exit')
    
    choice = input ("Choose an action (1-7): ")
    if choice == '1':
        show_all_music()
    elif choice == '2':
        show_ru_music()
    elif choice == '3':
        show_eng_music()
    elif choice == '4':
        add_ru_music()
    elif choice == '5':
        add_eng_music()
    elif choice == '6':
        remove_music_smart()
    elif choice == '7':
        print ('Buy!')
        break
    else:
        print ('Incorrect input, please try again.')
try:
    from main import first_var

    if first_var == 0:
        print("Решение верно :)")
    else:
        print(f"'first_var' имеет значение {first_var}, а должно 0!")
except:
    print("Не нахожу 'first_var'. Пррверьте название!")

input("Для выхода нажмите любую клавишу...")

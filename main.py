from tkinter import *
from tkinter import ttk
import math
import time
import fuzzywuzzy as fw
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pyautogui
data_neiro = [None, None, None, None, None, None, None, None]
while True:
    def start():
        gruz = input("введите название груза ( \n1) ящик \n2) автомобиль \n3) тяжеловес \n: ")
        print("создаю документ груза :" + str(gruz) + str(time.time()) + ".txt")
        for i in range(1):
            filename = str(gruz) + str(time.time()) + ".txt"
            if data_neiro[7] == None:
                data_safe = open(filename,"w")
            elif data_neiro[7] != None:
                data_safe = open(filename,"a")
        data_safe.write("length" + "," + "height" + "," + "width" + "," +  "massa" + ",""\n")
        data_1 = fuzz.ratio(gruz,"ящик")
        print(str(data_1) + " % сходства")
        if data_1 >= 50:
            print("Подобрана 4-х осная ж/д платформы \n"
                  "Характеристика 4-х осной ж/д платформы \n"
                  "Длина пола 13400 мм \n"
                  "Ширина пола 2870 мм \n"
                  "Масса тары 21 т \nВысота пола от УГР 1310 мм \n"
                  "Высота центра тяжести (ЦТ) от УГР 800 мм \n"
                  "База платформы 9720 мм")
            L = 13400
            W = 2870
            H = 1310
            def enter_the_length_of_the_load(enter_the_length_of_the_load):
                if 0 <= int(enter_the_length_of_the_load) <= 13400:
                    data_neiro[0] = 1
                elif int(enter_the_length_of_the_load) >= 13401:
                    data_neiro[0] = -1
                else:
                    data_neiro[0] = 0
                    print("неизвестный параметр")
                data_safe.write(enter_the_length_of_the_load + ",")
                if data_neiro[0] == 1:
                    print("Длина подходит")
                if data_neiro[0] == -1:
                    print("Длина не подходит")
            def enter_the_load_height(enter_the_load_height):
                if 0 <= int(enter_the_load_height) <= 1310:
                    data_neiro[1] = 1
                elif int(enter_the_load_height) >= 1311:
                    data_neiro[1] = -1
                else:
                    data_neiro[1] = 0
                    print("неизвестный параметр")
                data_safe.write(enter_the_load_height  + ",")
                if data_neiro[1] == 1:
                    print("Высота подходит")
                if data_neiro[1] == -1:
                    print("Высота не подходит")
            def enter_the_width_of_the_load(enter_the_width_of_the_load):
                if 0 <= int(enter_the_width_of_the_load) <= 2870:
                    data_neiro[2] = 1
                elif int(enter_the_width_of_the_load) >= 2871:
                    data_neiro[2] = -1
                else:
                    data_neiro[2] = 0
                    print("неизвестный параметр")
                data_safe.write(enter_the_width_of_the_load  + ",")
                if data_neiro[2] == 1:
                    print("Ширина подходит")
                if data_neiro[2] == -1:
                    print("Ширина не подходит")
            def enter_the_massa(enter_the_massa):
                if 0 <= int(enter_the_massa) <= 21000:
                    data_neiro[3] = 1
                elif int(enter_the_massa) >= 21000:
                    data_neiro[3] = -1
                else:
                    data_neiro[3] = 0
                    print("неизвестный параметр")
                data_safe.write(enter_the_massa  + ",")
                if data_neiro[3] == 1:
                    print("Масса подходит")
                if data_neiro[3] == -1:
                    print("Масса не подходит")


            enter_the_length_of_the_load(enter_the_length_of_the_load = input("введите длину груза, мм: "))
            enter_the_load_height(enter_the_load_height = input("введите высоту груза, мм: "))
            enter_the_width_of_the_load(enter_the_width_of_the_load = input("введите ширину груза, мм: "))
            enter_the_massa(enter_the_massa = input("введите массу груза, кг: "))

            

            # 1. Смещение ЦТ грузов в вагоне
            Displacement_of_the_CG_of_cargo = 0.5 * 13400
            for i in range(1):
                def calculate_center_of_mass(cargo_weights, cargo_positions):
                    total_weight = sum(cargo_weights)
                    center_of_mass = sum(
                        weight * position for weight, position in zip(cargo_weights, cargo_positions)) / total_weight
                    return center_of_mass

                def check_cargo_placement(center_of_mass, max_allowed_deviation):
                    if abs(center_of_mass) <= max_allowed_deviation:
                        return True
                    else:
                        return False

                def choose_railway_platform(cargo_weights, cargo_positions):
                    center_of_mass = calculate_center_of_mass(cargo_weights, cargo_positions)
                    max_allowed_deviation = 0.1  # Максимально допустимое отклонение
                    if check_cargo_placement(center_of_mass, max_allowed_deviation):
                        return "Platform A"
                    else:
                        return "Platform B"

                def visualize_cargo_placement(cargo_weights, cargo_positions):
                    plt.bar(cargo_positions, cargo_weights)
                    plt.xlabel("Position")
                    plt.ylabel("Weight")
                    plt.title("Cargo Placement")
                    plt.show()

                # Пример использования
                weights = [10, 20, 15, 25]  # Веса грузов
                positions = [1, 2, 3, 4]  # Позиции грузов
                center_mass = calculate_center_of_mass(weights, positions)
                print("Center of mass:", center_mass)

                if check_cargo_placement(center_mass, 0.1):
                    print("Cargo placement is within the allowed deviation.")
                else:
                    print("Cargo placement is not within the allowed deviation.")

                chosen_platform = choose_railway_platform(weights, positions)
                print("Chosen platform:", chosen_platform)

                visualize_cargo_placement(weights, positions)

                ####
                def calculate_windward_surface_area(L, W, H):
                    surface_area = 2 * (L * W + L * H + W * H)
                    return surface_area

                result = calculate_windward_surface_area(L, W, H)
                print("Наветренная поверхность груза:", result)

                #Высота центра проекции боковой поверхности груза

                def calculate_projection_height(shape, height):
                    if shape == "parallelepiped":
                        projection_height = height / 2
                    elif shape == "cylinder":
                        projection_height = height
                    else:
                        projection_height = None

                    return projection_height

                shape = "parallelepiped"  # Форма груза ("parallelepiped" - параллелепипед, "cylinder" - цилиндр)
                height = 10  # Высота груза в метрах

                projection_height = calculate_projection_height(shape, height)
                if projection_height is not None:
                    print("Высота центра проекции боковой поверхности: ", projection_height, "м")
                else:
                    print("Форма груза не распознана.")

                #h = (m1 * h1 + m2 * h2 + ... + mn * hn) / (m1 + m2 + ... + mn)
                """вычисления высоты центра тяжести:
                python
                m1 = 10  # масса первой части груза
                h1 = 2   # высота первой части над полом платформы
                m2 = 15  # масса второй части груза
                h2 = 3   # высота второй части над полом платформы
                h = (m1 * h1 + m2 * h2) / (m1 + m2)
                print(h)
                Формула для вычисления высоты центра тяжести платформы с грузом над УГР (уровнем грунтовой поверхности)
                def calculate_cg_height(masses, heights):
                    numerator = sum([m * h for m, h in zip(masses, heights)])
                    denominator = sum(masses)
                    cg_height = numerator / denominator
                    return cg_height
                    
                masses = [10, 15, 20]   # список масс частей груза
                heights = [2, 3, 4]    # список высот частей груза над УГР
                cg_height = calculate_cg_height(masses, heights)
                print(cg_height)
                """


            # 2. Общая высота ЦТ
            # 3. Устойчивость грузов с вагоном
            # 4. Расчет сил, действующих на Груз № 1
            # 5. Расчет сил, действующих на Груз № 2
            # 6. Расчет сил, действующих на Груз № 3
            # 7. Расчет сил, действующих на Груз № 4
            #### \8/. Устойчивость грузов в вагоне
            # 9. Устойчивость груза № 1 в вагоне
            #10. Устойчивость груза № 2 в вагоне
            #11. Устойчивость груза № 3 в вагоне
            #12. Устойчивость груза № 4 в вагоне
            #13. РАСЧЕТ КРЕПЛЕНИЯ ГРУЗА ОТ СМЕЩЕНИЙ В ПРОДОЛЬНОМ НАПРАВЛЕНИИ
            #14. Крепление груза 1
            #15. Крепление груза 2
            #16. Крепление груза 3
            #17. Крепление груза 4
            #18. РАСЧЕТ КРЕПЛЕНИЯ ГРУЗА ОТ СМЕЩЕНИЙ В ПОПЕРЕЧНОМ НАПРАВЛЕНИИ
            #19. Крепление груза 1
            #20. Крепление груза 2
            #21. Крепление груза 3
            #22. Крепление груза 4
            #23. РАСЧЕТ НА СЖАТИЕ И СМЯТИЕ ДЕРЕВЯННЫХ ЭЛЕМЕНТОВ КРЕПЛЕНИЯ
            #24. Расчет досок пола на смятие от груза 1
            #25. Расчет досок пола на смятие от груза 2
            #26. Расчет бруса поз. 1 на смятие от груза 1
            #27. Расчет брусков поз. 5 на смятие от груза 2


            def show_message():
                label["text"] = entry.get()  # получаем введенный текст

            root = Tk()
            root.title("Российские железные дороги")
            root.iconbitmap(default="railwaycarriage_4974.ico")

            width, height = pyautogui.size()
            root.geometry(str(width-400) + "x" + str(height-400))

            entry = ttk.Entry()
            entry.pack(anchor=NW, padx=6, pady=6)

            btn = ttk.Button(text="Click", command=show_message)
            btn.pack(anchor=NW, padx=6, pady=6)

            label = ttk.Label()
            label.pack(anchor=NW, padx=6, pady=6)

            #
            position = {"padx": 6, "pady": 6, "anchor": NW}

            languages = [
                {"name": "Ящик", "img": PhotoImage(file="./Рисунок1.png")},
                {"name": "Автомобиль", "img": PhotoImage(file="./1603631.png")},
                {"name": "Тяжеловес", "img": PhotoImage(file="./1603631.png")}
            ]

            lang = StringVar(value=languages[0]["name"])  # по умолчанию будет выбран элемент с value=python

            header = ttk.Label(textvariable=lang)
            header.pack(**position)

            for l in languages:
                btn = ttk.Radiobutton(value=l["name"], text=l["name"], variable=lang, image=l["img"], compound="top")
                btn.pack(**position)
            #


            root.mainloop()


            """fast_warning = input("Добавить груз ? да/нет: ")
            if fast_warning == "да":
                data_neiro[7] = 1
                
            if fast_warning == "нет":
                data_neiro[7] = 0"""

            print(data_neiro)
            print("в случае удачного добавления формирую платформы \nМожно будет добавлять нужные грузы в соответствии с данными о свободном месте")
            data_safe.close()



        else:
            print("неизвестный параметр")
            start()
    start()

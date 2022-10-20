# Консольная версия игры "Крестики-нолики"

# (срока 4) Создаётся множество возможных позиций для выбора хода
possible_positions = {"00", "01", "02", "10", "11", "12", "20", "21", "22"}

# (строки 8 - 10) Создаются пустые множества для записи всех ходов одного и второго игроков, а также пустое множество
# для записи ходов обоих игроков сразу
x_positions = set()
o_positions = set()
x_o_positions = set()

# (ст. 15 - 17) В виде словаря с целочисленными ключами и значениями в виде множеств создаётся каталог наборов всех
# возможных выигрышных комбинаций
winning_positions = {
    1: {"00", "01", "02"}, 2: {"10", "11", "12"}, 3: {"20", "21", "22"},
    4: {"00", "11", "22"}, 5: {"20", "11", "02"}, 6: {"00", "10", "20"},
    7: {"01", "11", "21"}, 8: {"02", "12", "22"}
}

# (ст. 21 - 24) В виде списков создаётся консольная имитация поля для игры в "Крестики-нолики"
ver = [0, 1, 2]
hor_0 = [0, "-", "-", "-"]
hor_1 = [1, "-", "-", "-"]
hor_2 = [2, "-", "-", "-"]


# (ст. 29 - 33) Создаётся функция, вызывающая главный экран с приветствием пользователя, игровым полем и указанием
# игрока, который должен сделать первый ход
def _starting_screen_():
    print()
    print("Welcome to Tic Tac Toe!")
    _show_grid_()
    print("First player to make move: 'x'")


# (ст. 37 - 43) Создаётся функция, которая при вызове отображает текущее состояние игрового поля
def _show_grid_():
    print()
    print(" ", *ver)
    print(*hor_0)
    print(*hor_1)
    print(*hor_2)
    print()


# (ст. 48 - 52) Создаётся функция, при вызове которой у игрока, играющего за "крестики", запрашивается ввод позиции для
# текущего хода, введенная строка "очищается" от пробелов и передаётся в качестве возвращаемого функцией значения
def _ask_x_():
    user_position = input("Enter the position for your 'x' (use 'space' key to divide the numbers): ")
    stripped_user_position = user_position.replace(" ", "")
    print()
    return stripped_user_position


# (ст. 57 - 61) Создаётся функция, при вызове которой у игрока, играющего за "нолики", запрашивается ввод позиции для
# текущего хода, введенная строка "очищается" от пробелов и передаётся в качестве возвращаемого функцией значения
def _ask_o_():
    user_position = input("Enter the position for your 'o' (use 'space' key to divide the numbers): ")
    stripped_user_position = user_position.replace(" ", "")
    print()
    return stripped_user_position


# (ст. 81 - 135) Создаётся основная функция для принятия и обработки введённого игроком за "крестики" значения позиции.
# - на вход функция принимает один параметр - введённую пользователем позицию;
# - множество всех сыгранных позиций игрока за "крестики" и множество всех выигрышных позиций объявляются глобальными
#   переменными;
# - первая проверка условным циклом - на корректно введённые координаты позиции для хода (через определение
#   принадлежности введённой позиции к множеству всех доступных позиций). При несоблюдении условия вызывается функция,
#   сообщающая об ошибке и инициирующая ввод координат позиции повторно;
# - вторая проверка условным циклом - на доступность введённой позиции. Если введённая позиция уже была зафиксирована
#   в множестве ходов "крестиков" или в множестве ходов "ноликов" - вызывается функция, сообщающая об ошибке и
#   инициирующая ввод координат позиции повторно;
# - далее идут условные операторы, реагирующие на введённые пользователем координаты;
# - если введённые координаты прошли все проверки, введёная позиция отображается в сетке, заменяя символом "крестик"
#   исходный символ, а также данная позиция заносится в множество всех позиций "крестиков" и в общее множество позиций
#   "крестиков" и "ноликов";
# - наконец, создаётся цикл, итерирующий все множества из словаря выигрышных комбинаций, внутри цикла условный оператор
#   проверяет, является ли выигрышная комбинация подмножеством всех зафиксированных на данный момент позиций "крестиков"
#   и в случае срабатывания данного условия - функция передает в качестве возвращаемого значения единицу.
def _get_answer_x_(position):
    global x_positions
    global winning_positions
    if position not in possible_positions:
        _reject_invalid_position_x_()
    elif position in x_positions or position in o_positions:
        _reject_occupied_position_x_()
    elif position == "00":
        hor_0.pop(1)
        hor_0.insert(1, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "01":
        hor_0.pop(2)
        hor_0.insert(2, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "02":
        hor_0.pop(3)
        hor_0.insert(3, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "10":
        hor_1.pop(1)
        hor_1.insert(1, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "11":
        hor_1.pop(2)
        hor_1.insert(2, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "12":
        hor_1.pop(3)
        hor_1.insert(3, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "20":
        hor_2.pop(1)
        hor_2.insert(1, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "21":
        hor_2.pop(2)
        hor_2.insert(2, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    elif position == "22":
        hor_2.pop(3)
        hor_2.insert(3, "x")
        x_positions.add(position)
        x_o_positions.add(position)
    for i in winning_positions:
        if winning_positions[i].issubset(x_positions):
            return 1


# (ст. 140 - 194) См. описание функции _get_answer_x_ выше. Функция _get_answer_o_ работает аналогично, только относится
# к пользователю, играющему за "нолики"
def _get_answer_o_(position):
    global o_positions
    global winning_positions
    if position not in possible_positions:
        _reject_invalid_position_o_()
    elif position in x_positions or position in o_positions:
        _reject_occupied_position_o_()
    elif position == "00":
        hor_0.pop(1)
        hor_0.insert(1, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "01":
        hor_0.pop(2)
        hor_0.insert(2, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "02":
        hor_0.pop(3)
        hor_0.insert(3, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "10":
        hor_1.pop(1)
        hor_1.insert(1, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "11":
        hor_1.pop(2)
        hor_1.insert(2, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "12":
        hor_1.pop(3)
        hor_1.insert(3, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "20":
        hor_2.pop(1)
        hor_2.insert(1, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "21":
        hor_2.pop(2)
        hor_2.insert(2, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    elif position == "22":
        hor_2.pop(3)
        hor_2.insert(3, "o")
        o_positions.add(position)
        x_o_positions.add(position)
    for i in winning_positions:
        if winning_positions[i].issubset(o_positions):
            return 1


# ( ст. 200 - 203) Создание функции, вызываемой в случае ввода пользователем некорректной позиции. Функция отображает
# сообщение об ошибке и заного инициирует ввод пользователем координат выбранной позиции для хода
# (для игрока за "крестики")
def _reject_invalid_position_x_():
    print("Please, enter a valid position coordinates!")
    print()
    return _get_answer_x_(_ask_x_())


# ( ст. 209 - 212) Создание функции, вызываемой в случае ввода пользователем некорректной позиции. Функция отображает
# сообщение об ошибке и заного инициирует ввод пользователем координат выбранной позиции для хода
# (для игрока за "нолики")
def _reject_invalid_position_o_():
    print("Please, enter a valid position coordinates!")
    print()
    return _get_answer_o_(_ask_o_())


# ( ст. 218 - 221) Создание функции, вызываемой в случае ввода пользователем уже занятой позиции. Функция отображает
# сообщение об ошибке и заного инициирует ввод пользователем координат выбранной позиции для хода
# (для игрока за "крестики")
def _reject_occupied_position_x_():
    print("This position has already been occupied! Please, choose another position!")
    print()
    return _get_answer_x_(_ask_x_())


# ( ст. 227 - 230) Создание функции, вызываемой в случае ввода пользователем уже занятой позиции. Функция отображает
# сообщение об ошибке и заного инициирует ввод пользователем координат выбранной позиции для хода
# (для игрока за "нолики")
def _reject_occupied_position_o_():
    print("This position has already been occupied! Please, choose another position!")
    print()
    return _get_answer_o_(_ask_o_())


# (ст. 234) Начало основного скрипта. Вызов функции стартового экрана
_starting_screen_()

# (ст. 239 - 264) Создание цикла, итерирующего очередь последовательных ходов игроков. Выполняется до тех пор, пока не
# будет выполнено одно из условий: либо один из игроков собирает выигрышные позиции (выводится сообщение о победителе
# и предложение начать игру заного), либо наступает ничья (выводится сообщение об этом и предложение начать игру заного)
while True:

    x = _get_answer_x_(_ask_x_())
    if x == 1:
        _show_grid_()
        print("  'x' is a winner!")
        print("Press 'Shift' + 'F10' to start over")
        break
    if x_o_positions == possible_positions:
        print("It's a tie!")
        print("Press 'Shift' + 'F10' to start over")
        break
    _show_grid_()

    o = _get_answer_o_(_ask_o_())
    if o == 1:
        _show_grid_()
        print("  'o' is a winner!")
        print("Press 'Shift' + 'F10' to start over")
        break
    if x_o_positions == possible_positions:
        _show_grid_()
        print("It's a tie!")
        print("Press 'Shift' + 'F10' to start over")
        break
    _show_grid_()

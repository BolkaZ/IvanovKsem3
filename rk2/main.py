    from operator import itemgetter

    class HardDrive:
        """Hard Drive"""
        def __init__(self, id, model, capacity_gb, computer_id):
            self.id = id
            self.model = model
            self.capacity_gb = capacity_gb
            self.computer_id = computer_id

    class Computer:
        """Computer"""
        def __init__(self, id, name, type, hard_drive_id, cost):
            self.id = id
            self.name = name
            self.type = type
            self.hard_drive_id = hard_drive_id
            self.cost = cost

    class ComputerHardDrive:
        """'Computers with Hard Drives' for implementing many-to-many relationship"""
        def __init__(self, computer_id, hard_drive_id):
            self.computer_id = computer_id
            self.hard_drive_id = hard_drive_id

    # Hard Drives
    hard_drives = [
        HardDrive(1, 'Seagate 1TB', 1000, 1),
        HardDrive(2, 'Western Digital 2TB', 2000, 2),
        HardDrive(3, 'Samsung 500GB', 500, 2),
    ]

    # Computers
    computers = [
        Computer(1, 'Computer 1', 'Desktop', 1, 800),
        Computer(2, 'Laptop 1', 'Laptop', 2, 1200),
        Computer(3, 'Computer 2', 'Desktop', 3, 700),
    ]

    computer_hard_drives = [
        ComputerHardDrive(1, 1),
        ComputerHardDrive(2, 2),
        ComputerHardDrive(3, 3),
        ComputerHardDrive(3, 2),
    ]

    # используется для сортировки
    from operator import itemgetter



    def a1_solution(one_to_many):
        res_a1 = sorted(one_to_many, key=itemgetter(2))
        return res_a1


    def a2_solution(one_to_many):
        res_a2_unsorted = []
        # Перебираем все жесткие диски
        for h in hard_drives:
            # Список компьютеров с данным жестким диском
            h_comps = list(filter(lambda i: i[0] == h.model, one_to_many))
            # Если есть компьютеры с этим жестким диском
            if len(h_comps) > 0:
                # Сумма объемов жестких дисков компьютеров
                h_capacities = [capacity for _, capacity, _ in h_comps]
                # Сумма объемов жестких дисков компьютера
                h_capacities_sum = sum(h_capacities)
                res_a2_unsorted.append((h.model, h_capacities_sum))

        # Сортировка по сумме объемов
        res_a2 = sorted(res_a2_unsorted, key=itemgetter(1), reverse=True)
        return res_a2



    def a3_solution(many_to_many):
        res_a3 = {}
        # Перебираем все компьютеры
        for c in computers:
            if 'Com' in c.name:
                # Список жестких дисков компьютера
                c_drives = list(filter(lambda ch: ch.computer_id == c.id, computer_hard_drives))
                # Только модели жестких дисков
                c_drives_models = [hard_drive.model for hard_drive in hard_drives if hard_drive.id in [drive.hard_drive_id for drive in c_drives]]
                # Добавляем результат в словарь
                # ключ - компьютер, значение - список моделей жестких дисков
                res_a3[c.name] = c_drives_models
        return res_a3





    def main():
        """Основная функция"""

        # Соединение данных один-ко-многим
        one_to_many = [(h.model, h.capacity_gb, c.name)
            for c in computers
            for h in hard_drives
            if h.computer_id == c.id]

        # Соединение данных многие-ко-многим
        many_to_many_temp = [(c.name, ch.computer_id, ch.hard_drive_id)
            for c in computers
            for ch in computer_hard_drives
            if c.id == ch.computer_id]

        many_to_many =  [(h.model, h.capacity_gb, comp_name)
            for comp_name, comp_id, hd_id in many_to_many_temp
            for h in hard_drives if h.id == hd_id]

        print('Задание А1')
        print(a1_solution(one_to_many))

        print('\nЗадание А2')
        print(a2_solution(one_to_many))

        print('\nЗадание А3')
        print(a3_solution(many_to_many))


    if __name__ == '__main__':
        main()





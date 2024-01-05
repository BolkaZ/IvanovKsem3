import unittest
from main import *

class TestRK2(unittest.TestCase):
    # Жесткие диски
    hard_drives = [
        HardDrive(1, 'Seagate 1TB', 1000, 1),
        HardDrive(2, 'Western Digital 2TB', 2000, 2),
        HardDrive(3, 'Samsung 500GB', 500, 2),
    ]

    # Компьютеры
    computers = [
        Computer(1, 'Computer 1', 'Desktop', 1, 800),
        Computer(2, 'Laptop 1', 'Laptop', 2, 1200),
        Computer(3, 'Computer 2', 'Desktop', 3, 700),
    ]

    # Связь многие-ко-многим
    computer_hard_drives = [
        ComputerHardDrive(1, 1),
        ComputerHardDrive(2, 2),
        ComputerHardDrive(3, 3),
        ComputerHardDrive(3, 2),
    ]

    def test_A1(self):
        one_to_many = [(h.model, h.capacity_gb, c.name)
                       for c in self.computers
                       for h in self.hard_drives
                       if h.computer_id == c.id]
        self.assertEqual(a1_solution(one_to_many),
                         [('Seagate 1TB', 1000, 'Computer 1'), ('Western Digital 2TB', 2000, 'Laptop 1'),
                          ('Samsung 500GB', 500, 'Laptop 1')])

    def test_A2(self):
        one_to_many = [(h.model, h.capacity_gb, c.name)
                       for c in self.computers
                       for h in self.hard_drives
                       if h.computer_id == c.id]
        expected_result = [('Western Digital 2TB', 2000), ('Seagate 1TB', 1000), ('Samsung 500GB', 500)]
        actual_result = a2_solution(one_to_many)
        self.assertCountEqual(actual_result, expected_result)

    def test_A3(self):
        many_to_many_temp = [(c.name, ch.computer_id, ch.hard_drive_id)
                             for c in self.computers
                             for ch in self.computer_hard_drives
                             if c.id == ch.computer_id]

        many_to_many = [(h.model, h.capacity_gb, comp_name)
                        for comp_name, comp_id, hd_id in many_to_many_temp
                        for h in self.hard_drives if h.id == hd_id]

        actual_result = a3_solution(many_to_many)
        expected_result = {
            'Computer 1': ['Seagate 1TB'],
            'Computer 2': ['Western Digital 2TB', 'Samsung 500GB']
        }

        # Сортируем значения в словарях перед сравнением
        for key in actual_result:
            actual_result[key] = sorted(actual_result[key])
        for key in expected_result:
            expected_result[key] = sorted(expected_result[key])

        print("Фактический результат:", actual_result)
        print("Ожидаемый результат:", expected_result)

        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()

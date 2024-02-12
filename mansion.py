import random


class Mansion:
    def __init__(self):
        self.current_room_alert = 'Вы проснулись в неизвестном вам месте. Попробуйте отсюда выбраться'
        self.rooms = {
            'Балкон': {'Север': None, 'Восток': None, 'Юг': 'Холл', 'Запад': None},
            'Спальня': {'Север': None, 'Восток': 'Холл', 'Юг': 'Подземелье', 'Запад': None},
            'Холл': {'Север': 'Балкон', 'Восток': 'Кухня', 'Юг': 'Коридор', 'Запад': 'Спальня'},
            'Кухня': {'Север': None, 'Восток': None, 'Юг': 'Оружейная', 'Запад': 'Холл'},
            'Подземелье': {'Север': 'Спальня', 'Восток': 'Коридор', 'Юг': None, 'Запад': None},
            'Коридор': {'Север': 'Холл', 'Восток': 'Оружейная', 'Юг': None, 'Запад': 'Подземелье'},
            'Оружейная': {'Север': 'Кухня', 'Восток': None, 'Юг': None, 'Запад': 'Коридор'}
        }
        self.current_room = random.choice(list(self.rooms.keys()))

    def move_to(self, direction):
        if self.rooms[self.current_room][direction] is not None:
            self.current_room = self.rooms[self.current_room][direction]
            self.current_room_alert = f'Вы переместились в {self.current_room}.'
            # print(self.current_room_alert)
            if self.current_room == 'Балкон':
                self.current_room_alert = 'Ура, вы нашли выход! Игра завершена.'
                # print(self.current_room_alert)
        else:
            self.current_room_alert = 'Нельзя пойти в этом направлении или комната не существует.'
            # print(self.current_room_alert)
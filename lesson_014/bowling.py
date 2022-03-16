class GetScore:

    def __init__(self, game_result, new_rules=False):
        self.valid_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', 'X', '-']
        self.index_strike = 0
        self.points = 0
        self.game_result = game_result.replace('-', '0')
        self.rules = new_rules
        self.frames = []

    def run(self):
        game_result = self.game_result.replace('X', 'X-')
        self.frames = [game_result[frame:frame + 2] for frame in range(0, len(game_result), 2)]
        if self.rules:
            self.calculate_main_points_new_rules()
            self.calculate_extra_points()
            return self.points
        else:
            self.calculate_main_points()
            return self.points

    def calculate_main_points(self):
        print('Считаем по старым правилам:', self.frames)
        for frame in self.frames:
            self.check_error(frame, self.frames)
            if 'X' in frame:
                self.points += 20
            elif '/' in frame:
                if frame[1] == '/':
                    self.points += 15
            elif frame.isdigit():
                frame = str(frame)
                sum_frame = sum(map(int, frame))
                if sum_frame <= 9:
                    self.points += sum_frame
                else:
                    raise Exception('Количество очков в фрейме не может превышать 9 (либо spare, либо strike)')
            else:
                for frame_with_zero in frame:
                    if frame_with_zero.isdigit():
                        self.points += int(frame_with_zero)

    def calculate_main_points_new_rules(self):
        print('Считаем по новым правилам:', self.frames)
        for frame in self.frames:
            self.check_error(frame, self.frames)
            if 'X' in frame:
                self.points += 10
            elif '/' in frame:
                self.points += 10
            else:
                sum_frame = sum(map(int, frame))
                if sum_frame <= 9:
                    self.points += sum_frame
                else:
                    raise Exception('Количество очков в фрейме не может превышать 9 (либо spare, либо strike)')

    def calculate_extra_points(self):
        for point in self.game_result:
            self.index_strike += 1
            if point == 'X':
                for bonus_points in self.game_result[self.index_strike: self.index_strike + 2]:
                    first_point = self.game_result[self.index_strike]
                    if 'X' in bonus_points:
                        self.points += 10
                    elif '/' in bonus_points:
                        self.points += 10 - int(first_point)
                    else:
                        self.points += int(bonus_points)
            elif point == '/':
                for bonus_points in self.game_result[self.index_strike: self.index_strike + 1]:
                    if 'X' in bonus_points:
                        self.points += 10
                    else:
                        self.points += int(bonus_points)

    def check_error(self, frame, frames):
        for point in frame:
            if point not in self.valid_symbols:
                raise Exception('Этот символ использовать нельзя: ' + point)
        if len(frame) != 2:
            raise Exception('В фрейме должно быть два броска, либо страйк')
        if len(frames) != 10:
            raise ValueError('Количество фреймов должно быть равно 10')
        if frame[0] == '/':
            raise Exception('Spare не может быть выбит в начале фрейма')
        if frame[1] == 'X':
            raise Exception('Strike выбивается только первым броском')

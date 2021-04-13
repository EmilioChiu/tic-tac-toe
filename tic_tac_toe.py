
class TicTacToe:
    def __init__(self, collection, symbol):
        self.collection = collection
        self.symbol = symbol

    def horizontal(self):
        start = 0
        for num in range(3):
            end = start + 3
            win_collection = []
            for n in self.collection[start: end]:
                if n == self.symbol:
                    win_collection.append(n)
                    if len(win_collection) == 3:
                        return True
            start += 3
        return False

    def vertical(self):
        for num in range(3):
            start = num
            end = start + 7
            win_collection = []
            for n in self.collection[start: end: 3]:
                if n == self.symbol:
                    win_collection.append(n)
                    if len(win_collection) == 3:
                        return True
        return False

    def right_diagonal(self):
        win_collection = []
        for n in self.collection[::4]:
            if n == self.symbol:
                win_collection.append(n)
                if len(win_collection) == 3:
                    return True
        return False

    def left_diagonal(self):
        start = 2
        end = start + 5
        win_collection = []
        for n in self.collection[start: end: 2]:
            if n == self.symbol:
                win_collection.append(n)
                if len(win_collection) == 3:
                    return True
        return False

    def check(self):
        if self.horizontal() or self.vertical() or self.left_diagonal() or self.right_diagonal():
            return True
        return False






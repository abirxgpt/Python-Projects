# class Game:
#     def __init__(self):
#         self.players = 4
#
#     def rules(self):
#         print("Do not Cheat.")
#
# class Ludo(Game):
#     def __init__(self):
#         super().__init__()
#     def colours(self):
#         print("4 colours required!")
#
# ludo_game = Ludo()
# ludo_game.colours()
# ludo_game.rules()
# print(ludo_game.players)



class Game:
    def __init__(self):
        self.players = 4

    def rules(self):
        print("Do not Cheat.")

class Ludo(Game):
    def __init__(self):
        super().__init__()

    def rules(self):
        super().rules()
        print("Complete Whole circle with all 4 pawns")
    def colours(self):
        print("4 colours required!")


ludo_game = Ludo()
ludo_game.rules()

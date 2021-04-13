from tic_tac_toe import TicTacToe


def same_symbol(p1_symbol):
    p2_symbol = input("choose your symbol player 2 (ex. 0 or x): ")
    if p1_symbol == p2_symbol:
        while True:
            p2_symbol = input("the symbol is already selected by the player one, choose another symbol: ")
            if p2_symbol != p1_symbol:
                print("now we can play")
                return p2_symbol
    return p2_symbol


def box_selected(p1_symbol, p2_symbol, collection):
    election = int(input(
        "to play choose the box with the number (ex. the center box would be the number 5)"
    ))
    if p2_symbol == collection[election - 1] or p1_symbol == collection[election - 1]:
        print("choose another box this is already selected")
        while True:
            election = int(input(
                "to play choose the box with the number (ex. the center box would be the number 5)"
            ))
            if player_2_symbol != collection[election - 1] or p1_symbol == collection[election - 1]:
                print("is not so hard, you see?")
                collection[election - 1] = p1_symbol
                return
    collection[election - 1] = p1_symbol
    return


play = input("wanna play? y/n: ")
if play == "y":
    tic_tac_toe = ["" for n in range(9)]
    players = input("1 or 2 players? ")

    if players == "2":
        print("lets play!")

        player_1_symbol = input("choose your symbol player 1 (ex. 0 or x): ")
        player_2_symbol = same_symbol(player_1_symbol)

        player_1 = TicTacToe(collection=tic_tac_toe, symbol=player_1_symbol)
        player_2 = TicTacToe(collection=tic_tac_toe, symbol=player_2_symbol)

        keep_play = True
        while keep_play:
            if "" in tic_tac_toe:
                print(f"""
                       {tic_tac_toe[0]}  |  {tic_tac_toe[1]}  |  {tic_tac_toe[2]}
                        ----------
                       {tic_tac_toe[3]}  |  {tic_tac_toe[4]}  |  {tic_tac_toe[5]}
                        ----------
                       {tic_tac_toe[6]}  |  {tic_tac_toe[7]}  |  {tic_tac_toe[8]}
                       """)

                print("turn of player 1")
                box_selected(p1_symbol=player_1_symbol, p2_symbol=player_2_symbol, collection=tic_tac_toe)

                print(f"""
                       {tic_tac_toe[0]}  |  {tic_tac_toe[1]}  |  {tic_tac_toe[2]}
                        ----------
                       {tic_tac_toe[3]}  |  {tic_tac_toe[4]}  |  {tic_tac_toe[5]}
                        ----------
                       {tic_tac_toe[6]}  |  {tic_tac_toe[7]}  |  {tic_tac_toe[8]}
                       """)

                if player_1.check():
                    print("player 1 win")
                    keep_play = False

                else:
                    print("turn of player 2")
                    box_selected(p1_symbol=player_2_symbol, p2_symbol=player_1_symbol, collection=tic_tac_toe)
                    print(f"""
                           {tic_tac_toe[0]}  |  {tic_tac_toe[1]}  |  {tic_tac_toe[2]}
                            ----------
                           {tic_tac_toe[3]}  |  {tic_tac_toe[4]}  |  {tic_tac_toe[5]}
                            ----------
                           {tic_tac_toe[6]}  |  {tic_tac_toe[7]}  |  {tic_tac_toe[8]}
                           """)

                    if player_2.check():
                        print("player 2 win")
                        keep_play = False

        if "" not in tic_tac_toe:
            print("draw")


def hangman(word):
    wrong = 0
    stages = ["",
              "_________          ",
              "|                  ",
              "|        |         ",
              "|        0         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "
              ]
    rletters = list(word)
#    print(rletters)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "文字を予想してね"
        char = input(msg)
        if char in rletters:
            print(char)
            print("正解を含んでます")
            cind = rletters.index(char)
            print(cind)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You're winner!!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! 正解は {}".format(word))

hangman("cat")

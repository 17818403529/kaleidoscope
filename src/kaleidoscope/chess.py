from copy import deepcopy


class Chess:
    def __init__(self, fen):
        self.fen = fen

    def gen_fen(self):
        pass

    def split_fen(self):
        fen = self.fen.split()
        self.position = fen[0]
        self.turn = fen[1]
        self.castling = fen[2]
        self.passer = fen[3]

    def conv_fen(self):
        self.split_fen()
        self.board = {"w": {}, "b": {}, "blank": [], "k": "", "K": ""}
        for row in "12345678":
            for col in "abcdefgh":
                self.board["blank"].append(col + row)

        row, col = 7, 0
        for i in self.position:
            if i == "/":
                row -= 1
                col = 0
            elif i in "1234567":
                col = (col + int(i)) % 8
            else:
                pos = "abcdefgh"[col] + "12345678"[row]
                if i in "rnbqp":
                    self.board["b"][pos] = i
                elif i in "RNBQP":
                    self.board["w"][pos] = i
                else:
                    self.board[i] = pos

                self.board["blank"].remove(pos)
                col = col + 1

    def cal_des(self, pos, vec, steps):
        row = "abcdefgh".index(pos[0]) + steps * vec[0]
        col = "12345678".index(pos[1]) + steps * vec[1]
        if col in range(0, 8) and row in range(0, 8):
            return "abcdefgh"[row] + "12345678"[col]
        else:
            return None

    def show_legal_moves(self, board):
        self.conv_fen()
        op = "b" if self.turn == "w" else "w"
        legal_moves = []

        for pos in board[self.turn].keys():
            piece = board[self.turn][pos]

            if piece in "RrBbQqKk":
                if piece in "Rr":
                    fea_vec = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                elif piece in "Bb":
                    fea_vec = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
                else:
                    fea_vec = [(1, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (1, 0), (0, -1), (0, 1)]

                if piece in "Kk":
                    fea_steps = 2
                else:
                    fea_steps = 8

                for vec in fea_vec:
                    for steps in range(1, fea_steps):
                        des = self.cal_des(pos, vec, steps)
                        if not des:
                            # out of board
                            break
                        else:
                            if des in board["blank"]:
                                legal_moves.append(piece.upper() + des)
                            elif des in board[self.turn]:
                                break
                            else:
                                legal_moves.append(piece.upper() + "x" + des)
                                break

            elif piece in "Nn":
                row, col = "abcdefgh".index(pos[0]), "12345678".index(pos[1])
                for des in [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1), (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]:
                    if des[0] in range(0, 8) and des[1] in range(0, 8):
                        _des = "abcdefgh"[des[0]] + "12345678"[des[1]]
                        if _des in board["blank"]:
                            legal_moves.append("N" + _des)
                        elif _des in board[op]:
                            legal_moves.append("Nx" + _des)

            else:
                if piece == "P":
                    for row in [-1, 1]:
                        des = self.cal_des(pos, (row, 1), 1)
                        if des:
                            if des[1] == "8":
                                pass
                            else:
                                if des in board[op]:
                                    legal_moves.append(pos[0] + "x" + des)

                    des = self.cal_des(pos, (0, 1), 1)

                    if not des:
                        if des[1] == "8":
                            pass
                        else:
                            if des in board["blank"]:
                                legal_moves.append(des)

                    if pos[1] == 1:
                        middle = self.cal_des(pos, (1, 0), 1)
                        if middle in board["blank"]:
                            des = self.cal_des(middle, (1, 0), 1)
                            if des in board["blank"]:
                                legal_moves.append(des)

                else:
                    for row in [-1, 1]:
                        des = self.cal_des(pos, (row, 1), 1)
                        if des:
                            if des[1] == "8":
                                pass
                            else:
                                if des in board[op]:
                                    legal_moves.append(pos[0] + "x" + des)

                    des = self.cal_des(pos, (0, 1), 1)

                    if not des:
                        if des[1] == "8":
                            pass
                        else:
                            if des in board["blank"]:
                                legal_moves.append(des)

                    if pos[1] == 1:
                        middle = self.cal_des(pos, (1, 0), 1)
                        if middle in board["blank"]:
                            des = self.cal_des(middle, (1, 0), 1)
                            if des in board["blank"]:
                                legal_moves.append(des)

        king_pos = board["K"] if self.turn == "b" else board["k"]
        print(king_pos)
        _legal_moves = []
        for i in legal_moves:
            if king_pos in i:
                _legal_moves.append(i + "+")
            else:
                _legal_moves.append(i)

        return _legal_moves

    def check(self, side, pos, des):
        board = deepcopy(self.board)


fen = "r1bq3r/6pp/1p2k3/1NbpBp1n/pn1P4/PP2PNP1/5PKP/2RQ1R2 w - - 0 12"
c = Chess(fen)

# print(c.show_legal_moves("w", "a3"))
c.conv_fen()
# print(c.board)
print(c.show_legal_moves(c.board))
# print(len(c.show_legal_moves()))
# print(c.board)
# print(c.white, "\n", c.black, "\n", c.blank)

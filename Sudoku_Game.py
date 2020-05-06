import tkinter
from tkinter import ttk, Canvas


class Sudoku:
    @staticmethod
    def character_limit(entry_text):
        try:
            if len(entry_text.get()) > 0 or not isinstance(entry_text.get(), int):
                entry_text.set(entry_text.get()[-1])
        except IndexError:
            pass

    @staticmethod
    def starter(b, n, e):
        for i in range(len(b)):
            b[i].set(n[i])
            e[i].configure(state='disabled')

    @staticmethod
    def valid_solution(*args):
        board = [[], [], [], [], [], [], [], [], []]
        for i, k in enumerate(args):
            k = k.get()
            if k == "":
                k = 0
            board[i // 9].append(int(k))
        print(board)

        vertical = [[], [], [], [], [], [], [], [], []]
        box = [[], [], [], [], [], [], [], [], []]
        for i in board:
            for k in i:
                if i.count(k) != 1:
                    return False
                vertical[i.index(k)].append(k)

        for i in range(0, 10, 3):
            for k in board[i - 3:i]:
                box[i - 3].extend(k[0:3])
                box[i - 2].extend(k[3:6])
                box[i - 1].extend(k[6:])

        for i in vertical:
            for k in i:
                if i.count(k) != 1:
                    return False

        for i in box:
            for k in i:
                if i.count(k) != 1:
                    return False

        return True

    def __init__(self, root):
        self.root = root
        self.root.geometry("462x505+550+250")
        self.root.title("Sudoku")
        self.root.resizable(False, False)
        self.canvas = Canvas(self.root, width=550, height=550, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 555, 555, 0,
                                     outline="#05f", fill="#000000")
        a1t = tkinter.StringVar()
        a2t = tkinter.StringVar()
        a3t = tkinter.StringVar()
        a4t = tkinter.StringVar()
        a5t = tkinter.StringVar()
        a6t = tkinter.StringVar()
        a7t = tkinter.StringVar()
        a8t = tkinter.StringVar()
        a9t = tkinter.StringVar()
        b1t = tkinter.StringVar()
        b2t = tkinter.StringVar()
        b3t = tkinter.StringVar()
        b4t = tkinter.StringVar()
        b5t = tkinter.StringVar()
        b6t = tkinter.StringVar()
        b7t = tkinter.StringVar()
        b8t = tkinter.StringVar()
        b9t = tkinter.StringVar()
        c1t = tkinter.StringVar()
        c2t = tkinter.StringVar()
        c3t = tkinter.StringVar()
        c4t = tkinter.StringVar()
        c5t = tkinter.StringVar()
        c6t = tkinter.StringVar()
        c7t = tkinter.StringVar()
        c8t = tkinter.StringVar()
        c9t = tkinter.StringVar()
        d1t = tkinter.StringVar()
        d2t = tkinter.StringVar()
        d3t = tkinter.StringVar()
        d4t = tkinter.StringVar()
        d5t = tkinter.StringVar()
        d6t = tkinter.StringVar()
        d7t = tkinter.StringVar()
        d8t = tkinter.StringVar()
        d9t = tkinter.StringVar()
        e1t = tkinter.StringVar()
        e2t = tkinter.StringVar()
        e3t = tkinter.StringVar()
        e4t = tkinter.StringVar()
        e5t = tkinter.StringVar()
        e6t = tkinter.StringVar()
        e7t = tkinter.StringVar()
        e8t = tkinter.StringVar()
        e9t = tkinter.StringVar()
        f1t = tkinter.StringVar()
        f2t = tkinter.StringVar()
        f3t = tkinter.StringVar()
        f4t = tkinter.StringVar()
        f5t = tkinter.StringVar()
        f6t = tkinter.StringVar()
        f7t = tkinter.StringVar()
        f8t = tkinter.StringVar()
        f9t = tkinter.StringVar()
        g1t = tkinter.StringVar()
        g2t = tkinter.StringVar()
        g3t = tkinter.StringVar()
        g4t = tkinter.StringVar()
        g5t = tkinter.StringVar()
        g6t = tkinter.StringVar()
        g7t = tkinter.StringVar()
        g8t = tkinter.StringVar()
        g9t = tkinter.StringVar()
        h1t = tkinter.StringVar()
        h2t = tkinter.StringVar()
        h3t = tkinter.StringVar()
        h4t = tkinter.StringVar()
        h5t = tkinter.StringVar()
        h6t = tkinter.StringVar()
        h7t = tkinter.StringVar()
        h8t = tkinter.StringVar()
        h9t = tkinter.StringVar()
        i1t = tkinter.StringVar()
        i2t = tkinter.StringVar()
        i3t = tkinter.StringVar()
        i4t = tkinter.StringVar()
        i5t = tkinter.StringVar()
        i6t = tkinter.StringVar()
        i7t = tkinter.StringVar()
        i8t = tkinter.StringVar()
        i9t = tkinter.StringVar()

        a1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a1t)
        a2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a2t)
        a3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a3t)
        a4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a4t)
        a5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a5t)
        a6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a6t)
        a7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a7t)
        a8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a8t)
        a9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=a9t)
        b1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b1t)
        b2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b2t)
        b3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b3t)
        b4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b4t)
        b5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b5t)
        b6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b6t)
        b7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b7t)
        b8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b8t)
        b9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=b9t)
        c1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c1t)
        c2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c2t)
        c3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c3t)
        c4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c4t)
        c5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c5t)
        c6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c6t)
        c7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c7t)
        c8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c8t)
        c9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=c9t)

        d1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d1t)
        d2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d2t)
        d3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d3t)
        d4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d4t)
        d5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d5t)
        d6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d6t)
        d7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d7t)
        d8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d8t)
        d9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=d9t)
        e1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e1t)
        e2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e2t)
        e3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e3t)
        e4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e4t)
        e5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e5t)
        e6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e6t)
        e7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e7t)
        e8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e8t)
        e9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=e9t)
        f1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f1t)
        f2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f2t)
        f3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f3t)
        f4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f4t)
        f5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f5t)
        f6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f6t)
        f7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f7t)
        f8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f8t)
        f9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=f9t)

        g1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g1t)
        g2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g2t)
        g3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g3t)
        g4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g4t)
        g5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g5t)
        g6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g6t)
        g7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g7t)
        g8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g8t)
        g9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=g9t)
        h1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h1t)
        h2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h2t)
        h3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h3t)
        h4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h4t)
        h5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h5t)
        h6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h6t)
        h7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h7t)
        h8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h8t)
        h9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=h9t)
        i1 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i1t)
        i2 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i2t)
        i3 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i3t)
        i4 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i4t)
        i5 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i5t)
        i6 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i6t)
        i7 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i7t)
        i8 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i8t)
        i9 = ttk.Entry(self.canvas, justify='center', font=('Boulder', 18, 'bold'), textvariable=i9t)

        a1.place(x=3, y=3, width=50, height=50)
        a2.place(x=53, y=3, width=50, height=50)
        a3.place(x=103, y=3, width=50, height=50)
        a4.place(x=156, y=3, width=50, height=50)
        a5.place(x=206, y=3, width=50, height=50)
        a6.place(x=256, y=3, width=50, height=50)
        a7.place(x=309, y=3, width=50, height=50)
        a8.place(x=359, y=3, width=50, height=50)
        a9.place(x=409, y=3, width=50, height=50)
        b1.place(x=3, y=53, width=50, height=50)
        b2.place(x=53, y=53, width=50, height=50)
        b3.place(x=103, y=53, width=50, height=50)
        b4.place(x=156, y=53, width=50, height=50)
        b5.place(x=206, y=53, width=50, height=50)
        b6.place(x=256, y=53, width=50, height=50)
        b7.place(x=309, y=53, width=50, height=50)
        b8.place(x=359, y=53, width=50, height=50)
        b9.place(x=409, y=53, width=50, height=50)
        c1.place(x=3, y=103, width=50, height=50)
        c2.place(x=53, y=103, width=50, height=50)
        c3.place(x=103, y=103, width=50, height=50)
        c4.place(x=156, y=103, width=50, height=50)
        c5.place(x=206, y=103, width=50, height=50)
        c6.place(x=256, y=103, width=50, height=50)
        c7.place(x=309, y=103, width=50, height=50)
        c8.place(x=359, y=103, width=50, height=50)
        c9.place(x=409, y=103, width=50, height=50)

        d1.place(x=3, y=156, width=50, height=50)
        d2.place(x=53, y=156, width=50, height=50)
        d3.place(x=103, y=156, width=50, height=50)
        d4.place(x=156, y=156, width=50, height=50)
        d5.place(x=206, y=156, width=50, height=50)
        d6.place(x=256, y=156, width=50, height=50)
        d7.place(x=309, y=156, width=50, height=50)
        d8.place(x=359, y=156, width=50, height=50)
        d9.place(x=409, y=156, width=50, height=50)
        e1.place(x=3, y=206, width=50, height=50)
        e2.place(x=53, y=206, width=50, height=50)
        e3.place(x=103, y=206, width=50, height=50)
        e4.place(x=156, y=206, width=50, height=50)
        e5.place(x=206, y=206, width=50, height=50)
        e6.place(x=256, y=206, width=50, height=50)
        e7.place(x=309, y=206, width=50, height=50)
        e8.place(x=359, y=206, width=50, height=50)
        e9.place(x=409, y=206, width=50, height=50)
        f1.place(x=3, y=256, width=50, height=50)
        f2.place(x=53, y=256, width=50, height=50)
        f3.place(x=103, y=256, width=50, height=50)
        f4.place(x=156, y=256, width=50, height=50)
        f5.place(x=206, y=256, width=50, height=50)
        f6.place(x=256, y=256, width=50, height=50)
        f7.place(x=309, y=256, width=50, height=50)
        f8.place(x=359, y=256, width=50, height=50)
        f9.place(x=409, y=256, width=50, height=50)

        g1.place(x=3, y=309, width=50, height=50)
        g2.place(x=53, y=309, width=50, height=50)
        g3.place(x=103, y=309, width=50, height=50)
        g4.place(x=156, y=309, width=50, height=50)
        g5.place(x=206, y=309, width=50, height=50)
        g6.place(x=256, y=309, width=50, height=50)
        g7.place(x=309, y=309, width=50, height=50)
        g8.place(x=359, y=309, width=50, height=50)
        g9.place(x=409, y=309, width=50, height=50)
        h1.place(x=3, y=359, width=50, height=50)
        h2.place(x=53, y=359, width=50, height=50)
        h3.place(x=103, y=359, width=50, height=50)
        h4.place(x=156, y=359, width=50, height=50)
        h5.place(x=206, y=359, width=50, height=50)
        h6.place(x=256, y=359, width=50, height=50)
        h7.place(x=309, y=359, width=50, height=50)
        h8.place(x=359, y=359, width=50, height=50)
        h9.place(x=409, y=359, width=50, height=50)
        i1.place(x=3, y=409, width=50, height=50)
        i2.place(x=53, y=409, width=50, height=50)
        i3.place(x=103, y=409, width=50, height=50)
        i4.place(x=156, y=409, width=50, height=50)
        i5.place(x=206, y=409, width=50, height=50)
        i6.place(x=256, y=409, width=50, height=50)
        i7.place(x=309, y=409, width=50, height=50)
        i8.place(x=359, y=409, width=50, height=50)
        i9.place(x=409, y=409, width=50, height=50)

        a1t.trace("w", lambda *args: Sudoku.character_limit(a1t))
        a2t.trace("w", lambda *args: Sudoku.character_limit(a2t))
        a3t.trace("w", lambda *args: Sudoku.character_limit(a3t))
        a4t.trace("w", lambda *args: Sudoku.character_limit(a4t))
        a5t.trace("w", lambda *args: Sudoku.character_limit(a5t))
        a6t.trace("w", lambda *args: Sudoku.character_limit(a6t))
        a7t.trace("w", lambda *args: Sudoku.character_limit(a7t))
        a8t.trace("w", lambda *args: Sudoku.character_limit(a8t))
        a9t.trace("w", lambda *args: Sudoku.character_limit(a9t))
        b1t.trace("w", lambda *args: Sudoku.character_limit(b1t))
        b2t.trace("w", lambda *args: Sudoku.character_limit(b2t))
        b3t.trace("w", lambda *args: Sudoku.character_limit(b3t))
        b4t.trace("w", lambda *args: Sudoku.character_limit(b4t))
        b5t.trace("w", lambda *args: Sudoku.character_limit(b5t))
        b6t.trace("w", lambda *args: Sudoku.character_limit(b6t))
        b7t.trace("w", lambda *args: Sudoku.character_limit(b7t))
        b8t.trace("w", lambda *args: Sudoku.character_limit(b8t))
        b9t.trace("w", lambda *args: Sudoku.character_limit(b9t))
        c1t.trace("w", lambda *args: Sudoku.character_limit(c1t))
        c2t.trace("w", lambda *args: Sudoku.character_limit(c2t))
        c3t.trace("w", lambda *args: Sudoku.character_limit(c3t))
        c4t.trace("w", lambda *args: Sudoku.character_limit(c4t))
        c5t.trace("w", lambda *args: Sudoku.character_limit(c5t))
        c6t.trace("w", lambda *args: Sudoku.character_limit(c6t))
        c7t.trace("w", lambda *args: Sudoku.character_limit(c7t))
        c8t.trace("w", lambda *args: Sudoku.character_limit(c8t))
        c9t.trace("w", lambda *args: Sudoku.character_limit(c9t))
        d1t.trace("w", lambda *args: Sudoku.character_limit(d1t))
        d2t.trace("w", lambda *args: Sudoku.character_limit(d2t))
        d3t.trace("w", lambda *args: Sudoku.character_limit(d3t))
        d4t.trace("w", lambda *args: Sudoku.character_limit(d4t))
        d5t.trace("w", lambda *args: Sudoku.character_limit(d5t))
        d6t.trace("w", lambda *args: Sudoku.character_limit(d6t))
        d7t.trace("w", lambda *args: Sudoku.character_limit(d7t))
        d8t.trace("w", lambda *args: Sudoku.character_limit(d8t))
        d9t.trace("w", lambda *args: Sudoku.character_limit(d9t))
        e1t.trace("w", lambda *args: Sudoku.character_limit(e1t))
        e2t.trace("w", lambda *args: Sudoku.character_limit(e2t))
        e3t.trace("w", lambda *args: Sudoku.character_limit(e3t))
        e4t.trace("w", lambda *args: Sudoku.character_limit(e4t))
        e5t.trace("w", lambda *args: Sudoku.character_limit(e5t))
        e6t.trace("w", lambda *args: Sudoku.character_limit(e6t))
        e7t.trace("w", lambda *args: Sudoku.character_limit(e7t))
        e8t.trace("w", lambda *args: Sudoku.character_limit(e8t))
        e9t.trace("w", lambda *args: Sudoku.character_limit(e9t))
        f1t.trace("w", lambda *args: Sudoku.character_limit(f1t))
        f2t.trace("w", lambda *args: Sudoku.character_limit(f2t))
        f3t.trace("w", lambda *args: Sudoku.character_limit(f3t))
        f4t.trace("w", lambda *args: Sudoku.character_limit(f4t))
        f5t.trace("w", lambda *args: Sudoku.character_limit(f5t))
        f6t.trace("w", lambda *args: Sudoku.character_limit(f6t))
        f7t.trace("w", lambda *args: Sudoku.character_limit(f7t))
        f8t.trace("w", lambda *args: Sudoku.character_limit(f8t))
        f9t.trace("w", lambda *args: Sudoku.character_limit(f9t))
        g1t.trace("w", lambda *args: Sudoku.character_limit(g1t))
        g2t.trace("w", lambda *args: Sudoku.character_limit(g2t))
        g3t.trace("w", lambda *args: Sudoku.character_limit(g3t))
        g4t.trace("w", lambda *args: Sudoku.character_limit(g4t))
        g5t.trace("w", lambda *args: Sudoku.character_limit(g5t))
        g6t.trace("w", lambda *args: Sudoku.character_limit(g6t))
        g7t.trace("w", lambda *args: Sudoku.character_limit(g7t))
        g8t.trace("w", lambda *args: Sudoku.character_limit(g8t))
        g9t.trace("w", lambda *args: Sudoku.character_limit(g9t))
        h1t.trace("w", lambda *args: Sudoku.character_limit(h1t))
        h2t.trace("w", lambda *args: Sudoku.character_limit(h2t))
        h3t.trace("w", lambda *args: Sudoku.character_limit(h3t))
        h4t.trace("w", lambda *args: Sudoku.character_limit(h4t))
        h5t.trace("w", lambda *args: Sudoku.character_limit(h5t))
        h6t.trace("w", lambda *args: Sudoku.character_limit(h6t))
        h7t.trace("w", lambda *args: Sudoku.character_limit(h7t))
        h8t.trace("w", lambda *args: Sudoku.character_limit(h8t))
        h9t.trace("w", lambda *args: Sudoku.character_limit(h9t))
        i1t.trace("w", lambda *args: Sudoku.character_limit(i1t))
        i2t.trace("w", lambda *args: Sudoku.character_limit(i2t))
        i3t.trace("w", lambda *args: Sudoku.character_limit(i3t))
        i4t.trace("w", lambda *args: Sudoku.character_limit(i4t))
        i5t.trace("w", lambda *args: Sudoku.character_limit(i5t))
        i6t.trace("w", lambda *args: Sudoku.character_limit(i6t))
        i7t.trace("w", lambda *args: Sudoku.character_limit(i7t))
        i8t.trace("w", lambda *args: Sudoku.character_limit(i8t))
        i9t.trace("w", lambda *args: Sudoku.character_limit(i9t))

        def val():
            print(Sudoku.valid_solution(a1, a2, a3, a4, a5, a6, a7, a8, a9,
                                        b1, b2, b3, b4, b5, b6, b7, b8, b9,
                                        c1, c2, c3, c4, c5, c6, c7, c8, c9,
                                        d1, d2, d3, d4, d5, d6, d7, d8, d9,
                                        e1, e2, e3, e4, e5, e6, e7, e8, e9,
                                        f1, f2, f3, f4, f5, f6, f7, f8, f9,
                                        g1, g2, g3, g4, g5, g6, g7, g8, g9,
                                        h1, h2, h3, h4, h5, h6, h7, h8, h9,
                                        i1, i2, i3, i4, i5, i6, i7, i8, i9, ))

        def reset():
            box = [a1t, a2t, a3t, a4t, a5t, a6t, a7t, a8t, a9t,
                   b1t, b2t, b3t, b4t, b5t, b6t, b7t, b8t, b9t,
                   c1t, c2t, c3t, c4t, c5t, c6t, c7t, c8t, c9t,
                   d1t, d2t, d3t, d4t, d5t, d6t, d7t, d8t, d9t,
                   e1t, e2t, e3t, e4t, e5t, e6t, e7t, e8t, e9t,
                   f1t, f2t, f3t, f4t, f5t, f6t, f7t, f8t, f9t,
                   g1t, g2t, g3t, g4t, g5t, g6t, g7t, g8t, g9t,
                   h1t, h2t, h3t, h4t, h5t, h6t, h7t, h8t, h9t,
                   i1t, i2t, i3t, i4t, i5t, i6t, i7t, i8t, i9t, ]
            for i in box:
                i.set("")

            entries = [a1, a2, a3, a4, a5, a6, a7, a8, a9,
                       b1, b2, b3, b4, b5, b6, b7, b8, b9,
                       c1, c2, c3, c4, c5, c6, c7, c8, c9,
                       d1, d2, d3, d4, d5, d6, d7, d8, d9,
                       e1, e2, e3, e4, e5, e6, e7, e8, e9,
                       f1, f2, f3, f4, f5, f6, f7, f8, f9,
                       g1, g2, g3, g4, g5, g6, g7, g8, g9,
                       h1, h2, h3, h4, h5, h6, h7, h8, h9,
                       i1, i2, i3, i4, i5, i6, i7, i8, i9, ]
            # for enabling disabled boxes
            for i in entries:
                i.configure(state="enabled")

        def start():
            boxes = [a7t, b2t, b6t, b8t, c1t, c3t, c7t, d2t, d5t, e4t, e6t, f5t, f8t, g3t, g7t, g9t, h2t, h4t, h8t, i3t]
            nums = [2, 8, 7, 9, 6, 2, 5, 7, 6, 9, 1, 2, 4, 5, 6, 3, 9, 4, 7, 6]
            entries = [a7, b2, b6, b8, c1, c3, c7, d2, d5, e4, e6, f5, f8, g3, g7, g9, h2, h4, h8, i3]
            Sudoku.starter(boxes, nums, entries)

        ttk.Button(self.root, text="Validate", command=val).place(x=3, y=462, width=148, height=40)
        ttk.Button(self.root, text="Reset", command=reset).place(x=157, y=462, width=147, height=40)
        ttk.Button(self.root, text="Start", command=start).place(x=310, y=462, width=147, height=40)


program = tkinter.Tk()
settings = Sudoku(program)
program.mainloop()

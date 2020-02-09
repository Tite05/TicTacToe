# tkinter Game: Tic Tac Toe
# Made in Python 3.6
########################################
import sys
import tkinter as tk
import tkinter.messagebox as messagebox

########################################

class TicTacToe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.pts1 = 0
        self.p1_pts = tk.IntVar()
        self.pts2 = 0
        self.p2_pts = tk.IntVar()
        self.create_entries()
        self.create_labels()
        self.create_buttons()
        self.player = 'P1'
        self.flags = 0
        self.buttons = [self.btn1, self.btn2, self.btn3,
                        self.btn4, self.btn5, self.btn6,
                        self.btn7, self.btn8, self.btn9]
        

    def create_entries(self):
        Entry = tk.Entry
        self._p1 = Entry(textvariable=self.player1, bd=3)
        self._p1.grid(row=1, column=1, columnspan=6, sticky='W')
        
        self._p2 = Entry(textvariable=self.player2, bd=3)
        self._p2.grid(row=2, column=1, columnspan=6, sticky='W')

        self._pts1 = Entry(textvariable=self.p1_pts, bd=2, width=3, justify='right', state='disabled')
        self._pts1.grid(row=1, column=2, columnspan=6)

        self._pts2 = Entry(textvariable=self.p2_pts, bd=2, width=3, justify='right', state='disabled')
        self._pts2.grid(row=2, column=2, columnspan=6)


    def create_labels(self):
        Label = tk.Label
        self.label1 = Label(text='Player 1:', font='Times 18 bold', bg='lightgray', fg='black', height=1, width=8)
        self.label1.grid(row=1, column=0)

        self.label2 = Label(text='Player 2:', font='Times 18 bold', bg='lightgray', fg='black', height=1, width=8)
        self.label2.grid(row=2, column=0)


    def create_buttons(self):
        Button = tk.Button
        self.btn1 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn1))
        self.btn1.grid(row=3, column=0)

        self.btn2 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn2))
        self.btn2.grid(row=3, column=1)

        self.btn3 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn3))
        self.btn3.grid(row=3, column=2)

        self.btn4 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn4))
        self.btn4.grid(row=4, column=0)

        self.btn5 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn5))
        self.btn5.grid(row=4, column=1)

        self.btn6 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn6))
        self.btn6.grid(row=4, column=2)

        self.btn7 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn7))
        self.btn7.grid(row=5, column=0)

        self.btn8 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn8))
        self.btn8.grid(row=5, column=1)

        self.btn9 = Button(text=' ', font='Arial 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: self.btn_click(self.btn9))
        self.btn9.grid(row=5, column=2)


    def retry_cancel(self, title, message):
        msgbox = messagebox.askretrycancel(title, message)
        if msgbox == True:
            self.restart_game()
        else:
            self.quit()


    def get_player(self, player):
        if player == 'P1':
            return self.player1.get() if len(self.player1.get()) > 0 and self.player1.get() != self.player2.get() else 'Player 1'
        else:
            return self.player2.get() if len(self.player2.get()) > 0 and self.player2.get() != self.player1.get() else 'Player 2'


    def disable_buttons(self):
        for btn in self.buttons:
            btn.configure(state='disabled')


    def mark_flags(self, *buttons):
        for btn in buttons:
            btn['bg'] = 'gray36'


    def set_winner(self, flag):
        self.disable_buttons()
        player = 'P1' if flag == 'X' else 'P2'
        if player == 'P1':
            self.pts1 += 1
            self.p1_pts.set(self.pts1)
        else:
            self.pts2 += 1
            self.p2_pts.set(self.pts2)
        self.retry_cancel('Tic Tac Toe', self.get_player(player) + ' Wins!')


    def btn_click(self, button):
        button.config(activebackground=button.cget('background'))
        button.config(activeforeground=button.cget('foreground'))
        if button["text"] == " " and self.player == 'P1':
            button["text"] = "X"
            self.player = 'P2'
            self.flags += 1
            self.check_win('X')
        elif button["text"] == " " and self.player == 'P2':
            button["text"] = "O"
            self.player = 'P1'
            self.flags += 1
            self.check_win('O')
        else:
            pass


    def check_win(self, flag):
        if self.flags < 9:
            if (self.btn1['text'], self.btn2['text'], self.btn3['text']) == (flag, flag, flag):
                self.mark_flags(self.btn1, self.btn2, self.btn3)
                self.set_winner(flag)
            elif (self.btn4['text'], self.btn5['text'], self.btn6['text']) == (flag, flag, flag):
                self.mark_flags(self.btn4, self.btn5, self.btn6)
                self.set_winner(flag)
            elif (self.btn7['text'], self.btn8['text'], self.btn9['text']) == (flag, flag, flag):
                self.mark_flags(self.btn7, self.btn8, self.btn9)
                self.set_winner(flag)
            elif (self.btn1['text'], self.btn5['text'], self.btn9['text']) == (flag, flag, flag):
                self.mark_flags(self.btn1, self.btn5, self.btn9)
                self.set_winner(flag)
            elif (self.btn3['text'], self.btn5['text'], self.btn7['text']) == (flag, flag, flag):
                self.mark_flags(self.btn3, self.btn5, self.btn7)
                self.set_winner(flag)
            elif (self.btn1['text'], self.btn4['text'], self.btn7['text']) == (flag, flag, flag):
                self.mark_flags(self.btn1, self.btn4, self.btn7)
                self.set_winner(flag)
            elif (self.btn2['text'], self.btn5['text'], self.btn8['text']) == (flag, flag, flag):
                self.mark_flags(self.btn2, self.btn5, self.btn8)
                self.set_winner(flag)
            elif (self.btn3['text'], self.btn6['text'], self.btn9['text']) == (flag, flag, flag):
                self.mark_flags(self.btn3, self.btn6, self.btn9)
                self.set_winner(flag)
            else:
                pass
        else:
            self.retry_cancel('Tic Tac Toe', 'It is a Tie!')
            

    def restart_game(self):
        self.create_buttons()
        self.player = 'P1'
        self.flags = 0

########################################

root = tk.Tk()
root.title('Tic Tac Toe')

TicTacToe(root).mainloop()
########################################
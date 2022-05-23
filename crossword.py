from tkinter import *
import tkinter.ttk as ttk

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):

        self.osi = 0
        self.rest = 0
        self.figma = 0
        self.frame = 0
        self.smtp = 0
        self.python = 0

        self.lbl_2 = Label(root, text="", bg="#F5F5F5", font=("courier", 16, "bold"),
                           justify=LEFT)
        self.lbl_2.place(x=400, y=8)

        frame = Frame(root)
        frame.pack(side=RIGHT, padx=10)

        text = Text(frame, width=40, wrap=WORD, padx=5, pady=5, font=("serif", 9))
        text.pack()
        text.insert("1.0", "1. Единица информации на канальном уровне "
                           "глобальной сетевой модели.\n\n"
                           "2. Глобальная модель всех сетевых сущностей, "
                           "состоящая из 7-ми логических уровней.\n\n"
                           "3. Онлайн-сервис для разработки интерфейсов "
                           "с возможностью организации "
                           "совместной работы в режиме реального времени.\n\n"
                           "4. Высокоуровневый язык программирования общего "
                           "назначения.\n\n"
                           "5. Система, полностью соответствующая "
                           "архитектурному стилю взаимодействия компонентов "
                           "распределённого приложения в сети и отвечающая "
                           "основным ограничениям, разработанным "
                           "Роем Филдингом.\n\n"
                           "6. Сетевой протокол, предназначенный для "
                           "передачи электронной почты.")
        text.config(state='disabled')

        # scrollbar = Scrollbar()
        # scrollbar.config(command=text.yview)
        # scrollbar.pack(side=RIGHT, fill=Y)

    # OSI
        self.lbl_1 = Label(root, text="2", bg="#F5F5F5",
                           font=("courier", 13, "bold"), fg="#0000CD")
        self.lbl_1.place(x=0, y=100, width=30, height=30)

        global entry_1_o
        entry_1_o = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                      bd=3.0, justify=CENTER)
        entry_1_o.place(x=30, y=100, width=30, height=30)

        global entry_1_s
        entry_1_s = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                        bd=3.0, justify=CENTER)
        entry_1_s.place(x=65, y=100, width=30, height=30)

        global entry_1_i
        entry_1_i = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                        bd=3.0, justify=CENTER)
        entry_1_i.place(x=100, y=100, width=30, height=30)

    # RESTFUL
        self.lbl_1_2 = Label(root, text="5", bg="#F5F5F5",
                             font=("courier", 13, "bold"), fg="#0000CD")
        self.lbl_1_2.place(x=65, y=0, width=30, height=30)

        global entry_2_r
        entry_2_r = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_2_r.place(x=65, y=30, width=30, height=30)

        global entry_2_e
        entry_2_e = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                        bd=3.0, justify=CENTER)
        entry_2_e.place(x=65, y=65, width=30, height=30)

        global entry_2_t
        entry_2_t = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_2_t.place(x=65, y=135, width=30, height=30)

        global entry_2_f
        entry_2_f = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_2_f.place(x=65, y=170, width=30, height=30)

        global entry_2_u
        entry_2_u = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_2_u.place(x=65, y=205, width=30, height=30)

        global entry_2_l
        entry_2_l = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_2_l.place(x=65, y=240, width=30, height=30)

    # FIGMA
        self.lbl_1_3 = Label(root, text="3", bg="#F5F5F5",
                             font=("courier", 13, "bold"), fg="#0000CD")
        self.lbl_1_3.place(x=35, y=170, width=30, height=30)

        global entry_3_i
        entry_3_i = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_3_i.place(x=100, y=170, width=30, height=30)

        global entry_3_g
        entry_3_g = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_3_g.place(x=135, y=170, width=30, height=30)

        global entry_3_m
        entry_3_m = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_3_m.place(x=170, y=170, width=30, height=30)

        global entry_3_a
        entry_3_a = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_3_a.place(x=205, y=170, width=30, height=30)

    # FRAME
        self.lbl_frame = Label(root, text="1", bg="#F5F5F5",
                             font=("courier", 13, "bold"), fg="#0000CD")
        self.lbl_frame.place(x=0, y=30, width=30, height=30)

        global entry_4_f
        entry_4_f = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_4_f.place(x=30, y=30, width=30, height=30)

        global entry_4_a
        entry_4_a = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_4_a.place(x=100, y=30, width=30, height=30)

        global entry_4_m
        entry_4_m = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_4_m.place(x=135, y=30, width=30, height=30)

        global entry_4_e
        entry_4_e = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_4_e.place(x=170, y=30, width=30, height=30)

    # SMTP
        self.lbl_smtp = Label(root, text="6", bg="#F5F5F5",
                               font=("courier", 13, "bold"), fg="#0000CD")
        self.lbl_smtp.place(x=170, y=105, width=30, height=30)

        global entry_5_s
        entry_5_s = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_5_s.place(x=170, y=135, width=30, height=30)

        global entry_5_t
        entry_5_t = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_5_t.place(x=170, y=205, width=30, height=30)

        global entry_5_p
        entry_5_p = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_5_p.place(x=170, y=240, width=30, height=30)

    # PYTHON
        self.lbl_smtp = Label(root, text="4", bg="#F5F5F5",
                              font=("courier", 13, "bold"), fg="#0000CD")
        self.lbl_smtp.place(x=140, y=240, width=30, height=30)

        global entry_6_y
        entry_6_y = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_6_y.place(x=205, y=240, width=30, height=30)

        global entry_6_t
        entry_6_t = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_6_t.place(x=240, y=240, width=30, height=30)

        global entry_6_h
        entry_6_h = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_6_h.place(x=275, y=240, width=30, height=30)

        global entry_6_o
        entry_6_o = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_6_o.place(x=310, y=240, width=30, height=30)

        global entry_6_n
        entry_6_n = Entry(root, font=("Times New Roman", 16), relief=SUNKEN,
                          bd=3.0, justify=CENTER)
        entry_6_n.place(x=345, y=240, width=30, height=30)

    # BUTTON
        global btn_1
        btn_1 = Button(root, text="Проверить", font=("courier", 11),
                       command=lambda: self.btn_click([
                           entry_1_o.get().upper(), entry_1_s.get().upper(),
                           entry_1_i.get().upper(), entry_2_r.get().upper(),
                           entry_2_e.get().upper(), entry_2_t.get().upper(),
                           entry_2_f.get().upper(), entry_2_u.get().upper(),
                           entry_2_l.get().upper(), entry_3_i.get().upper(),
                           entry_3_g.get().upper(), entry_3_m.get().upper(),
                           entry_3_a.get().upper(), entry_4_f.get().upper(),
                           entry_4_a.get().upper(), entry_4_m.get().upper(),
                           entry_4_e.get().upper(), entry_5_s.get().upper(),
                           entry_5_t.get().upper(), entry_5_p.get().upper(),
                           entry_6_y.get().upper(), entry_6_t.get().upper(),
                           entry_6_h.get().upper(), entry_6_o.get().upper(),
                           entry_6_n.get().upper()
                       ]),
                       bg="#FFFFFF", fg="#0000CD")
        btn_1.place(x=10, y=360, width=90, height=30)

    # CLICK
    def btn_click(self, list):

        self.lbl_2.configure(text="Неправильно!", fg="#FF0000")

    # OSI
        osi_o = list[0]
        osi_s = list[1]
        osi_i = list[2]

        if osi_o == "O" and osi_s == "S" and osi_i == "I":
            entry_1_o.config(state='disabled')
            entry_1_s.config(state='disabled')
            entry_1_i.config(state='disabled')
            if self.osi == 0:
                self.lbl_2.configure(text="Правильно!", fg="#0000CD")
                self.osi = 1
                self.success()

    # REST
        rest_r = list[3]
        rest_e = list[4]
        rest_t = list[5]
        rest_f = list[6]
        rest_u = list[7]
        rest_l = list[8]

        if rest_r == "R" and rest_e == "E" and osi_s == "S" and rest_t == "T" \
                and rest_f == "F" and rest_u == "U" and rest_l == "L":
            entry_2_r.config(state='disabled')
            entry_2_e.config(state='disabled')
            entry_1_s.config(state='disabled')
            entry_2_t.config(state='disabled')
            entry_2_f.config(state='disabled')
            entry_2_u.config(state='disabled')
            entry_2_l.config(state='disabled')
            if self.rest == 0:
                self.lbl_2.configure(text="Правильно!", fg="#0000CD")
                self.rest = 1
                self.success()

    # FIGMA
        figma_i = list[9]
        figma_g = list[10]
        figma_m = list[11]
        figma_a = list[12]

        if rest_f == "F" and figma_i == "I" and figma_g == "G" \
                and figma_m == "M" and figma_a == "A":
            entry_2_f.config(state='disabled')
            entry_3_i.config(state='disabled')
            entry_3_g.config(state='disabled')
            entry_3_m.config(state='disabled')
            entry_3_a.config(state='disabled')
            if self.figma == 0:
                self.lbl_2.configure(text="Правильно!", fg="#0000CD")
                self.figma = 1
                self.success()

    # FRAME
        frame_f = list[13]
        frame_a = list[14]
        frame_m = list[15]
        frame_e = list[16]

        if frame_f == "F" and rest_r == "R" and frame_a == "A" and frame_m == "M" \
                and frame_e == "E":
            entry_4_f.config(state='disabled')
            entry_2_r.config(state='disabled')
            entry_4_a.config(state='disabled')
            entry_4_m.config(state='disabled')
            entry_4_e.config(state='disabled')
            if self.frame == 0:
                self.lbl_2.configure(text="Правильно!", fg="#0000CD")
                self.frame = 1
                self.success()

    # SMTP
        smtp_s = list[17]
        smtp_t = list[18]
        smtp_p = list[19]

        if smtp_s == "S" and figma_m == "M" and smtp_t == "T" and smtp_p == "P":
            entry_5_s.config(state='disabled')
            entry_3_m.config(state='disabled')
            entry_5_t.config(state='disabled')
            entry_5_p.config(state='disabled')
            if self.smtp == 0:
                self.lbl_2.configure(text="Правильно!", fg="#0000CD")
                self.smtp = 1
                self.success()

    # PYTHON
        python_y = list[20]
        python_t = list[21]
        python_h = list[22]
        python_o = list[23]
        python_n = list[24]

        if smtp_p == "P" and python_y == "Y" and python_t == "T" \
                and python_h == "H" and python_o == "O" and python_n == "N":
            entry_5_p.config(state='disabled')
            entry_6_y.config(state='disabled')
            entry_6_t.config(state='disabled')
            entry_6_h.config(state='disabled')
            entry_6_o.config(state='disabled')
            entry_6_n.config(state='disabled')
            if self.python == 0:
                self.lbl_2.configure(text="Правильно!", fg="#0000CD")
                self.python = 1
                self.success()

    def success(self):
        if self.osi == self.rest == self.figma == self.frame == self.smtp == self.python == 1:
            self.lbl_2.configure(text="Решено!", fg="#008000")
            btn_1.config(state='disabled')


if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x400+200+200")
    root.title("Кроссворд")
    root.resizable(False, False)
    root["bg"] = "#F5F5F5"
    app = Main(root)
    app.pack()
    root.mainloop()
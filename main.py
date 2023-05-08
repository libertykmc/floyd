import math
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.title('Алгорти Флойда')
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        self.size_frame = ctk.CTkFrame(self, fg_color='transparent',)
        self.size_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        self.size_entry = ctk.CTkEntry(self.size_frame, placeholder_text='Количество вершин')
        self.size_entry.grid(row=0, column=0, padx=(0, 10))

        self.size_button = ctk.CTkButton(self.size_frame, text='Создать матрицу', command=self.create_matrix)
        self.size_button.grid(row=0, column=1)

        self.matrix_frame = ctk.CTkFrame(self)
        self.matrix_frame.grid(row=1, column=0, sticky='s')

        self.submit_btn = ctk.CTkButton(self, text='Рассчитать по алгоритму Флойда', command=self.floyd)
        self.submit_btn.grid(row=2, column=0, pady=10)

        self.output_matrix_frame = ctk.CTkFrame(self)
        self.output_matrix_frame.grid(row=3, column=0)

        self.matrix_size = 0
        self.prev_matrix_size = 0

    def create_matrix(self):
        size = self.size_entry.get()
        if not size.isnumeric(): return

        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                self.matrix[i][j].destroy()

        self.matrix_size = int(size)
        self.matrix = []

        for i in range(self.matrix_size):
            self.matrix.append([])
            for j in range(self.matrix_size):
                self.matrix[i].append(ctk.CTkEntry(self.matrix_frame, width=40))
                if i == j: self.matrix[i][j].insert(0, 'X')
                self.matrix[i][j].grid(row=i, column=j, padx=5, pady=5)

    def floyd(self):
        matrix = []

        for i in range(self.matrix_size):
            matrix.append([])
            for j in range(self.matrix_size):
                val = self.matrix[i][j].get()
                if i == j:
                    matrix[i].append(0)
                elif val.lower() == 'inf' or not val:
                    matrix[i].append(math.inf)
                else:
                    matrix[i].append(int(val))

        # --- floyd


        print(matrix)
        for k in range(self.matrix_size):
            prev = matrix.copy()
            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    matrix[i][j] = min(prev[i][j], prev[i][k] + prev[k][j])
            print(matrix)

        # --- floyd

        for i in range(self.prev_matrix_size):
            for j in range(self.prev_matrix_size):
                self.output_matrix[i][j].destroy()
                
        self.output_matrix = []
        self.prev_matrix_size = self.matrix_size

        for i in range(self.matrix_size):
            self.output_matrix.append([])
            for j in range(self.matrix_size):
                text = matrix[i][j]
                if i == j: text = 'X'
                elif text == math.inf: text = '∞'
                self.output_matrix[i].append(ctk.CTkLabel(self.output_matrix_frame, text=text))
                self.output_matrix[i][j].grid(row=i, column=j, padx=7)



if __name__ == '__main__':
    app = App()
    app.mainloop()

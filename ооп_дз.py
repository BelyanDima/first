class Task:
    def input(self):
        self.a = input('Введите данные: ')
        if self.a[-1].isalpha():
            print(task.st())
        else:
            print(task.dig())



    def st(self):
        gl = ('а','у','о','ы','э','е','ё','и','ю','я')
        g = 0
        s = 0
        gl1 = []
        s1 = []

        for i in self.a:
            if i in gl:
                g += 1
                gl1.append(i)
            else:
                s += 1
                s1.append(i)
        if g * s <= len(self.a):
            return f'Гласные буквы в слове: {gl1}'
        else:
            return f'Согласные буквы в слове: {s1}'

    def dig(self):
        ch = 0
        for i in str(self.a):
            if int(i) % 2 == 0:
                ch += int(i)
        return ch * len(str(self.a))


task = Task()
print(task.input())



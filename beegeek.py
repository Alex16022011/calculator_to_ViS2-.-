def sort_list(a):
    ye = []
    for q in a:
        if '.' in str(q):
            ye.append(float(q))
        else:
            ye.append(int(q))
    ye.sort()
    return ye

def from_en_to_ru(n):
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = 'NO'
    for i in n:
        if i in c:
            answer = 'YES'
            break
    if answer == 'YES':
        a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', "'", ';', '.', ',', '`']
        b = ['Ф', 'И', 'С', 'В', 'У', 'А', 'П', 'Р', 'Ш', 'О', 'Л', 'Д', 'Ь', 'Т', 'Щ', 'З', 'Й', 'К', 'Ы', 'Е', 'Г', 'М', 'Ц', 'Ч', 'Н', 'Я', 'Х', 'Ъ', 'Э', 'Ж', 'Ю', 'Б', 'Ё']
        for i in n:
            if i in a:
                t = a.index(i)
                r = b[t]
                y = n[n.index(i)]
                n[n.index(i)] = r
    answer2 = ''.join(n)
    return answer2
def correct_word(word):
    answer = 'False'
    list1 = ['МОДА', 'МЕДИАНА', 'РАЗМАХ', 'СРЕДНЕЕ АРИФМЕТИЧЕCКОЕ', 'УПОРЯДОЧИТЬ', 'КОЛИЧЕСТВО ЧИСЕЛ']
    if name not in list1:
        list2 = []
        for i in list1:
            if word[0] == i[0]:
                list2.append(list(i))
        list3 = list(word)
        if len(list2) > 1:
            for j in range(len(list2)):
                counter = 0
                for i in list3:
                    if i in list2[j]:
                        counter += 1
                if counter == len(list2[j]):
                    answer = 'True'
                    word = ''.join(list2[j])
                    break
        else:
            word = ''.join(list2[0])
    return word

from math import *
print('Здравствуйте!')
print()
print('Я умею вычислять: C из n по k (C), A из n по k (A), Факториал числа (P), Мода статистического ряда, Количество чисел, Отсортировывать список, Находить медиану ряда, Находить среднее арифметическое, Размах списка')
print()
e = int(input('Введите количество нужных вам попыток: '))
for abc in range(e):

    name = input('Введите слово (букву) нужной вам операции: ').upper()
    if name == 'P':
        mas = int(input('Факториал какого числа вы хотите подсчитать: '))
    elif name in 'CA':
        n = int(input('Из: '))
        k = int(input('По: '))
    else:
        name = list(name)
        name = from_en_to_ru(name)
        name = correct_word(name)
        qw = input('Введите список чисел: ')
        fas = ''
        for i in qw:
            if i == ',':
                fas += '.'
                continue
            if i != ';':
                fas += i
        qw = fas
        qw = qw.split()
        dek = sort_list(qw)

    if name == 'A':
        first = ''
        second = ''
        third = ''
        c = ''
        myset1 = set()
        myset2 = set()
        for j in range(1, n + 1):
            c += str(j)
            myset1.add(j)
            c += '*'
        c = c[:-1]
        q = 3
        q += len(c)
        d = ''
        for z in range(1, n - k + 1):
            d += str(z)
            myset2.add(z)
            d += '*'
        d = d[:-1]
        myset3 = myset1.copy()
        myset1 -= myset2
        myset2 -= myset3
        first += c
        first += '   '
        second += '-' * len(c)
        second += ' = '
        third += d
        third += ' ' * (len(c) - len(d) + 3)
        a = ''
        for i in myset1:
            a += str(i)
            a += '*'
        a = a[:-1]
        first += a
        first += '   '
        second += '-' * len(a)
        second += ' = '
        if len(myset2) == 0:
            third += ' ' * (len(a) // 2)
            third += '1'
            third += ' ' * (len(a) // 2)
        elif len(myset2) > 0:
            q = ''
            for i in myset2:
                q += str(i)
                q += '*'
            q = q[:-1]
            third += q
        m = factorial(n) // factorial(n - k)
        second += str(m)
        print(first)
        print(second)
        print(third)

    if name == 'P':
        print()
        cqw = ''
        for u in range(1, mas + 1):
            cqw += str(u)
            cqw += '*'
        cqw = cqw[:-1]
        print(cqw, '=', factorial(mas))
        print()

    if name == 'C':
        need3 = factorial(n) / (factorial(n - k) * factorial(k))
        output1 = ''
        myset1 = set()
        myset2 = set()
        for f in range(1, n + 1):
            output1 += str(f)
            output1 += '*'
            myset1.add(f)
        output1 = output1[:-1]
        output3 = ''
        for w in range(1, n - k + 1):
            output3 += str(w)
            output3 += '*'
            myset2.add(w)
        for y in range(1, k + 1):
            output3 += str(y)
            output3 += '*'
            myset2.add(y)
        myset3 = myset1.copy()
        myset1 -= myset2
        myset2 -= myset3
        a = ''
        b = ''
        for i in myset1:
            a += str(i)
            a += '*'
        a = a[:-1]
        for j in myset2:
            b += str(j)
            b += '*'
        b = b[:-1]
        output3 = output3[:-1]
        output2 = ''
        output2 += '-' * max(len(output1), len(output2))
        output2 += ' = '
        output1 += ' ' * (len(output2) - len(output1))
        output3 += ' ' * (len(output2) - len(output3))
        output1 += a
        output2 += '-' * max(len(a), len(b))
        output2 += ' = '
        output2 += str(need3)
        if len(b) > 1:
            output3 += b
        else:
            output3 += ' ' * (len(a) // 2)
            output3 += '1'
            output3 += ' ' * (len(a) // 2)
        output1 += ' ' * (len(output2) - len(output1))
        output3 += ' ' * (len(output2) - len(output3))
        print(output1, output2, output3, sep='\n')

    if name == 'РАЗМАХ':
        numbers = []
        for e in dek:
            numbers.append(int(e))
        if len(numbers) > 1:
            c = max(numbers)
            v = min(numbers)
            print(f'Размах: {c - v}')
        else:
            print('Размах: ', *numbers)

    if name == 'СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ СТАТИСТИЧЕСКОГО РЯДА' or 'СРЕДНЕЕ АРИФМЕТИЧЕCКОЕ' in name:
        numbers2 = dek
        first = second = third = ''
        second += 'Среднее арифметическое ряда = '
        first = third = ' ' * 29
        w = max(len(str(sum(numbers2))), len(str(len(numbers2)))) * '-'
        second += w
        first += ' '
        third += ' ' * (len(w) // 2 + 1)
        first += str(sum(numbers2))
        third += str(len(numbers2))
        second += ' = '
        second += str(sum(numbers2) / len(numbers2))
        first += ' ' * (len(second) - len(first))
        third += ' ' * (len(second) - len(third))
        print(first, second, third, sep='\n')

    if name == 'УПОРЯДОЧИТЬ':
        print('Упорядоченный ряд ', qw, ' = ', *dek)

    if name == 'МОДА':
        c = []
        counter1 = 2

        co = 0
        for d in range(len(qw)):
            r = qw.count(qw[d])
            if r >= counter1:
                c.append(qw[d])
                counter1 = r
            else:
                co += 1
        t = []
        for y in range(len(c)):
            rt = c.count(c[y])
            if rt >= counter1 and c[y] not in t:
                t.append(c[y])
                counter1 = rt
        if co == len(qw):
            print('Моды нет')
        else:
            print('Мода списка ', *qw, '=', *t, sep=' ')

    if name == 'МЕДИАНА':
        b = dek[:]
        if len(b) % 2 == 0:
            b = dek[:]
            for i in dek:
                dek[dek.index(i)] = str(i)
            while len(b) != 2:
                del b[0]
                del b[-1]
            c8 = int(b[0]) + int(b[1])
            t = str(b[0]) + ' + ' + str(b[1])
            n = ' '.join(qw)
            m = ' '.join(dek)
            a = 'Медиана списка  = ' + n + ' = ' + m + ' = '
            first = second = third = ''
            second += a
            first += ' ' * (len(second) + 1)
            third += ' ' * (len(second) + 1)
            second += '-' * len(m)
            first += t
            third += ' ' * ((len(second) - len(third)) // 2 - 1)
            third += '2'
            second += ' = '
            first += ' ' * (len(second) - len(first))
            third += ' ' * (len(second) - len(third))
            second += '-' * len(str(c8))
            first += str(c8)
            third += '2'
            second += ' = '
            second += str(c8 / 2)
            first += ' ' * (len(second) - len(first))
            third += ' ' * (len(second) - len(third))
            print(first, second, third, sep='\n')
        else:
            while len(b) != 1:
                del b[0]
                del b[-1]
            q8 = sorted(qw)
            print(f'Медиана списка  = ', *qw, ' = ', *q8, ' = ', b[0])

    if name == 'КОЛИЧЕСТВО ЧИСЕЛ':
        counter = []
        numbers = []
        for i in qw:
            if i not in numbers:
               numbers.append(i)
        numbers.sort()
        for i in numbers:
            c = qw.count(i)
            counter.append(c)
        print('Число:             Сколько раз встречается:')
        for i in range(len(counter)):
            print(numbers[i].ljust(10), '='.ljust(10), counter[i])
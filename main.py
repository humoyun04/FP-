# Fucntional Programming

from functools import reduce
print("Demak pastda korib turgan funksiyalarni raqamining joylashuvini kriting u sizga soragan vizifangizni yechib beradi:\n1.Recursion bilan sonlarni qoshib boradi!\n2.Functions orqali text larni katta yoki kichik qilib beradi!\n3.Map orqali ro'yxatdagi sonlarni oziga qoshib yana chiqaradi!\n4.Filter orqali filterlaydi harflarni!\n5.Lambda orqali sonni 3 topadi!\n6.Reduce orqali ro'yxatgi sonlarni barchasimi kopaytmasini xisoblaydi!\n ")
tanlov = int(input("Raqamni kriting: "))

while True:
    # 1 Recursion function
    if tanlov == 1:
        def Sum(L, i, n, count):
            if n <= i:
                return count

            count += L[i]

            count = Sum(L, i + 1, n, count)

            return count


        L = [1, 2, 3, 4, 5]
        count = 0
        n = len(L)
        print(Sum(L, 0, n, count))

    #  2 Functions
    elif tanlov == 2:
        def katta(text):
            return text.upper()


        def kichik(text):
            return text.lower()


        def end(func):
            greeting = func("Salom mening ismim Humoyun!")
            print(greeting)


        end(katta)
        end(kichik)

    # 3 Map
    elif tanlov == 3:
        numbers = (1, 2, 3, 4)
        sum = list(map(lambda n: n + n, numbers))
        print(sum)

    # 4 Filter
    elif tanlov == 4:
        def ajoyib(variable):
            harflar = ['a', 'e', 'i', 'o', 'u']
            if (variable in harflar):
                return True
            else:
                return False


        ozgaruvchilar = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
        filtered = list(filter(ajoyib, ozgaruvchilar))
        print("Filterlangan harflar: ", end="")
        print(filtered)

    #  5 Lamda

    elif tanlov == 5:
        cube = lambda x: x * x * x
        print(cube(7))


    # 6 Reduce

    elif tanlov == 6:
        def maxsulot(x, y):
            return x * y


        ans = reduce(maxsulot, [2, 5, 3, 7])
        print(ans)

    else:
        print("Bunday raqam mavjud emas!")

    text = input("Yana davom etirasizmi, H yoki Y: ")
    if text.lower() == "h":
        continue
    else:
        print("Thank You!")
        break













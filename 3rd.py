"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

initial_num=str(input("введите число:"))

snd=int(initial_num*2)
thrd=int(initial_num*3)

print(int(initial_num)+snd+thrd)
import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('input.in', 'r') as f:
    nums = f.read().splitlines()
N = np.zeros(len(nums))
for i in range(len(nums)):
    N[i] = float(nums[i])
U = np.array([N])
l = U.size
lx = np.arange(l)
t = np.zeros(l)
A = np.array([np.zeros(l)]*l)
for i in range(l-1):
    A[i][i] = A[i][i] + 1
    A[i+1][i] = A[i+1][i] -1

fig, ax = plt.subplots()
ax.axis([0, 50, -2, 2])
#  Создаем функцию, генерирующую картинки
#  для последующей "склейки":
def animate(i):
    ax.clear()
    ax.axis([0, 50, -1, 10])
    global U
    U = U - 0.5 * U.dot(A)
    line = ax.plot(lx, U.T)
    return line


#  Создаем объект анимации:
sin_animation = animation.FuncAnimation(fig,
                                        animate,
                                        frames=np.linspace(0, 255),
                                        interval=10,
                                        repeat=False)

#  Сохраняем анимацию в виде gif файла:
sin_animation.save('моя анимация.gif',
                   writer='imagemagick',
                   fps=30)
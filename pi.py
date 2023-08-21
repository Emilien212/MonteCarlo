from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0, np.pi/2)

total = 0
m = 10

for a in range(m):
    # Monte carlo
    n = 1000000
    In = []
    Out = []
    for _ in range(n):
        x = np.random.random()
        y = np.random.random()

        if x < (1-y**2)**(1/2):
            In.append((x, y))
        else:
            Out.append((x, y))

    plt.plot([i[0] for i in In], [i[1] for i in In], 'g.')
    plt.plot([i[0] for i in Out], [i[1] for i in Out], 'r.')

    plt.plot(np.cos(t), np.sin(t), 'black', linewidth=3)

    total_area = 1
    ratio = len(In)/n
    answer = np.pi/4

    print(f"Area : {total_area*ratio}\nError : {abs(total_area*ratio - answer)}\nError % : {100*abs(total_area*ratio - answer)/answer}%")

    total += total_area*ratio

    if a == m-1:
        plt.savefig(f"pi_{n}")
    
    plt.close()

print(f"Average 10 runs {round((total/m)*4, 5)}")
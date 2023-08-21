from matplotlib import pyplot as plt
import numpy as np

total = 0
m = 10

for a in range(m):
    # Monte carlo
    n = 1000000
    In = []
    Out = []
    for _ in range(n):
        x = (np.random.random() * 4)
        y = (np.random.random() * 4) 

        type(y)

        if y < -(16 - x**2)**(1/2) + 4  and y < -(16 - (x - 4)**2)**(1/2) + 4:
            In.append((x,y))
        elif y > -(16 - x**2)**(1/2) + 4  and y > -(16 - (x - 4)**2)**(1/2) + 4:
            In.append((x,y))
        else:
            Out.append((x,y))

    

    # points
    plt.plot([i[0] for i in In], [i[1] for i in In], 'g.')
    plt.plot([i[0] for i in Out], [i[1] for i in Out], 'r.')

    # first circle
    plt.plot(np.linspace(0, 4, 10000), -(16 - np.linspace(0, 4, 10000)**2)**(1/2) + 4, 'blue', linewidth = 4)

    # second circle
    plt.plot(np.linspace(0, 4, 10000), -(16 - (np.linspace(0, 4, 10000) - 4)**2)**(1/2) + 4, 'blue', linewidth = 4)

    # square
    plt.plot(np.linspace(0, 4, 10000), np.zeros((10000)), 'black', linewidth = 4)
    plt.plot(np.linspace(0, 4, 10000), np.ones((10000))*4, 'black', linewidth = 4)
    plt.plot(np.zeros((10000)), np.linspace(0, 4, 10000), 'black', linewidth = 4)
    plt.plot(np.ones((10000))*4, np.linspace(0, 4, 10000), 'black', linewidth = 4)

    total_area = 4**2
    ratio = len(In)/n
    answer = 16 - 8*(3)**(1/2) + 8*np.pi/3

    print(f"Area : {total_area*ratio}\nError : {abs(total_area*ratio - answer)}\nError % : {100*abs(total_area*ratio - answer)/answer}%")

    total += total_area*ratio

    if a == m-1:
        plt.savefig(f"fig2_{n}")
    
    plt.close()

print(f"Average 10 runs {round(total/m, 5)}")
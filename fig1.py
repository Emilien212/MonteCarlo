from matplotlib import pyplot as plt
import numpy as np


t = np.linspace(0, 2*np.pi, 10000)

# first circle
x_0 = 2*np.cos(t)
y_0 = 2*np.sin(t) + 2*((12)**(1/2))/3

# second circle
x_1 = 2*np.cos(t) - (2*((12)**(1/2))/3)*np.cos(np.pi/6)
y_1 = 2*np.sin(t) - (2*((12)**(1/2))/3)*np.cos(np.pi/3)

# third circle
x_2 = 2*np.cos(t) + (2*((12)**(1/2))/3)*np.cos(np.pi/6)
y_2 = 2*np.sin(t) - (2*((12)**(1/2))/3)*np.cos(np.pi/3)

# fourth circle
x_3 = ((2*((12)**(1/2))/3) + 2)*np.cos(t)
y_3 = ((2*((12)**(1/2))/3) + 2)*np.sin(t)


total = 0
m = 10

for a in range(m):
    # Monte carlo
    n = 1000000
    In = []
    Out = []
    for _ in range(n):
        x = (np.random.random() * ((2*((12)**(1/2))/3) + 2))*2 - ((2*((12)**(1/2))/3) + 2)
        y = (np.random.random() * ((2*((12)**(1/2))/3) + 2))*2 - ((2*((12)**(1/2))/3) + 2)

        if x**2 + y**2 < ((2*((12)**(1/2))/3) + 2)**2:
            if ((x)**2 + (y - 2*((12)**(1/2))/3)**2 < 4) or ((x + (2*((12)**(1/2))/3)*np.cos(np.pi/6))**2 + (y + (2*((12)**(1/2))/3)*np.cos(np.pi/3))**2 < 4) or ((x - (2*((12)**(1/2))/3)*np.cos(np.pi/6))**2 + (y + (2*((12)**(1/2))/3)*np.cos(np.pi/3))**2 < 4):
                Out.append((x, y))
            elif y < (-7+4*(3**(1/2)))*x**2 -(2*((12)**(1/2))/3)*np.cos(np.pi/3):
                Out.append((x, y))
            else:
                In.append((x, y))
        else:
            Out.append((x, y))


    plt.plot([i[0] for i in In], [i[1] for i in In], 'g.')
    plt.plot([i[0] for i in Out], [i[1] for i in Out], 'r.')

    plt.plot(x_0, y_0, 'blue', linewidth = 4)
    plt.plot(x_1, y_1, 'blue', linewidth = 4)
    plt.plot(x_2, y_2, 'blue', linewidth = 4)
    plt.plot(x_3, y_3, 'black', linewidth = 4)

    plt.plot((2+(3**(1/2))), -(3+2*((3)**(1/2)))/3, 'y.', markersize=10)
    plt.plot(-(2+(3**(1/2))), -(3+2*((3)**(1/2)))/3, 'y.', markersize=10)
    plt.plot(0, -(2*((12)**(1/2))/3)*np.cos(np.pi/3), 'y.', markersize=10)

    plt.plot(np.linspace(-4, 4, 10000), (-7+4*(3**(1/2)))*(np.linspace(-4, 4, 10000)**2) -(2*((12)**(1/2))/3)*np.cos(np.pi/3))

    total_area = (((2*((12)**(1/2))/3) + 2)*2)**2
    ratio = len(In)/n
    answer = (32*(3**(1/2))*np.pi - 22*np.pi + 12*(3**(1/2)))/9

    print(f"Area : {total_area*ratio}\nError : {abs(total_area*ratio - answer)}\nError % : {100*abs(total_area*ratio - answer)/answer}%")
    total += total_area*ratio

    if a == m-1:
        plt.savefig(f"fig1_{n}")
    
    plt.close()
        
    

print(f"Average 10 runs {round(total/m, 5)}")
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def draw(n, radius=1.0, rotation=0.0):

    n1=2**(n+2)
    cx, cy = 0.0, 0.0

    theta = np.linspace(0, 2*np.pi, 400)
    circle_x = cx + radius * np.cos(theta)
    circle_y = cy + radius * np.sin(theta)

    angles = np.linspace(0, 2*np.pi, n1, endpoint=False) + rotation
    verts_x = cx + radius * np.cos(angles)
    verts_y = cy + radius * np.sin(angles)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(circle_x, circle_y, label='Circle')
    ax.plot(np.append(verts_x, verts_x[0]), np.append(verts_y, verts_y[0]), linewidth=2, label='Polygon')
    ax.scatter(verts_x, verts_y, s=40, color='red')
    if n<=2:
        for i, (x, y) in enumerate(zip(verts_x, verts_y), start=1):
            ax.text(x*1.05, y*1.05, chr(64+i), fontsize=9, ha='center', va='center')
    # ax.text(cx*1.05, cy*1.05, f'θ/{2**(n+1)}')
    ax.plot([cx - radius, cx + radius], [cy, cy], color='gray', linestyle='--')
    ax.plot([cx, cx], [cy - radius, cy + radius], color='gray', linestyle='--')

    parts_per_quadrant = 2 ** (int(np.log2(n1)) - 1)
    angle_step = (np.pi / 2) / parts_per_quadrant
    for q in range(4):
        start_angle = q * (np.pi / 2)   
        for i in range(1, parts_per_quadrant):
            ang = start_angle + i * angle_step
            x_end = cx + radius * np.cos(ang)
            y_end = cy + radius * np.sin(ang)
            ax.plot([cx, x_end], [cy, y_end], color='gray', linestyle=':', linewidth=1)

    ax.set_aspect('equal', adjustable='box')
    margin = radius * 0.2
    ax.set_xlim(cx - radius - margin, cx + radius + margin)
    ax.set_ylim(cy - radius - margin, cy + radius + margin)
    ax.set_title(f"Circle with {n1}-sided inscribed polygon and {parts_per_quadrant} quadrant subdivisions")
    ax.axis('off')
    if n < 6:
        ax.legend()
    plt.show()

while True:
    
    n = input('Enter the Value of n: ')
    try:
        n = int(n)
    except ValueError:
        if n == 'oo':
            pass
        else:
            print('Wrong Input!')
    try:
        if n<=1024:
            x = symbols('x')
            ans = eval(str(4*(limit((2**x)*(sin((np.pi/4)/2**x)), x,n))))
            print(f'π = {ans}')
        else:
            print('Enter a value smaller than 1024 or oo')
    except Exception as e:
        x = symbols('x')
        ans = eval(str(4*(limit((2**x)*(sin((np.pi/4)/2**x)), x,n))))
        print(f'π = {ans}')
    try:
        if n<=10:
            draw(n=n, radius=1.0, rotation=np.pi/(2**(n+2)))
    except Exception as e:
        pass

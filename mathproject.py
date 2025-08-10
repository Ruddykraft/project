import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def draw_inscribed_polygon(n=5, radius=1.0, center=(0.0, 0.0), rotation=0.0, save_path=None):

    # if n < 3:
    #     raise ValueError("n must be >= 3 for a polygon.")
   
    theta = np.linspace(0, 2*np.pi, 400)
    circle_x = center[0] + radius * np.cos(theta)
    circle_y = center[1] + radius * np.sin(theta)

    
    angles = np.linspace(0, 2*np.pi, n, endpoint=False) + rotation
    verts_x = center[0] + radius * np.cos(angles)
    verts_y = center[1] + radius * np.sin(angles)


    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(circle_x, circle_y, label='Circle')  # Circle
    ax.plot([center[0] - radius, center[0] + radius], [center[1], center[1]], color='grey', linestyle='--')
    ax.plot([center[1], center[1]], [center[0] - radius, center[0] + radius], color='grey', linestyle='--')
    ax.plot(np.append(verts_x, verts_x[0]), np.append(verts_y, verts_y[0]), 
            linewidth=2, label=f'{n}-sided Polygon')  # Polygon
    ax.scatter(verts_x, verts_y, s=40, color='red')  # Vertices

    
    for i, (x, y) in enumerate(zip(verts_x, verts_y), start=1):
        ax.text(x*1.05, y*1.05, str(i), fontsize=10, ha='center', va='center')

    ax.set_aspect('equal', adjustable='box')
    margin = radius * 0.2
    ax.set_xlim(center[0] - radius - margin, center[0] + radius + margin)
    ax.set_ylim(center[1] - radius - margin, center[1] + radius + margin)
    ax.set_title(f"Circle (r={radius}) with {n}-sided inscribed polygon")
    ax.axis('off')
    ax.legend()
    plt.show()

# draw_inscribed_polygon(n=3, radius=1.0, rotation=np.pi/2)  
# draw_inscribed_polygon(n=4, radius=1.0, rotation=np.pi/4)   
while True:
    n = int(input())
    x = symbols('x')
    ans = eval(str(4*(limit((2**x)*(sin((np.pi/4)/2**x)), x,n))))
    print(ans)
    draw_inscribed_polygon(n=n + 3, radius=1.0, rotation=np.pi/(2**(n+2)))                     
# for i in range(10):
    
#     draw_inscribed_polygon(n=int(input()))

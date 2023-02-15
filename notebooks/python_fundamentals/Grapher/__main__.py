# -*- coding: utf-8 -*-
"""Draw a matplotlib figure onto a Tk canvas

This is based on code in:
https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_canvas_sgskip.html
Which is in turn inspired by matplotlib source: 
lib/matplotlib/backends/backend_tkagg.py
"""

import matplotlib.pyplot as plt
from math import pi, sin, cos

import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg


def draw_figure(canvas, mu, loc=(0, 0)):
    """Draws the plot"""
    
    # this is the overall Figure and the Axes object
    fig_1, ax_1 = plt.subplots(1,1, figsize = (9.,4.5)) 
    fig_1.set_label('Sin-Cos Plot')
    
    # Plotting the data...
    titles, x, y1, y2, y3 = sin_blend(mu)
    ax_1.plot(x, y1, '-', x, y2, '-', x, y3, '-')
    
    # add gridlines & legend
    ax_1.grid(True)
    ax_1.legend(titles[1:])

    
    figure_canvas_agg = FigureCanvasAgg(fig_1)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = fig_1.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo


def sin_blend(mu):
    """Create the figure we desire to add to an existing canvas (using matplotlib.pyplot)
    It returns three plots based on one x-axis series
    """
    #Generate data
    x = [0.025 * float(i) for i in range(101)]
    y1 = [sin(pi * i) for i in x]
    y2 = [cos(pi * i) for i in x]
    y3 = [mu * cos(2 * pi * i) + (1.0-mu) * sin(pi * i) for i in x]
    
    titles = ('x', 'sin(\u03C0x)', 'cos(\u03C0x)', '{:4.2f}cos(2\u03C0x) + {:4.2f}sin(\u03C0x)'.format(mu, 1 - mu))
    return (titles, x, y1, y2, y3)


def main():
    
    mu = 0.4  # default value

    # === Create a canvas with Tkinter ===
    w, h = 700, 350
    window = tk.Tk()
    window.title("A figure in a canvas")
    # --- Define top and bottom frames -----------------
    top_frame = tk.Frame(window)
    top_frame.pack()
    
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side = tk.BOTTOM)

    # --- Define elements in top frame -------------------
    lbl = tk.Label(top_frame, text="Scale Factor (in range 0.0 - 1.0)")
    lbl.pack(side=tk.LEFT)
    sf = tk.Entry(top_frame, width=10)
    sf.insert(tk.END, "{:4.2f}".format(mu))
    sf.pack(side=tk.LEFT)
    #print('lbl type', type(lbl))

    def clicked():
        # We have to set the photo as a global variable because 
        # otherwise it will be deleted on exiting the function
        global fig_1_photo  
        fig_1_photo = draw_figure(canvas, float(sf.get()))
    
    btn = tk.Button(top_frame, text="Plot", command=clicked)
    btn.pack(side=tk.LEFT)
    
    # --- Define elements in bottom frame -----------------
    canvas = tk.Canvas(bottom_frame, width=w, height=h)
    canvas.pack()
    # === End of Canvas creation ===========

    loc = (0,0)
    fig_1_photo = draw_figure(canvas, mu, loc)
    #canvas.update()
    
    
    # Add more elements to the canvas, potentially on top of the figure
    canvas.create_text(350, 135, text="This demonstrates how you can \ngenerate plots with tkinter", anchor="s")
        
    # Let Tk take over to generate the GUI
    window.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    main()

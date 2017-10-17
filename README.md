# CS510 CW 7

**Author(s):** **Chelsea Parlett-Pelleriti and Alice Wong**

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-07-YOURNAME.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-07-YOURNAME)

## Specification

1. Take a look at the [Screenshot Gallery](http://matplotlib.org/users/screenshots.html) for ```matplotlib```, as well as the [matplotlib Gallery](http://matplotlib.org/gallery.html) to get a feel for what the most used plotting library in python can do. We will be barely scratching the surface of its functionality in this class, so keep these references handy for future use.
1. Take a look at the [matplotlib Tutorial](http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html). It will be a useful reference for the rest of the classwork.
1. Create a Jupyter notebook ```matplotlib-tutorial.ipynb``` that imports ```matplotlib.pyplot as plt```. (It used to be necessary to include the magic line ```%matplotlib inline``` after you import matplotlib to render plots correctly inside the notebook itself, but this should no longer be needed.) Create a section "Simple plot" and work through the example in section 1.4.2 (Simple plot) of the tutorial. Make sure you understand how to draw curves, set styles of curves, set limits and ticks, set labels, set axis positions, create legends, create annotations, and tweak details. Keep in mind that the goal is to create publication-quality work. Your plots should be beautiful, but also informative. Be sure to code the solution yourself after thinking about it carefully and reading documentation - do not simply copy and paste the code.
1. In the "Other types of plots" section of the tutorial, complete the following exercises. Note that the [matplotlib Documentation](http://matplotlib.org/api/pyplot_api.html) is extensive, but can be difficult to read. It is usually better to find [examples](http://matplotlib.org/examples/index.html) to see how to use graphics packages productively.
    * Contour plot
    * Imshow
    * 3D Plots
1. Copy your CW06 complex plane modules into CW07. Work with your partner to create a class ```JuliaPlane``` with the functionality of HW06 - use one of your homeworks as the starting code, and modify it as needed. In the new ```JuliaPlane``` class, create a new method ```show(self)``` that plots an image of the complex plane after it has been transformed by the julia function.
    * Recall: it should be a plane of positive integers. Treat these numbers as grayscale values for ```imshow``` in ```matplotlib```.
    * Hint: Use the colormap ```plt.cm.hot``` for nice results. Feel free to try other colormaps for fun.
    * Hint: Try a ```bicubic``` interpolation to smooth out the plot a bit.
    * Hint: Use the ```extent``` keyword to set the axes labels properly.
    * Hint: Remember to put a plot label that indicates the chosen ```c``` value for the current ```JuliaPlane``` instance.
1. Create a Jupyter notebook ```julia-sets.ipynb``` that imports your code for ```JuliaPlane```. Create and plot sets with the following ```c``` values. Try other ```c``` values to see what happens - comment on your findings.
    * ```c = 0```
    * ```c = -1```
    * ```c = 0.3```
    * ```c = -1.037 + 0.17j```
    * ```c = -0.624 + 0.435j```
    * ```c = -0.8 + 0.2j```
    * ```c = -0.835 - 0.2321j```


## Assessment

It was interesting to see the patterns that were created by the different values of c. It seems like integers have more circular elements to the graphs, whereas complex and non whole numbers look more bumpy and like fractals. To be honest I'm not sure why these are occuring, but I can see patterns as I test out different values of c.

This project was difficult since I wasn't sure what my output should look like. In past assignments I knew what should come out of my code, so if somehting didn't look right, I'd notice and fix it. Since I don't have much practical experience with complex numbers, this wasn't the case here.


## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Chelsea Parlett-Pelleriti, and Alice Wong**

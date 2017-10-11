import cplane_np
import numpy as np
import matplotlib.pyplot as plt

# In your python module cplane-np-hw.py, create a function julia(c, max=100) that takes a complex parameter c and an optional positive integer max, and returns a function specified by the following algorithm:
# The returned function should take one complex parameter z as an input, and return one positive integer as an output.
# If the input number z has a magnitude abs(z) larger than 2, the function should output the integer 1.
# Otherwise, set a counter n=1.
# Increment n by 1, then transform the input z according to the formula z = z**2 + c. Check the resulting magnitude abs(z): If the magnitude now exceeds 2, then return the value of n; If the magnitude does not yet exceed 2, repeat this step.
# If the positive integer max is reached before the magnitude of z exceeds 2, the preceding loop should abort and return the output integer 0.

# Create a new class JuliaPlane that subclasses your ArrayComplexPlane class. We are going to extend that class with interesting functionality:
# Change the __init__ method to accept only a single argument c, which is a complex number. Have the init call the ___init___ method of the parent class, assuming the default values xmin=ymin=-2 and xmax=ymax=2 and xlen=ylen=1000. Have the init call also immediately apply the function julia to the plane, using the input argument c used to initialize the class. (Note that the transformed plane will now be a 2D array of positive integers, and fs will now contain one function.)
# Change the refresh method to accept only a single argument c, which is a complex number. Have this function regenerate a fresh plane and empty the fs list as before, but then apply the function julia to the plane with the updated argument c analogously to the initialization. (The zoom and apply methods should work the same as before.)
# Find a way to test that the resulting output is correct. (Hint: What happens when c=0?)
# Create a new method toCSV(self, filename) that exports the transformed plane of integers to a .csv file in a sensible way. Make sure that the file stores all the needed parameters for the plane, including the value of c and the current zoom settings (xmin, etc.).
# Create a new method fromCSV(self, filename) that imports a .csv file previously exported by the class. This method should reset the plane parameters to match the settings in the file, and refresh the plane array to the values stored in the .csv file directly.

# In a module test_cplane-np-hw.py write suitable test functions to verify that you accomplished your goals correctly.
def julia(c, max = 1000):
    def func510(z):
        if abs(z) > 2:
            return 1
        n = 1
        mag = abs(z)
        while mag < 2 and n < max:
            z = z**2 + c
            mag = abs(z)
            n += 1
        if n == max:
            return 0
        else:
            return n
    return func510
            
class JuliaPlane(cplane_np.ArrayComplexPlane):
    def gen_plane(self,c):
        '''make it plane'''
        self.plane =  []
        #xs-----------------------------------------------------------------------------
        self.dx = (self.c[1]-self.c[0])/(self.c[2]-1)
        multi = np.array(list(range(0,self.c[2]))*self.c[-1])  #array with index + 1, ylen times
        multi = multi * self.dx #multiply by dx to get how much to add
        multi = self.c[0] + multi
        #ys-----------------------------------------------------------------------------
        self.dy = (self.c[-2]-self.c[-3])/(self.c[-1]-1)
        vec_y = np.array(list(range(0,self.c[-1])))
        vec_y = np.repeat(vec_y,self.c[2])
        vec_y =  (self.c[-3] + vec_y*self.dy)*1j

        #together------------------------------------------------------------------------
        self.plane = multi + vec_y
        print(self.plane.reshape(self.c[2],self.c[-1]).transpose())
        return self.plane.reshape(self.c[2],self.c[-1]).transpose()
    def __init__(self,c = (-2,2,100,-2,2,100)):
        self.c = c
        self.fs = []
        print("init fx")
        self.plane = self.gen_plane(self.c)
#         self.plane = np.vectorize(julia(self.plane))
        f = np.vectorize(julia(0))
        self.plane =  f(self.plane)
        print("------------------------------")
        print(self.plane)
    def toCSV(self):
        print("PLA")
        print(self.plane)
        np.savetxt("510.csv",self.plane, header = 'xmax is: ' + str(self.c[0]) + 'xmin is: ' + str(self.c[1]) + 'xlen is: ' + str(self.c[2]) +
                   'ymax is: ' + str(self.c[3]) + 'ymin is: ' + str(self.c[4]) + 'ylen is: ' + str(self.c[5])) 
    def fromCSV(self):
        csv = np.array(list(i  for i in (open('510.csv', 'rb'))))
        print(csv)
#         self.c = csv[1]
    def show(self):
        #need x of  reals, y of complex, but now they're all reals...
        print(self.plane)
        plt.imshow(self.plane,  cmap = plt.cm.hot, interpolation = 'bicubic', extent = [self.c[0], self.c[1], self.c[3], self.c[4]])
        
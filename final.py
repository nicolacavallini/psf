# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from matplotlib import cm

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    lambda_ = 633.e-9

    alpha_ = 30.*np.pi

    w20 = 5*lambda_

    k = 2.*np.pi/lambda_

    A = lambda x : np.sqrt((k*w20)**2.+6*np.pi*alpha_ * x)

    B = lambda y : np.sqrt((k*w20)**2.+6*np.pi*alpha_ * y)

    omega = {}

    omega[4] = lambda a, b : (a-k*w20)**2. + (b-k*w20)**2

    omega[3] = lambda a, b : (a-k*w20)**2. + (b+k*w20)**2

    omega[2] = lambda a, b : (a+k*w20)**2. + (b-k*w20)**2

    omega[1] = lambda a, b : (a+k*w20)**2. + (b+k*w20)**2

    x,y = np.meshgrid(np.linspace(-10,60,1000),
                      np.linspace(-10,60,1000))

    threshold = 9*alpha_**2.

    is_inside = {}

    for key, function in omega.items():
        is_inside[key] = function(A(x),B(y)) <= threshold


    condition = np.logical_and(np.logical_and(is_inside[1],is_inside[2]),
                               np.logical_and(is_inside[3],is_inside[4]))

    #condition = is_inside[1]

    image = 255*np.ones((1000,1000,3))
    image[condition] = np.array([255,0,0])

    condition = np.logical_and(np.logical_and(is_inside[1]==False,is_inside[2]),
                               np.logical_and(is_inside[3],is_inside[4]))

    image[condition] = np.array([0,255,0])


    condition = np.logical_and(np.logical_and(is_inside[1]==False,is_inside[2]==False),
                               np.logical_and(is_inside[3],is_inside[4]))

    image[condition] = np.array([0,0,255])

    condition = np.logical_and(np.logical_and(is_inside[1]==False,is_inside[2]),
                               np.logical_and(is_inside[3]==False,is_inside[4]))

    image[condition] = np.array([255,255,0])

    condition = np.logical_and(np.logical_and(is_inside[1]==False,is_inside[2])==False,
                               np.logical_and(is_inside[3]==False,is_inside[4]))

    image[condition] = np.array([255,0,255])




    print(image.shape)

    #norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())

    fig, ax = plt.subplots()
    ax.imshow(np.flip(image,0))
    plt.axis('equal')
    plt.show()
    #
    #
    #
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    #
    #
    # surf = ax.plot_surface(x,y,omega[4](A(x),B(y)) , cmap=cm.coolwarm,
    #                    linewidth=0, antialiased=False)
    #
    # plt.show()

    #omega4(A(x),B(y)) <= 9*alpha_**2.



    #fig, ax = plt.subplots()
    #ax.imshow(o4)
    #plt.show()

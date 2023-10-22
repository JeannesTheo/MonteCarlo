import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


"""
    Method written by Donal Byrne to show the value function for the blackjack game
"""
def plot_blackjack_values(V):
    def get_Z(x, y, usable_ace):
        if (x,y,usable_ace) in V:
            return V[x,y,usable_ace]
        else:
            return 0

    def get_figure(usable_ace, ax):
        x_range = np.arange(11, 22)
        y_range = np.arange(1, 11)
        X, Y = np.meshgrid(x_range, y_range)
        
        Z = np.array([get_Z(x,y,usable_ace) for x,y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, vmin=-1.0, vmax=1.0)
        ax.set_xlabel('Player\'s Current Sum')
        ax.set_ylabel('Dealer\'s Showing Card')
        ax.set_zlabel('State Value')
        ax.view_init(ax.elev, -120)

    fig = plt.figure(figsize=(20, 20))
    ax = fig.add_subplot(211, projection='3d')
    ax.set_title('Usable Ace')
    get_figure(True, ax)
    ax = fig.add_subplot(212, projection='3d')
    ax.set_title('No Usable Ace')
    get_figure(False, ax)
    plt.show()


"""
    Method written by Donal Byrne to show the policy for the blackjack game
    Slightly adapted by us, to display a clearer plot
"""
def plot_policy(policy):
    def get_Z(x,y, usable_ace):  # Swapped x and y
        if (x, y, usable_ace) in policy:  # Swapped x and y
            return policy[(x, y, usable_ace)]  # Swapped x and y
        else:
            return 1

    def get_figure(usable_ace, ax):
        x_range = np.arange(1,11)
        y_range = np.arange(21,9,-1)
        X,Y = np.meshgrid(x_range, y_range)  # Swapped X and Y
        Z = np.array([get_Z(x,y,usable_ace) for x,y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
        surf = ax.imshow(Z, cmap=plt.get_cmap('Pastel2', 2), vmin=0, vmax=1, extent=[0.5, 10.5,9.5, 21.5])
        plt.xticks(x_range)  # Swapped x_range with y_range
        plt.yticks(y_range)  # Swapped x_range with y_range
        # plt.gca().invert_yaxis()
        ax.set_xlabel('Dealer\'s Showing Card')  # Swapped x and y labels
        ax.set_ylabel('Player\'s Current Sum')  # Swapped x and y labels
        ax.grid(color='w', linestyle='-', linewidth=1)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.1)
        cbar = plt.colorbar(surf, ticks=[0,1], cax=cax)
        cbar.ax.set_yticklabels(['0 (STICK)', '1 (HIT)'])
        cbar.ax.invert_yaxis()

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(121)
    ax.set_title('Usable Ace')
    get_figure(True, ax)
    ax = fig.add_subplot(122)
    ax.set_title('No Usable Ace')
    get_figure(False, ax)
    plt.show()
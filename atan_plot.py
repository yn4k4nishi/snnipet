#!/usr/bin python3
import numpy as np
import matplotlib.pyplot as plt

w_0 = 100
nu = 0.01
N = 1e6
q = 3
epsilon_0 = 1.2
m = 1e-4


def main():
    w = np.linspace(0, 200, 1e5)
    theta_1 = np.arctan( w * nu / (w_0**2 - w**2 ) )

    c = 50**2 #N * q**2 / epsilon_0 / m
    theta_2 = np.arctan( w * nu / (w_0**2 - w**2 + c ) )

    theta = theta_1 - theta_2

    plt.plot( w, theta_1 )
    plt.plot( w, theta_2 )
    plt.plot( w, theta )
    plt.show()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import numpy as np

class system:
    """Class to construct particle based systems for simulation.

    Attributes:
        xyz (:obj:`ndarray [nbeads x 3]`): Coordinates for each bead in system
    """
    def __init__(self):
        self.xyz = None # numpy array with the coordinates of each bead

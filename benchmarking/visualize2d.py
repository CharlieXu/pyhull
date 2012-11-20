#!/usr/bin/env python

"""
Generates the Delaunay triangulation and convex hull for a random set of 2D
points and plot them. For testing purposes.
"""

from __future__ import division

__author__ = "shyuepingong"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "shyuep@gmail.com"
__status__ = "Beta"
__date__ = "11/19/12"

import itertools

import numpy as np

from pyhull.delaunay import DelaunayTri
from pyhull.convex_hull import ConvexHull
from pyhull.voronoi import VoronoiTess

import matplotlib.pyplot as plt

points = np.random.randn(30, 2)


for pt in points:
    plt.plot(pt[0], pt[1], 'ro')

d = DelaunayTri(points)

for s in d.simplices:
    for c1, c2 in itertools.combinations(s.coords, 2):
        plt.plot([c1[0],c2[0]], [c1[1], c2[1]], 'k-')

d = ConvexHull(points)

for s in d.simplices:
    for c1, c2 in itertools.combinations(s.coords, 2):
        plt.plot([c1[0],c2[0]], [c1[1], c2[1]], 'b-')

d = VoronoiTess(points)
points = d.points
vertices = d.vertices
for r in d.regions:
    for i in xrange(len(r)):
        ind1 = r[i]
        ind2 = r[(i+1) % len(r)]
        if ind1 and ind2:
            c1 = vertices[ind1]
            c2 = vertices[ind2]
            plt.plot([c1[0],c2[0]], [c1[1], c2[1]], 'g-.')

plt.show()
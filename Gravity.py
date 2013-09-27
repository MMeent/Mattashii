#!/usr/bin/env python

import sys
import math
import random
from collections import defaultdict

WIDTH, HEIGHT = 900, 600

PLANETS = 3

# The density of the planets - used to calculate their mass
# from 
DENSITY = 0.001

# The gravity coefficient, for this universe
GRAVITYSTRENGTH = 1.e4

# The global list of planets
g_listOfPlanets = []

class State:
  """Class representing position and velocity."""
  def __init__(self, x, y, vx, vy):
    self._x, self._y, self._vx, self._vy = x, y, vx, vy

  def __repr__(self):
    return 'x:{x} y:{y} vx:{vx} vy:{vy}'.format(
      x=self._x, y=self._y, vx=self._vx, vy=self._vy)

class Derivative:
  """Class representing velocity and acceleration."""
  def __init__(self, dx, dy, dvx, dvy):
    self._dx, self._dy, self._dvx, self._dvy = dx, dy, dvx, dvy
  def __repr__(self):
    return 'dx:{dx} dy:{dy} dvx:{dvx} dvy:{dvy}'.format(
      dx=_dv, dy=_dy, dvx=_dvx, dvy=_dvy)

class Planet:
  """Class representing a planet. The "_st" member si an instance of "State",
  carrying the planet's position and velocity - while the "_m" and "_r"
  members represent the planet's mass and radius."""
  def __init__(self):
    self._st = State(
      float(random.randint(0.,WIDTH)),
      float(random.randint(0.,HEIGHT)),
      float(random.randint(0.,300.)/100.)-1.5,
      float(random.randint(0.,300.)/100.)-1.5)
    self._r = 1.5
    self.setMassFromRadius()
    self._merged = False

  def __repr__(self):
    return repr(self._st)

  def acceleration(self, state, unused_t):
    """Calculate acceleration caused by other planets"""
    ax = 0.0
    ay = 0.0
    for p in g_listOfPlanets:
      if p is self or p._merged:
        continue # ignore ourselves and merged planets
      dx = p._st._x - state._x
      dy = p._st._y - state._y
      dsq = dx*dx + dy*dy # distance squared
      dr = math.sqrt(dsq) 
      force = GRAVITYSTRENGTH*self._m*p._m/dsq
      # accumulate acceleration...
      ax += force*dx/dr
      ay += force*dy/dr
    return (ax, ay)

  def initialDerivative(self, state, t):
    """Part of Runge-Kutta method."""
    ax, ay = self.acceleration(state, t)
    return Derivative(state._vx, state._vy, ax, ay)

  def nextDerivative(self, initialState, derivative, t, dt):
    """Part of Runge-Kutta method."""
    state = State(0., 0., 0., 0.)
    state._x = initialState._x + derivative._dx*dt
    state._y = initialState._y + derivative._dy*dt
    state._vx = initialState._vx + derivative._dvx*dt
    state._vy = initialState._vy + derivative._dvy*dt
    ax, ay = self.acceleration(state, t+dt)
    return Derivative(state._vx, state._vy, ax, ay)

  def updatePlanet(self, t, dt):
    """Tunge-Kutta 4th order solution to update planet's pos/vel"""
    a = self.initialDerivative(self._st, t)
    b = self.nextDerivative(self._st, a, t, dt*0.5)
    c = self.nextDerivative(self._st, b, t, dt*0.5)
    d = self.nextDerivative(self._st, c, t, dt)
    dxdt = 1.0/6.0 * (a._dx + 2.0*(b._dx + c._dx) + d._dx)
    dydt = 1.0/6.0 * (a._dy + 2.0*(b._dy + c._dy) + d._dy)
    dvxdt = 1.0/6.0 * (a._dvx + 2.0*(b._dvx + c._dvx) + d._dvx)
    dvydt = 1.0/6.0 * (a._dvy + 2.0*(b._dvy + c._dvy) + d._dvy)
    self._st._x = dxdt*dt
    self._st._y = dydt*dt
    self._st._vx = dvxdt*dt
    self._st._vy = dvydt*dt

  def setMassFromRadius(self):
    """From _r, set _m: The volume is (4/3)*Pi*(r^3)"""
    self._m = DENSITY*4.*math.pi*(self._r**3.)/3.

  def setRadiusFromMass(self):
    """Reversing the setMassFromRadius formula, to calculate radius form
    mass (used after merging of two planets - mass is added, and new 
    radus is calculated from this"""
    self._r = (3.*self._m/(DENSITY*4.*math.pi))**(0.3333)

def main():
  global g_listOfPlanets, PLANETS
  if len(sys.argv) == 2:
    PLANETS = int(sys.argv[1])
  
  g_listOfPlanets=[]
  for i in xrange(0, PLANETS):
    g_listOfPlanets.append(Planet())

  def planetsTouch(p1, p2):
    dx = p1._st._x - p2._st._x
    dy = p1._st._y - p2._st._y
    dsq = dx*dx + dy*dy
    dr = math.sqrt(dsq)
    return dr<=(p1._r + p2._r)

  t, dt = 0., 1.

  while True:
    t += dt
    planet = 0.
    for p in g_listOfPlanets:
      planet += 1.
      print "PLANET!!!"
    if not p._merged:
        p.updatePlanet(t,dt)
        print "p:{nr} t:{time} x:{X} y:{Y} vx:{vX} vy:{vY}".format(
          nr = planet, 
          time = t,
          X = p._st._x, 
          Y = p._st._y, 
          vX = p._st._vx, 
          vY = p._st._vy)

    for p1 in g_listOfPlanets:
      print "hi"
      if p1._merged:
        continue
      for p2 in g_listOfPlanets:
        if p1 is p2 or p2._merged:
          continue
        if planetsTouch(p1, p2):
          if p1._m < p2._m:
            p1, p2 = p2, p1
          p2._merged = True
          newvx = (p1._st._vx * p1._m + p1._st._vx * p2._m) / (p1._m + p2._m)
          newvy = (p1._st._vy * p1._m + p2._st._vy * p2._m) / (p1._m + p2._m)
          p1._m += p2._m
          p1.setRadiusFromMass()
          p1._st._vx, p1._st._vy = newvx, newvy

if __name__ == "__main__":
  main()

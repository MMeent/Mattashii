#!/usr/bin/env python

import math

class SpacialData():
    def __init__(self, x, y, z, vx, vy, vz):
        self._x, self._y, self._z = x, y, z
        self._vx, self._vy, self._vz = vx, vy, vz

    def __repr__(self):
        return "x:{x} y:{y} z:{z} vx:{vx} vy:{vy} vz:{vz}".format(
            x  = self._x, 
            y  = self._y,
            z  = self._z,
            vx = self._vx,
            vy = self._vy,
            vz = self._vz)


#TODO: Time control
#
#class TimeData
#  def __init__(self, SolarYear, SolarDay, Day, Hour)
#    self._sy, self._sd = SolarYear, SolarDay
#    self._d, self.h = Day, Hour
#
#  def __repr__(self):
#    return "Date: {date} Time: {time}".format(
#      date = self

class Derivative(object):
    def __init__(self, dx, dy, dz, dvx, dvy, dvz):
        self._dx, self._dy, self._dz = dx, dy, dz
        self._dvx, self._dvy, self._dvz = dvx, dvy, dvz
        self.ax, self.ay, self.az = 0., 0., 0.

    def __repr__(self):
        return "dx:{dx} dy:{dy} dz:{dz} dvx:{dvx} dvy:{dvy} dvz:{dvz}".format(
            dx  = self._dx,
            dy  = self._dy,
            dz  = self._dz,
            dvx = self._dvx,
            dvy = self._dvy,
            dvz = self._dvz)

class Body(object):
    def __init__(self, x, y, z, vx, vy, vz, mass):
        self._sd = SpacialData(x, y, z, vx, vy, vz)
        self._mass = mass
        self._ax, self._ay, self._az = 0., 0., 0.

    def __repr__(self):
        return " mass: {mass} \n {data}".format(
            mass = self._mass,
            data = repr(self._sd))
#todo: implement Time Control
    
    def distance(self, body):
        dx = self._st._x - body._st._x
        dy = self._st._y - body._st._y
        dz = self._st._z - body._st._z
        delta = math.sqrt(dx*dx + dy*dy + dz*dz)
        return delta
    
    def delta(a, b):
        delta = a - b
        return delta
    
    def CalcForce(self, body, Gc):
        delta = distance(body)
        force = Gc * body._mass * self._mass / (delta*delta)
        return force

    def accelerate(self, body, Gc):
        Acc = CalcForce(body, Gc)
        self._ax += force*delta(self._st._x, body._st._x)/distance(body)
        self._ay += force*delta(self._st._y, body._st._y)/distance(body)
        self._az += force*delta(self._st._z, body._st._z)/distance(body)

    def update(self, dt):
        self._x += self._vx*dt
        self._y += self._vy*dt
        self._z += self._vz*dt
        self._vx += self._ax*dt
        self._vy += self._ay*dt
        self._vz += self._az*dt
        self._ax, self._ay, self._az = 0., 0., 0.

class Sattelite(object):
    def __init__(self, x, y, z, vx, vy, vz, mass, name):
        self.body = Body(x, y, z, vx, vy, vz, mass)
        self._name = name

    def __repr__(self):
        return " Sattelite: {name} \n{data}".format(
            name = self._name,
            data = repr(self.body))

class Moon(object):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, aPressure, name):
        self.body = Body(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._pre = aPressure
        self._name = name

    def __repr__(self):
        return " Moon: {name} \n radius: {rad} \n pressure: {pre} \n{data}".format(
            name = self._name,
            rad = self._rad,
            pre = self._pre,
            data = repr(self.body))

class Planet(object):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, aPressure, name):
        self.body = Body(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._pre = aPressure
        self._name = name

    def __repr__(self):
        return " Planet: {name} \n radius: {rad} \n pressure: {pre} \n{data}".format(
            name = self._name,
            rad = self._rad,
            pre = self._pre,
            data = repr(self.body))


class Star(object):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, name):
        self.body = Body(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._name = name

    def __repr__(self):
        return " Star: {name} \n radius: {rad} \n{data}".format(
            name = self._name,
            rad = self._rad,
            data = repr(self.body))

class Astroid(object):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, name):
        self.body = Body(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._name = name

    def __repr__(self):
        return " Astroid: {name} \n radius: {rad} \n{data}".format(
            name = self._name,
            rad = self._rad,
            data = repr(self.body))

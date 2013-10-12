#!/usr/bin/env python

import math

class SpatialData():
    def __init__(self, x, y, z, vx, vy, vz):
        self.body.sd._x, self.body.sd._y, self.body.sd._z = x, y, z
        self.body.sd._vx, self.body.sd._vy, self.body.sd._vz = vx, vy, vz

    def __repr__(self):
        return "x:{x} y:{y} z:{z} vx:{vx} vy:{vy} vz:{vz}".format(
            x  = self.body.sd._x,
            y  = self.body.sd._y,
            z  = self.body.sd._z,
            vx = self.body.sd._vx,
            vy = self.body.sd._vy,
            vz = self.body.sd._vz)


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
        self.body.ax, self.body.ay, self.body.az = 0., 0., 0.

    def __repr__(self):
        return "dx:{dx} dy:{dy} dz:{dz} dvx:{dvx} dvy:{dvy} dvz:{dvz}".format(
            dx  = self._dx,
            dy  = self._dy,
            dz  = self._dz,
            dvx = self._dvx,
            dvy = self._dvy,
            dvz = self._dvz)

class Body(SpatialData):
    def __init__(self, x, y, z, vx, vy, vz, mass):
        super(SpatialData, self).__init__(x, y, z, vx, vy, vz)
        self.body.mass = mass
        self.body.ax, self.body.ay, self.body.az = 0., 0., 0.

    def __repr__(self):
        return " mass: {mass} \n {data}".format(
            mass = self.body.mass,
            data = repr(self.body.sd))
#todo: implement Time Control
    
    def distance(self, body):
        dx = self.body.st._x - body.body.st._x
        dy = self.body.st._y - body.body.st._y
        dz = self.body.st._z - body.body.st._z
        delta = math.sqrt(dx*dx + dy*dy + dz*dz)
        return delta
    
    def delta(a, b):
        delta = a - b
        return delta
    
    def CalcForce(self, body, Gc):
        delta = distance(body)
        force = Gc * body.mass * self.body.mass / (delta*delta)
        return force

    def accelerate(self, body, Gc):
        Acc = CalcForce(body, Gc)
        self.body._ax += force*delta(self.body.st._x, body.body.st._x)/distance(body)
        self.body._ay += force*delta(self.body.st._y, body.body.st._y)/distance(body)
        self.body._az += force*delta(self.body.st._z, body.body.st._z)/distance(body)

    def update(self, dt):
        self.body.sd._x += self.body.sd._vx*dt
        self.body.sd._y += self.body.sd._vy*dt
        self.body.sd._z += self.body.sd._vz*dt
        self.body.sd._vx += self.body._ax*dt
        self.body.sd._vy += self.body._ay*dt
        self.body.sd._vz += self.body._az*dt
        self.body._ax, self.body._ay, self.body._az = 0., 0., 0.

class Sattelite(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, name):
        super(Body, self).__init__(x, y, z, vx, vy, vz, mass)
        self._name = name

    def __repr__(self):
        return " Sattelite: {name} \n{data}".format(
            name = self._name,
            data = super(Body, self).__repr__())

class Moon(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, aPressure, name):
        super(Body, self).__init__(x, y, z, vx, vy, vz, mass)
        self.body._rad = radius
        self._pre = aPressure
        self._name = name

    def __repr__(self):
        return " Moon: {name} \n radius: {rad} \n pressure: {pre} \n{data}".format(
            name = self._name,
            rad = self.body._rad,
            pre = self._pre,
            data = super(Body, self).__repr__())

class Planet(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, aPressure, name):
        super(Body, self).__init__(x, y, z, vx, vy, vz, mass)
        self.body._rad = radius
        self._pre = aPressure
        self._name = name

    def __repr__(self):
        return " Planet: {name} \n radius: {rad} \n pressure: {pre} \n{data}".format(
            name = self._name,
            rad = self.body._rad,
            pre = self._pre,
            data = super(Body, self).__repr__())


class Star(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, name):
        super(Body, self).__init__(x, y, z, vx, vy, vz, mass)
        self.body._rad = radius
        self._name = name

    def __repr__(self):
        return " Star: {name} \n radius: {rad} \n{data}".format(
            name = self._name,
            rad = self.body._rad,
            data = super(Body, self).__repr__())

class Astroid(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, name):
        super(Body, self).__init__(x, y, z, vx, vy, vz, mass)
        self.body._rad = radius
        self._name = name

    def __repr__(self):
        return " Astroid: {name} \n radius: {rad} \n{data}".format(
            name = self._name,
            rad = self.body._rad,
            data = super(Body, self).__repr__())

#!/usr/bin/env python

import math

class SpatialData(object):
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

class Body(SpatialData):
    def __init__(self, x, y, z, vx, vy, vz, mass):
        super(Body, self).__init__(x, y, z, vx, vy, vz)
        self.mass = mass
        self.ax, self.ay, self.az = 0., 0., 0.

    def __repr__(self):
        return " mass: {mass} \n {data}".format(
            mass = self.mass,
            data = super(Body, self).__repr__())

    def serialize(self):
        return { "body" : {
                 "SpatialData" : { 
                     "x" : self._x,
                     "y" : self._y,
                     "z" : self._z,
                     "vx" : self._vx,
                     "vy" : self._vy,
                     "vz" : self._vz },
                 "mass" : self.mass } }

#todo: implement Time Control
    
    def distance(self, body):
        dx = self._x - body._x
        dy = self._y - body._y
        dz = self._z - body._z
        delta = math.sqrt(dx*dx + dy*dy + dz*dz)
        return delta
    
    def delta(a, b):
        delta = a - b
        return delta
    
    def CalcForce(self, body, Gc):
        delta = distance(body)
        force = Gc * body.mass * self.mass / (delta*delta)
        return force

    def accelerate(self, body, Gc):
        force = CalcForce(body, Gc)
        self._ax += force*delta(self._x, body._x)/distance(body)
        self._ay += force*delta(self._y, body._y)/distance(body)
        self._az += force*delta(self._z, body._z)/distance(body)

    def update(self, dt):
        self._x += self._vx*dt
        self._y += self._vy*dt
        self._z += self._vz*dt
        self._vx += self._ax*dt
        self._vy += self._ay*dt
        self._vz += self._az*dt
        self._ax, self._ay, self._az = 0., 0., 0.

class Satellite(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, name):
        super(Satellite, self).__init__(x, y, z, vx, vy, vz, mass)
        self._name = name

    def __repr__(self):
        return " Sattelite: {name} \n{data}".format(
            name = self._name,
            data = super(Satellite, self).__repr__())

    def serialize(self):
        data = super(Satellite, self).serialize()
        data.update({ "name" : self._name })
        return data

    @staticmethod
    def deserialize(data):
        bdata = data["body"]
        spdata = bdata["SpatialData"]
        return Satellite(spdata["x"],
                         spdata["y"],
                         spdata["z"],
                         spdata["vx"],
                         spdata["vy"],
                         spdata["vz"],
                         bdata["mass"],
                         data["name"])

class Moon(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, aPressure, name):
        super(Moon, self).__init__(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._pre = aPressure
        self._name = name

    def __repr__(self):
        return " Moon: {name} \n radius: {rad} \n pressure: {pre} \n{data}".format(
            name = self._name,
            rad = self._rad,
            pre = self._pre,
            data = super(Moon, self).__repr__())

    def serialize(self):
        data = super(Moon, self).serialize()
        data.update({ "body" : { "radius" : self._rad },
                      "name" : self._name,
                      "SurfacePressure" : self._pre,
                    })
        return data

    @staticmethod
    def deserialize(data):
        bdata = data["body"]
        spdata = bdata["SpatialData"]
        return Moon(spdata["x"],
                    spdata["y"],
                    spdata["z"],
                    spdata["vx"],
                    spdata["vy"],
                    spdata["vz"],
                    bdata["mass"],
                    bdata["radius"],
                    data["SurfacePressure"],
                    data["name"])


class Planet(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, aPressure, surTemp, name):
        super(Planet, self).__init__(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._pre = aPressure
        self._temp = surTemp
        self._name = name

    def __repr__(self):
        return " Planet: {name} \n radius: {rad} \n pressure: {pre} \n{data}".format(
            name = self._name,
            rad = self._rad,
            pre = self._pre,
            data = super(Planet, self).__repr__())


    def serialize(self):
        data = super(Planet, self).serialize()
        data.update({ "body" : { "radius" : self._rad },
                      "name" : self._name,
                      "SurfacePressure" : self._pre,
                      "SurfaceTemperature" : self._temp
                    })
        return data

    @staticmethod
    def deserialize(data):
        bdata = data["body"]
        spdata = bdata["SpatialData"]
        return Planet(spdata["x"],
                      spdata["y"],
                      spdata["z"],
                      spdata["vx"],
                      spdata["vy"],
                      spdata["vz"],
                      bdata["mass"],
                      bdata["radius"],
                      data["SurfacePressure"],
                      data["SurfaceTemperature"],
                      data["name"])


class Star(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, surTemp, name):
        super(Star, self).__init__(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._temp = surTemp
        self._name = name

    def __repr__(self):
        return " Star: {name} \n radius: {rad} \n{data}".format(
            name = self._name,
            rad = self._rad,
            data = super(Star, self).__repr__())

    def serialize(self):
        data = super(Star, self).serialize()
        data.update({ "body" : { "radius" : self._rad },
                      "name" : self._name,
                      "SurfaceTemperature" : self._temp
                    })
        return data

    @staticmethod
    def deserialize(data):
        bdata = data["body"]
        spdata = bdata["SpatialData"]
        return Star(spdata["x"],
                    spdata["y"],
                    spdata["z"],
                    spdata["vx"],
                    spdata["vy"],
                    spdata["vz"],
                    bdata["mass"],
                    bdata["radius"],
                    data["SurfaceTemperature"],
                    data["name"])


class Asteroid(Body):
    def __init__(self, x, y, z, vx, vy, vz, mass, radius, name):
        super(Star, self).__init__(x, y, z, vx, vy, vz, mass)
        self._rad = radius
        self._name = name

    def __repr__(self):
        return " asteroid: {name} \n radius: {rad} \n{data}".format(
            name = self._name,
            rad = self._rad,
            data = super(Star, self).__repr__())
    def serialize(self):
        data = super(Moon, self).serialize()
        data.update({ "body" : { "radius" : self._rad },
                      "name" : self._name,
                    })
        return data

    @staticmethod
    def deserialize(data):
        bdata = data["body"]
        spdata = bdata["SpatialData"]
        return Asteroid(spdata["x"],
                       spdata["y"],
                       spdata["z"],
                       spdata["vx"],
                       spdata["vy"],
                       spdata["vz"],
                       bdata["mass"],
                       bdata["radius"],
                       data["name"])

if __name__ == "__main__":
    print "help me"
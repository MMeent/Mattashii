__author__ = 'matthias'

def GravityConstant():
    return 6.67384e-11

def writeDTime():
    return 3600

def timeStep():
    return 1

def Objects():
    data = [
        {
            "name": "Sun",
            "type": "Star",
            "SurfaceTemperature": 5.778,
            "radius": 696342000,
            "mass": 1.9891e+30,
            "x": 0.0,
            "y": 0.0,
            "z": 0.0,
            "vx": 0.0,
            "vy": 0.0,
            "vz": 0.0
        },
        {
            "name": "Mercury",
            "type": "Planet",
            "SurfaceTemperature": 340,
            "SurfacePressure": 0,
            "radius": 2439.7,
            "mass": 3.3022e+23,
            "x": 1.0,
            "y": 2.0,
            "z": 3.0,
            "vx": 1.0,
            "vy": 2.0,
            "vz": 3.0
        },
        {
            "name": "Venus",
            "type": "Planet",
            "SurfaceTemperature": 737,
            "SurfacePressure": 9200000,
            "radius": 6051.8,
            "mass": 4.8676e+24,
            "x": 1.0,
            "y": 2.0,
            "z": 3.0,
            "vx": 1.0,
            "vy": 2.0,
            "vz": 3.0
        },
        {
            "name": "Earth",
            "type": "Planet",
            "SurfaceTemperature": 288,
            "SurfacePressure": 101325,
            "radius": 6371,
            "mass": 5.97219e+24,
            "x": 1.0,
            "y": 2.0,
            "z": 3.0,
            "vx": 3.0,
            "vy": 2.0,
            "vz": 1.0
        },
        {
            "name": "Mars",
            "type":"Planet",
            "SurfaceTemperature": 210,
            "SurfacePressure": 636,
            "radius": 3396.2,
            "mass": 6.4185e+23,
            "x": 3.0,
            "y": 2.0,
            "z": 1.0,
            "vx": 3.0,
            "vy": 2.0,
            "vz": 1.0
        }
    ]
    return data
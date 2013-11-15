__author__ = 'matthias'
import controllers
import default

def Objects(jsonfile):
    json = controllers.openJson(jsonfile)
    objs = json["Objects"]
    if objs != []:
        return objs
    else:
        return default.Objects()
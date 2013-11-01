import GBodies

def by_name(data, n):
    for obj in data:
        if obj["name"] == n:
            return obj

def by_type(data, t):
    objects = []
    for obj in data:
        if obj["type"] == t:
            objects.append(obj)

    return objects

def by_id(data, id):
    for obj in data:
        if obj["id"] == id:
            return obj
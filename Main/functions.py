import json

from Main.models import Block


def coords(points):

    # Weighted signal strength
    print("points" + str(points))
    res = json.loads(points)
    print(type(res))
    a=list()
    for index, val in enumerate(res):
      print(index, val)

      a.append(tuple(val))
    print("After" + str(a))

    ws = sum(p[2] for p in a)
    a = tuple( (x,y,signal/ws) for (x,y,signal) in a )

    # Approximate
    return (
        sum(p[0]*p[2] for p in a), # x
        sum(p[1]*p[2] for p in a) # y
    )




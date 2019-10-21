from Main.models import Block


def coords(points):
    """ Given points in (x,y, signal) format, approximate the position (x,y).

        Reading:
        * http://stackoverflow.com/questions/10329877/how-to-properly-triangulate-gsm-cell-towers-to-get-a-location
        * http://www.neilson.co.za/?p=364
        * http://gis.stackexchange.com/questions/40660/trilateration-algorithm-for-n-amount-of-points
        * http://gis.stackexchange.com/questions/2850/what-algorithm-should-i-use-for-wifi-geolocation
    """
    # Weighted signal strength
    print(points)
    for i in range(len(points)):
        points[i] = tuple(points[i])
    print("After" + points)

    ws = sum(p[2] for p in points)
    points = tuple( (x,y,signal/ws) for (x,y,signal) in points )

    # Approximate
    return (
        sum(p[0]*p[2] for p in points), # x
        sum(p[1]*p[2] for p in points) # y
    )



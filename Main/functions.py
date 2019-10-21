from Main.models import Block


def coords(dist):
    for i,j in dist.items():
        bl=Block.objects.get(tag=i)
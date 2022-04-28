import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

polyList = [(500,300),(800,300),(900,500),(400,500)]
polygon = Polygon(polyList)

print(polygon.contains(Point(900,400)))
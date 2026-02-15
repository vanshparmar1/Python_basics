import arrow
# Get the current brewing time
brewing_time = arrow.utcnow()
brewing_time.to("europe/rome") 
#print(f"Brewing time in Rome: {brewing_time.format('YYYY-MM-DD HH:mm:ss')}")
from collections import namedtuple
chaiProfile = namedtuple("ChaiProfile", ["name", "spice_level", "sweetness"])
 

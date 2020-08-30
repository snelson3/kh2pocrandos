
HELP = """ randomizes the "tint" of the world, code descr says it's for timeless but is for everywhere
Also unsure if it actually affects timeless river, and if different values matter
e102b makes things normal (except it doesn't work in timeless)
Options - some arguments can be passed in through command line using format 'ARGNAME=VALUE'
        Alternatively set an os environment variable USE_KH2_{ARGNAME}=VALUE
help - display this string
seed - sets a specific seed for the random number generator
outpath - sets a different path for the output pnach file, default is same directory as script
setvalue - instead of randomizing the value use a set value (Value needs to be in HEX)
"""

from kh2lib import Randomizer

CODE = "20194858 000{}"
out_fn = "F266B00B (Timeless).pnach"
comment = "Turn world tint to {}"
r = Randomizer(ramcode=CODE, helpstr=HELP, out_fn=out_fn, comment=comment)
# Length of number to randomize
r.randomize_value(5)



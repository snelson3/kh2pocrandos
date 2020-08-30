HELP = """ Randomizes the joint location of various characters weapons
Options - some arguments can be passed in through command line using format 'ARGNAME=VALUE'
        Alternatively set an os environment variable USE_KH2_{ARGNAME}=VALUE
help - display this string
seed - sets a specific seed for the random number generator
outpath - sets a different path for the output pnach file, default is same directory as script
replacement - comma separated mapping of specific replacements to make instead of randomizing
    format: 'sora->riku, roxas->sora'
ignore - comma separated list of mapping keys to exclude from the randomization
"""

mapping = {
    "MickeyC": ("01CE2694", (2, 2)), # Hooded coat
    "Mickey": ("01CE26FC", (2, 2)),
    "Goofy": ("01CE268C", (2, 2)),
    "Donald": ("01CE2684", (2, 2)),
    "Riku": ("01CE2704", (2, 2)),
    "Roxas": ("01CE26DC", (2,2)),
    "Sora": ("01CE267C", (2,2)),
}

from kh2lib import Randomizer

CODE = "{} 00{}00{}"
out_fn = "F266B00B (Joints).pnach"
comment = "Give {} weapon joint value {}"
r = Randomizer(ramcode=CODE, mapping=mapping, helpstr=HELP, out_fn=out_fn, comment=comment)
r.randomize_mapping()
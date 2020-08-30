HELP = """ Randomizes the models for each of Soras forms")
Options - some arguments can be passed in through command line using format 'ARGNAME=VALUE'
        Alternatively set an os environment variable USE_KH2_{ARGNAME}=VALUE
help - display this string
seed - sets a specific seed for the random number generator
outpath - sets a different path for the output pnach file, default is same directory as script
replacement - comma separated mapping of specific replacements to make instead of randomizing (probably broken for this script)
    format: 'sora->riku, roxas->sora'
ignore - comma separated list of mapping keys to exclude from the randomization
"""

mapping = {
    "Sora": ("21C954F4", "00000000"),
    "V-Sora": ("21C95554", "464C5442"),
    "W-Sora": ("21C955B4", "4647414D"),
    "L-Sora": ("21CBD2D4", "4631484B"),
    "M-Sora": ("21C95614", "46495254"),
    "F-Sora": ("21C95674", "46544C55"),
    "A-Sora": ("21C956D4", "464C5448"),
}

from kh2lib import Randomizer

CODE = """{} {}303031
{} {}
"""
out_fn = "F266B00B (Models).pnach"
comment = "Give {} Model of {}"
r = Randomizer(ramcode=CODE, mapping=mapping, helpstr=HELP, out_fn=out_fn, comment=comment)
r.randomize_mapping(mode="models")
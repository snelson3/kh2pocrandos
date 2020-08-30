HELP = """ Randomizes the status according to the Neo Status Mod (status being "most things about that character")
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
    "Sora": ("01C95534", "01"),
    "Donald": ("01C95834", "02"),
    "Goofy": ("01C95894", "03"),
    "MickeyR": ("01C957D4", "04"), # Regular
    "Auron": ("01C95B94", "05"),
    "Mulan": ("01C95AD4", "06"),
    "Aladdin": ("01C95A74", "07"),
    "JackSparrow": ("01C95BF4", "08"),
    "JackSparrowS": ("01CB5F94", "08"), # Skeleton?
    "Beast": ("01C958F4", "09"),
    "JackSkellingtonH": ("01C95954", "0A"), # Halloween
    "JackSkellingtonC": ("01C959B4", "0A"), # Christmas
    "Simba": ("01C95A14", "0B"),
    "Tron": ("01C9DE74", "0C"), 
    "Riku": ("01CB5E14", "0D"),
    "Roxas": ("01C95774", "0E"),
    "RoxasDW": ("01C9F674", "0E"), #Duel Wield
    "RikuF": ("01CB9F54", "0D"),
    "RikuH": ("01CB8C94", "0D"), 
    "Ping": ("01C95B34", "0F")
}

from kh2lib import Randomizer

CODE = "{} 000000{}"
out_fn = "F266B00B (Status).pnach"
comment = "Give {} status of {}"
r = Randomizer(ramcode=CODE, mapping=mapping, helpstr=HELP, out_fn=out_fn, comment=comment)
r.randomize_mapping()
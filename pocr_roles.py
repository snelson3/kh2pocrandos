HELP = """ Randomizes the Universal Role Mod code (Turns everything that is role A into role B)
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
    "Player": ("2036C3DC", "154"),
    "PartyMembers": ("2036C3E0", "164"),
    "NPCs": ("2036C3E4", "298"),
    "Bosses": ("2036C3E8", "17C"),
    "Enemies": ("2036C3EC", "1A4"),
    # "Weapons": ("2036C3F0", "")
    "Partners": ("2036C400", "1F4"),
    "LargeBosses": ("2036C40C", "244"),
    "Summons": ("2036C428", "350"),
    "ToughEnemy": ("2036C430", "3A0")
}

from kh2lib import Randomizer

CODE = "{} 0016F{}"
out_fn = "F266B00B (Roles).pnach"
comment = "Turn role {} into role {}"
r = Randomizer(ramcode=CODE, mapping=mapping, helpstr=HELP, out_fn=out_fn, comment=comment)
r.randomize_mapping()




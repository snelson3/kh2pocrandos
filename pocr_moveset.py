HELP = """ Randomizes movesets between actors using Neomoveset mod code, will likely be very broken
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
"Sora": ("01C95536", "01"),
"Valor Form": ("01C95596", "02"),
"Wisdom Form": ("01C955F6", "03"),
"Master Form": ("01C95656", "04"),
"Final Form": ("01C956B6", "05"),
"Anti Form": ("01C95716", "06"),
"Roxas": ("01C95776", "09"),
"Donald": ("01C95836", "11"),
"Goofy": ("01C95896", "14"),
"Mickey (hooded)": ("01C957D6", "1C"),
"Beast": ("01C958F6", "1F"),
"Jack Skellington": ("01C95956", "20"),
"Jack Skellington (Christmas Town costume)": ("01C959B6", "20"),
"Simba": ("01C95A16", "21"),
"Aladdin": ("01C95A76", "17"),
"Mulan": ("01C95AD6", "19"),
"Ping": ("01C95B36", "1A"),
"Auron": ("01C95B96", "18"),
"Jack Sparrow": ("01C95BF6", "22"),
"Roxas (Dual Wield)": ("01C9F676", "0A"),
"Mermaid Sora": ("01CA1776", "08"),
"Card Sora": ("01CAB196", "38"),
"Dice Sora": ("01CAB1F6", "37"),
"Turtle Goofy": ("01CAB856", "15"),
"Mickey": ("01C9F2B6", "1C"),
"Light Cycle Sora": ("01CAAD16", "36"),
"Lion Sora": ("01C9C916", "07"),
"Donald (Halloween Town)": ("01C9CE56", "16"),
"Goofy (Halloween Town)": ("01C9CEB6", "13"),
"Donald (Atlantica)": ("01CA0CF6", "11"),
"Goofy (Atlantica)": ("01CA0D56", "14"),
"Valor Form (Halloween Town)": ("01CA1D76", "0C"),
"Wisdom Form (Halloween Town)": ("01CA1DD6", "0D"),
"Master Form (Halloween town)": ("01CA1E36", "0E"),
"Final form (Halloween Town)": ("01CA1E96", "0F"),
"Anti Form (Halloween Town)": ("01CA1EF6", "10"),
"Goofy (Timeless River)": ("01CA6156", "34"),
"Goofy (Space Paranoids)": ("01CA7DD6", "33"),
"Donald (Space Paranoids)": ("01CA8016", "31"),
"Donald (Timeless River)": ("01CA9ED6", "32"),
"Gull Donald": ("01CAAAD6", "12"),
"Sora (Space Paranods)": ("01CAC996", "25"),
"Valor Form (Space Paranoids)": ("01CAD056", "26"),
"Valor Form (Timeless River)": ("01CAD0B6", "2C"),
"Wisdom Form (Space Paranoids)": ("01CAD116", "27"),
"Wisdom Form (Timeless River)": ("01CAD176", "2D"),
"Master Form (Space Paranoids)": ("01CAD1D6", "28"),
"Master Form (Timeless River)": ("01CAD236", "2E"),
"Final Form (Space Paranoids)": ("01CAD296", "29"),
"Final Form (Timeless River)": ("01CAD2F6", "2F"),
"Anti Form (Space Paranoids)": ("01CAD356", "2A"),
"Anti Form (Timeless River)": ("01CAD3B6", "20"),
"Sora (KH1 Costume)": ("01CAEC76", "01"),
"Riku": ("01CB5E16", "23"),
"Skeleton Jack Sparrow": ("01CB5F96", "24"),
"Riku (from Final Battle)": ("01CB9F56", "41"),
"Tron": ("01C9DE76", "1B"),
"Sora (Christmas Town)": ("01CBD016", "0B"),
"Valor Sora (Christmas Town)": ("01CBD076", "0C"),
"Wisdom Sora (Christmas Town)": ("01CBD0D6", "0D"),
"Master Sora (Christmas Town)": ("01CBD136", "0E"),
"Final Sora (Christmas Town)": ("01CBD194", "0F"),
"Anti Sora (Christ mas Town)": ("01CBD1F6", "10"),
"Donald (Christmas Town)": ("01CBD254", "13"),
"Goofy (Christmas Town)": ("01CBD2B6", "16"),
"Limit Form": ("01CBD316", "42"),
"Limit Form (Halloween Town)": ("01CBD376", "43"),
"Limit Form (Christmas Town)": ("01CBD3D6", "43"),
"Limit Form (Space Paranoids)": ("01CBD436", "44")
}


from kh2lib import Randomizer

CODE = "{} 000000{}"
out_fn = "F266B00B (Moveset).pnach"
comment = "Give {} moveset of {}"
r = Randomizer(ramcode=CODE, mapping=mapping, helpstr=HELP, out_fn=out_fn, comment=comment)
r.randomize_mapping()
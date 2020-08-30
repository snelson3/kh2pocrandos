# Randomizes the music that plays globally

HELP = """ randomizes the music that plays globally (so I think only two different songs will play, one for battles and one for gummi/town/boss)
Options - some arguments can be passed in through command line using format 'ARGNAME=VALUE'
        Alternatively set an os environment variable USE_KH2_{ARGNAME}=VALUE
help - display this string
seed - sets a specific seed for the random number generator
outpath - sets a different path for the output pnach file, default is same directory as script
setvalue - instead of randomizing the value use a set value (Value needs to be in HEX)
"""

from kh2lib import Randomizer

VALUES = """32- Station of Serenity.
33- Station of Serenity Battle
34- Twilight Town (Sora's story)
35- Twilight Town Battles (Sora's story)
36- TWTNW
37- TWTNW battle music
38- Port Royal.
39- Port Royal Battles.
3B- 1st Armor Xemnas Battle
3C- Dash to the Unknown
3E- Twilight Xemnas Battle
3F- 13th Rememberance*
40- Christmas Town*
41- Christmas Town Battles*
42- The Other Promise*
43- Rage Awakened*
44- Cavern of Rememberance*
45- CoR Battle*
52- Mini-Game
54- Agrabah Battle (super fast)
55- Space Paranoids Battle
56- Freeze
58- Music when Sora awakens
59- Reunion (one when Sora, Riku, and Kairi reunite)
5A- Music when Riku removes blindfold (i THINK)
5B- Kairi's Theme
5C- New Journey
5D- Evil Music (when the Villians plot)
5E- Solemn Music (when Sora finds out what happens when he uses the keyblade)
5F- No Hope 
60- Happy March (when Maleficent and Pete die in TWTNW)
61- Silly music (like when Sora visits Santa)
63- Longing (when Kairi is taken from her home)
64- Underworld Music
65- Beast Castle Music
66- Underworld Battle Music
67- Olympus Coliseum Theme
68- Beast Castle Battle Music
6C- Ariel's Song (background to the one she sings in the cave)
6D- Conclusion Song to Atlantica (background music)
6E- Large Boss Battle (like against the MCP or Jafar)
6F- Chaotic Battle (used in 1000 Heartless event)
70- Land of Dragon Battle 
71- Swim this way (background music to "swim this way" in Atlantica)
72- Nobodies attack
73- Special Boss Battle (like against against the Experiment in Halloween Town)
74- Land of Dragon Town
75- Annoying Battle (like against Pete or the Hyenas)
76- Twilight Town (Roxas story)
77- Twilight Town Battles (Roxas story)
78- Arena Battles
79- Mini Boss Battles (like in Beast's Castle during first visit)
7A- Atlantica Tutorial 
7B- Atlantica Tutorial (when you do something right)
7D- Conclusion to Atlantica Tutorial
7F- Agrabah Town
80- Agrabah Battle
81- Atlantica Town
82- Neverland Clock Tower (KH1 never sounds in KH2)
83- Ambush (battle music for most scripted battles)
84- Ending to Beast's Castle (when belle and beast dance together)
85- Yen Sid Tower
86- Twilight Town battle (Sora's story)
87- Space Paranoids
88- Space Paranoids Battle
89- Gummi´s World Map.
8A- Gummi Menu
8B- Gummi Construction
8C- Under the Sea (this one doesn't hang the game) 
8D- 100 Acre Wood
8E- Gummi Victory
8F- Disney Castle.
90- Halloween Town
91- Struggle in Hollow Bastion 
92- Roxas' Theme
93- Atlantica Battle (KH1 never sounds in KH2)
94- Gummi Launch
95- Halloween Town Battles.
96- Disney Boss Battle (KH1 never sounds in KH2)
97- The 13th Struggle (Organization XIII battles)
98- Hollow Bastion.
99- Hollow Bastion Battles.
9A- Port Royal
9C- Ansem Final Battle (KH1 never sounds in KH2)
9D- Nothing
9E- 100 Acre Minigame 
9F- 100 Acre Minigame (when riding the broom thing)
A2- Evil Music (when Villians plot)
A3- Bad Omen
A4- Olympus Coliseum Mini-game
A7- Bad Omen (this one can be used in worlds as well)
AF- Shocker Music (like when Maleficent revives)
B9- 13th Dilema
BA- Pride Lands Theme
BB- Pride Lands battles
BC- One Winged Angel
BD- Timeless River Theme
BE- Timeless River Battles"""

mapping = { i.split('- ')[1]: i.split('- ')[0] for i in VALUES.split("\n")}
CODE = """10347D34 000000{}
10347D44 000000{}"""
out_fn = "F266B00B (music).pnach"
comment = "Turn music to {} and {}"
r = Randomizer(ramcode=CODE, mapping=mapping, helpstr=HELP, out_fn=out_fn, comment=comment)
# Length of number to randomize
r.randomize_choices()




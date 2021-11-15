import pickle

FILENAME = 'brain'

# save brain with {} to reset the save file
def save_brain(brain):
    outfile = open(FILENAME, 'wb')
    pickle.dump(brain, outfile)
    outfile.close()

def load_brain():
    infile = open(FILENAME, 'rb')
    brain = pickle.load(infile)
    infile.close()
    return brain

# Brain format with defaults
brain_format = {'nice': 0, 'start': 'wow'}
brain = load_brain()

# update brain since the last save
for key in brain_format:
    if not key in brain:
        brain[key] = brain_format[key]

############################
# GOALS
############################
# interpret player speech
# generate speech
############################

#---------------------------
# generate:
#---------------------------
# items (mundane/magical)
# magic system (usable by all players and mobs)
# harmless mobs (archetypes: https://en.wikipedia.org/wiki/Stereotypes_of_animals)
# conversational npcs
# monsters (archetypes: aberration, beast, celestial, construct, dragon, elemental, fey, fiend, giant, humanoid, monstrosity, ooze, plant, undead)

#---------------------------
# game master ideas
#---------------------------
# UNIVERSAL NEEDS:
# - Sleep, security
# - Breath, clean and good air
# - Water
# - Food, excrement
# - Warmth, shelter

# CONVERSATIONAL NPCS:
# - alignment chart
# - 16 personalities
# - emotions
# - posessions
# - individual goals
# - religion
# - culture
# - quests
# - politics
# - jobs

# PLAYERS: (inspired by what??? what are the max levels??? no max level because the gamemaster can keep making more monsters.)
# - attributes
# - classes
# - skills
# - perks/abilities
# - weapons arts
# - magic spells

# MONSTERS
# HARMLESS MOBS
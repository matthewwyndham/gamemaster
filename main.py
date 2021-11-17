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
brain_format = {
    'perceptions': [], # what is happening in the world?
    'automations': [], # make things easier by creating routines for circumstances you've seen before
    'thoughts': [], # now, temporary
    'goals': [], # future
    'memories': [], # long/short term, specific experiences
    'motivation': [], # old, general
    'actions': [] # how to affect the world
    # perception -> automations? -> thoughts -> goals / motivations -> memories / automations -> actions
}
brain = load_brain()

# update brain since the last save
for key in brain_format:
    if not key in brain:
        brain[key] = brain_format[key]

# print(brain)
# save_brain(brain)

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
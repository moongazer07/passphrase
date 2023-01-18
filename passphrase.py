import random
import string

# Mnemonic word list
mnemonic_words = ["dog", "cat", "car", "house", "tree", "computer", "book", "flower", "sun", "moon", "star", "ocean", "beach", "mountain", "valley", "river", "lake", "island", "forest", "desert", "jungle", "tiger", "lion", "giraffe", "monkey", "bird", "butterfly", "ant", "bee", "snake", "fish", "shark", "whale", "dolphin", "seagull", "crab", "lobster", "clam", "oyster", "scallop", "mussel", "shrimp", "prawn", "squid", "octopus", "cuttlefish", "jellyfish", "starfish", "urchin", "coral", "seaweed", "kelp", "sponge", "anemone", "urchin", "crustacean", "mollusk", "plankton", "barnacle", "krill", "plankton", "zooplankton", "phytoplankton", "ciliate", "dinoflagellate", "radiolarian", "foraminifera", "diatom", "coccolithophore", "prymnesiophyte", "chlorophyte", "rhodophyte", "phaeophyte", "xanthophyte", "cryptophyte", "pelagophyte", "bacterioplankton", "virioplankton", "protist", "fungus", "lichen", "moss", "fern", "cycad", "conifer", "ginkgo", "gnetophyte", "angiosperm", "monocot", "dicot", "gymnosperm", "pteridophyte", "bryophyte", "alga", "protozoa", "amoeba", "paramecium", "euglena", "diatom", "radiolarian", "foraminifera", "coccolith", "dinoflagellate", "ciliate", "zooplankton", "phytoplankton", "barnacle", "krill", "plankton", "zooplankton", "phytoplankton", "ciliate", "dinoflagellate", "radiolarian", "foraminifera", "diatom", "coccolithophore", "prymnesiophyte", "chlorophyte", "rhodophyte", "phaeophyte", "xanthophyte", "cryptophyte", "pelagophyte", "bacterioplankton", "virioplankton", "protist", "fungus", "lichen", "moss", "fern", "cycad", "conifer", "ginkgo", "gnetophyte", "angiosperm", "monocot", "dicot", "gymnosperm"]

# Function to generate passphrase
def generate_passphrase(length):
    # Initialize empty passphrase
    passphrase = ""
    
    # Add mnemonic word to passphrase
    
    # Add random characters to passphrase
    for i in range(length - 1):
        passphrase += random.choice((random.choice(string.ascii_uppercase + string.digits),random.choice(mnemonic_words)+"-"))
    
    # Return the generated passphrase
    return passphrase

# Generate passphrase of length 8
print(generate_passphrase(10))

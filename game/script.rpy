# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character(_("Me"), color="#ffa500")
define c_bud = Character(_("Bud"), color="#228B22")
define c_dia = Character(_("Diana"), color="#ff0000")
define c_cos = Character(_("Cosmo"), color="#ff1493")
define c_par = Character(_("Paris"), color="#006400")
define c_dyl = Character(_("Dylan"), color="#daa520")




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg poppies with fade

    "It's my first day in the fields at Wildflower High"
    "To be honest it's a little unnerving."
    "I've always been around plants during my time at Bee school"
    "But those were always neatly segregated little gardens."
    "Oh jeez can I even say that here? Is that offensive?"
    "As I watch the hustle and bustle of the big field I start to wonder just how I'm going to fit in here."
    "Just when I'm starting to feel like turning back I recognise a familiar face pushing through the crowd towards me"

    show bud at right

    c_bud "Hey, Dude. It's me, Bud"

    c_bud "We chatted in the dorms while you were getting set up. You're on exchange from the Bee school right?"

    me "Yeah, I guess you could say I'm a transplant"

    c_bud "..."

    voice "sounds/hitsvape.ogg"

    "He pulls out a vape and takes a pull to cover the awkward silence"

    "It doesn't help"

    c_bud "Yeah, you probably don't want to say that sort of thing around here."

    "Shit. So much for breaking the ice"

    me "I'm so sorry, I-"

    c_bud "-It's cool man. I'm chill. Just try not to bring that out in polite society."

    c_bud "Speaking of - you've got no where to hang before school right? How about you come and meet the gang."

    scene bg tree with pushright

    "I busy myself cursing myself over and over in my head while he leads me under a shady tree in the middle of the school grounds."

    "Despite the ragtag group of friendly faces there, I recognise that the rest of the field is keeping a healthy distance from this bunch."

    "So much for getting in with the cool kids during my time here."

    show bud at right with easeinright

    c_bud "Sup guys. Look who I brought along."

    "The handful of mismatched plants look at me confusedly."

    "I start to think maybe this wasn't the best idea"

    c_bud "He's the exchange student from Bee school."

    "They still look confused."

    me "Hi. I'm a t-"

    "Bud cuts me off before I can even get a word in."

    c_bud "Transfer. He's the Transfer student."

    "Bud gives me a subtle nod before sitting down and patting a clear spot next to him."

    hide bud with easeoutbottom

    "The others still look wary, but they seem to expect this sort of weirdness from Bud so I feel more at ease sitting down"

    "As I get myself settled, I catch a waft of sweet perfume from the strange looking plant next to me and can't help but stare."

    show diana at left with moveinbottom

    "She smiles an enrapturing smile at me as she catches me staring"

    c_dia "Well I say, do you look at all the pretty little flowers like this?"

    "Before I can even start to blush, her captivating smile turns into a frown as the plant across from me kicks her leg"

    show paris at center with hpunch

    c_par "Be careful of Diana, she's a real maneater. Ha."

    "Diana crosses her arms in a mock pout and withdraws a bit to gingerly rub her foot."
    hide diana with moveoutleft

    c_par "I'm Paris - you'll excuse me if I don't get up to shake your hand"

    show cosmo at left with easeinleft

    c_cos "Enjoy that joke while it lasts. It gets old real quick. I'm Cosmo by the way"

    "The Dainty pink flower seems to have an easy charm about him that makes me feel more comfortable already."

    c_cos "You've already met Bud, no surprise there. That just leaves, Dylan"

    show dylan at right with easeinright

    "The brilliant yellow flower to his left smiles shyly at me before returning to his book."

    "Cosmo takes no time at all stepping in to fill the silence though."

    c_cos "Bud didn't ever give us your name."

    "Bud pays no attention to the dig, already lying on his back staring at tree branches."


    define mc = Character("[pname]")

#python:
    $pname = renpy.input("So what should we call you?")
    $pname = pname.strip()

    if not pname:
         $pname = "Type something you fuck"

    mc "[pname]. My name is [pname]."

    c_cos "Well, [pname]. Welcome to Wildflower High. It must be hard being the only Bee here but we're already a bunch of misfits anyway so if Bud thinks you're cool, I think you're cool."

    "I smile in response and catch a furtive glance from Dylan before he meets my eyes and hides his face back behind his book."

    mc "Yeah. Yeah I can be cool."

    "Maybe this won't be so bad after all"

    # This ends the game.

    return

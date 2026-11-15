# Define Characters
define p = Character("Me", color="#c8c8ff")
define f = Character("Keith", color="#ffc8c8")
define g = Character("The Entity", color="#ff5050")

#images
image bg starting_page = im.Scale("bg_starting_page.png", 1920, 1280)
image bg dark_woods = im.Scale("bg_dark_woods.png", 1920, 1280)
image bg mansion_exterior = im.Scale("bg_mansion_exterior.png", 1920, 1280)
image bg grand_hall = im.Scale("bg_grand_hall.png", 1920, 1280)
image bg red_corridor = im.Scale("bg_red_corridor.png", 1920, 1280)
image bg misty_hallway = im.Scale("bg_misty_hallway.jpg", 1920, 1280)
image bg silver_mirror = im.Scale("bg_silver_mirror.png", 1920, 1280)
image bg scary_sky = im.Scale("bg_scary_sky.png", 1920, 1280)
image bg haunted_gate = im.Scale("bg_haunted_gate.png", 1920, 1280)
image bg old_wardrobe = im.Scale("bg_old_wardrobe.png", 1920, 1280)
image bg green_glow = im.Scale("bg_green_glow.png", 1920, 1280)
image bg ritual_book = im.Scale("bg_ritual_book.png", 1920, 1280)
image bg locked_desk = im.Scale("bg_locked_desk.png", 1920, 1280)
image bg bricked_window = im.Scale("bg_bricked_window.png", 1920, 1280)
image bg hidden_chamber = im.Scale("bg_hidden_chamber.png", 1920, 1280)
image bg broken_bookshelf = im.Scale("bg_broken_bookshelf.png", 1920, 1280)
image bg spooky_bushes = im.Scale("bg_spooky_bushes.png", 1920, 1280)
image bg entity_figure = im.Scale("bg_entity_figure.png", 1920, 1280)
image bg sewer_stream = im.Scale("bg_sewer_stream.png", 1920, 1280)
image bg rainy_night = im.Scale("bg_rainy_night.png", 1920, 1280)
image bg old_clock = im.Scale("bg_old_clock.png", 1920, 1280)

# The game starts here
label start:
    scene black

    # Continuous background audio loop
    play music "audio/clement_panchout_unsettling_victory_2019.wav" fadein 0.5 volume 1.0 loop

    scene bg starting_page
    with fade

    "{size=+10}{b}ESCAPE: THE HAUNTED MANSION{/b}{/size}"
    "“Some paths lead to places from which there is no return...”"
    "A single night that could turn out to be the very last of your life."
    "Prepare yourself to face your deepest fears."

    with vpunch
    "The game is about to begin..."

    scene bg dark_woods
    with fade

    "The rain lashes violently against the car windows as we drive down the deserted winding road of Blackwood Ridge."
    "It was supposed to be a simple weekend road trip to clear our heads from college stress."
    "Instead, our car engine died right outside the notorious, abandoned Blackwood Manor which is a place locals swore is cursed."

    f "Are you sure this was a good shortcut? My phone has zero signal, and it's freezing out here."
    p "Relax, we just need to find a landline or wait out the storm inside. Look, that old manor is right up the hill."

    scene black
    scene bg mansion_exterior
    with dissolve

    "We push open the creaking iron gates and walk up the overgrown stone path. The mansion looms above us like a giant sleeping beast under the dark sky."
    "We step inside the grand foyer, brushing the dust off our jackets, looking around at the antique portraits hanging on the rotting walls."

    f "It smells like old dust and... something metallic. Let's just check if there's a phone and get out of here quickly."
    p "Agreed. Let's look around carefully before the storm gets worse."

    menu:
        "Inspect the dusty old clock in the corner for clues.":
            jump explore_clock_area

        "Walk over to the heavy grand fireplace to warm our hands for a moment.":
            jump explore_fireplace

label explore_fireplace:
    "As we step near the cold fireplace, a sudden gust of wind blows through the room!"
    "A heavy portrait slips from the wall and crashes right where we were standing a second ago!"

    with vpunch

    p "Whoa! Close call! That almost crushed us right on the spot!"
    jump manor_lockdown

label explore_clock_area:
    scene black
    scene bg old_clock
    with dissolve
    "We inspect the ancient clock, but suddenly its heavy ticking stops completely. Absolute silence fills the room."
    jump manor_lockdown

label manor_lockdown:
    scene black
    scene bg grand_hall
    with dissolve

    "Before we can process anything, the heavy oak main doors slam shut behind us with a deafening bang!"
    "CLANG! The iron deadbolts slide into place automatically by themselves."

    f "The doors are locked from the outside! We can't push them open!"
    p "Don't panic. There has to be another way out of this cursed hallway."

    with vpunch
    g "You dared to step into my domain... None of you shall leave alive."

    menu:
        "Dash toward the old wooden service staircase on the left.":
            jump run_staircase

        "Hide inside the dusty old wardrobe right beside you.":
            jump hide_wardrobe

        "Slam our combined weight against the heavy front doors to break them open.":
            jump break_front_doors

label break_front_doors:
    scene black
    scene bg red_corridor
    with dissolve
    "We throw our entire weight against the oak doors, but they don't budge an inch! The entity strikes our backs with a chilling shockwave!"

    with vpunch
    g "Fools! You cannot escape the way you came."

    p "Ugh! That hurt... but we can't stay exposed here! Run for the service staircase!"
    jump run_staircase

label hide_wardrobe:
    scene black
    scene bg old_wardrobe
    with dissolve
    "We slip inside the dark wardrobe, holding our breath. But the dry wooden floorboards creak loudly under our shoes..."
    "The entity's freezing cold hand rips the wardrobe doors wide open! A massive sudden scare!"

    with vpunch
    g "Found you hiding in the dark..."

    p "No! We're not giving up here! Grab that heavy brass candlestick!"
    f "Take this, spirit!"
    "We throw the heavy metallic object straight through the entity's projection, shattering its focus long enough to break free and sprint toward the staircase!"
    jump reached_upstairs

label run_staircase:
    "We sprint blindly through the dark corridors, taking the service steps two at a time, our hearts hammering against our ribs."
    jump reached_upstairs

label reached_upstairs:
    scene black
    scene bg misty_hallway
    with dissolve

    "We finally reach the second floor and lock ourselves inside an old, abandoned study room."
    "Dusty bookshelves line the walls, and a faint, supernatural green glow emanates from an open journal resting on the mahogany desk."

    f "We're trapped upstairs now! There are no windows here, only a sheer drop to the courtyard!"
    p "Look at that journal... it's glowing. This must be left behind by the original owner who tried to trap the spirit decades ago."

    menu:
        "Quickly flip through the glowing ritual book pages.":
            jump read_journal

        "Search the locked desk drawers for a hidden master key or tool instead.":
            jump search_drawer

        "Look at the bricked window to see if we can break through.":
            jump search_window

        "Inspect the hidden chamber door tucked behind the shelves.":
            jump inspect_hidden_chamber

label inspect_hidden_chamber:
    scene black
    scene bg hidden_chamber
    with dissolve
    "We push open the hidden chamber panel, and a secret passage opens up, letting us slide down into the dark cellar!"
    with vpunch
    p "Ouch! ...Wait, look around. There's a way out through here!"
    jump cellar_escape_path

label search_drawer:
    scene black
    scene bg locked_desk
    with dissolve
    "We yank open the locked desk forcefully, but it triggers a hidden tripwire! A broken bookshelf collapses, blocking our main exit path."

    with vpunch
    scene bg broken_bookshelf
    with dissolve

    p "Damn it! The key isn't here... but look, the ritual book slipped out of the shelf when it collapsed!"
    f "Hurry! The study door is starting to splinter and break down!"
    p "I've got it right here! Let's use its power to fight back!"
    jump final_confrontation

label search_window:
    scene black
    scene bg bricked_window
    with dissolve
    "We try to break through the bricked window, but it's completely sealed solid with ancient magic!"
    "The entity hears us instantly and cuts off our path! A risky setback!"
    with vpunch
    p "No time to regret! We have to find another way out!"
    jump balcony_escape_path

label read_journal:
    scene black
    scene bg ritual_book
    with dissolve
    p "I'm rapidly scanning the ritual book pages... Yes! It contains the exact words to banish the entity!"
    f "Then what are we waiting for? Let's face it!"
    jump final_confrontation

label cellar_escape_path:
    scene black
    scene bg sewer_stream
    with dissolve
    "The cellar leads right towards a flowing sewer stream opening into the wild."

    menu:
        "Force our way through the sewer stream together!":
            jump ending_sewer_escape

        "Climb back up to face the entity directly with courage.":
            jump final_confrontation

label balcony_escape_path:
    scene black
    scene bg spooky_bushes
    with dissolve
    "We escape towards the balcony and jump down into the spooky bushes below."

    menu:
        "Take a leap of faith together into the dark courtyard below!":
            jump ending_secret_escape

        "Turn back inside the mansion to face the entity head-on.":
            jump final_confrontation

label final_confrontation:
    scene black
    scene bg entity_figure
    with dissolve

    "The entity corners us at the end of the grand hallway. The ambient temperature drops to absolute zero, frosting our breath."
    with vpunch
    g "Your time has expired. Turn back to dust or perish here."

    menu:
        "Stand our ground and use the ritual book against the entity!":
            jump ending_true_comeback

        "Sacrifice yourself so your friend can escape safely through the front doors.":
            jump ending_sacrifice

        "Try to negotiate with the spirit by offering our deepest memories.":
            jump ending_negotiation

        "Cower in fear and give up all hope entirely.":
            jump ending_bad


label ending_true_comeback:
    scene black
    scene bg green_glow
    with dissolve
    p "We came too far to lose everything now! We bounce back from every darkness!"
    with vpunch
    "With a final surge of adrenaline, we read the ritual words aloud directly toward the glowing entity."
    "A blinding wave of pure light shatters the darkness. The mansion's age-old curse is finally broken forever!"
    f "We did it! We actually beat the nightmare!"
    p "I told you... no matter how hard life or the darkness hits us, we always bounce back."
    "{b}The End{/b}"
    return

label ending_secret_escape:
    scene black
    scene bg spooky_bushes
    with dissolve
    "We take a desperate leap of faith into the spooky bushes below, crashing safely into the overgrowth."
    "We scramble out of the iron gates just as the haunted mansion collapses into ruins behind us."
    f "We survived! We outsmarted the curse completely!"
    p "Sometimes, stepping back to fight another day is the truest form of bouncing back."
    "{b}The End{/b}"
    return

label ending_sewer_escape:
    scene black
    scene bg sewer_stream
    with dissolve
    "We squeeze through the sewer stream, scraping our arms, until we pop out right into freedom!"
    f "Ugh, we're soaking wet and covered in mud... but we are alive!"
    p "A messy comeback is still a triumphant victory. Let's head home!"
    "{b}The End{/b}"
    return

label ending_negotiation:
    scene black
    scene bg rainy_night
    with dissolve
    p "Wait! We know you were wronged here centuries ago! You don't have to suffer anymore!"
    "The entity pauses abruptly, its harsh red glow softening into a faint, sorrowful blue as old human memories are acknowledged."
    g "You... truly understand my suffering... You are free to walk out alive."
    "The heavy front doors swing open gently by themselves, allowing us to walk out into the peaceful rainy night."
    "{b}The End{/b}"
    return

label ending_sacrifice:
    scene black
    scene bg mansion_exterior
    with dissolve
    p "Run! Don't look back for a second, I'll hold it off right here!"
    f "No! I can't leave you behind—!"
    p "GO! Trust me! Bounce back and live a full life for both of us!"
    "I shove my friend out the front door just as the heavy iron locks slam shut forever, trapping me inside with the dark spirit. But my friend escapes safely."
    "{b}The End{/b}"
    return

label ending_bad:
    scene black
    scene bg scary_sky
    with dissolve
    "We cower in fear, letting doubt, panic, and terror consume our minds completely."
    "The suffocating darkness swallows us whole, adding our lost souls to the mansion's endless collection."
    "GAME OVER: Never let fear stop you from fighting back."
    "{b}The End{/b}"
    return
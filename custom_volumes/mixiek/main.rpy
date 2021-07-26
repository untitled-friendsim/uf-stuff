image {{package_id}}_endcard_goodend = "{{assets}}/images/{{package_id}}_endcard_goodend.png"
image {{package_id}}_endcard_badend1 = "{{assets}}/images/{{package_id}}_endcard_badend1.png"
image {{package_id}}_endcard_badend2 = "{{assets}}/images/{{package_id}}_endcard_badend2.png"

init:
    $ suspense = Fade(5, 0, 0, color="#FFFFFF")
    $ pushdown = PushMove(0.25, "pushdown")

label __package_entrypoint___mixiek:
    $ renpy.block_rollback()
    $ main_menu = False
    $ eyechoice = False
    $ namechoice = False
    $ calmdown = False
    $ hidecouch = False

    window hide

    $ quick_menu = True

    pause(1)

    "And, just as it happened time and time again. You were thrust once again into an unknown world, full of infinite possibility and potential, with no prior memory of anything that happened further back than a mere second ago. You've gotten used to this feeling by now, somehow, even despite your lack of memory."
    "Giddy with excitement, you open your eyes and look forward to new adventures, new friends and a whole new world to explore."
    "As you open your eyes and look in front of you, you see..."

    play sound "{{assets}}/music/sfx/suspense.mp3"
    show background pavement with suspense
    pause(1)
    stop sound

    "The pavement."
    !mixiekq "what... the everloving fuck are you doing on the pavement"

    play sound "{{assets}}/music/sfx/rustle.mp3"
    show background city_background1 with pushdown

    "You hastily get up and adjust yourself, but you get up just TOO fast and end up flailing around in a manner that can only be described as comical."

    show mixiek idle with moveinbottom

    "Somewhere in this maniacal flailing you somehow manage to set yourself upright and look this disembodied voice in the eyesss..."
    "Eye. You look him in the eye."

    queue music "{{assets}}/music/mixiek_loop.mp3" loop
    show mixiek startled at bounce

    !mixiekq "jegus christ what the fuck was that"
    "I uh.. I was just-{nw}"

    show mixiek shocked at bounce

    "Before you can get any word in, his expression shifts to that of absolute and utter shock and perplexion. As if he's just been presented with an alien species."
    "The alien gently crouches down and leans into your face, as if he's inspecting you for faults or damages."

    show mixiek intrigue:
            ease .5 zoom 1.5
    pause (3)
    show mixiek dazed at center:
            ease .5 zoom 1.0

    "After peering in uncomfortably close for an uncomfortably long amount of time, he retracts and stands up straight, looking you up and down in the process."
    !mixiekq "what the fuck are you?"
    "..."
    "I'm not sure?"
    "You inspect him further and realise you really ARE presented with some sort of alien species. He has two pairs of angular, amber horns protruding from the sides of his head and turning vertically at a right angle..."
    "He's got an overbite resembling fangs and..."

    pause (1)

    "One big busted-in eye."

    play sound "{{assets}}/music/sfx/chatter.mp3"
    show mixiek shocked

    "You suddenly hear some chatter approaching and see your new accomplice freeze up, his whole body tensing up as he peers behind the two of you."
    !mixiekq "fuck-"

    play sound "{{assets}}/music/sfx/rustle.mp3"
    show background alleyway with hpunch

    "Before you can even get a word in, you feel a sharp tug on your shoulder and he pulls you into an adjacent alleyway"
    "Are you about to die?"
    "He immediately shushes you and gestures his hand, as if commanding you to crouch, and/or stay on the down-low. You assume that's what he means, and you also assume it's a good idea, since you assume he's nervous for a reason."
    "Realistically, you shouldn't be assuming so much, but being placed face-first on the pavement of an alien planet with no prior recollection of anything in your life doesn't realy leave you with many options."
    
    show mixiek idle at sitting

    !mixiekq "there were people coming."
    "You gaze at him, confused, as if to signal you have no idea what the fuck is going on."
    "He starts speaking in a raspy, sharp whisper."
    !mixiekq "look, i get you're very clearly not from around here. so let me give you some much-needed fucking exposition"
    !mixiekq "you're in the worst fucking suburb on nebros. trolls just go around here and kill and attack for sport, the only exception are other people hiding like me, just trying not to get massacred out here."
    "... Trolls?"
    !mixiekq "us. our race. we're called trolls. i'll go off on one and assume you're not one of us."
    !mixiekq "regardless, whatever group of trolls was approaching was way too confident in walking around these parts not to be a danger to your and my health."
    "The young troll pauses slowly, taking in a deep breath, as if coming to his senses, whilst still looking mildly infuriated"
    "Some time passes and you see him peer out over the corner of the left-side building."
    "On the complete opposite end of the street, you see another troll, same sorta colours and same sorta vibe as your friend over here, give a distant thumbs-up in your direction, as if to signify that any danger is clear by now."
    
    show mixiek idle at center
    pause(1)
    show mixiek idle at sigh:
        yalign 0.5

    !mixiekq "danger's cleared. it was just a gang of olivebloods. they would've fucking had us if we hadn't dipped."
    "He turns back towards you and looks you up and down again."
    !mixiekq "so... look. i've got a few questions, to say the fucking least"
    !mixiekq "first of all, what the fuck are you"
    !mixiekq "second of all, who the fuck are you"
    !mixiekq "and third of all, where the fuck are you from and why the fuck were you just laying outside on the pavement."
    "You, in a very detailed yet quick fashion, tell the troll that you have absolutely no idea and don't remember ANYTHING as to who you are or how you got there."
    
    show mixiek pity

    !mixiekq "thats..."
    "He looks kinda shocked and kinda pained in a way, as if he's having a hard time trying to process everything that has just happened in the past 15 minutes."
    
    show mixiek pity at sigh:
        yalign 0.5

    "After some brief deliberation he breathes in and sighs deeply."
    !mixiekq "and you are completely alone and know nobody."
    "Well, yes you suppose you are."
    "His face shifts to an expression of deep concern and sympathy"
    !mixiekq "look, and this is only a one-time offer. but if you're hurt..."
    "He pauses for a few seconds and looks conflicted."
    
    show mixiek idle
    
    !mixiekq "you can stay the night at my hive. only the night. i have food, drink and games. but i'm not letting you stay any longer than one night. got it?"
    "You gladly take the offer! To be frank, you're fucking terrified of whatever's going on in this part of town!"
    !mixiekq "okay."
    "He turns around, as if expecting you to follow him."
    
    show background city_background2 with fade
    
    "As you start walking, he looks back for a second."
    !mixiekq "oh, and it's quite a walk by the way. so uh, bare with."
    "As he faces forward again, you both begin to make your way over to his hive."
    
    show mixiek idle at breathe:
        yalign 0.5
    
    "You immediately notice how quickly he's walking. You can only just about manage to keep up with his pace, but given the circumstances earlier you kinda understand why he'd try to get there as fast as possible."
    "As you haste your way towards this \"Hive\", whatever that may be, you catch glimpses of other aliens around you, all walking in the same wary, brisk pace. Some still only just emerging from cover."
    "Very soon into the walk, you begin to sweat. This place is SUPER fucking hot. Yet, you see no sun in sight? To be quite honest, you're super confused and you hate it here. You really really hope your gray friend lives far, far away from here."
    "Maybe somewhere colder and less hostile."
    "Suddenly, you feel the air get thicker, and the sky start turning a dark shade of blonde."
    
    show mixiek shocked at bounce:
        yalign 0.5
    show background city_background2_sand with dissolve
    
    !mixiekq "you've got to be fucking kidding me."
    "Your new friend seems fairly panicked. Frozen still in place yet again, just as he stood before."
    !mixiekq "quick, get in here"
    
    play sound "{{assets}}/music/sfx/rustle.mp3"
    show background dumpster with hpunch
    
    "As he pulls you into an adjacent dumpster, you see a thick, flaxen cloud of sand approaching, and quite quickly at that."
    "Just as quickly as the sand is approaching, the young troll slams the lid of the dumpster shut."
    "God this place fucking reeks."
    "Cutting you off mid-though, you suddenly feel it."
    "The sandstorm hits the dumpster all at once, the heat rising and a loud booming reverberating throughout each and every one of the 4 walls surrounding you."
    "You have no idea how you ended up in this deserty hellscape, but you want out."
    "During your mini existensial crisis, you can just about hear your friend trying to yell over the storm"
    !mixiekq "THAT WAS FUCKING CLOSE, JEGUS CHRIST"
    "You yell back at him, asking what the hell is going on."
    !mixiekq "A FUCKING SANDSTORM YOU DUMBASS, WHAT DOES IT LOOK LIKE."
    "Now that you think about it, that explains the sand."
    "You ask if this planet always sucks and wants to kill you this much."
    !mixiekq "YEAH PRETTY MUCH"
    "Well fuck."
    "Slowly, after what feels like an eternity, you feel the storm start to slowly subside as your friend lifts the lid and peeks out."
    !mixiekq "alright, it's mostly over now... but there's still fucktons of sand in the air."
    "He looks around, as if he's looking for something in the dumpster."
    "Soon enough his eyes light up as he grabs the cleanest looking rag of clothing and passes it to you"
    
    show mixiek idle
    
    !mixiekq "take this cloth. keep it over your mouth and dont breathe in the air. it might be disgusting but itll stop you from dying."
    
    show mixiek idle_scarf
    
    "While he's talking he reaches into his pocket, pulls out a scarf, and puts it on."
    
    hide mixiek idle_scarf
    
    "Once he's finished, he lifts open the lid of the dumpster, leaps out and beckons you to make your way out."
    
    play sound "{{assets}}/music/sfx/rustle.mp3"
    show background city_background2_sand with hpunch
    show mixiek idle_scarf with moveinbottom:
        xalign 0.5
        yalign 0.5
    
    "After some struggling, and some pulling on his end, you manage to hobble your way over the edge and land on your feet."
    "The air around you feels incredibly hot and coarse, yet it's nothing like what the initial storm felt like."
    !mixiekq "there's still a lot of sand in the air, and the winds are quite strong. i know you have that cloth but it'd be much safer if you just stood behind me for the length of this walk."
    "You give a muffled okay, and position yourself behind him, which quite conveniently blocks most of the wind and sand from getting to you."
    "As you two begin to walk he starts talking again, however his words are muffled behind the fabric of his scarf."
    !mixiekq "sandstorms like this happen quite often. the sun heats up one side of the planet, the lava bubbles, bubbles pop and it sends a heatwave over the sands."
    "... What?"
    !mixiekq "it doesn't matter."
    "As you walk further, and further and further away, you start to think to yourself... Just how far does he live from here? How much more walking do you need to do?"

    menu:
        "You feel like you should maybe break the monotony? Start some conversation maybe?"
        "Ask about his eye":
            
            $ eyechoice = True
            
            "So... you ask about his eye maybe?"
            "You've kinda been wondering ever since you dropped in here, so let's go with that"
            
            show mixiek angry_scarf1
            
            "As soon as you ask hoever, he pauses mid-stride. You see him tense up and clench his fist"
            "This seems... bad"
            !mixiekq "don't ask about my eye."
            "... Uh oh"
            "You fucked up"
            "He turns around to face you. While he does seem a bit short compared to everyone else, he still absolutely towers over you."
            !mixiekq "look. i understand you're probably hurt, confused and fucked up to all hell right now."
            
            show mixiek at angry_scarf2
            
            !mixiekq "but you don't just look at someone, who's very clearly fucking injured"
            
            show background city_background2_sand with hpunch
            
            !mixiekq "and just ask like it's fucking NOTHING"
            "As he bellows the word nothing, you see a spark or two of what seems to be pure, cyan and pink energy shoot out of him."
            
            show mixek at angry_scarf3
            
            !mixiekq "i'm fucking BLIND in that eye, dickweed. even my lens is still cracked the fuck up. do you think this is a fucking joke or something? something you just bring up in small talk?"
            "As he gets louder and louder you can see him start tearing up underneath his glasses."
            "You feel stumped, and kind of awful, you try to apologise and explain -{nw}"
            
            show mixiek at angry_scarf4
            
            !mixiekq "no. fuck you and your shitty ass apologies. i'm going back to my hive."
            "..."
            !mixiekq "and don't you fucking dare follow me."
            "And just like that and as he says that, he turns around in tears and bolts off, leaving you behind. Alone in the sands."
            
            call ending pass ("{{package_id}}_endcard_badend1", False, True)
        
        "Ask for his name":

            $ namechoice = True

            "So... you decide to ask him about his name."
            !mixiekaq "mixiek. mixiek kakkki. just skip the bullshit and call me mix, the whole name is a mouthful."
            "Oh! Alright. Well your new friend Mixiek is definitely an odd fellow. But he steams a good ham!{nw}"

            $ _history_list.pop()

            "Oh! Alright. Well your new friend Mixiek is definitely an odd fellow. But he seems rather nice!{fast}"
            "You see his pace slow as he reaches into his pockets, fumbling around a bit until he pulls out his keys."
            !mixiekaq "we're here."
            "You see the entrance to whatever this \"Hive\" must be. While you're stood there gazing around, trying to figure out what exactly you're looking at he unlocks the door and walks in."
            
            show mixiek idle at left:
                yalign .5
                ease .5
            
            "As he steps in, he moves aside and dusts off his clothes, or, er. Sands off his clothes? You're not too sure on that one."
            "As he sands off his clothes, you take a look around and start feeling, admittedly, quite daft for expecting something grand and interesting."
            "Hive is just what these \"trolls\" call houses it seems!"
            "Somehow overhearing your train of tought (or potentially overhearing you talking to yourself), he turns his head towards you, a confused expression on his face."
            !mixiekaq "what the fuck is a house?"
            
            pause (2)
            
            "You reply explaining that \"house\" is just what you call a hive where you're from"
            !mixiekaq "uh huh. okay."
            "You can't quite tell if he's displeased, disgusted or just flat out doesn't understand what you're on about. Which you don't blame him for, since you have absolutely no idea what he's on about half of the time either."
            "You scan your eyes around the hive. It's... pretty cool actually."
            "It is however, also quite cramped. There's not a lot of floor space, and sand lines the tops of furniture alongside the usual dust you'd see in an averagely unkempt room."
            "The windows seem reinforced and bolted shuit, while in the upper right corner is what looks like a small AC unit, with a dark gray mesh over it. The floor is generally just littered with drink cans and crisp packets."
            "Posters seem to cover the walls almost entirely. There's loads of movie scenes and posters, from \"ramboh\" to \"rockyy balboa\" and even \"legislacerator dredd\". These all look quite to you... yet familiar?"
            "One thing that does however catch your eye is the abundance of movie posters starring a gray-skinned, nubby-horned Sylvester Stallone."
            
            show mixiek idle at center:
                yalign .5
                ease .5
            
            !mixiekaq "you can make yourself at home btw. if you want you can like, lay on the couch or something, i don't fucking know."
            !mixiekaq "to be quite frank, i don't know and don't care what you do, as long as you stay clear of the bedroom and don't touch my fucking recuperacoon."
            "You ask what the fuck a recuperacoon is."
            !mixiekaq "oh it's just like a bed but filled with slime."
            "... Wait, how does he know what a bed is?"
            
            show mixiek thinking
            
            !mixiekq "i..."
            
            pause (1)
            show mixiek idle talk
            
            !mixiekq "i don't know?"
            "This interaction does definitely strike you as odd, but you don't really dwell on it. To be fair, if you were to dwell on everything strange that has happened today you'd still be laying on the pavement."
            "Thinking nothing of the odd comment, you decide to do what any reasonable person would do and leap face-first onto the aforementioned couch."
            
            play sound "{{assets}}/music/sfx/thud.mp3"
            
            "And as soon as you do, you hit a dislodged spring in the couch, causing you to recoil in pain and fall onto the floor from the couch in the process."
            !mixiekq "dumbass"
            "In your defense, couches are supposed to be soft and comfortable."
            
            show mixiek phone
            
            "As you begin to slowly get up, having probably strained and pulled every joint and muscle in your body from the fall, you see him idly tapping away at his phone, with a dull, thoughtless expression occupying his face."
            
            show mixiek phoine disgust
            
            "This expression suddenly shifts to a disgusted frown as his screen lights up a {hemocolor=cerulean}cobalt blue{/hemocolor}."
            
            show mixiek phone angry
            
            "Suddenly, as furious as a provoked wildebeest, he starts hitting away at his phone keyboard, using his entire body to furiously mash away at what you assume to be some sort of instant messaging app, with a raging look on his face."
            "As he gets more and more into it, you start seeing sky blue and pink sparks zapping around him, causing his hair to slightly stand on end and fill the room with a noticeable tingling."

            menu:
                
                "This feels dangerous... you decide to..."
                "Interfere and try to calm him down":
                
                    $ calmdown = True
                
                    call ending pass ("{{package_id}}_endcard_badend2", False, True)
                
                "Hide behind the couch":
                
                    $ hidecouch = True
                
                    call ending pass ("{{package_id}}_endcard_goodend", True, True)
                
                    $ achievement.grant("!mixiekwin")

    return

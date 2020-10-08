##### [Toph] Camp Naked
label gallery_earthtraining5:
    call gallery_dCharacter_3Common

    show toi toi09
    show toi_blink with dissolve
    t "i think being in the village makes you think you can relax."
    y "woman, this is some of the least relaxed i have ever been."
    y "there isn't even any air conditioning."
    hide toi_blink
    with dissolve
    t "what's air conditioning?"
    y "okay, see! that's what i'm talking about!"
    show toi toi06 with dissolve
    t "come on, wuss."
    t "you're not gonna learn earthbending by being light on your feet."
    t "you gotta put in the work."
    y "ugh, that's the worst sentence i've ever heard."
    t "you gotta to put in the work."
    y "well, don't repeat it!"
    y "fine, where are we going?"
    show toi toi04 with dissolve
    t "up in the mountains by the lake."
    y "the... aw, man."
    t "suck it up, fancy dancer."
    y "fancy... dancer?"
    t "yeah, because of all your fancy lightfooted dance moves when you fight."
    show toi toi07
    show toi_blink
    with dissolve
    t "pfft. like a wuss."
    y "sometimes you are mean to me, and i don't appreciate it."
    hide toi_blink with dissolve
    t "come on."
    hide toi with dissolve
    y "uughhhhhhhhhhhhhhhhh..."
    y "fine!"
    y "i don't like the look of that sky, though."
    y "......"
    y "i'm sure it'll be fine."
    scene black with fade
    t "come on!"


    show flicker_lightning
    pause 0.4
    "a sudden downpour makes you feel like you're standing in lake laogai instead of beside it."
    y "fuck all the ducks!"
    y "what the fuck is this weather!?"
    y "it's been sunny every fucking day!"
    y "and then we leave the damn village-"
    y "not my idea, by the way!"
    t "quit whining!"
    t "we need to find some shelter!"
    y "hold on, i see a cave!"
    y "come on!"
    "you grab toph by her hand and pull her to a small cave on a nearby hill."
    hide flicker_lightning
    scene black

    show tocs_bg 0:
        xpos 0
    with fade
    call pauseInterface
    y "well, that was sudden."
    y "......."
    y "you know, it's pretty when you're not in it."
    y "damn, i'm drenched."
    y "how about you, toph?"

    show tocs_bg:
        linear 5 xpos -250
    pause 5

    t "i feel like I fell in the lake."
    t "....again...."
    y "still sorry about that."
    t "And that rain is freezing cold, too!"
    y "i know...."
    y "it's not lost on me that i was complaining about air conditioning and then we get freezing rain."
    t "sounds like the spirits are out to get you."
    y "hah. right. what a joke. spirits manipulating my life. hah."
    y "......"
    t "ugh... stupid weather..."
    t "If you hadn't pulled me here, I could've made us some shelter right where we stood, you know."
    y "Fuck... you're right..."
    y "i forget we can earthbend."
    t "ahem."
    y "that {i}you{/i} can earthbend."
    y "oh well, we're here now."
    y "and it doesn't look like the rain is going to let up anytime soon."
    y "Guess we're stuck here for the moment."
    show tocs_face angry
    t "Booooring!!!"
    y "We can tell each other scary stories around a campfire."
    hide tocs_face angry
    t "what campfire?"
    show tocs_face ashamed
    t "I'm so wet and cold, i'd eat a dick for a little warmth."
    y "......."
    y "....hold that thought."
    "You dash outside and break off branches from the closest bush you can find and run back inside again."
    y "There!"

    show tocs_bg 0:
        xpos -250
    show expression "bk3/toph/cave/firewood.png" with Dissolve(2.0)
    pause 1
    call pauseInterface
    y "a little firebending and we'll be nice and comfy in no time."
    t "what are you talking about?"
    t "you haven't learned to firebend yet."
    y "uh.... let's worry about that in a minute."
    y "first things first."
    "You start taking off all your clothes."
    t "what are-"
    show tocs_face angry
    t "Hey! What do you think you're doing!?"
    y "My clothes are wet and chilling me to the bone, so I'm taking them off."
    hide tocs_face angry
    y "I just got another dose of that rain while getting wood for the fire."
    y "you know, like... thirty seconds ago?"
    show tocs_face angry
    t "that doesn't mean you can just strip in front of me!"
    y "....why not?"
    y "It's not like you can see my junk, can you?"
    show tocs_face ashamed
    t "....it's just...."
    y "Yeah?"
    hide tocs_face
    t ".....fine....."
    y "Why don't you take off your clothes too?"
    y "We can dry them and warm ourselves by the fire, once I get it going."
    show tocs_face angry with hpunch
    t "i'm not going to get naked in front of you!!"
    y "first: ow, you're loud."
    y "and second: not naked, just keep your underwear on."
    y "You're not going to get warm if you keep wearing all of that."
    y "hell, you're likely to get hypothermia."
    show tocs_face ashamed
    t "...I...ehmm..."
    t "....I'm not wearing underwear...."
    y "....."
    t "....."
    y "....kinky."
    show tocs_face angry
    t "it's not like that!!"
    show tocs_face ashamed
    t "I didn't have anything clean this morning so...."
    y "Pfffft. so what?"
    y "If you sit like you're sitting now, I won't be able to see anything, naked or not."
    y "And as for your chest...."
    y "I've got nipples too, you know."
    y "But hey, fine. Do whatever you're comfy with."
    t "*sigh...*"
    t "Turn around."
    y "Huh?"
    t "Just turn around until I say you can turn back again."
    y "Okay."
    hide expression tocs_face
    show expression "#000" with Dissolve(3.0)
    t "You can turn back again."
    hide expression "#000"

    show tocs_bg 1:
        xpos 0
    show tocs tocs02
    with Dissolve(2.0)
    call pauseInterface
    t "You can't say anything about this to anyone....ever..."
    y "Sure."
    show tocs_face angry
    t "{size=40}...ever!!{/size}" with hpunch
    y "My lips are sealed."
    hide text
    hide tocs_face angry
    t "so, how about that fire?"
    t "It's nice losing those wet clothes, but it's still cold."
    y "One nice warm fire coming up."
    y "I'll hang the clothes from some branches so they'll dry faster."
    show expression "bk3/toph/cave/clothes_hang_1.png"
    show expression "bk3/toph/cave/clothes_hang.png" with Dissolve(2.0)
    call pauseInterface
    y "the wood is a bit wet so it's going to be smoky at the start."

    show tocs_smoke with Dissolve(2.0):
        xpos 400 ypos -30
    call pauseInterface
    t "*cough* *cough*"
    y "Just a few more moments now....."

    show expression "#d3d3d3":
        alpha 0.0
        linear 6 alpha 0.6

    t "It *cough* is only getting worse! *cough*"
    t "Can't you airbend this away?!"
    t "Before we suffocate?"
    y "Oh, crap, of course, we need to get some airflow going."
    y "I'll try earthbending a makeshift chimney above the fire."
    y "Help me out if it looks like I'm bringing this cavern's ceiling down on our heads."
    t "sure *cough* just hurry up *cough*...."
    play sound "audio/earthquake.mp3"
    with sshake
    hide expression "#d3d3d3" with Dissolve(4.0)
    y "It's clearing up!"
    hide tocs_smoke
    show tocs_fire
    with Dissolve(2.0)

    y "Boom, baby!!! Fire!"
    show tocs tocs03
    call pauseInterface
    t "ooohh, that's better!"
    t "I can already feel the cold leaving my body."
    y "(she really does have a cute little body.)"
    y "(wish i could just lean forward and pinch that nipple...)"
    t "And you even used earthbending instead of airbending to solve the smoke problem!"
    t "I guess this day won't be a waste after all!"
    t "Good job, twinkletoes!"
    y "Well, I'm supposed to master earthbending so... "
    y " (not to mention I can't even airbend a feather off the ground....)"

    t "so... how come you can firebend?"
    y "oh. right."
    y "well...."
    y "uh...."
    t "i bet it was what you learned from jeong jeong, right?"
    y "who?"
    y "i mean... yes?"
    t "that fire nation deserter that taught you stuff before we met?"
    t "you burned katara and made zhao destroy his fleet?"
    y "....yes."
    y "i lead a very active life...."
    y "apparently."
    t "you once told me that you swore to never firebend again, though..."
    t "what made you change your mind?"
    y "a life-or-death situation."
    t "i don't think this is a life-or-death situation."
    y "it might be a life-or-death situation."
    t "yeah... but i don't think it is a life-"
    y "stop saying \"life-or-death situation\"."
    y "and quit arguing with me or i'll put this fire out and build my own."
    y "with blackjack. and hookers."
    show tocs_face ashamed with dissolve
    t "what?"
    y "speaking of, it's too bad I don't have a deck of cards with me."
    hide tocs_face ashamed with dissolve
    t "Why, you wanna play solitaire?"
    y "Nah, I was more thinking along the lines of playing reverse strip poker!"
    y "you know... where you have to put clothes on?"
    y "....because we're already naked?"
    y "....."
    y "laugh at my jokes, damn it!"
    t "....card games aren't really my thing...."
    y "Oh... right... sorry, I keep forgetting."
    y "wanna tell some stories instead?"
    t "Sure..."
    show expression "#000" with Dissolve(5.0)
    show text "{color=#ffffff}you and toph share some stories as time passes and the fire slowly dies out.{/color}"
    call pauseInterface

    show expression "bk3/toph/cave/firewood_burned.png"
    hide tocs_fire
    show tocs_bg 2
    hide tocs_light
    show tocs tocs04

    show tocs_smoke:
        alpha 0.4
        xpos 400 ypos -30

    hide expression "#000"
    hide text
    with Dissolve(5.0)
    call pauseInterface
    t "and that's the last time i masturbated with the heavyweight championship belt-"
    t "oh, hey! It stopped raining!"
    y "Nice, and I think our clothes are dry too."
    y "(i guess Toph's forgotten we're still naked...)"
    hide tocs_smoke with Dissolve(2.0)

    menu:
        "let her know you have a full view":
            y "Uhh...."
            t "What is it?"
            y "I'm happy to see you relax yourself around me, but...."
            y "I'm seeing it all, right now."
            show tocs_face realize with dissolve
            call pauseInterface
            y "...and can't look away."
            show tocs_face angry
            show tocs tocs05 with hpunch
            t "Aaaaaah! I knew this was a mistake!"
            t "you should've told me!!!"
            y "I did! Just now!"
            
        "Enjoy the view some more":
            t "Finally! Time to finish today's training!"
            y "...uh-huh..."
            t "My bum feels all sore from sitting here so long."
            y "...uh-huh..."
            t "Are you really listening to what I'm saying?"
            y "...uh-huh..."
            t "If you're really listening say something besides uh-huh."
            y "...uh-huh..."
            show tocs_face angry
            t "aaang!!" with hpunch
            y "Wha..what is it?!"
            show tocs_face ashamed
            t "Aang... why has your heartbeat been increasing the last minute or so...?"
            y "It has?"

            t "Yeah, I can easily sense it with my earthbending when you're sitting naked..."
            t "....on the ground...."
            show tocs_face realize with dissolve
            "a look of realization suddenly appears on toph's face."

            t "......"
            call pauseInterface
            show tocs tocs05 with hpunch
            show tocs_face angry
            t "You pervert!!"
            t "You... you are... ogling me!"
            y "Wha... no... okay, yes..."
            y "I mean, I just didn't want to embarrass you{size=9}....and perhaps take a longer look....{/size}"

    "Toph angrily gets up, grabs her now dry clothes, and dashes out of the cave."
    hide expression "bk3/toph/cave/clothes_hang.png"
    hide tocs_face
    hide tocs
    y "well... shit."
    y "still, any day you see tits is a good day."
    
    return
##### [Toph] Titplay
label gallery_toph_titplay3:
    call gallery_dCharacter_3Common
    
    show tonf tonf15 with Dissolve(1.5)
    t "aang..."
    t "do you..."
    show tonf tonf17 with dissolve
    t "want to see my... breasts again?"
    y "oh, definitely."
    stop music
    play music "audio/Unwritten Return.mp3"
    show tonf tonf51
    with Dissolve(2.0)
    call pauseInterface
    t "um..."
    t "here."

    show tonf tonf52 with Dissolve(2.0):
        ypos 972
    call pauseInterface
    t "i can make them look a little larger..."

    show tonf tonf52:
        ypos 972
        linear 3 ypos 720

    "Toph sticks out her chest as far as possible in an effort to make her small breasts seem bigger."
    hide tonf
    show tonf tonf52
    y "They're beautiful."

    hide tonf
    show tonf tonf52
    t "You can touch them if you want."
    show tonf tonf53 with Dissolve(2.0)
    y "Wow, I can feel your heartbeat. It's going pretty fast."
    y "Can I move my hand?"
    t "Okay."
    t "wait."
    t "do you... like me, aang?"
    y "yes. i do."
    t "I... like you, too."
    t "okay, go ahead. i'm ready."
    show tonf tonf54
    call pauseInterface
    y "we'll go slow, okay?"
    t "...okay..."
    call pauseInterface
    t "how are they?"
    y "i can cup them perfectly in my hand..."
    y "and these..."
    show tonf tonf55
    t "hnmgh...."
    call pauseInterface
    y "...cute little nipples..."
    call pauseInterface

    show tonf tonf56
    y "can't ignore this one..."
    call pauseInterface
    t "ahh... ah... ohhn..."
    y "You okay?"
    t "I'm... feeling..."

    show tonf tonf57
    t "oohhhhn...."
    call pauseInterface
    y "feeling what?"
    t "a little... little lightheaded..."
    y "that's okay."
    y "relax..."
    call pauseInterface
    y "let go."

    show tonf_lewd with Dissolve(1.5)
    t "ahhn...."
    y "there you go..."
    call pauseInterface
    "toph's nipples respond firmly and fiercely to your touch... push out, hard and determined from her little lumps."
    t "ah... ohh... this is... is really... nice..."
    t "feeling... warm... and..."
    t "wet...?"
    y "that's okay, let it happen."
    t "i'm... ah..."
    t "I'm hot... it feels... ahh..."

    show tonf tonf58
    t "unngghh!!"
    t "ohh!!"
    call pauseInterface
    t "oh, my goddd.... aaang..."
    "the feel of her soft, giving skin is almost more than you can take."
    "her nipple pops in and out of your mouth as toph pushes her chest up towards you..."
    "forces you to take more of her breast... which you greedily gobble in her ecstasy."
    t "aang, it's... ah... i'm... i don't..."
    y "sshhh... ride it... ride the wave..."
    t "I can't... your tongue... i'm..."

    show expression "bk3/toph/lovetits/blink.png":
        xpos 600
    with dissolve
    t "aaahh....." with ushake
    t "{size=+5}aaaaahhhhh.........." with vshake
    t "{size=+12}aaaaaaahhhhhhhhhh!!!!!!!!!!!!" with hpunch
    t "....hnghhh...."
    t ".............."
    t "stop... stopstopstop...."
    show tonf tonf53 with Dissolve(1.5)
    hide expression "bk3/toph/lovetits/blink.png" with dissolve
    t "that...."
    hide tonf_lewd with dissolve
    t "that was incredible..."
    t "I need... i'm gonna need more of those."
    y "I... will be happy to provide."
    show tonf tonf51 with Dissolve(1.5)
    t "is it... are we okay?"
    y "more than okay. we're great."
    y "go get some rest."
    t "thank you. i'm so... so tired..."
    t "goodnight..."
    t "and thank you..."

    return
##### [Toph] Footjob
label gallery_love_toph_footjob1:
    call gallery_dCharacter_3Common

    $ toff_clotheson = True
    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"
    show toff toff01 with dissolve
    
    call pauseInterface
    y "before we start..."

    menu:
        "clothes on":
            y "keep your clothes on."
            t "okay..."
            $ toff_clotheson = True

        "clothes off":
            y "take your clothes off."
            t "....."
            t "that's a little forward, isn't it?"
            y "i've seen you naked before."
            y "and come on, you like that i'm fascinated by your body."
            t "........."
            t "okay..."
            $ toff_clotheson = False
            call pauseInterface
            y "fuck yeah!"
            y "alright..."

    y "here we go."
    y "ahem."
    y "\"he'd always noticed her feet, from the first moment they met.\""
    y "\"she was small and lithe - perfect for hugging or throwing around - but her feet were the real perfection.\""
    t "........."
    y "...ahem."
    y "\"they faced each other, an air of expectation and anxious hesitation between them.\""
    y "\"she knew what he wanted... and might even be enjoying his discomfort.\""
    y "\"he opened his mouth, uncertain of what to say, when she widened her smile into a predatory grin.\""
    y "\"she spread her legs - slowly, almost casually - in a sultry invitation that froze him in place.\""
    t "........"
    show toff toff00 with dissolve
    t "........."
    call pauseInterface
    y "....."
    y "......ahem."
    y "\"she was something between a maiden and a tiger...\""
    y "\"she had a stubborn determination to always get what she wanted... it was a trait he admired in her...\""
    y "\"...but she was a virgin. pure as a snowy midnight.\""
    y "\"she had never seen or felt a penis, despite a new growing, burning interest.\""
    y "\"torn between fascination and hesitancy, she attempted to put him at ease with a simple compliment... and invitation.\""
    y "\"she-"
    t "aang, have i told you lately how strong you've become?"
    t "i'm sure... you must have a great body with all the training we've been doing."
    t "i'd... love to feel it."
    y "....ahem."
    y "\"spurred by her intimacy and flattery, he started to shed his clothing.\""
    y "\"as he began removing his robe and wizard hat, he checked to see if he hadn't misread her tone...\""
    y "\"...but she simply looked at him, waiting for him to lay down and reveal himself.\""
    t "......"
    y "......"
    y "..............."

    show toff toff02 with Dissolve(2.0)

    y "\"he found himself suddenly naked... prostrate before her delicate feet...\""
    y "\"anxious and trembling.\""
    y "\"sensing his hesitation, and coupled with her own desire to feel her first penis...\""
    y "\"she stretched her toes out and gently wrapped them around his cock.\""

    show toff toff03 with dissolve
    t "*oh!*"
    t "Mmmm...."
    call pauseInterface
    y "\"surprised by her own confidence, she pressed forward in her discovery of him...\""
    y "\"testing him and watching his face as she explored his growing manhood.\""
    y "\"with alternating strokes, she gripped and rubbed the length of his shaft.\""
    show toff toff04
    call pauseInterface
    y "ohhh... ah..."
    t "keep reading."
    y "\"massaging his cock with steady, even strokes, she bent her legs to better cup his member in her arches.\""
    y "\"seeing with her feet, she watched and studied the head of his penis as it peaked through her arches...\""
    y "\"...only to be swallowed back into her feet.\""
    y "\"she... ah... she could hear him softly groaning, the sound drawing a hungry need from inside her.\""
    y "\"she blushed with a unfamiliar but pleasureable wet heat.\""
    y "\"feeling... feeling him... ah... begin to thrust into her supple grip, she... ah... sped up.\""

    show toff toff05
    call pauseInterface

    y "Hnngh..."
    y "oh, spirits..."
    t "keep going..."
    y "\"her vigor brought out new fervor between them as he thrust and humped in rhythm with her friction.\""
    y "\"he fuck... fucked her smooth and firm feet, wet with sweat and precum, drawing closer to orgasm...\""
    y "\"when she suddenly... slowed?\""

    show toff toff04
    y "......."
    y "you-"
    t "shh."
    t "don't stop."
    y "that's {i}my{/i} line."
    t "go on...."
    y "........"
    y "\"she cooed that she wanted his cum... but wanted to wait... until his balls were swollen and ready to cover her little feet.\""
    y "\"seeing him enraptured and momentarily wrapped around her metaphorical finger...\""
    y "\"she couldn't help but ask him a question she's wondered for a long time.\""

    show expression "bk3/toph/footjob3/unsure.png":
        xpos 0 ypos 0
    t "....."
    t "aang...?"
    t "Do... do you think I'm pretty?"
    y "You know I do."
    hide expression "bk3/toph/footjob3/unsure.png"

    t "hehe, I just like hearing you say that."
    t "Do you think I'm... prettier than... I dunno... Katara?"

    y "much prettier, but please don't tell her i said that."

    t "really?"
    t "you're not just saying that?"
    t "...because i have your cock between my toes?"
    y "it's not between your toes."
    show toff_lewd
    t "are you sure?"
    show toff toff08 with Dissolve(1.5)
    call pauseInterface
    t "now keep reading."
    y "........."
    y "\"....she gripped the head of his cock with her nimble toes... squeezing and tugging at the soft underside of his cock's head.\""

    show toff toff06
    call pauseInterface
    y "\"surprised by her skill, he looked at her inquisitively, to which she gave a simple answer.\""
    t "...When you go barefoot all the time, you pick up a trick or two."

    y "\"...still gripping him between her little toes, she pumped him with an unbelievable, unparalleled expertise."
    y "\"he found himself lost in a world of bliss as she licked her lips and stared... focusing on his swollen, pulsing member.\""
    y "f-fuuuck... that feels nice."
    t "Maybe it'll feel even better when I do this."

    show toff toff07
    y "Oh, fuck..."
    y "nnghh..."
    t "finish the story, aang."
    t "i want to know how it ends."
    y "\"she... she sped her pace, pumping him to the brink.\""
    y "\"her small toes flexing and curling teasingly around his thrusting cock as he slid in an out...\""
    y "\"fucking and pounding even deeper into her feet at an accelerated pace.\""
    y "\"she wiggled her toes, and in a whisper began to beg for it... to beg for his thrusts... his cum...\""

    show expression "bk3/toph/footjob3/unsure.png":
        xpos 0 ypos 0
    hide toff_lewd
    t "..........."
    t "ummm....."
    t "{size=-3}...give... give me your cum, aang..."
    t "{size=-3}give it to me... let it... out..."
    t "{size=-3}fuck my feet... fuck my cute little feet..."
    y "ohhh... yes... yeah... unnhh..."

    hide expression "bk3/toph/footjob3/unsure.png"
    t "......."
    t "...don't hold back... thrust... yeah... fuck them... fuck them..."
    y "ungh... ohh..."
    show toff_lewd
    t "{size=+3}ugh... yes... fuck... that's it... fuck my feet, aang! fuck them! ughhn!"
    y "ohhh... toph... toph, i... i..."

    t "r-read... read the end... the... the end..."
    y "\"cup... ah... cupping the head of his cock with her foot and toes... she... ah... she squeezed once, hard... and...\""
    show toff toff09
    t "like this?"
    y "unngh!!"
    call pauseInterface
    y "\"he... nnghh.... shot... a... a... desperate, built up cumload right into her... her... toes...\""
    t "her what?"
    y "Her... her fucking..."
    y "hhgng!!"
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/footjob3/sperm1.png"
    call pauseInterface
    y "Fuck!"
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/footjob3/sperm2.png"
    call pauseInterface
    t "yes, aang..."
    t "shoot it into my toes..."
    play sound "audio/splurt2.ogg"
    show expression "bk3/toph/footjob3/sperm3.png"
    call pauseInterface
    y "unnhh.... damn..."
    y "....phew...."
    y "you just... prevented me from painting the ceiling white..."
    "toph lets out a little giggle... unlike her usual persona."
    t "hehe!"
    y "ahh... damn, girl."
    hide toff_lewd
    t "that was... a good story."
    y "i wholeheartedly agree."
    t "we should do that again some time."
    y "fucking... agreed..."
    t "okay, i need to go clean off."
    t "umm.... goodnight!"
    call pauseInterface

    return
##### [Toph] Blowjob
label gallery_love_toph_blowjob:
    call gallery_dCharacter_3Common

    $ toph_licking = False
    play music "audio/Unwritten Return.mp3"
    scene bg_bk3_tophome_0
    show tobb tobb50 with dissolve

    show tobb tobb51 with dissolve
    "toph lays down on top of you, her small, perky nipples pressing against you."

    if toph_chat == 14:
        y "so, what're we doing here, toph?"

        show tobb tobb52 with dissolve
        t "well..."
        t "i was kinda thinking..."

        show tobb tobb53 with dissolve
        t "i want you to be with me."
        t "and... i want you to be happy with my attention, and not feel like you need someone else..."
        t "and..."
        show tobb tobb52 with dissolve
        t "i'm really horny from that conversation with katara."

    show tobb tobb54 with dissolve
    "toph leans her face into your cock and you can feel her breathe deeply."
    t "mmmmm.... such a strong smell."

    if toph_chat == 14:
        show tobb tobb54_1 with dissolve
        t "you know, i was also thinking... well..."
        y "yeah?"
        t "I'm a little frustrated."
        y "you are?"
        y "why?"
        t "well..."
        show tobb tobb54 with dissolve
        t "i can't really see your cock."
        t "i got a feel for it with my feet, but it seems to me that the best way to really become familiar with it..."
        t "...is probably to put it in my mouth."
        show tobb tobb53 with dissolve
        t "that way i can run my tongue all over your cock."
        t "i think the mouth might be the most sensitive place in the body."
        show tobb tobb54 with dissolve
        t "well... second most sensitive."
        call pauseInterface
        t "but maybe i'm directing my thoughts to the wrong head...."

    show tobb tobb60 with Dissolve(1.5)



    $ temp_counter = 0

    while temp_counter < 3:
        play sound "audio/kiss.mp3"
        show tobb tobb61

        show tobb_heart:
            xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
            xzoom 1 yzoom 1 alpha 1.0
            linear 1.0 xzoom 4 yzoom 4 alpha 0.0
        pause 0.5
        show tobb tobb60
        pause 0.5
        $ temp_counter += 1


    "Toph kisses the top of your dick with her soft, wet lips..."
    "you throb against her kisses, feeling like you've grown an inch."

    menu:
        "switch back to sideview":
            show tobb tobb55
            $ tobb_frontview = False

        "stay with this view":
            show tobb tobb62
            $ tobb_frontview = True

    t "*glug!* *shlurp!* *gltch!*"
    "toph passionately slurps as she sucks..."
    "her slobbering, smacking, gulping sounds rebound from the stone walls as her mouth eagerly works your cock."
    y "Oh fuck, that feels good!"
    
    y "when did you stop being shy?!"
    t "*sluurp!* *gagh!* *shluurp!*"

    menu:
        "return the favor":
            $ toph_licking = True
            y "I can't let you have all the fun...."
            show tobb_fhead behind tobb
            show tobb tobb64
            with Dissolve(1.5)
            t "hhmm...?"
            call pauseInterface
            show tobb tobb65 with Dissolve(1.5)
            t "hmmgh...!"
            call pauseInterface

            show expression "bk3/toph/blowjob2/pussyfluid.png":
                alpha 0.0
                linear 3.0 alpha 0.6

            show tokp_lick:
                xpos 450 ypos 320
            t "hgghh.... *gltch!*... ahhh.... uhhn!!!"
            y "it's about time i gave your pussy some love, toph."
            t "mmmgh!!!"
            "toph slobbers on your cock with deep, fast sucks and a wild tongue that laps at your shaft every time you pop out of her mouth."
            t "anhh... *guulp!*... anhhh... *slluuurp!*... ohhh..."
            hide tobb_fhead

            show expression "bk3/toph/blowjob2/bbody_head.png" behind tobb:
                xpos 374 ypos -100
            with dissolve
            t "yes! lick... lick me, aang!"
            t "I never knew... i didn't know you could... it's so good!"
            t "don't stop!"
            t "It's so... so... good... i'm...."
            t "i'm... gonna make you cum!"
            hide expression "bk3/toph/blowjob2/bbody_head.png"
            show tobb_fhead behind tobb
            "toph attacks your cock with her mouth, sucking and slurping on you desperately."
            y "alright, then...."
            y "first one to cum loses!"
            t "Get... *shlurp*... ready to lose!"
            call pauseInterface
            hide tokp_lick
            hide tobb_fhead
            hide expression "bk3/toph/blowjob2/pussyfluid.png"

        "Let toph go on undisturbed":
            pass

    if tobb_frontview == False:
        show tobb tobb55

    else:
        show tobb tobb62
    t "*mmmhn....*"
    call pauseInterface
    t "ready to... shoot your... load?"

    if tobb_frontview == False:
        show tobb tobb70
        "without waiting for an answer to her halting question, toph shoves your cock down her throat."
        ya "fuck!"
        t "*gagh!* *sluurp!*"

    else:
        show tobb tobb71
        "without waiting for an answer to her halting question, toph shoves your cock down her throat."
        ya "fuck!"
        t "*gagh!* *sluurp!*"

    call pauseInterface

    y "hhngh!!"
    ya "you want my cum?"
    t "mmhmm!"
    t "give it!"

    if tobb_frontview == False:
        show tobb tobb70_1
        t "*shluurp!* *mghgm!*"
        call pauseInterface
        t "give it to me!"
        show tobb tobb70_2
        call pauseInterface
        t "give me your sperm, aang!"

        menu:
            "cum in throat":
                $ love_toph_bj_facial = False
                show tobb tobb57 with vpunch

            "cum on face":
                $ love_toph_bj_facial = True

    else:
        show tobb tobb71_1
        t "*shluurp!* *mghgm!*"
        call pauseInterface
        t "give it to me!"
        show tobb tobb71_2
        call pauseInterface
        t "give me your sperm, aang!"

        menu:
            "cum in throat":
                $ love_toph_bj_facial = False
                show tobb tobb59 with vpunch

            "cum on face":
                $ love_toph_bj_facial = True

    if not love_toph_bj_facial:
        ya "fuck!"
        t "mmghm!!"
        play sound "audio/splurt2.ogg"
        with flash
        play sound "audio/splurt3.ogg"
        with flash
        play sound "audio/splurt1.ogg"
        with flash
        "you shiver as waves of cum explode deep into toph's throat."
        play sound "audio/gulp2.mp3"
        t "*gulp* *gulp* *gulp* *gulp*"
        "thick ropes of sperm must be pouring themselves into her mouth, but she keeps sucking firmly, all the way to the base."
        play sound "audio/gulp2.mp3"
        t "*gulp* *gulp* *gulp*"
        "you can feel her muscles squeeze and vibrate as she moans into your cock."

        if tobb_frontview:
            show tobb tobb63 with dissolve
        t "*mmmnmm...*"
        y "unnghh...."

    else:
        if tobb_frontview == False:
            show tobb tobb51 with dissolve
            t "let me have-"
            play sound "audio/splurt2.ogg"

            show expression "bk3/toph/boobjob/spermshot.png":
                xpos 142 ypos 80
            with flash
            t "ah...!"
            hide expression "bk3/toph/boobjob/spermshot.png"

            show expression "bk3/toph/footjob3/sperm1.png":
                xpos -45 ypos 110
            with flash

        else:
            show tobb tobb60 with dissolve
            t "let me have-"
            play sound "audio/splurt2.ogg"

            show expression "bk3/toph/boobjob/spermshot.png":
                xpos -30 ypos 80
            with flash
            t "ah...!"
            hide expression "bk3/toph/boobjob/spermshot.png"

            show expression "bk3/toph/footjob3/sperm1.png":
                xpos -220 ypos 117
            with flash
            
        t "wow..."
        call pauseInterface

    if not love_toph_bj_facial:
        show tobb tobb51

        show expression "katara/k_avlegs_spermouth_xtra.png":
            xpos 235 ypos 57
        with Dissolve(1.5)


        t "mah!!"
        t "not bad..."

        if toph_licking:
            t "and yes! i win!"
            y "yeah... you do..."

        y "you've got a little, uh..."
        t "what?"
        y "well... you've got some jizz dripping..."
        t "oh, sorry...."
        play sound "audio/gulp2.mp3"
        hide expression "katara/k_avlegs_spermouth_xtra.png"
        with dissolve
        t "{size=+5}*gulp!*"
        t "...ah!"
        t "is it gone? did i get it?"
        y "....yes."
        show tobb tobb54 with Dissolve(1.5)
        t "mmm... you know, it smells even better, now."
        t "but i think..."
        show tobb tobb51 with dissolve

    else:
        t "it's... on my face..."
        y "sorry, i just sort of... exploded."
        t "no, i don't mind... being a little mess."
        t "I just... wasn't expecting it, is all."

        if toph_licking:
            t "and yes! i win!"
            y "yeah... you do..."
        t "it's very... strong smelling."
        y "i think it's good for your skin, actually."
        y "some very pretty girls use it regularly."
        t "oh!"
        t "well, then i'll keep it on for a bit."
        y "fuck yeah."
        t "also... i think..."

        if tobb_frontview:
            show tobb tobb51
            hide expression "bk3/toph/footjob3/sperm1.png"

            show expression "bk3/toph/footjob3/sperm1.png":
                xpos -45 ypos 110
            with Dissolve(1.5)

    t "that you..."
    show tobb tobb53 with dissolve
    t "and this guy here..."
    t "...should probably head home."
    show tobb tobb52 with dissolve
    t "unless you want to spend the night?"

    return
##### [Toph] Fuck (Cowgirl)
label gallery_toph_shadow_fuck:
    call gallery_dCharacter_3Common

    $ totx_head = 'happy'

    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"
    show totx totx08
    show expression "bk3/toph/shadowfuck/silhouette.png":
        alpha 1.0
    show expression "bk3/toph/shadowfuck/silhouette.png":
        linear 3.0 alpha 0.0
    with fade
    pause 3
    "You barely touch the ground before Toph crawls on your lap."
    t "like this?"
    y "mm-hmm."
    t "You're so warm... It's really nice to hold you like this while we're both naked."
    call pauseInterface
    hide expression "bk3/toph/shadowfuck/silhouette.png"


    show expression "bk3/toph/shadowfuck/hands.png"
    show totx totx05 with Dissolve(1.5)
    t "I think... i think i'm ready, aang."
    y "are you sure?"
    t "...i think so..."
    call pauseInterface
    t "Katara has filled me in on some of the details..."
    t "I want to do this at my pace, though."
    t "okay?"
    y "of course."
    t "don't do anything unless I say so, okay?"
    y "absolutely."
    y "does that mean you don't want me to make suggestions?"
    $ totx_head = 'worried'
    t "no, you can... you can totally help me..."
    t "just... just don't push it, okay?"
    y "okay."
    show totx totx06 with Dissolve(1.0)
    t "I'm going to hold on to you so you need to... ahumm... aim it...?"
    y "i think now would be the time to put the tip in."
    t "okay..."
    call pauseInterface
    t "just... just the tip, okay?"
    t "Slowly."
    t "Veeerry slowly."
    "You do as Toph asks you."
    "It's tight, but not as impossible as you feared."
    play sound "audio/gltch2b.mp3"
    $ totx_head = 'careful'
    show totx totx04
    $ totx_head = 'shock'

    t "Aaaah!" with hpunch
    call pauseInterface
    $ totx_head = 'careful'
    t "ooooohh that... that wasn't so bad..."
    t "But we're not there yet..."
    call pauseInterface
    play sound "audio/gltch2b.mp3"
    show totx totx03 with Dissolve(1.5)
    t "HNnnnn, a little more.."
    call pauseInterface
    play sound "audio/gltch2b.mp3"
    show totx totx02 with Dissolve(1.5)
    t "Not quite there yet...."
    call pauseInterface
    play sound "audio/gltch2b.mp3"
    show totx totx01 with Dissolve(1.5)
    t "aaahh!"
    t "Okay... that's as far as it goes."
    t "I'm just going to sit like this for a moment."
    call pauseInterface
    "after a long silent moment and a slightly pained expression toph starts to smile."
    $ totx_head = 'happy'
    t "you're all the way in."
    t "Or at least as far as I can get it."
    call pauseInterface
    y " You're truly fearless, Toph."
    t "I'm going to move up and down now..."
    t "And remember... you're absolutely forbidden from moving!"
    y "I won't move a finger!"
    t "{size=-4}your fingers aren't the problem..."
    y "what are you muttering?"
    t "...here goes..."
    $ totx_head = 'careful'

    show totx totx100
    t "This is fine... I can take it..."
    call pauseInterface
    $ totx_head = 'happy'
    "after a couple of runs, you can feel Toph getting a lot wetter and sliding up and down more easily."
    t "Getting better now..."
    t "a lot better!"
    t "Did you do something?"
    t "You know... with waterbending?"
    y "Nope, this is all you."
    t "aahh...."
    t "*mmmm...*"
    t "oh, aang..."
    t "this is... amazing!"
    t "why haven't we been... ah..."
    call pauseInterface
    t "that's it!"
    t "get ready, because I'm ready for more!"
    t "i think my pussy is hungry!"
    t "*giggle!*"
    y "did you just giggle?"
    t "i'm happy!"
    t "here we go!"
    $ totx_head = 'lewd'
    show totx totx101
    y "oh fuck!!"
    call pauseInterface
    y "I'm telling you right now, a few more of those and I'm going to fill you to the brim with my babymaker juice!"
    t "That's okay."
    t "You can cum inside!"
    y "Here it comes!"
    hide expression "bk3/toph/shadowfuck/hands.png"
    hide totx
    show totx totx01

    show totx totx07 with Dissolve(1.5)
    show expression "bk3/toph/shadowfuck/body_5_dick.png" with Dissolve(1.5)
    play sound "audio/splurt2.ogg"
    pause 0.4
    play sound "audio/splurt1.ogg"
    pause 0.4
    show expression "bk3/toph/shadowfuck/sperm_inside.png" with Dissolve(1.5)
    play sound "audio/splurt2.ogg"
    pause 0.4
    t "ohh!!!"
    call pauseInterface
    t "it's... wow...!"
    t "my insides are so hot...."
    play sound "audio/splurt3.ogg"
    hide totx
    hide expression "bk3/toph/shadowfuck/body_5_dick.png"
    hide expression "bk3/toph/shadowfuck/sperm_inside.png"
    $ totx_head = 'shock'
    show totx totx01
    show expression "bk3/toph/shadowfuck/hands.png"
    t "Aaah!"
    t "it's... it's still going!"
    t "You weren't kidding about filling me up!"
    call pauseInterface
    $ totx_head = 'happy'
    show totx totx02
    pause 0.3
    show totx totx03
    pause 0.3
    show totx totx06
    show expression "bk3/toph/shadowfuck/sperm_outside.png"
    with Dissolve(1.5)
    show totx_spermdrip
    call pauseInterface
    t "Oh, wow..."
    t "I can feel it literally gush out of me!"

    t "I think I'll go and clean myself up a bit."
    $ toph_back_disappear = 3
    t "get some rest, aang."
    y "that's... no longer going to be difficult..."

    return
##### [Toph] Fuck (Missionary)
label gallery_toph_fuckonback:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"

    show toty toty07 with vshake
    "you place toph down on the bedroll."
    t "oof!"
    y "time for round two!"
    call pauseInterface
    show toty toty06 with Dissolve(1.5)
    y "i'm not going easy on you this time."
    t "......"
    t "...good."
    t "make me yours, aang."
    show toty toty00 with dissolve
    y "ready?"
    t "i... i think..."
    t "i want you, i just don't know if it will..."
    show toty toty01
    t "ooohh...."
    t "okay... i want you."
    t "i want you {i}hard{/i}, aang."
    y "no turning back from here..."
    t "aang..."
    t "love me... however you need."
    play sound "audio/gltch2b.mp3"
    show toty toty02
    t "*aahhh....*"
    y "and....."
    show toty toty99
    y "here we go..."
    t "oohhh... unngh..."
    call pauseInterface
    t "there's... just... so {i}much{/i} of you..."
    t "this is... a really deep position..."
    t "you don't have to be so gentle... i can take it."
    y "you think so?"
    t "i took you before-"
    show toty toty101
    t "{size=+6}ohh!!"
    t "ffffuck!!"
    call pauseInterface
    y "it's so cute when you swear."
    t "what... what the... what the fuck!!"
    t "it's... it's hitting something... in me... not supposed to... ah... ah..."
    y "probably your womb."
    y "this is the baby-maker position."
    t "it's... ah... too... too much... "
    t "but... ah... but good... ah..."
    y "alright... ready to get serious?"
    t "{size=+6}serious-?"
    show toty toty102
    t "ahhh!! ahhhh!!! ahhhhhhh!!!"
    call pauseInterface
    y "fuck yes!"
    t "too... too much!! too much penis!!"
    y "it's a \"cock\", toph."
    y "say \"cock\"."
    t "c-cock! ah! so... so much cock! too deep! ah!"
    y "you are sooo... damn tight!"
    t "ah! ah! ah! cock! cock!"
    y "time for the jackhammer!"
    t "nooooo....!!"
    show toty toty103
    t "ah! cock! fuck! ungh! ungh!"
    call pauseInterface
    t "c-cock! too... much! aang! easy! easy! please!!"
    y "oh shiiiit!"
    show toty toty104
    t "aaaaaaaaaaaahhhhhhhhhhhhhhh!!!!!!!!!!"
    "toph's whole body, including her vocal chords, vibrate with your relentless thrusts into her clutching virgin pussy."
    call pauseInterface
    y "here comes the baby batter!"
    t "give... give... semen... want... happy... ahh... ah... cock..."

    menu:
        "come inside":
            show toty toty01_1 with dissolve
            play sound "audio/splurt2.ogg"

            show toty toty04_1
            with vpunch
            t "oh!"
            play sound "audio/splurt3.ogg"
            with flash
            t "ohh... fuck!!"
            play sound "audio/splurt3.ogg"
            show toty toty04 with dissolve
            with flash
            "you shoot several blasts of cum as far into toph as you can manage, filling her womb with splashing sperm."
            show toty toty06
            show expression "bk3/toph/fuckonback/openpussy.png"
            show expression "bk3/toph/fuckonback/dick_outside_sperm.png"
            with dissolve
            "she shivers with satisfaction and exhaustion."

            y "Hmmm..."

        "come outside":
            hide toty
            show toty toty06
            show expression "bk3/toph/fuckonback/openpussy.png"
            t "give me your semen, aang!"
            play sound "audio/splurt2.ogg"

            show expression "bk3/toph/fuckonback/openpussy.png"
            show expression "bk3/toph/fuckonback/spermout_1.png"
            with flash
            call pauseInterface
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/fuckonback/spermout_2.png"
            with flash
            call pauseInterface
            play sound "audio/splurt1.ogg"
            show expression "bk3/toph/fuckonback/spermout_3.png"
            with flash
            call pauseInterface
            "she shivers with satisfaction and exhaustion."
            pass

    y "you know... at some point i might have you stop taking those contraceptives."
    t "i... might like that..."
    y "sleep well, toph."
    t "hrgh... ah..."

    call pauseInterface
    
    return
##### [Toph] Sleep Masturbation
label gallery_toph_chat22:
    call gallery_dCharacter_3Common

    scene bg_a_farm_mainhall
    show tofj tofj50:
        ypos 170 zoom 0.8
    show screen fuzzy_edges
    with Dissolve(1.5)
    call pauseInterface
    y "toph...?"
    y "what the-"
    show al_blink
    with dissolve

    a "oh, look where we are... back at the farm."
    a "i wonder why?"
    y "azula?!"
    a "ahh... {i}she's{/i} why."
    a "so this is your new breeding sow."
    a "i see you've made her a whore like the others."
    y "she's not a whore!"
    a "right... and you actually care for this one."
    y "of course i do!"
    a "oh?"
    a "let's test that, shall we?"
    a "earthbender, have you anything to add?"
    t "take me..."
    t "i am your... fuck puppy..."
    y "you're not my \"fuck puppy\", toph, i care about you."
    a "sure you do."
    t "use... me..."
    y "toph it's not like that!"
    a "no?"
    scene bg_a_prison_inside_9

    show tofj tofj50:
        ypos 170 zoom 0.8
    show al_blink
    with Dissolve(2)
    y "what... what's happening?"
    t "fuck... me... ruin... me..."
    y "toph, don't... don't say that..."
    a "well this is an interesting turn, wouldn't you say?"
    a "you've taken us to a prison."
    a "fascinating."
    y "i haven't done anything!"
    y "you... you're doing this!"
    show ale
    hide al_blink
    with dissolve
    a "i'm really not."
    y "what do you want, azula?"
    y "why are you here?"
    show alu
    hide ale
    with dissolve
    a "there's no need to be so rude."
    a "i'm here because we need each other."
    y "we do?"
    a "yes... more than you know, sadly..."
    a "and this is purely your subconscious."
    a "i'm just letting it... run around a little."
    a "you're going to kill her, you know."
    y "what? that's insane."
    a "you'll kill everybody."
    a "if you make the wrong choice."
    y "what choice?"
    a "we'll speak on it another time, perhaps..."
    y "okay, who are you?"
    y "you're not azula."
    show ale
    hide alu
    with dissolve
    a "are you so sure?"
    a "maybe i'm not, but..."
    a "well... this one needs your attention, it seems."
    t "[povname]... i need you..."
    t "take me, [povname]..."
    y "toph why are you...."
    y "....."
    y "you called me [povname]."
    t "i did. so?"
    t "that is your name..."
    y "but you shouldn't know it..."
    y "this... this is a dream..."
    a "of course it's a dream, avatar."
    "{i}hsss...."
    "{i}but that doesssn't make it untrue..."
    ya "snake bitch!"
    ya "show yourself!"
    "{i}hsss...."
    ya "show yourself! {i}now{/i}!"
    "{i}very well..."
    stop music
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
    hide screen fuzzy_edges
    scene black
    with Dissolve(1.5)
    scene bg_dream with Dissolve(1.5)
    y "what... the...?"

    show tonb tonb01:
        parallel:
            ypos 720
            linear 2.0 ypos 0

        parallel:
            alpha 0
            linear 2.0 alpha 1
    pause 2.0

    show tonb tonb01:
        ypos 0 xpos 0
        linear 3.0 ypos 30
        linear 3.0 ypos 0
        repeat
    "{i}you asssked me to ssshow myssself..."
    "{i}well... here i am..."
    "{i}i have been trying to reach you...."
    "{i}you don't lisssten..."
    y "I thought the other spirit chick said you were contained?"
    "{i}we mussst ssspeak..."
    "{i}thisss isss where i have the mossst power..."
    y "why are you here now?"
    "{i}the eyesss..."
    "{i}you pulled them from my ssstatue..."
    "{i}i wasss contained there, forced to reach out through sssleep..."
    "{i}but ssshe did not expect thisss..."
    "{i}even i did not expect thisss..."
    y "expect what...?"
    y "what... what happened?"
    "{i}Do you like thisss form, avatar?"
    y "i... no?"
    y "not particularly..."
    hide tonb tonb01 with Dissolve(1.5)

    show tonb tonb101 with Dissolve(1.5):
        parallel:
            xpos -1000
            linear 1.0 xpos 0

        parallel:
            ypos 0
            linear 1 ypos 15
            linear 1 ypos 0
            repeat

    "{i}How about thisss?"
    call pauseInterface
    y "that... is better, actually."
    y "but fuck those crystal eyes. i'll just throw them away."
    "{i}it isss too late for that, avatar..."
    "{i}you have accepted the eyesss... and a ssshadow of me hasss nessstled in your conssscience."
    "{i}...and {b}ssshe{/b} cannot help you here..."
    y "....what!?"
    y "you're in my mind!?"
    y "oh, fuck... is this how i die?"
    "{i}.....you will not die here....."
    y "Oh. that's good."
    "{i}in fact... i bring you a gift..."
    "{i}a peace offering...."
    "{i}you have nothing to fear from me..."
    y "that has not proven to be the case before."
    "{i}i am in your mind, avatar..."
    "{i}but i can help you...."
    y "help me?"
    y "you're a snake demon!"
    "{i}a ssspirit... not a demon..."
    "{i}i have a name..."
    y "i don't care!"
    "{i}sssee how i will help you..."
    y "....how?"
    "{i}i will protect you..."
    "{i}i have {/i}been{i} protecting you..."
    "{i}you will sssee..."
    hide tonb with dissolve
    y "wait... where are you going?"
    y "give me some answers!"
    scene black with Dissolve(1.5)
    y "wait, come back!"
    pause 1

    scene black
    scene expression "ebackgrounds/bg_night_tophhome.jpg"
    show totc totc10
    with eye_open
    ya "(ah!)" with hpunch
    y "(okay... okay... just a dream...)"
    y "(...what the hell was that all about?)"
    y "(those fucking statue eyes...)"
    y "(there's no way i can go back to sleep... i need to walk or something.)"

    y "...toph seems okay."
    y "I hope... i hope that dream was just my fears and not... reality..."
    t "*mummble...* dick... *mummble...*"
    y "aw, that's cute."

    show totc totc11 with Dissolve(2.0)
    t "Sss'too warm..."

    show totc totc12
    pause 2

    show totc totc13

    t "Yaaawnn..."
    show totc totc11
    t "don... don't lick me there... aanng thaass durrtee..."
    t "I...dun't care... itsa exit..."

    show totc totc12
    pause 2
    show totc totc11 with Dissolve(1.5)
    t "mmmm... my mum has normal sized boohbies... why dsyou assk?"

    y "Maybe my dream self wanted a view into the future?"
    y "Oh crap... did I say that out loud?"
    show totc totc14

    t "Huh, wha..."
    show expression "bk3/toph/nightmare/face_angry.png"
    t "Intruder!"
    show expression "bk3/toph/nightmare/handswing.png"

    show expression "bk3/toph/nightmare/block.png":
        xpos 1200 ypos 300 xzoom 0.5 yzoom 0.5
        linear 2.0 xpos -700 ypos 200 xzoom 2.0 yzoom 2.0
    "You barely avoid a stone flying past you at a hair's width." with hpunch
    hide expression "bk3/toph/nightmare/face_angry.png"
    t "Aang?"
    hide expression "bk3/toph/nightmare/handswing.png" with Dissolve(1.5)
    t "What are you doing?"
    y "Just checking up on you."
    y "I had this... weird dream."
    y "it seemed super real and I couldn't get another wink of sleep..."
    y "i was gonna go for a walk or something."
    t "Really?"
    t "that doesn't seem like you."
    t "you must be pretty shaken."
    t "What happened in your dream?"
    y "it... i..."
    y "...huh."
    y "I can't quite remember."
    y "i know it was bad, and you were definitely there..."
    show expression "bk3/toph/nightmare/face_amused.png"
    t "Hehehe..."
    y "My anguish amuses you?"
    t "It looks like it's my turn to put {i}your{/i} worries to rest!"
    hide expression "bk3/toph/nightmare/face_amused.png"
    t "I'm pretty tough, Aang... but even i need help sometimes."
    t "the point is... i'm here for you, too."
    t "if you need it."
    y "i guess..."
    show expression "bk3/toph/nightmare/face_amused.png"
    t "besides, i'm your little fuck puppy!"
    "you feel your veins suddenly freeze ice cold."
    y "say... say that again."
    t "i'm your fuck puppy!"
    t "arf! arf!"
    y "why are you doing that...?"
    hide expression "bk3/toph/nightmare/face_amused.png"
    t "I'm... not actually sure..."
    t "i think i dreamt it?"
    t "i had a pretty weird dream myself, come to think of it."
    y "oh...?"
    t "yeah, azula was there, and then this snake lady appeared..."
    y "...."
    t "...but before she could say anything, ice cream starting pouring out of the sky and i swam to my new castle."
    show expression "bk3/toph/nightmare/face_amused.png"
    t "weird, huh?"
    y "...very."
    hide expression "bk3/toph/nightmare/face_amused.png"
    t "hey, it's okay."
    y "what?"
    t "you seem... upset."
    t "i'm only joking."
    t "come here, wanna snuggle until we fall asleep again?"
    y "yeah, i... i think i need that."
    scene black with Dissolve(1.5)
    "You and Toph spoon together and after some light kissing and stroking..."
    call pauseInterface
    show expression "ebackgrounds/bg_night_tophhome.jpg"
    show totc totc15
    with Dissolve(1.5)

    t "Aang?"
    y "Yeah?"
    t "Would you... like to have children? I mean, eventually?"
    y "perhaps..."

    y "You still using that stuff Suki gave you?"
    t "Yeah... in fact I should visit her again, because I'm almost out."
    y "If you do run out we could always start using that other entrance."
    y "Just to be on the safe side."
    t "What other entrance?"
    t "What are you talk... wait..."
    show expression "bk3/toph/nightmare/face_angryzoom.png"
    t "That's dirty!!!"
    t "that's where poop comes out!!!"
    t "Are you crazy?!"
    y "It's really not that big of a deal..."
    y "...and not a single part of you is dirty."
    hide expression "bk3/toph/nightmare/face_angryzoom.png"
    t "...I still think it's weird and strange."
    y "Well, you haven't run out of Suki's stuff just yet soo..."
    y "...how about practicing some old fashioned baby-making?"
    y "That cuddling from before has made me hard as fuuuuck."
    t "I guess we could do a quickie...."

    scene black with Dissolve(1.5)
    "The rest of the night you and Toph practice."
    call pauseInterface

    scene bg_day_tophhome:
        xzoom -1.0
    with Dissolve(2.0)
    y "*Yawn!*"
    y "Hmmmm... where's Toph?"
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg" with Dissolve(2.0)
    hide expression "ebackgrounds/bg_night_tophhome.jpg"
    y "Not here..."
    show expression "ebackgrounds/bg_bk3_tophome_day.jpg" with Dissolve(2.0)
    hide expression "ebackgrounds/bg_bk3_tophome_0.jpg"

    y "Not here either."
    y "she must've gone out I guess."
    y "Now where's toph's toilet..."

    show expression "ebackgrounds/toilet.jpg"
    show totc totc20 with hpunch
    t "Ah!!! "
    y "ah!"
    show totc totc21
    t "Do you mind?!?"
    t "I'm... I'm kinda busy here!"
    y "Sorry!"
    hide expression "ebackgrounds/toilet.jpg"
    hide tost

    return
##### [Toph] Ass Massage
label gallery_toph_ass_massage2:
    call gallery_dCharacter_3Common

    show expression "bk3/toph/assmassage/background.jpg"
    show toam toam01
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    with fade
    suki "oh, hey."
    suki "what are you guys doing here?"
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    show toam toam02 with Dissolve(1.5)
    t "we just thought it'd be fun to-"
    y "to come. here."
    suki "oh. cool."
    suki "i don't know how much free time i have to chat, though..."
    suki "there's a lot to do."
    show toam toam03
    t "oh, don't worry, we're not here to be in your w-"
    show toam toam04
    t "-ay!!"
    suki "What is it Toph?"
    show toam toam05
    t "Hahaha... nothing nothing at all."
    t "Just... remembered something."
    show toam toam06
    "You start rubbing while the girls resume their conversation."
    t "so h-how... are y-you?"
    call pauseInterface
    show toam toam07
    t "{size=-6}hungh..."
    suki "You certain you're alright, Toph?"
    call pauseInterface
    "you grip and squeeze toph's firm little ass cheeks."
    "they tense and release as you knead them."
    "you can feel the edges of her pussy lips as you pull her small, giving buttocks apart."
    "your thumb occasionally presses against her tight, tiny anus... tensing her up as she squeezes your fingers."
    t "Yeah... ev-everything is... arright."
    show toam toam08
    suki "hey, do you mind waiting here for a moment?"
    suki "I'll be back in a minute or five."
    t "Suuuure... take your time."
    show toam toam15 with Dissolve(1.5)
    hide toam
    show tonf tonf16
    with dissolve
    t "Aang!!"
    t "give me some warning next time!"
    y "why?"
    ym "did you get too wet?"
    show tonf tonf17
    t "just..."
    t "we only have a few minutes!"
    t "so get to it!"

    hide tonf
    show toam toam09
    show expression "bk3/toph/assmassage/fluid_skin.png"
    with Dissolve(1.5)
    t "rub your cock on me!"
    t "i want to feel it in my ass...."
    y "That sounds-"
    t "shut up!"
    t "hurry!"
    hide expression "bk3/toph/assmassage/fluid_skin.png"
    show toam toam10
    with dissolve
    y "you got it!"
    show toam toam11
    t "Ooh!"
    call pauseInterface
    t "mmm... yeah... rub me down..."
    t "right here... right in this public... fucking... bar..."
    t "this is crazy, you know that, right?!"
    show toam toam12
    t "Fuuucckk... this feels even better than last time!"
    call pauseInterface
    show toam toam13
    y "I'll go a bit faster so I can finish this before Suki returns."
    t "do it!!"
    call pauseInterface
    t "yeah... yeah..."
    t "how's my tight ass? gripping your big shaft?"
    t "you like abusing my soon-to-be cummy buttcheeks?"
    t "getting your fucking load out right here in this bar?"
    t "come on, aang... come on baby..."
    y "Hnnnngh... i'm getting super close to coming...."
    t "yeah! fuck it out!"
    t "Cum all over my ass!!"
    t "Don't leave any evidence Suki can find!"
    call pauseInterface
    play sound "audio/splurt2.ogg"
    show toam toam14
    show expression "bk3/toph/assmassage/sperm1.png"
    with flash
    call pauseInterface
    play sound "audio/splurt3.ogg"
    show expression "bk3/toph/assmassage/sperm2.png"
    with flash
    call pauseInterface
    play sound "audio/splurt1.ogg"
    show expression "bk3/toph/assmassage/sperm3.png"
    with flash
    call pauseInterface
    show toam toam09
    t "that felt so good!"
    t "my legs are shaking."
    t "you got it all over my little... vagina... too?"
    y "i really did."
    call pauseInterface
    y "in fact, maybe we can-"
    t "suki!"
    t "I think Suki's coming back!"
    t "i gotta put my pants back on!"
    hide expression "bk3/toph/assmassage/sperm1.png"
    hide expression "bk3/toph/assmassage/sperm2.png"
    hide expression "bk3/toph/assmassage/sperm3.png"
    show toam toam02
    show expression "bk3/toph/assmassage/shotcumstain2.png"
    with Dissolve(1.5)
    call pauseInterface
    suki "oof, it's nice to sit."
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    suki "you guys seem... flushed."
    hide expression "bk3/toph/assmassage/suki_eyesonplayer.png"
    show toam toam16
    t "just... just having a... good time."
    suki "okay..."

    show toam toam01
    show tonf tonf17
    t "I think we should go home, Aang."
    suki "wait, what's that on your butt-"
    t "bye!"
    hide tonf
    show expression "bk3/toph/assmassage/suki_eyesonplayer.png":
        xpos 0 ypos 0
    hide expression "bk3/toph/assmassage/shotcumstain2.png"
    with dissolve
    y "i'm... gonna go with her."
    suki "did you guys just-"
    y "see ya!"

    return
##### [Toph] Anal (Prone)
label gallery_love_toph_anal1:
    call gallery_dCharacter_3Common

    $ tota_assfuck_seeface = False
    $ tota_assfuck_xray = False

    scene bg_bk3_tophome_2
    show tota tota00 with Dissolve(1.5)
    t "o-okay."

    $ tota_assfuck_seeface = True
    t "just be gentle, okay?"
    t "i want to... to make you happy but... i'm small."

    show tota tota01 with dissolve

    t "i put a finger in there the other day and it's... it's really tight."
    show tota tota02 with dissolve
    t "try not to... to tear or hurt me, okay?"
    y "i'll be careful."
    y "try and relax... being tense will make it more difficult."
    t "that's easy for you to say..."
    y "here it goes."
    $ tota_assfuck_seeface = False

    show tota tota10b
    with Dissolve(1.5)

    t "uunnghh..."
    "toph takes several deep breaths."
    t "O-okay... okay..."
    t "This isn't so bad."
    t "Just... just a penis going into my anus..."
    t "nothing to be alarmed about."
    t "it's just like normal... but entirely different..."
    t "....and against what nature intended."
    y "Alright, I'll put in the head now."
    $ tota_assfuck_seeface = True
    t "it's... it's not in?"
    y "no, this is just the tip."
    $ tota_assfuck_seeface = False
    t "oh..."
    y "...Ready?"

    t "s-sure thing..."
    $ tota_assfuck_seeface = True
    t "wait, don't we... uh... don't we need lubricant or something?"
    y "i mean... i don't have any with me."
    y "i could spit on it?"
    y "how about that?"
    t "i think that's a... a good idea."
    $ tota_assfuck_seeface = False
    t "this is... already kind of difficult..."

    show tota tota01 with dissolve
    y "okay."
    play sound "audio/spit.mp3"
    show expression "bk3/joodee/titplay/spithead.png":
        xpos 325 ypos 225
        alpha 1.0
        linear 4.0 alpha 0
    with ushake
    t "oh!"
    t "that was... wet."
    y "well, yeah."
    y "okay, that should do it."
    show tota tota10
    with Dissolve(1.5)
    t "hngh..."
    y "just sliding back in..."
    t "o-okay..."
    y "it's going in now... ready?"
    t "........"

    show tota tota03 with hpunch


    t "{size=+20}ahhh!! fuck!!"
    $ tota_assfuck_seeface = False

    show tota tota11 with Dissolve(1.5)
    t "unnghh.... ohhh.... oh...."

    y "The head is in."
    $ tota_assfuck_seeface = True
    t "....I noticed...."
    call pauseInterface
    show tota tota12 with Dissolve(1.5)
    t "Ohh... ohh... it's..."
    t "ow..."
    call pauseInterface
    t "it's painful, i'm sorry..."
    y "just a bit more."
    show tota tota13 with Dissolve(1.5)
    t "ahhh...!! ah...."
    call pauseInterface
    show tota tota14 with Dissolve(1.5)
    t "ohhh...!!!"


    y "I'll just do some short strokes now, okay?"
    t "Oh... okay..."
    show tota tota102 with Dissolve(1.5)
    call pauseInterface
    t "oohh... ahh..."
    t "oww... uh..."
    y "you okay?"
    t "Ah... that's... that's okay..."
    t "Short strokes are... are okay..."

    t "Just keep doin' it like this for a bit... please..."
    "you pop in and out of the tight hole..."
    "the constant pressure of her little entrance squeezing around your cock feels incredible."
    call pauseInterface
    "After several minutes of slowly prodding Toph's ass, never going deeper than the tip, you feel her relax."
    t "Okay... this is a lot better..."

    t "I think it's okay for you to go deeper now."
    y "Just yell when I need to stop."

    y "here we go."
    show tota tota100

    with Dissolve(1.5)
    t "ohhhhhh...... {i}fuuuuck{/i}, aang!"
    y "it's so cute when you swear."
    t "well... fuck!"
    t "Hnnnff... I... I could do this..."
    y "you are doing this..."
    t "i mean... i could... get used to this..."
    t "this... this isn't so bad..."
    t "just keep going slowly..."
    $ tota_assfuck_seeface = True
    t "It's still weird, but not impossible to... enjoy."
    call pauseInterface

    menu:
        "turn xray on":
            $ tota_assfuck_xray = True

        "leave xray off":
            pass
    call pauseInterface
    $ tota_assfuck_seeface = False
    y "Think you're ready for me putting my weight behind it?"
    t "I... can take it!"
    t "I want to... i want to make this good for you!"
    y "it's already good for me, toph."
    t "no, i can... i can do it!"
    t "g-go ahead!"
    y "Here it comes!"
    $ tota_assfuck_seeface = True
    show tota tota101
    t "AAhh!!"
    y "Should I stop?"
    t "HNG... NO! Keep going!!"
    t "does it... does it feel good?"
    y "fuck yes..."
    t "g-good! ohhh...."
    call pauseInterface
    t "you're... all the way in my stomach..."
    t "unngh... ahh..."
    t "there's so much... of you... ahh..."
    y "i need... i need more!"
    show tota tota103
    t "ahhh!! ahhh!!"
    t "ohh... ahh!"
    t "wait!"
    y "oh, shit, should i-"
    t "keep... don't... stop...!!"
    t "i just... ah... i need to... you're just so..."
    t "you're just so... {size=+5}big{/size} inside me!"
    call pauseInterface
    t "i can't... ohh... ow..."
    y "do you need me to stop?"
    t "no, keep... keep going... oww..."
    t "you can... you can go faster... if you... ah... if you need to..."
    y "fuck yes!"
    show tota tota104
    t "ahhh!!"
    call pauseInterface
    y "fuck! this ass is so fucking... tight!!"
    t "ungh... unghh... ohh..."
    y "why haven't i been slamming this ass for ages?!"
    t "fu... fuck! ah!"


    t "i... i love..."
    show tota tota105
    t "i... love you! i love you!"

    t "you have my ass... you have all of me!"

    show tota tota107

    $ tota_assfuck_seeface = False
    y "I'm close to exploding!"
    y "Any preferences about where I'll make a mess?!!"
    t "Hnno!!"

    menu:
        "come outside":
            hide tota

            show tota tota01a

            with Dissolve(1.5)
            y "Here it comes!!"

            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/spermout1.png"
            with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/spermout2.png"
            with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/spermout3.png"
            with flash
            y "All over your pretty white butt."

        "come inside":
            hide tota
            show tota tota14
            $ toph_assfuck_xray = False
            show expression "bk3/toph/ass_fuck/inanus.png"
            with Dissolve(1.5)

            pause 0.5

            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/sperm1.png" with hpunch

            y "Hhnnn~"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/sperm2.png" with hpunch

            y "HNNNGGG!!"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/ass_fuck/sperm3.png" with hpunch

            hide expression "bk3/toph/ass_fuck/inanus.png"
            hide expression "bk3/toph/ass_fuck/sperm1.png"
            hide expression "bk3/toph/ass_fuck/sperm2.png"
            hide expression "bk3/toph/ass_fuck/sperm3.png"

            hide tota
            show tota tota01a
            show expression "bk3/toph/ass_fuck/sperm4.png"
            with Dissolve(2.0)

    $ tota_assfuck_seeface = True
    show tota tota01
    show expression "bk3/toph/ass_fuck/face_lewd.png"

    t "Now give me a kiss you big oaf."
    t "I need a bath."

    show pink with dissolve
    play sound "audio/kiss.mp3"
    pause 0.5
    "toph leans back towards you and plants a surprisingly soft and gentle kiss on your lips."
    "she holds it there for a moment and falls back onto her stomach."
    hide pink with dissolve
    t "ahh..."
    t "come on, let's go."
    call pauseInterface
   
    return
##### [Toph] Anal (Cowgirl)
label gallery_love_toph_anal2:
    call gallery_dCharacter_3Common

    scene bg_bk3_tophome_2
    show tota tota19
    with eye_open
    pause 1
    play music "audio/Unwritten Return.mp3"

    t "sit."
    y "okay..."
    show tota tota29 with Dissolve(1.5)
    t "i was thinking..."
    call pauseInterface


    t "...do you want to dump a load in my cute little butt?"
    y "hell yeah i do."

    t "here..."
    show expression "bk3/toph/ass_fuck/zbottle.png" with dissolve
    show expression "bk3/toph/ass_fuck/zbottle_fluid.png":
        alpha 1.0
        linear 4.0 alpha 0.0
    pause 0.5
    y "Lubricant?"
    t "yeah, and plenty of it!"
    t "i'm gonna fuck you {i}hard{/i}."
    t "and i think this will help both of us."
    hide expression "bk3/toph/ass_fuck/zbottle.png"
    hide expression "bk3/toph/ass_fuck/zbottle_fluid.png"
    show tota tota21 with Dissolve(1.5)
    t "go ahead... aim him somewhere... interesting."
    call pauseInterface
    show tota tota22
    show expression "bk3/toph/ass_fuck/zput_itin.png"
    with Dissolve(1.5)
    y "Here?"
    t "That's a fine place."
    hide expression "bk3/toph/ass_fuck/zput_itin.png" with Dissolve(1.5)
    t "now, i want you to sit back..."
    t "...while i make you cum with my tight, teen ass."
    show tota tota26 with Dissolve(1.5)
    y "oh, fuck..."
    t "*mmmm...*"
    t "How does.. this feel?"
    y "*swallows*"
    call pauseInterface
    show tota tota27 with Dissolve(1.5)
    t "and... further..."
    y "oh, shit..."
    call pauseInterface
    show tota tota22 with Dissolve(1.5)
    t "Warmup is done!"
    show tota tota110
    t "ahh!"
    call pauseInterface
    t "ahhhn... yeah...!!"
    call pauseInterface

    t "What I really want..."
    t "...is for you to experience how it feels..."
    t "...when I put my full weight on your big dick in this position."

    call pauseInterface
    show tota tota22 with Dissolve(1.5)

    t "i'm gonna make you cum... and there's nothing you can do about it."

    show tota tota111
    pause 1
    t "ugh!"
    t "fuck!"
    call pauseInterface
    y "sh-shit!"
    t "i'm taking it... *fuck!*... all the way to... *ugh!*... balls!"
    y "hell yeah you are!"
    t "you gonna... ugh... cum!?"
    y "soon...!!"
    y "I never thought such a small, slender frame could generate this much of a downwards... hnnng... force!"
    t "And this is me still playing nice!"
    call pauseInterface
    y "what's you playing mean?"
    show tota tota22 with dissolve
    t "i thought you'd never ask!"
    show tota tota112
    t "ungh! ahhh! mmm!"
    y "what the fuck, toph!?"
    call pauseInterface
    t "watch my... *ugh!*... bouncing little titties while i... *mmgh!*"
    t "while i squeeze out your... *ah!*... cum with my tight... *mmh!*... teen butt!"
    t "stuff my butt with your fucking cum!"
    show tota tota113
    t "Ah... I... I can feel something happening!"
    t "you're getting... bigger?!"
    t "are you... *ah!*... gonna shoot that big... *mmgh!*... fucking load in my ass!?"
    call pauseInterface
    t "i'm going to milk your fucking cock!"
    t "give me your cum, love!"

    menu:
        "cum inside":
            hide tota
            show tota tota24 with vpunch
            play sound "audio/gltch2b.mp3"
            pause 1
            show tota tota24 with vpunch
            play sound "audio/gltch2b.mp3"
            pause 1

            show tota tota25 with Dissolve(1.5)

        "cum outside":
            hide tota
            show tota tota24
            show tota tota20 with Dissolve(1.5)
            t "cover me!"
            show expression "bk3/toph/ass_fuck/zbody_1_blink.png":
                xpos 0 ypos 0

            show expression "bk3/toph/ass_fuck/zsperm_1.png"
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface
            show expression "bk3/toph/ass_fuck/zsperm_2.png"
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface
            show expression "bk3/toph/ass_fuck/zsperm_3.png"
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface
            hide expression "bk3/toph/ass_fuck/zbody_1_blink.png"
            call pauseInterface

    y "that... that was... what the shit..."
    t "i was hoping you'd say that."
    y "how did... you..."
    t "aang, i... you make me so happy."
    t "i will make you happy too... for as long as you'll have me."
    t "i love you... and i'm not taking that back."
    t "now... i need to wipe this off..."
    t "i'll see you later!"
    t "bye!"
    call pauseInterface
    show tota tota18
    hide expression "bk3/toph/ass_fuck/zsperm_3.png"
    hide expression "bk3/toph/ass_fuck/zsperm_2.png"
    hide expression "bk3/toph/ass_fuck/zsperm_1.png"
    with dissolve
    y "i should go as well..."
    y "whew."
        
    return
##### [Toph + Katara] Threesome Scissor
label gallery_katara_toph_scissor:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    scene bed_inside
    show tote tote01
    with Dissolve(1.5)

    k3 "i think aang's getting excited."
    t "he's {i}been{/i} excited."
    t "his heartrate's been going a zillion beats a minute."
    y "that seems... high."
    k3 "well..."

    show tote tote02 with dissolve
    k3 "why don't i take care of that for you?"
    call pauseInterface
    t "uhh..."
    k3 "come on!"
    k3 "toph's obviously not jumping to the challenge."
    k3 "plus i'm the oldest, so you should start with me."

    t "if anyone's gonna take care of his penis, it's gonna be me!"

    show tote tote03 with dissolve
    t "come on, sexy!"
    t "i'll give you a {i}real{/i} tight experience."
    call pauseInterface
    k3 "hmmgh...."
    k3 "actually..."
    show tote tote02 with dissolve
    k3 "how about a little competition?"
    call pauseInterface
    t "compe... tition?"
    k3 "to see who has the best pussy!"
    t "i don't know..."
    k3 "here's the twist -- no penetration allowed!"
    t "what? how would that work?"
    k3 "aang, lay on the bed."
    show tote tote04 with Dissolve(1.5)
    k3 "perfect, now follow my lead, toph..."

    show tote tote11 with Dissolve(1.5)
    t "like this?"
    k3 "right."
    y "oh... damn..."
    "katara and toph's pussy lips press into your cock, slightly enveloping it."
    "their vaginas are so small that their lips don't even come close to touching."
    "but you can feel a hot wetness on each side that makes it impossible to tell."

    k3 "what do you think, aang?"
    y "i think... that this isn't just about me."
    y "you girls should enjoy yourselves, and each other, as much as with me."
    y "in fact, I think you should kiss each other."

    show tote tote06 with Dissolve(1.5)
    "katara takes toph's hand and they pull toward each other, their pussies pressing harder into your shaft."
    k3 "mmmm...."
    t "ohhh..."
    "toph moans into katara's mouth."
    "they're clearly both enjoying it."
    "you stay silent for a minute while they each explore the feeling of the other girl's lips on theirs."
    call pauseInterface
    y "you know.... I said a little kiss, but..."
    y "...a long one is fine too."

    show tote tote07 with Dissolve(1.5)
    "tentatively, they flick their tongues out and wrap them around each other's."
    "the kiss increases in energy, the two girls beginning to really delve into the other's mouth."
    "they press their lips and tongues into one another as you watch them taste each other's saliva."
    y "Wow, you guys are taking to this a lot better than I expected."
    y "....don't forget about me."

    show tote tote11 with Dissolve(1.5)
    t "haha... aw, is someone feeling left out?"
    y "...a little."
    k3 "we haven't forgotten you, handsome."
    t "i kinda did."
    t "your lips are so soft, Katara!"
    k3 "yours too!"

    t "i can't believe how sexy it is kissing you with this big dick between us..."
    t "i'm so horny!"
    k3 "i know... i'm soaking his balls..."
    t "i thought that was me?"
    t "can i put him in me?"
    k3 "that's not the game!"
    k3 "what do you think aang... are you ready to judge our pussies?"
    y "this is already my favorite sport."

    k3 "alright toph, move your pussy up and down, like this."
    show tote tote100
    call pauseInterface
    k3 "just like that!"
    k3 "mmmmm...."
    "The two girls slide their wet pussies over your shaft, which throbs with every pressing grind."
    call pauseInterface
    k3 "Having two pretty girls using their lips on each other..."
    k3 "and their other lips on your dick..."
    k3 "...must be pretty nice, Aang."
    y "Nice? "
    y "I don't think it can get any better than this."

    call pauseInterface
    y "You two can get a bit rougher if you want."
    y "that'll help."
    k3 "oh? is that right?"

    show tote tote103
    k3 "like this?"
    call pauseInterface
    y "uhhhh..."
    t "i think he liked that."
    k3 "how about a little more?"
    call pauseInterface
    t "oh fuck... that feels good..."
    t "come on... yeah... ah... ah..."

    show tote tote101
    k3 "yes... ungh...."
    call pauseInterface
    y "oh shit..."
    k3 "you gonna cum, aang?"
    k3 "from my pussy?"
    t "no, he's gonna cum from mine!"
    t "isn't that right, aang?"
    t "isn't my pussy so wet and hot?"
    k3 "not more than mine!"
    y "Hnnng... i'm gonna..."

    hide tote
    show tote tote11
    with Dissolve(1)
    t "you gonna cum, twinkletoes?"
    t "cover these hot young bodies in sperm?"
    show tote tote13 with dissolve
    k3 "will you soak us, aang?"
    k3 "tits and tummies sticky with your cum?"
    y "don't stop!"
    k3 "you heard him!"
    show tote tote104 with Dissolve(1)
    call pauseInterface
    y "fuck!"
    y "Okay now i'm really gonna cum!"
    t "cum from my hot pussy!"
    k3 "no, mine!"
    play sound "audio/gltch2b.mp3"
    show expression "bk3/katara/scissor/spermshot.png"
    pause 0.3
    hide expression "bk3/katara/scissor/spermshot.png" with Dissolve(1.0)
    play sound "audio/gltch2b.mp3"
    show expression "bk3/katara/scissor/spermshot.png"
    pause 0.3
    show tote tote11
    show expression "bk3/katara/scissor/sperm1.png"
    with Dissolve (1.5)
    hide expression "bk3/katara/scissor/spermshot.png" with Dissolve(1.0)

    call pauseInterface

    y "aaaah...."
    k3 "so?"
    y "...what?"
    t "who's was better?"
    y "....yes."
    t "that's not-"
    y "yes."
    k3 "hahaha... oh, aang..."
    k3 "this was a lot of fun, toph."
    k3 "thank you."
    t "i think we're all welcome."
    k3 "i think aang's about to fall asleep."
    t "let's join him."
    k3 "mm-hmm."
    call pauseInterface
 
    return
##### [Toph + Katara] Threesome Blowjob
label gallery_kat_toph_bj:
    call gallery_dCharacter_3Common

    show expression "ebackgrounds/bed_inside.jpg"
    show tote tote23
    show expression "bk3/katara/scissor/black.png":
        alpha 1.0
        linear 5.0 alpha 0.8

    t "I... I think I feel something..."
    t "A slightly increased pulse... it's slipping away again..."
    show expression "bk3/katara/scissor/black.png":
        alpha 0.8
        linear 2.0 alpha 1.0
    t "Should I take over?"
    show expression "bk3/katara/scissor/black.png":
        alpha 1.0
        linear 5.0 alpha 0.5
    show tote tote24
    k3 "Keep sucking that dick Toph... i think..."
    y "Whhaaa...ss... goin...on...?"
    "your voice sounds heavy and tired."
    show tote tote24a
    k3 "He's waking up!!"
    k3 "Aang!!"
    k3 "How are you feeling?!"
    show expression "bk3/katara/scissor/black.png":
        alpha 0.5
        linear 1.0 alpha 1.0
        linear 2.0 alpha 0.0
    y "...like shit..."
    y "As if someone replaced my brain with a cabbage..."
    hide expression "bk3/katara/scissor/black.png"
    show tote tote19 with Dissolve(1.5)
    t "so normal."
    y "screw... you..."
    t "He's fine!"
    t "I knew he'd come out of it."
    t "i wasn't worried for a single minute!"
    t "Aang's as tough as this fella is hard!"
    show tote tote21

    play sound "audio/kiss.mp3"
    show tobb_heart:
        xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
        xzoom 1 yzoom 1 alpha 1.0
        linear 1.0 xzoom 4 yzoom 4 alpha 0.0
    pause 1.3
    hide tobb_heart
    show tote tote19 with Dissolve(1.5)
    k3 "I'll have some of that too!"
    show tote tote22

    play sound "audio/kiss.mp3"
    show tobb_heart:
        xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
        xzoom 1 yzoom 1 alpha 0.5
        linear 1.0 xzoom 4 yzoom 4 alpha 0.5
    pause 1.3
    hide tobb_heart
    show tote tote19 with Dissolve(1.5)
    t "I feel like kissing some more..."
    k3 "Who's gonna stop us?"
    show tote tote20 with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show tobb_heart:
        xpos 560 ypos 350 xanchor 0.5 yanchor 0.5
        xzoom 1 yzoom 1 alpha 1.0
        linear 1.0 xzoom 4 yzoom 4 alpha 0.0
    pause 1.3
    hide tobb_heart
    show tote tote19 with Dissolve(1.5)
    y "I feel woozy."
    k3 "Don't get up just yet, you lost a lot of stamina."
    k3 "Maybe you should keep going Toph, Just to be sure."

    menu:
        "Yeah keep going":
            show tote tote24

        "That's not necessary":
            pass

    call pauseInterface
    y "Okay so, I like what I'm seeing, but I have no memory of starting all of this."
    y "What's going on?"
    k3 "I don't really know, I just found you on the floor, unconscious."
    k3 "It looks like a spirit almost sucked you dry of your lifeforce."
    show tote tote19 with dissolve
    t "I suggested to just give you a blowjob, to keep your blood flowing, and enticing your spirit to stay put!"
    k3 "That's right!"
    k3 "It was Toph's idea and she wasn't bawling her eyes out at all while you were lying there on the brink of death."
    t "Yeah, I... hey!!"
    show tote tote24 with dissolve
    t "*grumble...*"
    k3 "We've been taking turns, keeping you warm with our bodies and giving you continuous blowjobs."
    k3 "We figured your mind wouldn't leave before you got the chance to cum."
    y "Sooo... why didn't I cum?"
    k3 "My waterbending kept your sperm from escaping your balls. "
    k3 "It was easy!"
    y "That's not terrifying at all..."
    y "Thanks. "
    y "I owe you both big time."
    k3 "We'll continue for a few more minutes."
    k3 "Just to be certain."
    y "sounds good to me..."
    show tote tote19 with dissolve
    t "Can you take this one Katara?"
    t "I'd like to talk to Aang and that's kinda hard with a dick in my mouth."
    k3 "Of course!"
    show tote tote23 with Dissolve(1.5)
    call pauseInterface
    t "I... it was really devastating to see you lying there and not knowing what would happen."
    t "Not knowing whether you'd live or die..."
    y "Sorry, I didn't want to make you worry."
    t "I know... but it made me think and reconsider a lot of things..."
    t "You're not perfect, Aang."
    t "But neither am I, and I'm not willing to let whatever it is we have to be destroyed by something like jealousy."
    t "Me and Katara did a lot of talking."
    t "With one of us sucking your dick and the other listening, we've really come to understand each other better."
    t "I'm still not happy with your crazy sexdrive including anyone other than me."
    t "But... I'd rather share you than not have you at all."
    show tote tote27 with Dissolve(1.5)
    t "*Sniff...* I thought you were going to die and I'd never see you again..."
    y "Please don't cry Toph, if you cry I'll cry and things will get super awkward."
    y "I'm still alive!"
    y "and even if I did die I'd come back for you!"
    y "I'm the avatar, baby!"
    y "I reincarnate at the drop of a hat."
    y "and when I do, I'll come back and capture your heart all over again!"
    t "*Sniff...* but what if you'd reincarnate as a girl?"
    y "Well, I guess you'd have to learn how to munch carpet!"
    show tote tote23
    t "Hah..ahhahahah!! You dumbass!"
    t "You better shave or you can wait a long time for that to happen!"
    show tote tote19 with Dissolve(1.5)
    k3 "Ready for some unloading?"
    y "Fuck yeah!"
    y "I have two balls filled to the brim, and I'm going to dedicate one to each of my saviors."
    t "You go first, Katara."
    show tote tote25 with Dissolve(1.5)
    k3 "Aaaah!!"
    play sound "audio/gltch2b.mp3"
    pause 0.5
    play sound "audio/gltch2b.mp3"
    show expression "bk3/katara/scissor/bj_sperm_katside.png"
    k3 "oh!!"
    show tote tote26
    hide expression "bk3/katara/scissor/bj_sperm_katside.png"
    show expression "bk3/katara/scissor/bj_sperm_katside.png":
        xpos 75
    with Dissolve(1.5)
    t "My turn!"
    show expression "bk3/katara/scissor/bj_sperm_topside.png"
    play sound "audio/gltch2b.mp3"
    pause 0.5
    play sound "audio/gltch2b.mp3"
    t "ahhhh....!!!"
    hide expression "bk3/katara/scissor/bj_sperm_katside.png"
    hide expression "bk3/katara/scissor/bj_sperm_topside.png"
    show tote tote19
    show expression "bk3/katara/scissor/bj_sperm_katfront.png"
    show expression "bk3/katara/scissor/bj_sperm_topfront.png"
    with Dissolve(1.5)
    k3 "how do we look?"
    t "sticky?"
    t "my face feels very... warm."
    t "and... soaking wet."
    k3 "isn't it nice?"
    t "i love the smell..."
    y "I'm taking a mental snapshot of this moment and will consider it as my most precious memory."
    k3 "Well, we've bothered you long enough. "
    k3 "you don't want to push yourself too hard."
    t "you did a good job cumming on our faces, twinkletoes."
    k3 "you did! now get some well deserved rest!"
    y "I will..."
    
    return
##### [Ajala] Anal
label gallery_ajala_assfuck:
    call gallery_dCharacter_3Common
    
    show expression "maze/love_ceilingview_1.jpg"
    hide tosh
    show tosh tosh11
    with dissolve
    ct "hold on!"
    call pauseInterface
    ct "don't do anything... anything stupid!"
    ct "we can... we can work this out!"
    y "you know... i don't think we can."
    ct "W-what are you going to do?"
    y "oh, that's right... you can't see what's happening back here, can you?"

    y "I'm going to put something in your ass."
    y "Just like you did to Suki."

    y "but don't worry... I won't put a piece of metal in there."
    y "I'll use something harder, thicker and longer."
    ct "d-don't."
    ct "i-i'm serious. don't... don't do that!"
    y "well, i might change my mind..."
    y "If you're a good girl."
    ct "...what... can i do?"
    y "i'll give you three seconds to figure it out."
    y "three."
    ct "w-what?"
    y "two."
    ct "wait!"
    ct "i'm sorry! i'm-i'm a stupid slut!"
    ct "and... and..."
    y "and?"
    show tosh tosh15 with dissolve
    call pauseInterface
    ct "and... i know i deserve a cock in my ass, but..."
    y "ha! ass-butt."
    ct "no... no... please, i'm... i'm just a caretaker!"
    ct "I just take care of the tunnels!"
    ct "please let me go!"
    show tosh tosh17 with dissolve
    y "you're not just a caretaker, you're the head guard, and a total cunt."
    ct "...yes! yes, it's true!"
    ct "i'm a total, raging cunt!"
    ct "please! whatever you need me to say, i'll say!"
    ct "i'm the head bitch!"
    y "with a big, tasty ass."
    ct "w-with a big, t-tasty ass..."
    y "you've had cocks in it before, i bet."
    ct "j-just toys!"
    ct "please......"
    y "hmm... you've begged very well..."
    y "maybe i'll let you go."
    ct "thank-"

    show tosh tosh12 with Dissolve(1.5)
    "her ass is resistant, but with a little push past her entrance..."
    "...you slide the head of your dick in surprisingly smoothly."
    ct "aaahhh!!"

    call pauseInterface
    y "That's right. How you like that, huh?"
    ct "ah! hgngh..."
    show tosh tosh12_1
    ct "you- you asshole!"
    y "no, let's focus on {i}your{/i} asshole."
    ct "pull it ou-"
    show tosh tosh101

    ct "nnnnhhhghhh!!"
    call pauseInterface
    ct "you said you'd let me go!"
    ct "*ah!* *mmng!* *ngh!*"
    show tosh tosh101_1
    ct "i'll *ungh!* kill you when *ah!* i get out!"
    y "{i}if{/i} you get out."
    y "besides, what about all that sexy talk you were doing?"
    y "about your tasty ass?"
    show tosh tosh101
    ct "*hngh!* *ah!* *ngh...*"
    ct "you... hgh... made me..."
    y "we both know what you were really begging for."
    ct "ahh... ohhn..."
    y "starting to enjoy it, huh?"
    ct "n-no... oh... ohhh... anhh...."
    call pauseInterface
    show tosh tosh101_1
    ct "I can't... ngh... believe this is happening... ah... this can't really be happening..."
    y "I bet you didn't expect to get some dick up your ass today, huh?"
    y "Maybe getting some of what you've been dishing out will make you think twice in the future."

    ct "f-fuck... you..."
    show tosh tosh101
    call pauseInterface
    y "bitch, i can see your pussy... hell, i can {i}smell{/i} your pussy."
    y "you are more turned on than anyone i've ever seen."
    y "and i've known some sluts."

    ct "nghg... mmm... ah.... ngh... not... not true..."
    y "oh, damn... you're close to cumming aren't you?"
    ct "ahh... ah... ohhh... ngh....."
    ct "nnn.... ha.... no..."
    y "should i stop?"
    show tosh tosh101_1
    ct "don't... almost... ahh..."
    y "you gonna cream, slut?"
    ct "ohhhhhhhh......."
    y "are you really gonna-"
    ct "{size=+4}uuhhhh....."
    show tosh tosh101
    ct "{size=+10}fuck!!!!" with vshake
    ct "{size=+10}me!!!!" with vshake
    show tosh tosh102

    call pauseInterface
    y "oh, fuck you got tight!"
    ct "{size=+10}mmmmmmmnghghpph!!! ahhh!!" with vshake
    y "hngh!"

    ct "{size=+10}yes!!!" with vshake
    show tosh tosh12
    play sound "audio/splurt2.ogg"
    with flash
    y "fuck!"
    ct "{size=+10}unngh!"
    ct "{size=+10}fill it!"
    play sound "audio/splurt1.ogg"
    show tosh tosh14
    with flash
    ct "{size=+10}yes!"
    show tosh tosh14_1
    ct "{size=+10}do it! fill my ass!"

    play sound "audio/splurt2.ogg"
    show tosh tosh12
    with flash
    ct "ohh...."
    hide tosh tosh12_1
    hide expression "maze/love_ceilingview_1.jpg"
    show tosh tosh16
    with Dissolve(1.5)

    ct "{size=-5}.......fuck."
    call pauseInterface
    y "....have fun?"
    ct "don't... don't say anything."

    ct "don't fucking talk to me right now..."
    y "alright, but..."
    y "I left you something nice to remember me by."
    y "...."
    y "It's sperm. I left my sperm in your ass."
    ct "I'll... i'll remember this..."
    y "While longing for more?"
    ct "n-no...."
    ct "......"
    ct "..........."
    ct ".................."
    y "you sure?"
    ct "....i've...."
    ct "I've never...."
    ct "....never been fucked like that...."
    ct "ever...."
    ct ".........."
   
    call pauseInterface

    return
##### [Ajala] Dildos
label gallery_ajala_dildos:
    call gallery_dCharacter_3Common

    show expression "maze/love_ajala_surprise.png" with hpunch
    ct "You found the girls!"
    ct "And they're safe and sound again!"
    hide expression "maze/love_ajala_surprise.png"
    show expression "maze/love_ajala_delight.png"
    with Dissolve(1.5)
    ct "Thank you."
    ct "And I'm guessing you'd like your reward now?"
    y "Yes, please."
    ct "Close your eyes."
    y "It's not that I don't trust you, but..."
    y "I did knock you out using a similar trick."
    y "So... I'll just keep them open."
    ct "Then I'll just show you something instead."

    hide expression "maze/love_ajala_delight.png"
    show expression "maze/love_ajala_toys.png":
        linear 5.0 ypos -150
    with Dissolve(1.5)
    call pauseInterface
    ct "Whenever I miss you... I use these."
    ct "They're a poor substitute for the real thing though."
    y "....."
    "As you stare at Ajala's bottom you hear someone shouting."
    call pauseInterface

    return
##### [Ajala] Fuck (Against the Wall)
label gallery_ajala_wonfight_10:
    call gallery_dCharacter_3Common

    show expression "ebackgrounds/bg_tunnelwall.jpg"
    show totv totv01
    ct "oooh..."
    y "okay, you're gonna tell me how to make that equipment undo hypnosis."
    ct "fine..."
    ct "what you do is..."
    show black with dissolve
    "ajala tells you how you'll have to change the equipment to get it to fully undo hypnosis."
    hide black with dissolve
    y "and that will do it?"
    ct "that will do it..."
    y "great!"
    y "and now..."
    y "Now spread those legs of yours."
    y "I wanna see my prize."

    show totv totv02 with Dissolve(1.5)
    call pauseInterface
    y "That's a nice looking pussy."
    y "People can say what they want about your body, but your tits and puss are as fine as any other out there."
    y "I'm going to pound that so hard you'll be walking bowlegged for the rest of the week."

    show totv totv03 with Dissolve(1.5)
    bk3_ajavag "....prove it."
    y "Oh, I will."
    y "You're a big girl, so I'll jump right in."

    show totv totv04

    bk3_ajavag "Hnnnnngh..."
    y "Oh, you're surprisingly tight."
    y "You training your pussy muscles too?"
    y "Doesn't matter."
    y "I'll tear down that soft fortress of yours..."
    y "one thrust at a time."
    call pauseInterface
    bk3_ajavag "You... ah... could go a little slower..."
    y "You want me to slow down?"
    bk3_ajavag "ah... just a... little..."

    y "You're absolutely right... I could do that."

    show totv totv03
    show totv_fuck_fast
    bk3_ajavag1 "{size=+4}AAAAAAh!!!"
    y "Or I could slam it in as hard as I can!"
    bk3_ajavag2 "Ah!! Sooo deep!"
    y "Come on, girl!"
    y "If you can't take my ramrod at full thrust, nobody can."
    y "Take one for the team!"
    y "And then another one! and another one!"
    call pauseInterface
    bk3_ajavag2 "Fuck.... fuck.... fuck...."
    y "I'm getting close!"
    y "veerry close..."
    bk3_ajavag2 "Ah! D-don't stop!"
    bk3_ajavag2 "Keep slamming it in!"
    y "Did I awaken your taste for cock?"
    bk3_ajavag2 "Yes! I need it! I need it badly!"

    hide totv_fuck_fast
    show totv_fuck_fastest
    y "Ready or not... here I cum!"


    menu:
        "cum inside":
            hide totv_fuck_fastest
            #$ b3love_ajala_mazevag = 2

            show totv totv06 with Dissolve(1.5)
            show totv totv07 with Dissolve(1.5)

            y "Sharing is caring."
            pause 0.8
            play sound "audio/gltch.mp3"
            pause 0.8
            play sound "audio/gltch2.mp3"
            show expression "bk3/ajala/vag/cum_xray.png" with Dissolve(3.0)
            call pauseInterface

            hide expression "bk3/ajala/vag/cum_xray.png"
            show totv totv08
            with Dissolve(1.5)
            y "Man, I came buckets!"

            show totv totv09
            show expression "bk3/ajala/vag/sperm_outside_4.png"
            with Dissolve(1.5)

            show expression "bk3/ajala/vag/sperm_outside_5.png" behind totv:
                xpos 550 ypos 550
                linear 3.0 ypos 590 xpos 530
            pause 3.5
            y "Looks like she's out cold!"

        "cum outside":
            hide totv_fuck_fastest
            show totv totv02 with Dissolve(1.5)
            y "Here's some moisturizer for your skin."
            play sound "audio/gltch.mp3"
            show expression "bk3/ajala/vag/sperm_outside_1.png" with Dissolve(1.5)
            play sound "audio/gltch2.mp3"
            show expression "bk3/ajala/vag/sperm_outside_2.png" with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/vag/sperm_outside_3.png" with Dissolve(1.5)
            y "That felt awesome."
            y "We absolutely need to do this again sometime."


    call pauseInterface
    y "Just enjoy the afterglow, you luscious muscle maiden."
    y "Fuck you next time."

    return
##### [Ajala] Fuck 
label gallery_ajala_dunk:
    call gallery_dCharacter_3Common

    show expression "ebackgrounds/ajala_dunkscene.jpg"
    $ temp_boolean = False
    show toxf toxf00
    ct "Hi, aang."
    ct "Could you help me with something?"
    y "Again?"
    play music "audio/Unwritten Return.mp3"
    hide toxf
    show toxf toxf01
    with Dissolve(1.5)
    y "uhhh, what are you doing?"
    ct "Holding this position is great for your abs... but more importantly..."
    ct "I want you to rip my pussy to shreds!"
    y "I certainly can, figuratively speaking."
    y "But don't you want me to earn it?"
    ct "No! I mean yes I do, but I can't enjoy it as much when I'm already worn out from fighting you."
    ct "I want to savor the experience."
    ct "Mark me as yours, avatar!"

    hide toxf

    show toxf toxf10:
        xpos 0 ypos 0
    with Dissolve(1.5)

    show toxf toxf10:
        linear 4.0 ypos -280

    ct "No matter what you think of my muscles, my pussy is still as soft and penetrable as any other girl's."

    menu:
        "Admire her fit body and pussy":
            y "I think you have an awesome body."
            y "And your muscular physique is a big part of that."
            y "You have to train hard to get like this and it makes you all the more attractive."
            y "....but waving that pussy in front of my face certainly seals the deal."

        "Only acknowledge her pussy.":
            y "You have a gorgeous pussy."
            y "And I'm going to wreck it."
            "Ajala looks slightly disappointed, as if she was hoping to hear something more, but quickly regains herself."

    ct "Would you like to see... all the way inside? "

    menu:
        "Gape that cunt for me, baby!":
            show toxf toxf11:
                linear 2.0 ypos -350
            y "That's a lovely cervix."

            hide toxf
            show toxf toxf03
            with Dissolve(1.5)
            y "...let's see if I can push into it."

        "No time for sightseeing":
            y "No need, my one eyed snake will take a more direct look for me."


    hide toxf
    show toxf toxf04
    with Dissolve(1.5)
    ct "Ooohh... I can't wait any longer! Do it!"

    show toxf toxf05 with Dissolve(1.5)
    "You lift up Ajala's legs."
    ct "Why...?"
    y "I can go in deeper like this."
    y "Now taste my cock!"
    show toxf toxf08 with hpunch
    pause 1
    show toxf toxf05 with Dissolve(1.5)


    show toxf toxf100
    ct "Aaaahh!!"
    call pauseInterface
    y "You're insides feel so hot!"
    y "Let's speed this up!"

    show toxf toxf101
    ct "Ah! Ah! Ah!"

    call pauseInterface

    show toxf toxf102
    y "This time with some more force!!!"
    call pauseInterface
    "You push down hard into Ajala's cunt, forcibly smacking your balls against her ass in the process."
    y "Take this! And this!"
    ct "AAAaah!! I'm going crazy!!!"

    menu:
        "cum inside":
            $ temp_boolean = False
            show toxf toxf08
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface
            show toxf toxf09

            show expression "bk3/ajala/dunk/spermin.png":
                xpos 20 ypos 30
            with Dissolve(1.5)
            ct "I'm so full...."
            hide expression "bk3/ajala/dunk/spermin.png"
            hide toxf

            show toxf toxf10:
                ypos -210

            show expression "bk3/ajala/dunk/spermin2.png":
                ypos -210

            show expression "bk3/ajala/dunk/frontbody_lewdface.png":
                ypos -210
            call pauseInterface
            scene black

        "cum in gaping cunt":
            $ temp_boolean = False
            hide toxf
            show toxf toxf04
            with Dissolve(1.5)
            y "Open it up for me."
            show toxf toxf02
            y "awesome"
            hide toxf

            show toxf toxf11:
                linear 2.0 ypos -350
            y "Gonna drown that womb in my cum."
            show expression "bk3/ajala/dunk/frontdick.png" with Dissolve(1.5)

            show toxf toxf11:
                ypos -350
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/dunk/frontsperm1.png"
            with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/dunk/frontsperm2.png"
            with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/dunk/frontsperm3.png"
            with flash
            call pauseInterface
            scene black

        "cum outside":
            $ temp_boolean = True
            hide toxf
            show toxf toxf04
            with Dissolve(1.5)
            y "Here I cum!"

            play sound "audio/gltch2b.mp3"
            show toxf_spermshot
            show expression "bk3/ajala/dunk/spermout1.png"

            y "Hnngg..."
            play sound "audio/gltch2b.mp3"
            show toxf_spermshot
            show expression "bk3/ajala/dunk/spermout2.png"
            y "Nnnghhh!!!"
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show toxf_spermshot
            show expression "bk3/ajala/dunk/spermout3.png"
            ct "You could provide for a small village with this amount!"
            y "It wouldn't be the first time."
            call pauseInterface
            scene black


    hide toxf

    if temp_boolean:
        show expression "ebackgrounds/ajala_dunkscene.jpg"

        show toxf toxf00b:
            xpos 0 ypos 0
            linear 5.0 ypos -200
        with Dissolve(1.5)

    else:
        show expression "ebackgrounds/ajala_dunkscene.jpg"

        show toxf toxf00a:
            xpos 0 ypos -780
            linear 7.0 ypos -100
        with Dissolve(1.5)
        pause 5

    ct "Thanks, Aang."
    ct "..."

    return 
##### [Katara] Train Handjob
label gallery_love_train_hj:
    call gallery_dCharacter_3Common

    scene totr totr101
    show toki toki01
    k3 "what's that?"
    y "what?"
    k3 "you're sitting on something."
    y "i am?"
    "you reach under your seat and find a magazine..."
    "...but the pages are stuck together."
    k3 "is that a pornlove?"
    y "yeah, but... ew... the pages are stuck together..."
    y "man, what a waste."
    k3 "that is a waste, isn't it?"
    k3 "i mean... how will you get off without a magazine?"
    y "......."
    y "i don't {i}need{/i} a magazine, it just helps."
    show toki toki_smile
    k3 "what if... i helped you instead?"
    y "...we're on a train, katara."
    y "we'd get caught."
    k3 "maybe not."
    hide toki with dissolve
    "katara slips onto the seat next to you."
    y "what are you..."
    k3_h "want me to jack you off?"
    y "...."
    y "...are you serious?"
    k3_h "yeah!"
    k3_h "come on, it'll be fun!"
    y "we're on a train... we could get caught."
    k3_h "i don't care."
    y "i don't know..."
    show tokh arm_hj
    with Dissolve(1)
    "ignoring you, katara pulls out your cock and lightly wraps her hand around it."
    y "um."
    "she grips her fingers around your shaft and squeezes you as she pulls."
    k3_n "mmm... you got hard quickly."
    y "w-well yeah... damn..."
    show tokh arm_hj2
    "katara's stroking becomes more insistent."
    y "unnngh...."
    k3_h "you're getting turned on, aren't you?"
    k3_n "hmmm..."
    "you look back down at her hand, now truly pumping your cock."
    hide totr
    hide tokh
    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    show expression "maze/sp_prisonbitch.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    show expression "maze/sp_prisonbitch_clothes.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    show tokh arm_hj2
    with Dissolve(1.5)

    dap2 "hello, is this-"
    dap2 "oh!"
    y "um... occupied..."
    dap2 "i... i see that..."
    dap2 "i'll just... go..."
    dap2 ".........."
    k3_p "you like his cock, don't you?"
    dap2 "um..."
    k3_n "don't be shy."
    dap2 "it... it is handsome..."
    y "why... fuck... why are you wearing those rags?"
    dap2 "i escaped a... a real maze of a place."
    dap2 "i haven't had a chance to change."
    k3_n "would you like to see something fun?"
    show tokh arm_hj3
    "katara speeds up even more, working your cock to ecstasy."
    y "oh... oh shit..."
    call pauseInterface
    "the woman stares at your cock as katara rapidly hand-fucks it."
    k3_n "you're among friends here... you can take off your clothes."
    dap2 "i don't know if-"
    k3_p "do it."
    dap2 "...o-okay..."
    hide expression "maze/sp_prisonbitch_clothes.png" with dissolve
    y "oh... shit... that... worked..."
    dap2 "i've been... been following orders for so long..."
    k3_n "you can relax, you're in good hands...."
    y "are you... talking to... her or me, katara?"
    k3_n "yes."
    y "unnhh..."
    k3_h "oh dear, are you about to cum?"
    y "fffuuuuuu...."
    k3_p "huh? you gonna cum?"
    k3_p "you gonna cum all over my little hands?"
    k3_u "right here on the train?"
    k3_u "we won't be able to hide it, you know..."
    k3_n "what will people say?"
    y "uhh... katara... unh..."
    k3_p "do it. cum on her."
    dap2 "wait..."
    k3_p "cum on that slut."
    k3_p "let me see you shoot that big load."
    y "I'm... gonna..."
    dap2 "hold on, i don't-"
    k3_h "shoot that big, sticky, thick load on-"

    play sound "audio/splurt2.ogg"
    hide totr
    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    hide expression "maze/sp_prisonbitch.png"
    show expression "maze/sp_prisonbitch.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    show expression "maze/sp_prisonbitch_sperm1.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    hide tokh
    show tokh arm_hj3
    with flash
    dap2 "oh!"
    play sound "audio/splurt3.ogg"
    hide totr
    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    hide expression "maze/sp_prisonbitch.png"
    show expression "maze/sp_prisonbitch.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    hide expression "maze/sp_prisonbitch_sperm1.png"
    show expression "maze/sp_prisonbitch_sperm2.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    hide tokh
    show tokh arm_hj3
    with flash

    dap2 "you... you're... you're cumming all over m-"
    k3_h "drench that bitch!"
    play sound "audio/splurt2.ogg"
    hide totr
    show totr totr101:
        ypos -10
        linear 1 ypos 0
        ypos 0
        linear 1 ypos -10
        repeat
    hide expression "maze/sp_prisonbitch.png"
    show expression "maze/sp_prisonbitch.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    hide expression "maze/sp_prisonbitch_sperm2.png"
    show expression "maze/sp_prisonbitch_sperm3.png":
        xpos 300 ypos 0
        linear 1 ypos 10
        ypos 10
        linear 1 ypos 0
        repeat
    hide tokh
    show expression "bk3/katara/handjob/kat_arm_6.png":
        xpos 400 ypos 320
    show expression "azula/handjob/az_sperm_3.png":
        xzoom -1 rotate 20 xpos 100 ypos -165
    with flash
    call pauseInterface
    dap2 "......."
    k3_h "mmmm.... good for you, aang..."
    k3_h "you came all over that slut."
    k3_h "you also came all over my hand..."
    dap2 "i... i think i should... i should go..."
    hide expression "maze/sp_prisonbitch_sperm3.png"
    hide expression "maze/sp_prisonbitch.png"
    with moveoutright
    "the woman leaves in a hurry, but gives one last look before closing the door."
    k3_h "hahahaha!"

    return
##### [Katara] Party Sex
label gallery_katara_party_fuck2:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    scene inside_hospital
    show tokp tokp20 with Dissolve(1.5)
    y "...well, fuck me."
    show tokp tokp21
    k3 "that's the plan."

    show tokp tokp22 with Dissolve(1.5):
        ypos 400
        easeout 6 ypos -50
        easein 4 ypos 400
    call pauseInterface
    k3 "like the view?"
    k3 "it's all yours..."
    k3 "but before we begin..."
    k3 "do you have any requests?"

    menu:
        "small":
            $ tokp_titsize = 'small'

        "medium":
            $ tokp_titsize = 'medium'

        "big":
            $ tokp_titsize = 'big'

    hide tokp
    show tokp tokp00 with Dissolve(1.5)
    k3 "wanna saddle up, cowboy?"
    call pauseInterface
    y "what? are you a horse now?"
    k3 "i'm just a simple, high-class girl... looking to get ridden."
    k3 "don't tell my papa."
    show tokp tokp01
    k3 "especially don't tell him... how wet i am right now."
    call pauseInterface
    k3 "my pussy's on fire, baby..."
    k3 "Mmmm...."
    k3 "you gonna fill this little cunt?"
    k3 "wanna make me cry?"
    y "give me a better view."
    y "open that pussy."
    k3 "if that's what you want..."
    show tokp tokp02
    call pauseInterface
    k3 "is this what you like? making me spread my pussy?"
    k3 "me on display?"

    menu:
        "get a taste first":
            y "I want to lick those pretty lips."

            show expression "bk3/katara/party/lewd.png":
                xpos 418 ypos 111

            show tokp_lick:
                xpos 430 ypos 320
            k3 "aahhh....ohhhhh..."
            k3 "soo... hot..."
            y "you... taste... so... fucking... good..."
            k3 "ahh... ngh... yes..."
            k3 "don't stop... don't ever stop..."
            y "these are your best lips."
            k3 "mmmmm.... that's it, avatar..."
            k3 "lick my little kitty...."
            hide tokp_lick
            hide expression "bk3/katara/party/lewd.png"

        "straight to the dicking!":
            pass

    show expression "bk3/katara/party/solodick.png" with Dissolve(2.0):
        xpos 390 ypos 600
        linear 2 ypos 300
    y "i can't wait any more."
    k3 "don't, baby. don't wait."
    k3 "i've been dying for your cock."

    show tokp tokp04
    k3 "i was so wet thinking about you fucking toph after the party."
    y "i... didn't, though..."
    k3 "didn't stop me thinking about it..."
    k3 "and jilling off behind a cart."

    hide expression "bk3/katara/party/solodick.png"

    show tokp tokp05 with dissolve
    call pauseInterface
    k3 "mmm... yes..."
    y "let me know if you need me to go slow or-"
    k3 "hush... and put it inside me."

    show tokp tokp03
    call pauseInterface
    k3 "ahhh...."
    k3 "Mmm... yes, baby..."
    k3 "oh, fuck yes... i've been waiting... ah... for this..."
    call pauseInterface
    k3 "work my little cunt, baby..."
    k3 "stretch that wet, slurping pussy-"
    show tokp tokp100
    k3 "ahh!"
    call pauseInterface
    k3 "ah! oh! fu-fuck!"
    k3 "eas-easy! ah!"
    k3 "yess.... oh, fuck me!"
    k3 "fuck me, aang!"
    k3 "fill up your whore!"
    call pauseInterface
    k3 "put your seed in my warm, tight pussy!"
    k3 "i know you need it! i know you need it!"
    k3 "let it out! let me take it!"

    menu:
        "cum inside":
            show tokp tokp08 with Dissolve(1.0)
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            show tokp tokp06
            with flash
            y "unngh..."
            k3 "mmm.... so warm... deep up in my pussy..."
            call pauseInterface
            show tokp tokp07
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "filling me... coating me..."
            k3 "i love fingering myself while stuffed and leaking your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."

        "cum outside":
            show tokp tokp02 with Dissolve(1.0)
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/katara/party/spermout1.png"
            y "unngh..."
            k3 "mmm.... so warm... cover me..."
            play sound "audio/splurt1.ogg"
            show expression "bk3/katara/party/spermout2.png"
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "coating me... marking me..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/katara/party/spermout3.png"
            y "hngh..."
            k3 "mmmm... thank you."
            k3 "i love fingering myself while drenched in your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."

        "piss on me katara":
            k3 "Wha-what?"
            y "Make me golden!"
            k3 "Okay, but don't forget you asked me!"
            show tokp tokp08 with Dissolve(1.0)

            show tokp_piss:
                xpos 370 ypos 100
            k3 "aanhhh....."
            y "yes! cover me, whore!"
            k3 "mmmnn... fuck...."
            call pauseInterface
            y "I'm gonna cum!"
            k3 "ahhh... cum.... nngh.... cum, baby...."
            ya "take... it!"
            k3 "give it all to me!"
            play sound "audio/splurt2.ogg"
            hide tokp_piss
            show tokp tokp06
            with flash
            y "unngh..."
            k3 "mmm.... so warm... deep up in my pussy..."
            call pauseInterface
            show tokp tokp07
            k3 "fuck yes..."
            k3 "hngh... i love your cum...."
            k3 "filling me... coating me..."
            k3 "i love fingering myself while stuffed and leaking your thick, white load..."
            k3 "did you need that as much as i did?"
            y "maybe more."
            k3 "mmm... i doubt it."

    call pauseInterface
    return
##### [Katara] Fuck
label gallery_katara_rub_sex:
    call gallery_dCharacter_3Common

    $ temp_boolean = False
    $ temp_boolean2 = False
    scene floor_tokt
    show totk totk03
    with Dissolve(1)
    play music "audio/Unwritten Return.mp3"
    call pauseInterface
    k3 "aren't i good girl, master?"
    k3 "have you gotten a good eye-full?"
    y "not yet, slut."
    show totk totk04 with dissolve
    "you see a shiver a pleasure run through katara." with vshake
    show totk totk03 with dissolve
    k3 "master?"
    y "you're going to put two fingers in that cute little pussy."
    k3 "right here?"
    y "do as you are told, slut."
    show totk totk01 with Dissolve(1)
    "katara begins rubbing her fingers against her pussy."
    "she lets out a little gasp as she slips her fingers inside."
    k3 "ahh..."
    k3 "mmmm..."
    call pauseInterface
    k3 "ohhh... yes..."

    menu:
        "spit on her tits":
            $ temp_boolean2 = True
            play sound "audio/spit.mp3"
            show expression "bk3/joodee/titplay/spithead.png":
                xpos 100 ypos 180
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 30 ypos -305
            with flash
            "you spit... but miss and hit katara's chin instead."
            "luckily, most of it slides off of her face and onto her tit."
            show totk totk02
            hide expression "bk3/joodee/titplay/spitmouth.png"
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 80 ypos -264
            with dissolve
            "katara slowly looks up at you with surprise, spit dripping its way down around her well-rounded breast."
            "you notice, grinning, that she doesn't even slow down finger-fucking her pussy."

            k3 "you... spit on me."
            y "is that a problem?"

            "katara blinks once, carefully, smiling mischeviously."
            k3 "no."
            show totk totk01
            hide expression "bk3/joodee/titplay/spitmouth.png"
            show expression "bk3/joodee/titplay/spitmouth.png":
                rotate 40
                xpos 30 ypos -305
            with dissolve
            y "want me to spit on you again?"
            k3 "...maybe..."

        "call her beautiful":
            y "you're so beautiful, katara."
            show totk totk02
            "katara looks at you warmly, her fingers still working vigorously in and out of her cunt."
            play sound "audio/kiss.mp3"
            with pflash
            "she gives you a warm, wet kiss and pulls back gently."
            k3 "don't ruin the game, love..."
            y "right."
            y "*ahem*"
            y "you want me to spit on you?"
            k3 "...maybe..."

    y "too bad."
    y "stop."
    k3 "w-what..."
    y "i said stop!" with hpunch
    show totk totk00

    if temp_boolean2:
        hide expression "bk3/joodee/titplay/spitmouth.png"
        show expression "bk3/joodee/titplay/spitmouth.png":
            rotate 40
            xpos 80 ypos -264
    with dissolve
    k3 "i... why?"
    y "i can hear your sopping wet pussy... there's no way your little fingers are cutting it."
    y "i mean, look at it."
    scene black
    scene expression "ebackgrounds/ceiling_1.jpg"
    hide totk
    show totk totk17
    with fade
    y "you're dripping down your legs."
    k3 "I... i know..."
    call pauseInterface
    y "it looks to me..."
    show totk totk14 with Dissolve(1.5)
    "you stand behind katara and slide your hand down over belly as she lifts her arms."
    k3 "oh!"
    y "...like you could use a little help."
    call pauseInterface

    k3 "don't... don't tease me, aang..."
    k3 "i'm... i'm aching here..."
    y "what do you want?"
    k3 "i-in... put them in... please..."
    k3 "be... be inside me..."
    y "oh? was i right? do you need help?"
    k3 "...yes! yes, you were right!"
    k3 "please... i need help... i need your help..."
    k3 "will you please-"
    show totk totk11 with Dissolve(1)
    k3 "ohhh... {i}fuck{/i}!"
    call pauseInterface
    "you slide two fingers in and out of katara's already very moist pussy."
    k3 "ohh... oh yes... ohh... aang..."
    k3 "spirits, that's... goooood..."
    call pauseInterface
    k3 "you got... how did you get so good..."
    k3 "did you practice on a lot of bitches while you were gone?"
    y "...gone?"
    k3 "you... ah... you know what i... ah... mean..."

    "The amount of pussy I got...."

    y "you have the sweetest pussy in the world, katara."
    k3 "i'm... unnh... so happy you... ahh... think so..."
    k3 "it's all yours... you're so so so... good with it..."
    k3 "it belongs to you... oh spirits... you really... ah... own this pussy..."
    y "so speaking of skills i gained..."
    y "Let me show you a new trick."
    k3 "what-"
    show totk totk15 with vpunch
    k3 "oh, {i}fuck{/i}!!!"
    "you start finger-fucking her at a furious pace, her whole body bucking against your hand in pleasure."
    k3 "AAAaaaah!!!!"
    k3 "oh, fuck!"
    k3 "oh fuck, aang!"
    k3 "i'm... i'm..."
    y "cum, katara!"
    y "you slut, you little brown slut, i wanna feel you squirt!"
    k3 "ungh... ah... ah...!!!"
    y "who owns you!?"
    k3 "you do!"
    y "who owns you!?"
    k3 "{size=+5}{i}you!!!"

    show expression "bk3/suki/pussyrub/pjuice_1.png" with vshake
    k3 "Aaah!!!"

    show expression "bk3/suki/pussyrub/pjuice_2.png" with vshake
    k3 "AAahh!!"

    show totk totk16
    show expression "bk3/suki/pussyrub/pjuice_3.png" with vshake
    k3 "AAAAAAAAAAAahh!!"
    call pauseInterface

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.5)

    k3 "fuck... fuck... fuck..."
    k3 "Okay, I'm not... i'm not complaining, but what.."
    show totk totk17 with dissolve
    "you gently pull your arm away, and katara leans back against you."
    k3 "shit... fuck, my legs are shaking..."
    k3 "what about you?"

    show totk totk06 with Dissolve(1.5)
    "You drop your pants and stick your erect dick in between her legs."
    k3 "oh..."
    k3 "aang... umm..."
    k3 "i love your cock, you know that, but..."
    k3 "it's... it's not safe today..."
    k3 "but... but you can rub against me..."
    k3 "Just... just rub a bit..."
    k3 "i want... i want to feel your cock on my clit..."
    show totk totk05

    call pauseInterface
    k3 "oh, spirits..."
    k3 "i should have known you wouldn't be able to keep it in your pants."
    y "are you disappointed?"
    k3 "are you kidding?"
    k3 "you should have started with this."
    k3 "I'm surprised you didn't..."
    k3 "you know how much i love your cock, aang."
    call pauseInterface
    "katara's still soaking pussy immediately lubricates your cock..."
    "her wet juices coat your cock as fuck against her warm, plush lips with a velvet smoothness."
    k3 "ahhh..."
    k3 "it's too bad we can't have sex..."
    y "are you sure we can't?"
    k3 "i'm sure... today isn't a safe day..."
    k3 "you can go ahead and cum between my thighs, though."
    y "you're so slick though, it's hard not to accidentally-"
    show totk totk06 with dissolve
    show totk totk07 with vpunch
    k3 "ah!"
    k3 "a-aang!"
    k3 "y-you're inside me!"
    call pauseInterface

    y "fuck you're tight... and wet..."
    show totk totk08 with Dissolve(1.5)
    k3 "unnh..."
    k3 "what... ah... are you... {i}fuck...{/i} doing...?"
    call pauseInterface
    y "i'm using your body... is that a problem?"
    k3 "my pussy is... unh... yours to use whenever, aang..."
    k3 "you know that..."
    k3 "I just want to remind you... mmmgh... it's not... ah... safe..."
    y "who gives a shit?"

    menu:
        "rub her tits while you fuck her":
            $ temp_boolean = True
            y "Lift your arms."
            show totk totk09 with dissolve
            k3 "why...?"
            show totk totk10 with dissolve
            "You start kneading her tits tenderly as you slide your shaft in and out of katara."
            k3 "ohhhh.... fuck, you know me..."
            call pauseInterface

        "keep going like this":
            call pauseInterface
            pass

    k3 "we... we shouldn't be doing this..."
    k3 "what are we doing..."
    y "i'm enjoying your body."

    if temp_boolean:
        y "...and your big, warm tits."
    y "and you don't seem to be stopping me."
    k3 "i... i can't... i'm... oh... i'm powerless with you..."
    k3 "whatever... whatever you want... whatever you need..."
    k3 "take it..."
    show totk totk08 with Dissolve(1)
    y "Okay, then."
    y "you asked for it."
    show totk totk100
    call pauseInterface
    "you start pumping your hard cock into Katara's tight pussy at a higher speed."
    k3 "HHNNnnngg!"
    k3 "i'm... i'm getting close again, my love..."
    y "damn, I'm about to cum, too."
    y "Where do you want it Katara? In or outside!?"
    k3 "Whatever... unf! you like!"
    k3 "i'd love to be full of your baby batter, but..."
    k3 "...if you don't want kids, you shouldn't shoot it in me..."
    k3 "unghh.... fuck, i love this cock!"
    y "oh shit you got even tighter!"
    k3 "it feels so good!!"
    y "fuck, i'm gonna cum!"

    menu:
        "Inside it is!":
            $ temp_boolean2 = True
            $ katara_cum_inside = True
            y "Here... it... comes !"
            show totk totk12
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            k3 "Mmmm...."
            y "Once for fun."
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Twice for making sure."
            k3 "fuck..."
            k3 "i can feel you drowning my womb..."
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "And thrice just because I find it impossible to pull out of you before emptying my sack."

            hide totk
            show totk totk06
            show expression "bk3/katara/rub/sperm_flowout.png"
            with Dissolve(1.5)
            y "....aaand I'm empty."
            k3 "Mmmmmm... I hope you are!"
            k3 "How can your balls contain this much?!"
            y "Spermbending?"
            call pauseInterface

        "cum outside":
            $ temp_boolean2 = False
            hide totk
            show totk totk19
            with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"
            show expression "bk3/katara/rub/body_butt_sperm1.png"
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/katara/rub/body_butt_sperm2.png"
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/katara/rub/body_butt_sperm3.png"
            call pauseInterface
            "You barely manage to pull out and cum all over Katara's ass."
            y "You're just too pretty and sexy, Katara!"
            k3 "You're pretty handsome too."
            call pauseInterface

    k3 "that felt amazing."
    hide expression "bk3/katara/rub/sperm_flowout.png"
    hide expression "bk3/katara/rub/body_butt_sperm1.png"
    hide expression "bk3/katara/rub/body_butt_sperm2.png"
    hide expression "bk3/katara/rub/body_butt_sperm3.png"
    play sound "audio/kiss.mp3"
    show pink
    show totk totk03
    call pauseInterface
    scene black
    scene floor_tokt
    show totk totk03
    with Dissolve(2)

    if temp_boolean2:
        k3 "it was dangerous finishing in me, aang..."
        k3 "i'm happy you did, though..."
        k3 "i love how i feel when you're filling me with your... spunk."
        k3 "...do you want to see my belly swell up with your kid?"
        k3 "is that why you came in me?"
        y "maybe."
        k3 "i'm always yours, you know."
        k3 "whatever you'd like to do with me."
        k3 "one thing to keep in mind, though..."
        k3 "we will have to work on toph if i'm going to have your offspring swelling up my belly."
        k3 "we'll worry about that later though, if it happens."

    else:
        k3 "we have to do this again."
        k3 "soon."
        y "we will."
        k3 "i can't be without your cock anymore, aang... i just can't."
        y "i understand, we'll figure it out."
        k3 "we will have to work on toph, but..."
        k3 "we'll worry about that later."

    k3 "oh..."
    k3 "you poor thing, you're a mess."
    y "what? my dick?"
    k3 "yes."
    k3 "come here..."
    hide totk with Dissolve(1)
    scene black
    scene floor_tokt
    show expression "bk3/toph/anal/bodykat0.png"
    show expression "bk3/toph/anal/dick_hold.png"
    with Dissolve(1)
    k3 "every woman should clean her man's cock after sex."
    y "....i couldn't agree more."
    hide expression "bk3/toph/anal/dick_hold.png"
    show expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*shluuurp!*"
    show expression "bk3/toph/anal/dick_hold.png"
    hide expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*ah!*"
    k3 "i taste pretty good...."
    k3 "and so do you."
    k3 "your semen is a gift... especially if your girl makes you cum."
    y "you did do that..."
    k3 "exactly!"
    k3 "the mess is my fault, after all."
    k3 "besides, you have places to go, and things to do!"
    k3 "i can't let you go out there with a cum-and-pussy-juice covered cock..."
    k3 "i have my pride."
    hide expression "bk3/toph/anal/dick_hold.png"
    show expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*mmhh...*"
    "katara gives your cock a final, long, deep suck."
    show expression "bk3/toph/anal/dick_hold.png"
    hide expression "bk3/toph/anal/dick_suck.png"
    with dissolve
    k3 "*mwah!*"

    return
##### [Smellerbee] Blowjob
label gallery_smellerbee_blowjob2:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg"
    show tosb tosb01 with Dissolve(1.5)

    sb "Show me your penis."
    y "okay..."
    show tosb tosb02
    sb "It looks... big..."
    y "Wanna stop?"
    sb "No way."
    show tosb tosb06
    sb "*Sniff* *sniff*"
    show tosb tosb02
    sb "It has a funny smell."
    sb "Not bad, just particular."
    show tosb tosb03
    sb "I'm going to start with a... with a handjob."

    show tosb tosb04
    sb "Pretty easy."
    sb "Does this feel good?"
    y "Yeah... it's really nice."
    show tosb tosb05
    sb "I'm getting the hang of this."
    $ smellerbee_fountain = True

    menu:
        "cum on her face":
            y "I'm about to cum!"
            sb "O-okay... aim for my mouth so I can keep my clothes clean."
            show expression "bk3/smellerbee/bj/openmouth.png"
            sb "Go ahead."
            play sound "audio/splurt2.ogg"
            show expression "bk3/smellerbee/bj/sperm1.png"
            call pauseInterface
            play sound "audio/splurt3.ogg"
            show expression "bk3/smellerbee/bj/sperm2.png"
            call pauseInterface
            play sound "audio/splurt1.ogg"
            show expression "bk3/smellerbee/bj/sperm3.png"
            show tosb tosb03
            y "Ah fuck. that was great."
            call pauseInterface
            show expression "bk3/smellerbee/bj/sperm4.png"
            hide expression "bk3/smellerbee/bj/sperm3.png"
            hide expression "bk3/smellerbee/bj/sperm2.png"
            hide expression "bk3/smellerbee/bj/sperm1.png"
            hide expression "bk3/smellerbee/bj/openmouth.png"
            play sound "audio/gulp2.mp3"
            sb "*gulp*"
            sb "That was a bit more than I expected."
            y "You didn't have to swallow it, you know."
            sb "I... guess I just wanted to taste it."
            sb "It's not as bad as I heard."
            hide expression "bk3/smellerbee/bj/sperm4.png"
            show tosb tosb00 with Dissolve(1.5)

            show tosb tosb50
            sb "If you want to do this again sometimes come and look me up."
            sb "See you later, Aang!"
            hide tosb tosb00

            call pauseInterface
            return

        "suppress cumming":
            pass

    show tosb tosb03
    sb "This really doesn't feel like enough."
    sb "Can't I do something more?"
    y "Well, I guess there's one thing which I'd like more..."


    y "Just doing the same, but with your mouth."
    sb "If my mouth is what it'll take, then that's what I'll do."
    show tosb tosb10
    "Just pushing the tip against her lips feels fantastic."
    y "You can start whenever you feel like it."
    y "Start with the tip."
    y "You can go deeper when you feel comfortable doing so."
    show tosb tosb100
    sb "*sluurp* *gulp*"
    call pauseInterface
    y "This is awesome... I'm very happy you're willing to do this for me."
    show tosb tosb101

    y "you can really... ugh... go deep..."
    sb "*gltch* *mghg* *gag*"
    call pauseInterface
    show tosb tosb102
    y "I'm getting very close to cumming...."
    y "Here it comes!"
    sb "go ahead!"
    sb "cum in my mouth when you're ready."
    play sound "audio/splurt2.ogg"
    show tosb tosb16
    with flash
    play sound "audio/splurt3.ogg"
    with flash
    show tosb tosb17
    play sound "audio/splurt1.ogg"
    with flash


    sb "I managed to swallow most of it, but that was a big load!"
    show tosb tosb00 with Dissolve(1.5)
    call pauseInterface

    sb "If you want to do this again sometimes, come and look me up."
    show tosb tosb50
    sb "See you later, Aang!"
    hide tosb tosb00

    call pauseInterface

    return
##### [Smellerbee] Fuck
label gallery_smellerbee_fuck:
    call gallery_dCharacter_3Common

    $ temp_boolean = False
    show tosb tosb51
    sb "aang, quick!! Follow me into this alley!"
    hide tosb with dissolve
    "smellerbee races around the corner before you can process what happened."
    "a little delayed, you follow in behind her."
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg"
    show toxg toxg10:
        ypos -300
        linear 6.0 ypos 0
    with Dissolve(1.5)
    y "uuhh... your pants are missing..."
    sb "i met jet! he told me you saved him!!!"
    y "I can't see them anywhere."
    y "Did you throw them in a garbage bin?"
    sb "I was so happy Jet is okay... "
    y "Do you need money for a new pair?"
    sb "I just can't help myself."
    y "Maybe some tight fitting jeans with rips in it?"
    sb "I thought I would never see him again..."
    y "oh, yeah, about Jet...."

    show toxg toxg09 with Dissolve(1.5)
    sb "...I take this off, you bend me over and take me like a little bitch in heat?"
    call pauseInterface
    hide toxg
    show expression im.Flip("bk3/smellerbee/bj/bg_alley_fountain.jpg",horizontal=True)
    show expression "bk3/smellerbee/fuck/shadow.png"
    with Dissolve(1.5)

    show toxg toxg00b with Dissolve(1.5)

    sb "Come on! I want a dick in my little pussy for once!"
    call pauseInterface
    show toxg toxg00
    y "...I can do that."
    call pauseInterface
    show toxg toxg00a
    sb "Ah!!"
    sb "Oh, sorry. I'm reasonably new to anything not going up my ass."
    show toxg toxg01
    y "We can take our time."
    show toxg toxg04 with Dissolve(1.5)
    sb "Mmmmmmmhhh!!"
    call pauseInterface
    show toxg toxg01 with Dissolve(1.5)
    sb "Give it to me Aang!"
    sb "I'm ready!"

    hide toxg
    show toxg toxg100:
        xpos 20 ypos 0
    sb "That's it!"
    call pauseInterface
    sb "Aaah... you're stretching my pussy in every direction under the sun!"
    sb "I LOVE IT!"
    y "Hngh... glad to be of service."
    sb "My pussy has needed servicing for a loooong time now."
    call pauseInterface
    y "Just... just asking, but would you mind if I cum inside you?"
    sb "That's no problem."
    sb "Make a nice creampie or cum all over me."
    sb "It's all fine."
    call pauseInterface
    sb "Can... Can you slam it?"
    sb "Like really hard?"
    sb "my cunt is so new it's practically under warranty."
    sb "so treat me like it!"
    sb "slam me hard!"
    sb "Don't let my small stature fool you! I can take it. I need it!"
    y "Honestly, I was going to do that anyway."
    y "Starting...."
    hide toxg
    show toxg toxg101
    y "now!!!" with flash
    sb "{size=+6}HGHHGHNNNGNG!!"
    call pauseInterface
    sb "{size=+6}YESSS!!"
    sb "{size=+6}FUCK IT! fUCK IT HARD!!!"

    menu:
        "cum inside":
            $ temp_boolean = True
            show toxg toxg07
            play sound "audio/gltch2b.mp3"
            show toxg toxg07 with hpunch
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show toxg toxg07 with hpunch
            call pauseInterface
            hide toxg
            show toxg toxg08
            show toxg_spermdrip
            with Dissolve(1.5)
            call pauseInterface
            sb "That... was a BIG load you fired off in me!"

        "cum outside":
            hide toxg
            show toxg toxg08
            with dissolve
            y "Cumming... now!"
            play sound "audio/gltch2b.mp3"
            show toxg_spermshot
            show expression "bk3/smellerbee/fuck/spermout1.png"
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show toxg_spermshot
            show expression "bk3/smellerbee/fuck/spermout2.png"
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show toxg_spermshot
            show expression "bk3/smellerbee/fuck/spermout3.png"
            call pauseInterface

    sb "...fuck, i'm sticky!"
    y "um..."
    sb "it's great!"
    call pauseInterface

    scene black
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg" with Dissolve(1.5)

    if temp_boolean == True:
        show toxg toxg11:
            ypos -100
            linear 6.0 ypos 0
        with Dissolve(1.5)

        sb "I think I gained a pound or two from that!"

    else:
        show toxg toxg12 with Dissolve(1.5)
        sb "Good thing I took all of my clothes off this time!"

    sb "See you later, Aang."
    y "count on it."
    
    return
##### [June] Masturbate
label gallery_june_headlock_scene:
    call gallery_dCharacter_3Common

    show expression "maze/maze_ns_2.jpg":
        xzoom 2 yzoom 1.5 xpos -1000 ypos -300

    show tojl tojl04
    $ temp_Loop = True

    while temp_Loop:
        menu:
            "Locked":
                hide tojl tojl05
                show tojl tojl04
            "Freed":
                hide tojl tojl04
                show tojl tojl05
            "Continue":
                $ temp_Loop = False

    
    show tojl_tug
    ju "mmmm... yeah pump that cock..."
    call pauseInterface
    y "Hnngg..."
    ju "....."
    ju "Oh, watch out for Ajala if you keep running through these tunnels."
    y "NNgg... who's that?"
    ju "She's the head of the guards here and has biceps as thick as her thighs."
    ju "I've heard some scary stories about her"
    y "I'll keep it... in mind."
    y "By...the...way... I'm looking for... someone to run... my tavern."
    y "There's hard liquor... tips.."
    ju "Certainly sounds like something I'd enjoy."
    ju "I'll think about it."
    y "Good..."
    y "Gimme some dirty talk to speed things up here."
    ju "...look at that disgusting, smelly cock..."
    y "hey..."
    ju "just pumping recklessly right in my face..."
    ju "I bet you'd stick that in a girl without washing it and not even feel ashamed!"
    y "Go on!"
    ju "You filthy pig! You're the worst! You're a disgrace to all decency!"
    ju "Gonna blast your sperm all over my face!?"
    ju "Do it!"
    y "Wraaah!!"
    hide tojl_tug
    play sound "audio/splurt2.ogg"

    show expression "bk3/june/headlock/tug1.png":
        xpos 545 ypos 390

    show expression "bk3/june/headlock/sperm1.png":
    ju "mmm..."
    y "fuck you, bitch!"
    play sound "audio/splurt1.ogg"

    show expression "bk3/june/headlock/sperm2.png":
    hide expression "bk3/june/headlock/sperm1.png"
    ju "i... wow. well done."
    ju "i'm impressed... i've never seen such a big load before."
    ju "you... are something special."
    call pauseInterface
    y "Fuck that was nice."
    y "You have a great face for cumming on!"
    ju "....thank you, i suppose."
    ju "i hope you feel happily sated... this was certainly new for me."
    hide expression "bk3/june/headlock/tug1.png" with dissolve
    hide expression "bk3/june/headlock/sperm2.png" with Dissolve(1.5)

    return
##### [June] Play with her Tits
label gallery_june_titplay_standing:
    call gallery_dCharacter_3Common

    show expression "ebackgrounds/inside_brothel_1.jpg"
    show totz totz40
    y "ahh..."
    y "they're so soft and smackable..."
    show totz totz41 with Dissolve(1.5)
    y "I like titties.... a lot."


    $ temp_boolean = True
    $ totz_emote = 'neutral'

    while temp_boolean:
        show totz totz41

        menu:
            "massage":
                show totz totz43
                call pauseInterface
                y "Soooo soooooft."
                y "It's like digging into big sexy marshmallows."
                call pauseInterface

            "hit breasts":
                $ temp_counter = 0
                $ totz_emote = 'shock'

                while temp_counter < 6:
                    show totz totz42
                    show totz_hit
                    play sound "audio/slap.mp3"
                    pause 1.0
                    hide totz_hit
                    play sound "audio/slap.mp3"
                    show totz_hit:
                        xpos 200 xzoom -1
                    pause 1.0
                    hide totz_hit
                    $ temp_counter  += 1

                show totz totz41
                y "I don't think I've ever smacked something so tasty looking."

            "nipple search":
                show totz totz44
                call pauseInterface
                y "Am I weird for getting a thrill out of this?"
                call pauseInterface

            "done":
                $ temp_boolean = False

        $ totz_emote = 'neutral'

    show totz totz40 with Dissolve(1.5)
    ju "See you later."

    return
##### [June] Handjob
label gallery_love_june_handjob2:
    call gallery_dCharacter_3Common

    $ totj_hairlock = 'on'
    $ temp_boolean = True
    play music "audio/Unwritten Return.mp3"
    scene hospital_tilted with dissolve

    show totj totj08 with dissolve

    while temp_boolean:
        menu:
            "yes pubes":
                $ june_pubes = 'bush'

            "no pubes":
                $ june_pubes = 'shaven'

            "continue":
                $ temp_boolean = False



    ju "there."
    ju "is that a nice view?"
    call pauseInterface
    y "sure."
    ju "......"
    ju "well?"
    y "well what?"
    ju "ugh..."
    show totj totj01
    ju "are you gonna take it out or not?"
    y "in a second, but first..."
    call pauseInterface

    menu:
        "brush lock of hair aside":
            $ totj_hairlock = 'off'

        "leave it like this":
            $ totj_hairlock = 'on'

    show totj totj02

    if totj_hairlock == 'off':
        y "i want to see your face..."
        y "...when i make a mess of it."

    else:
        y "stay just like that..."
        y "so i can make a mess of you."
    ju "......"
    ju "are you..."
    ju "....just take it out, already."
    y "alright, let's get this party started then."
    "you undo your pants, and drop trou."
    y "there you go."

    play sound "audio/slap.mp3"
    show totj totj03
    with vshake
    ju "oh!"
    "your cock falls out and gives june's face a hearty slap."
    call pauseInterface
    ju "alright, come here..."
    show totj totj04
    with dissolve
    "june's soft fingers and palm curl around the base of your shaft."
    ju "but i do {i}not{/i} want you to make a mess on me, got it?"
    y "let's wait and find out."
    ju ".....ugh."
    ju "i guess i'll make you feel good."
    show totj totj05
    call pauseInterface
    y "uunghhh...."

    "she squeezes and pulls upwards, loosening her warm grip slightly on the way down..."
    "...just to squeeze hard again as she tugs up towards the head."
    "her fingers tenderly roam the length of your cock, sliding all the way up and back again..."
    "tightening and loosening her grip with careful pulsing, june watches your face relax in ecstasy."
    ju "mmm... there you go."
    call pauseInterface
    ju "this is... nice."
    y "unnh... fuck..."
    ju "you have a nice cock here."
    ju "{i}really{/i} nice."
    ju "maybe...."
    ju "....nevermind."
    y "what... ah... are you... uh... thinking... about?"
    ju "nothing. just enjoy."
    ju "...and hurry up about it."
    y "you could be more enthusiastic about this, you know."
    y "it might take me some time to-"

    show totj totj13
    y "herk."
    call pauseInterface
    ju "how's that, huh?"
    ju "still gonna take you a while?"
    y "f-fuck..."
    ju "come on, baby... cum for me..."
    ju "I can feel you warming in my hand..."
    ju "your nerves are on fire, aren't they?"
    ju "you just want to cum in my hand, don't you?"
    call pauseInterface
    ju "let me know when you're close and i'll get out of the way."
    y "yeah... ah... that's not happening."

    show totj totj04 with Dissolve(2.0)
    ju "....."
    ju "what?"
    y "you think i'm going to cum on the floor after this work?"
    y "no, no, no."
    show totj totj07 with Dissolve(2.0)
    ju "...um..."
    y "you're doing this for a big load of splooge."
    y "so... you're going to take a big load of splooge."
    ju "i didn't agree to-"
    ya "get to work! grab my cock!"
    show totj totj09 with Dissolve(2.0)
    ju "......."
    ju "I... guess that's... fair..."
    call pauseInterface
    ju "come on... come on..."
    y "hmm?"
    ju "get out of there..."
    "June seems fully absorbed in her stroking as her palm twists and fingers curl around the head..."
    "her eyes don't leave your cock as she varies her pace and length of stroke."
    ju "that's it... that's it, baby..."
    ju "let it go... let it all go..."
    call pauseInterface

    menu:
        "Keep it nice and slow":
            y "fuck! don't stop!"
            "june digs in deeper, pulling and squeezing and milking you with all she has."
            pass

        "pump it like a supersoaker!":
            y "fuck! faster!"
            show totj totj10
            "June speeds up her pace, pulling and squeezing and milking you with all she has."
    call pauseInterface
    "she vigorously works your member as your legs begin to tremble in bliss and urgency."
    ju "I can feel it..."
    ju "the pleasure's building, isn't it?"
    "her voice is soft and seductive, whispering as she works for your cum."
    ju "you're close, aren't you?"
    "you indeed feel the rising pressure surging up from your loins as you clench your muscles trying to hold it back."
    "feeling your approaching climax, june thumbs the underside of the head every time she strokes down, forcing you to the point of no return."
    ya "oh! fuck!"
    show expression "bk3/june/tug/openmouth.png"
    ju "cum in my mouth!"
    ju "I-i don't want it on me!"
    ju "cum! cum in my mouth!"
    call pauseInterface

    menu:
        "cum in her mouth":
            hide expression "bk3/june/tug/openmouth.png"
            show totj totj12 with Dissolve(2.0)
            "you grab june's pretty face and force your cock into her mouth...."
            "making sure that her lips fully engulf the head...."
            "but still close enough to the entrance that she'll taste the cum."
            ju "{size=+5}mmmgnh!! mmgh!!"
            call pauseInterface
            y "ungh!"
            play sound "audio/splurt2.ogg"
            with flash
            ju "hgmgh! ghm!"
            "the vibration of her moans and mild protests only serve to propel your spunk harder into her throat."
            y "take it, whore!"
            play sound "audio/splurt2.ogg"
            with flash
            y "ahhh...."
            show totj totj08
            "you pull your cock from her mouth, and to her credit, she keeps a tight seal around the head -- making sure not to spill a drop."
            ju "......"
            y "is your mouth full?"
            ju "...mmgn-hmm..."
            y "what was that?"
            ju "...'eth..."
            y "show me."
            show expression "bk3/june/tug/sperminmouth.png" with dissolve
            ju "aahhh....."
            "june opens her mouth, semen tumbling and dripping down her tongue and chin, sticking to her tits and stomach."
            call pauseInterface
            ju "thatisthfied?"
            y "i'm certainly satisfied right now."
            ju "good."
            ju "...i nee' oo clean thith themen off."
            ju "'an i go 'ow?"

            menu:
                "in a second":
                    y "not yet, i want a good look."
                    ju "......."
                    ju "...fucking enjoy, then."
                    call pauseInterface

                "go ahead":
                    pass

        "cum on face":
            y "you know where it's going to go, don't you?"
            ju "yes, i know where it's going to go..."
            ya "stay there!"

            show totj totj11
            ju "right in my mou-"

            y "hngh!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/tug/spermout1.png"
            with flash
            ju "hey!?!"
            y "fuck yeah!"
            play sound "audio/splurt3.ogg"
            hide expression "bk3/june/tug/spermout1.png"
            show expression "bk3/june/tug/spermout2.png"
            with flash
            ju "what the fuck..."
            ju "you just-"
            y "take this, whore!"
            play sound "audio/splurt2.ogg"
            hide expression "bk3/june/tug/spermout2.png"
            show expression "bk3/june/tug/spermout3.png"
            with flash
            call pauseInterface
            ju "you... came on my face."
            y "what did you expect?"
            ju "......."
            ju "that was... quite a healthy load."
            hide expression "bk3/june/tug/openmouth.png"
            show totj totj08
            with dissolve
            ju "i hope you're statisfied."
            y "i'm certainly satisfied right now."
            ju "good."
            ju "...i need to go clean this sperm off my face."
            ju "again."
            ju "I wish you'd stop doing that."
            ju "can i go now?"

            menu:
                "in a second":
                    y "not yet, i want a good look."
                    ju "......."
                    ju "...fucking enjoy, then."
                    call pauseInterface

                "go ahead":
                    pass

    return
##### [June] Sex
label gallery_june_lovefuck:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    scene expression "bk3/june/lovefuck/bg_bed.jpg" with dissolve

    ju "before we get started, remind me..."
    ju "how do you feel about pubic hair?"

    menu:
        "yes pubes":
            $ june_pubes = 'bush'

        "no pubes":
            $ june_pubes = 'shaven'

    ju "well that's lucky, because..."
    show totp totp00
    show totp_sex totp_stare
    with Dissolve(1.5)
    y "*cough...*"
    call pauseInterface

    y "amazing view, just as before."
    ju "i'm glad you approve."
    ju "because..."
    show totp totp01 with Dissolve(1.5)
    ju "i want you inside me."
    call pauseInterface


    y "you and me both."
    ju "you're cute, you know that?"
    ju "Let me make things clearer."
    show totp totp02 with Dissolve(1.5)
    ju "please... come have your way with me."
    call pauseInterface
    y "gulp."
    ju "I want you to pound me with that delicious cock until i scream, aang."
    ju "look at all this sweet pussy... it's yours."
    ju "you're the mighty, throbbing, powerful avatar."

    show totp totp03 with Dissolve(1.5)


    ju "come into me."
    ju "my squeezing, pulsing, begging pussy is waiting for you."
    ju "come and claim it, baby."
    ju "plant your fucking flag in me and claim your territory."
    ju "mark me yours."
    call pauseInterface
    y "......"
    y "beg."
    ju "please, avat... aang."
    ju "don't you want to slip inside?"
    ju "please... let me feel you on my pussy..."
    ju "just... just rub it on my lips a little first... ease me into it..."
    y "...you asked for it."
    play sound "audio/gltch2b.mp3"
    show totp_sex totp_rub with dissolve
    ju "unnnghh...."
    ju "fuuuuck yesss...."
    call pauseInterface
    "you slip against june's juicy, soft pussy."
    "the plush lips are so wet and engulfing you risk cumming just from the slickness."
    ju "yes, avatar... aang... yes baby..."
    ju "i feel you... i feel the avatar's cock... pressing against my cunt..."

    if june_pubes == 'bush':
        hide totp_sex totp_rub
        show expression "bk3/june/lovefuck/rubp_1.png"
        with dissolve
        ju "mmmm.... watcha doing there?"
        call pauseInterface
        play sound "audio/gltch2b.mp3"
        hide expression "bk3/june/lovefuck/rubp_1.png"
        show expression "bk3/june/lovefuck/fuckp_1.png"
        with dissolve
        ju "*aahhh....*"
        call pauseInterface

    if june_pubes == 'shaven':
        hide totp_sex totp_rub
        show expression "bk3/june/lovefuck/rub_1.png"
        with dissolve
        ju "mmmm.... watcha doing there?"
        call pauseInterface
        play sound "audio/gltch2b.mp3"
        hide expression "bk3/june/lovefuck/rub_1.png"
        show expression "bk3/june/lovefuck/fuck_1.png"
        with dissolve
        ju "*aahhh....*"
        call pauseInterface

    ju "that's it, avatar..."
    ju "what are you waiting for?"
    ju "you want it, don't you?"
    ju "you want me?"
    ju "take me!"
    ju "don't tease me..."
    ju "slide it in... slide it deep, deep inside me..."
    ju "or maybe i should say..."
    show head_eyeonplayer with dissolve
    ju "don't."
    ju "don't you dare."
    ju "you can rub my pussy, but you're not allowed inside me."
    ju "don't you dare put it-"
    play sound "audio/gltch2b.mp3"
    show totp_sex totp_fuck
    show head_shock_2
    hide head_eyeonplayer
    with pflash
    ju "ohhhhh....."
    ju "fuucckkk yesss...."
    call pauseInterface
    ju "fill... fill my tight, juicy cocksleeve..."
    hide head_shock_2
    show head_shock_3
    with dissolve
    ju "yess... oh hell yeah..."
    ju "have your way with me... please... own me, baby... that's it..."
    ju "stuff that pussy, baby..."
    ju "oh spirits..."
    call pauseInterface
    ju "are you... having... ah... fun with my tight... cock-slurping pussy?"
    ju "because fuck..."
    ju "you're much... much thicker than i... i thought you'd be..."
    ju "i've never... ah... had... such... ah... it's so... fucking... filling me... ah..."
    hide head_shock_3
    with dissolve
    hide totp_sex
    ju "what..."
    call pauseInterface
    y "you want it?"
    ju "i want it."
    y "you want it?"
    show head_eyeonplayer
    ju "{size=+6}i want it!"
    ya "you want it?!"
    ju "{size=+6}i want-"
    show totp totp05

    if june_pubes == 'shaven':
        show totp_fuck2_1 with vpunch

    else:
        show totp_fuck2_1p with vpunch

    hide expression "bk3/june/lovefuck/fuck_1.png"
    hide expression "bk3/june/lovefuck/fuckp_1.png"
    ju "{size=+10}oh fat fucking spirits of cock!!!"
    ju "shit!"
    ju "shit! shit! fuck!"
    ju "fuck that's deep!"
    call pauseInterface
    ju "avatar!"
    ju "avatar, please! stop! wait! ah!"
    call pauseInterface

    if june_pubes == 'shaven':
        hide totp_fuck2_1
        show totp_fuck2_2

    else:
        hide totp_fuck2_1p
        show totp_fuck2_2p
    ju "unghh... ungh.... fuuuck....!!"
    ju "don't speed uuuuppp!!!"
    call pauseInterface
    y "\"avatar\" isn't my name, bitch!"
    y "say my name!"
    ju "a-aang!"

    menu:
        "fast":
            $ love_june_fast = True

            if june_pubes == 'shaven':
                hide totp_fuck2_2
                show totp_fuck2_3_1

            else:
                hide totp_fuck2_2p
                show totp_fuck2_3_1p

        "slow":
            $ love_june_fast = False

            if june_pubes == 'shaven':
                hide totp_fuck2_2
                show totp_fuck2_3

            else:
                hide totp_fuck2_2p
                show totp_fuck2_3p

    ju "please, aang! g-gentle! please! ah!"
    ju "you're too bi-big for... ah... this... ah!"
    call pauseInterface
    y "Gonna cum!!"

    if love_june_fast:
        if june_pubes == 'shaven':
            hide totp_fuck2_3
            hide totp_fuck2_3_1
            show totp_fuck2_4_1

        else:
            hide totp_fuck2_3p
            hide totp_fuck2_3_1p
            show totp_fuck2_4_1p

    if not love_june_fast:
        if june_pubes == 'shaven':
            hide totp_fuck2_3
            hide totp_fuck2_3_1
            show totp_fuck2_4

        else:
            hide totp_fuck2_3p
            hide totp_fuck2_3_1p
            show totp_fuck2_4p
    ju "yesss...."
    ju "unngh! ungh! ah! ohhngh! fuck!"
    call pauseInterface
    ju "fuck it's good! fuck it's so good!"
    ju "give...! oh...! let it... ah... out! fuck! let it out!"
    ju "Please! fuck! fucking fuck! please! fuck!"

    menu:
        "inside":
            $ totp_preg = True
            play sound "audio/splurt2.ogg"

            if june_pubes == 'shaven':
                hide totp_fuck2
                hide totp_fuck2_4_1
                hide totp_fuck2_4
                show expression "bk3/june/lovefuck/fuck_6.png"

            else:
                hide totp_fuckp2
                hide totp_fuck2_4_1p
                hide totp_fuck2_4p
                show expression "bk3/june/lovefuck/fuckp_6.png"
            with flash
            ju "unngh!!"
            ju "fuck... fuck..."
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/lovefuck/head_shock.png" with vpunch
            ju "oh spirits!"
            ju "there's so fucking mu-"
            play sound "audio/splurt3.ogg"
            hide expression "bk3/june/lovefuck/head_shock.png"
            with flash

            if june_pubes == 'shaven':
                hide expression "bk3/june/lovefuck/fuck_6.png"

            else:
                hide expression "bk3/june/lovefuck/fuckp_6.png"

            show expression "bk3/june/lovefuck/cum_outside.png"
            show totp totp06
            ju "unnngh...."
            call pauseInterface

        "outside":
            play sound "audio/splurt2.ogg"

            if june_pubes == 'shaven':
                hide totp_fuck2
                hide totp_fuck2_4_1
                hide totp_fuck2_4

            else:
                hide totp_fuckp2
                hide totp_fuck2_4_1p
                hide totp_fuck2_4p
            show expression "bk3/june/lovefuck/sperm_out_1.png"
            with flash
            call pauseInterface
            ju "oh... oh fuck..."
            ju "my... my puss... pussy... ah..."
            play sound "audio/splurt3.ogg"
            show expression "bk3/june/lovefuck/sperm_out_2.png"
            with flash
            call pauseInterface
            ju "so... there's so... fucking mu-"
            play sound "audio/splurt2.ogg"
            show expression "bk3/june/lovefuck/sperm_out_3.png"
            with flash
            ju "unnghh...."
            call pauseInterface

    show totp totp07 with Dissolve(1.5)
    ju "so... good..."
    ju "and sore..."
    ju "not... not bad, avatar...."
    ju "...fuck."
    ju "need... sleep."
    y "i'll let you rest then."
    ju "thank... you..."
    call pauseInterface
    
    return
##### [Suki] Anal Fingering
label gallery_suki_headlock_removal:
    call gallery_dCharacter_3Common

    show expression "bk3/suki/headlock/ani_torso.png"
    show tosh tosh03
    call pauseInterface
    y "Okay... so how should I go about it?"
    y "Lick it first to loosen you up?"
    suki "What?! NO!"
    suki "I couldn't ever face you again!"
    y "Well, in that case, just try to relax."
    y "I don't have any lubricant with me, and I'm guessing you don't want me to cum on your ass to help glide it in?"
    suki "....are you seriously asking me whether you should cum on my ass?"
    y "hey, i'm just trying to be a friend."
    suki "Just... just go in dry."
    show tosh tosh04 with dissolve
    y "alright, but you asked for it."
    y "I'll do my best, but this won't be a fun experience {size=9}....for you....{/size}"
    y "Just imagine this is a prostate exam."
    suki "Isn't that a guy thing?"
    y "{i}worldstar!!!"
    show tosh tosh100
    suki "ah!"
    call pauseInterface
    "suki squeezes your finger tightly; it's clear that her rear has never been penetrated before."
    y "you gotta relax a little, suki... it's like i'm wearing a ring, here."
    suki "Hnngh... you're going in so deep..."
    y "Just trying to get that key."
    call pauseInterface
    suki "What's taking so long?"
    y "I'm trying my best, but you're somehow both too tight and too slippery."
    y "it would certainly help if you'd stop squirming."
    suki "Sorry, it's just that... having a friend digging in my ass is... awkward."
    y "speaking of awkward... if you see me with a raging boner, that's totally a normal physical reaction to this situation."
    call pauseInterface
    y "Wait, I think I felt something just now!"
    show tosh tosh04

    y "damn girl... what else can that ass do?"
    suki "let's find that out later."
    y "....i like you."
    call pauseInterface

    return
##### [Suki] Masturbate
label gallery_love_suki_mast:
    call gallery_dCharacter_3Common

    scene expression "bk3/suki/pussyrub/background.jpg" with Dissolve(1)
    play music "audio/Unwritten Return.mp3"
    show tosr tosr01 with vshake
    suki "Pffff."
    suki "it's good to get off of my feet for a moment!"
    call pauseInterface
    suki "It feels like I've done nothing but walk today!"
    y "Yeah, but it beats being locked up in a woodblock, right?"

    show tosr tosr02
    suki "You got that right!"
    call pauseInterface

    suki "speaking of..."
    suki "i'm having a really stressful day..."
    y "....."
    y "Here? Now?"
    show tosr tosr10
    suki "You don't want to?"

    show tosr tosr04 with hpunch
    suki "ooh!"

    hide tosr
    show tosr tosr05
    show tosr_pussyrub1

    suki "Hmmm...."
    call pauseInterface
    y "i can feel a pair of tasty little lips down here."
    suki "mmmm...."
    y "I wonder what happens if i rub them?"
    suki "aahh..."
    suki "I've been looking forward to this so much."
    y "oh?"
    suki "I... i've been thinking about this..."
    suki "a lot."
    y "I can tell, I already feel you moistening right through your pants."
    suki "w...wait..."
    suki "I can't... walk around the rest of the night with soggy pants."
    suki "J-just a moment."
    hide tosr_pussyrub1 with dissolve
    "With a fluid motion Suki slips down her pants."

    show tosr tosr06
    suki "There, that should solve that problem."
    call pauseInterface
    y "Someone could come over here any moment."
    y "we're... really visible."
    suki "Unless that's a problem for you, I really don't care who sees us."
    y "That's all I needed to hear."

    menu:
        "stick your fingers in her mouth first":
            y "why don't you wet my fingers? "
            y "I doubt it's needed for lubrication by now, but I just like doing it."
            show tosr tosr07
            show expression "bk3/suki/pussyrub/hand_mouth.png"
            "Suki greedily sucks on your fingers."
            call pauseInterface
            y "Everytime i feel like my dick can't get any harder, reality proves me a liar."
            y "Time for some pussy play."
            hide expression "bk3/suki/pussyrub/hand_mouth.png"

        "go straight for the pussy":
            pass


    show tosr tosr11 with Dissolve(1.5)
    show tosr tosr12 with Dissolve(1.5)
    suki "*mmmmm....*"
    call pauseInterface
    suki "You're... you're really... really..."
    suki "{i}good{/i} at this."
    call pauseInterface
    suki "h-how.... ohh..."
    y "I've had some practice."
    show tosr_pussyrub1

    show tosr tosr07
    "You let your fingers glide over her wet pussy..."
    "...easily slipping your fingers deep within."
    "Making sure you stimulate her clit, you keep going up and down, in and out, at a steady and unrelenting pace."
    suki "I would never have... have believed something like this could ever feel so damn good."
    suki "I've done it for myself, but it... ahhh... just isn't the same."
    suki "Not even close."
    suki "You can help me search for that \"key\" whenever you want, Aang."
    hide tosr_pussyrub1
    show expression "bk3/suki/pussyrub/hand_drip.png"
    with Dissolve(1.5)
    y "whoa, I believe you."
    y "It's like an honest-to-god waterfall down there!"

    menu:
        "make her taste it":
            hide expression "bk3/suki/pussyrub/hand_drip.png"
            show expression "bk3/suki/pussyrub/hand_mouth.png"
            suki "*mmmmm...*"
            suki "i 'aste 'ood."
            y "i'll have to try it myself later."
            suki "*mmmm....*"
            hide expression "bk3/suki/pussyrub/hand_mouth.png"

        "Make her cum!":
            hide expression "bk3/suki/pussyrub/hand_drip.png"

    y "Enough with all this foreplay, I'm going to make you cum so hard you'll be launching yourself."
    show tosr tosr07
    show tosr_pussyrub2
    suki "Ohh... oh... fuck..."
    "You start rubbing Suki's clit with renewed vigor, using every bit of stamina left in your fingers."
    call pauseInterface
    hide tosr_pussyrub2
    show tosr tosr13
    suki "Aaah! AAhhh!!"

    show expression "bk3/suki/pussyrub/pjuice_1.png" with hpunch
    suki "Ah!"
    show expression "bk3/suki/pussyrub/pjuice_2.png" with hpunch
    suki "AAahh!!"
    show expression "bk3/suki/pussyrub/pjuice_3.png" with hpunch
    suki "AAAAAAAAAAAahh!!" with hpunch

    show tosr tosr11 with dissolve
    call pauseInterface

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.0)

    show tosr tosr07

    suki "OOoooh spirits..."
    suki "I... I came so hard..."
    show tosr tosr07
    suki "Ah... I just... I just need a moment.."
    y "Certainly."
    y "Just make sure you don't slip when you stand up."
    y "The floor is kind of wet."
    y "you think you can still work after this?"
    suki "f...fuck the customers..."
    suki "i'm taking a \"me\" day."
    y "...fair enough."
    y "I'll see you later."
    suki "anhh...."
    call pauseInterface
    
    return
##### [Suki] Fuck (Cowgirl)
label gallery_suki_lovefuck:
    call gallery_dCharacter_3Common

    $ totn_head = 'face'
    $ totn_fuck = 'rub'
    play music "audio/Unwritten Return.mp3"
    scene expression "bk3/june/blowjob/inside_tavern_2.jpg"
    show totn totn03 with Dissolve(1.5)

    "suki strips and crawls on you, pressing her tits firmly against your chest."
    suki "want me to tease you a bit?"
    suki "or do you want me to be your cock-sleeve right from the start?"

    menu:
        "tease me":
            y "tease me first."
            y "i want to feel you rub against me."
            y "give me an appetizer, girl."
            suki "yes sir...."
            $ totn_fuck = 'rub'
            show totn totn100
            $ totn_head = 'face'
            suki "*mmm...*"
            call pauseInterface
            suki "this feels really nice."
            suki "Having your stiff rod slide between my buttcheeks..."
            suki "Can you feel the softness of my pussy lips?"
            y "It's super soft.."
            suki "your precum's getting me going..."
            suki "I'm making your dick all wet from my pussy juice."
            suki "How long do you think you could stand me teasing you like this without cumming?"
            suki "Two minutes?"
            suki "Perhaps five?"
            y "we could... ah... we could test it..."
            suki "we could..."
            $ totn_head = 'back'
            suki "But that's not what you want...."
            call pauseInterface
            suki "Playing like this is nice but what you really want..."
            suki "...is to ram my little pussy with your cock, isn't it?"
            suki "*mmh...*"
            suki "imagine how your dick, wet with my love juice, slips inside all the way at the first go."
            suki "Going far deeper than your fingers could..."
            suki "you think we can get it all the way in with one thrust?"
            $ totn_head = 'face'
            suki "*Mmmmm...*"
            call pauseInterface
            suki "I can feel it throbbing... eager with anticipation..."
            suki "Enough foreplay."
            suki "Time to put it in."

        "sleeve":
            pass


    show totn totn03
    suki "aiming..."
    call pauseInterface
    show totn totn02 with Dissolve(1.5)
    suki "connecting..."
    suki "{size=-5}oh, fuck...."
    call pauseInterface
    $ totn_fuck = 'penetrate'
    show totn totn03 with dissolve
    suki "nice and secure..."
    show totn totn03
    suki "Oh... {i}fuck{/i} yes."
    call pauseInterface
    suki "this is more like it..."
    suki "You have great finger technique aang, but..."
    suki "...but what I really need right now is a big fat cock greedily kissing my womb."


    show totn totn100
    suki "hunngh...!!!"
    call pauseInterface
    y "damn suki..."
    suki "Ah! You're stretching me so wide!"
    suki "I'm going to be feeling this in the morning!"
    y "you have such a delicious fucking ass..."
    y "that pussy is sucking me in..."
    call pauseInterface
    suki "Can you take all of me, Aang?"
    suki "Can you take me slamming down on you?"


    menu:
        "Make that ass bounce girl":
            y "give it to me!"
            suki "That's what I wanted to hear!"
            $ totn_head = 'back'
            show totn totn101
            suki "*MMmmmmmmhhh...*"
            call pauseInterface

        "Let's take things easy... for now":
            y "nice and easy... this feels amazing..."
            $ totn_head = 'face'
            suki "Aaah... you're no fun."
            suki "but I'm still going to milk you dry."
            $ totn_head = 'back'
            call pauseInterface


    suki "I'm going to leave your sack so empty you'll need a week to recover!"
    call pauseInterface
    $ totn_head = 'face'
    y "If there's one thing I have absolute confidence in, it's my ability to make the white stuff."
    suki "Let's see you prove that."
    suki "How about it Aang?"
    suki "Are you ready to fill me all up?"
    call pauseInterface

    y "I think I'll...."

    menu:
        "cum on your ass":
            y "Sit still and spread those asscheeks, Suki!"
            show totn totn09 with Dissolve(1.5)
            suki "Do it!"
            call pauseInterface
            suki "Spray your seed all over my ass, Aang!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/suki/lovefuck/spermout_1.png"
            call pauseInterface
            play sound "audio/splurt3.ogg"
            show expression "bk3/suki/lovefuck/spermout_2.png"
            call pauseInterface
            play sound "audio/splurt2.ogg"
            show expression "bk3/suki/lovefuck/spermout_3.png"
            call pauseInterface
            show totn totn10 with Dissolve(1.5)
            call pauseInterface
            suki "That's more than I was expecting!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/suki/lovefuck/spermout_4.png"
            suki "Ah! Aang!"
            suki "Are you trying to drown me?"
            suki "it...it's everywhere!"
            suki "You could literally fill up jars!"
            suki "I gotta take a shower quick or I'll be stuck to the floor."
            suki "Let's do this again soon."
            call pauseInterface

        "cum inside your cunt":
            y "I'm gonna fill up your cum-sucking cunt!"
            suki "yes! talk dirty! I love it!"
            y "slurp my cum out with your juicy cunt, suki!"
            suki "yes!!!"
            $ totn_impreg = True
            play sound "audio/splurt2.ogg"
            show totn totn03
            with flash
            y "hngh!"
            suki "ffuuuuucck!!!!"
            play sound "audio/splurt3.ogg"
            with flash
            call pauseInterface
            show totn totn08 with Dissolve(1.5)
            suki "I could fill a bucket with what's dripping out of me!"
            call pauseInterface
            $ totn_head = 'back'
            suki "*mmmm...*"
            play sound "audio/kiss.mp3"
            with pflash
            "suki fiercely kisses your mouth with hers, sucking your bottom lip as she pulls back."
            suki "*mwa!*"
            suki "Thanks for the extra thick filling, Aang."
            call pauseInterface

    return
##### [Suki] Bar Blowjob
label gallery_suki_barblow:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    show expression "bk3/suki/barblow/floor.jpg"
    show expression "bk3/suki/barblow/floor_body.png"
    show expression "bk3/suki/barblow/floor_torso.png":
        xpos 360 ypos 10
    show expression "bk3/suki/barblow/floor_head.png":
        xpos 360 ypos 25
    show expression "bk3/suki/barblow/desk.png":
        xpos 0 ypos 0

    y "oh!" with hpunch
    y "easy, girl..."

    suki "...hehehe..."


    show expression "bk3/suki/barblow/floor_torso.png":
        xpos 360 ypos 10
        linear 4.0 ypos 60
    show expression "bk3/suki/barblow/floor_head.png":
        xpos 360 ypos 25
        linear 4.0 ypos 90
    show expression "bk3/suki/barblow/desk.png":
        xpos 0 ypos 0
        linear 2.0 alpha 1.0
        linear 2.0 alpha 0.8

    call pauseInterface

    y "you haven't forgotten that we're surrounded by people, right?"

    suki "well, you're the bartender."
    suki "take their orders."

    "Suki pulls down your pants while a customer approaches the bar."
    show expression "bk3/suki/barblow/flash.png"
    show expression "bk3/suki/barblow/floor_dick.png"
    pause 0.2
    hide expression "bk3/suki/barblow/flash.png" with dissolve

    suki "don't mess up any orders, aang..."
    call pauseInterface

    scene black
    hide text
    show expression "ebackgrounds/bar.jpg"
    show toxc toxc01
    show expression "bk3/suki/barblow/top.png":
        alpha 0.8
    with Dissolve(1.5)
    call pauseInterface
    "you feel warm breath panting against your cock as the customer stops at the bar."

    suki "Hmmmm... it looks delicious!!!"
    y "{size=-5}shut up, suki..."
    show toxc toxc02

    suki "I'm going to have some fun with this."
    bk3c "Sorry, did you say something?"
    y "...no."
    y "What can I get you?"

    bk3c "tequila."
    y "you got it."
    show toxc toxc03
    show expression "bk3/suki/barblow/arm_holddick.png"
    with Dissolve(1.5)
    "Suki takes your dick in her mouth and start making circular motions with her tongue."

    y "hnnnnh..."
    call pauseInterface

    bk3c "come on man, i don't have all night."
    y "here you go."

    show toxc_servedrink
    play sound "audio/thud.mp3"
    cus "That's... not what I ordered."
    y "Ah sorry, this one is on the house."
    bk3c "Thanks!"
    hide toxc_servedrink
    show toxc toxc04
    hide expression "bk3/suki/barblow/arm_holddick.png"
    with Dissolve(1.5)
    y "ungh! shit!"
    bk3c "hey, don't beat yourself up man, it happens."
    y "go sit down!"
    bk3c "...i like when you take charge."
    "the customer walks back to their table."
    y "Suki, that feels reeeally nice, but..."
    y "I don't think I'll be able to get anyone's order right with my dick in your mouth."
    y "Especially when you do that thing with your tongue."
    show toxc toxc08 with Dissolve(1.5)
    "With a small plopping sound Suki pulls her lips from your cock."

    suki "suck it up."
    y "really?"
    suki "well, if i'm sucking it up, you should too."
    suki "it's not like i get their drinks right anyway."
    y "......."
    y "I'd be a lot more upset with that work ethic if you didn't say that right after taking my cock out of your mouth."
    suki "It's the magic of a good blowjob!"
    bk3c "hey, that-"
    y "ah!"
    y "i mean... hello-"
    show toxc toxc05 with dissolve
    y "ah!"
    suki "mmmmghhh...."
    bk3c "....."
    y "....hello, sir."
    bk3c "...right."
    bk3c "well, that dirty harry actually tasted pretty damn good, Can I have another one?"
    y "You finished it already?!"
    bk3c "I was thirsty!"
    y "i-"
    show toxc toxc06 with dissolve
    suki "*gahgh*"
    y "-oof."
    bk3c "what?"
    y "i was saying..."
    show toxc toxc106
    suki "*sluuurp!*"
    call pauseInterface
    y "oh sweet baby roku."
    bk3c "....what?"
    y "i was... i was gonna say..."
    y "that i like that in my customers..."
    bk3c "like what?"
    y "you... being thirsty... fuck..."
    bk3c "did... you just call me a thirsty fuck?"
    y "no... the... the fuck was unrelated..."
    bk3c "just get me another tequila."
    y "sure."

    play sound "audio/thud.mp3"
    show toxc_servedrink

    y "Here you go!"
    bk3c "Thanks!"
    hide toxc_servedrink

    "they walk back to their table."
    y "this is... getting stressful."
    show toxc toxc08 with dissolve
    suki "yeah? you sure you're not having fun?"
    y "...maybe a little."
    suki "hey, so..."
    show toxc toxc04 with dissolve
    y "ah..."
    suki "*mmmmmm....*"
    suki "*slluuurp*"


    show toxc toxc05 with Dissolve(1.5)
    show toxc toxc100
    call pauseInterface
    suki "*schluurrrpp...* *schlurp...* *schurp...* *sccchlluuuurp...*"
    y "uuuuhhhhh...."
    call pauseInterface
    "the wet warmth radiating from her mouth engulfs and soaks you as she sucks and gulps at your cock."
    call pauseInterface
    suki "i'm gonna make you blow so hard."
    show toxc toxc04 with dissolve
    suki "come on, let's get this face fucked."
    show toxc toxc06 with Dissolve(1.5)
    show toxc toxc107
    call pauseInterface
    suki "*suck!* *slurp!*"
    y "damn!"
    y "this... is... nuts..."
    suki "*gasp!*"
    bk3c "hey, it's me again, can i-"
    y "damn you!"
    suki "*schluurrrpp* *schluurrrpp*"
    bk3c "What's that sound I keep hearing?"
    y "Pro... pro...aaahh...bably a cat."
    show toxc toxc06 with Dissolve(1.5)
    suki "Meww!! Meeewww!!"
    y "No! Bad kitty! Bad Kitty!!"
    show toxc toxc107
    suki "*slllurp!*"
    bk3c "Another Dirty Harry please."
    y "one tequila, coming up."
    play sound "audio/thud.mp3"
    show toxc_servedrink
    y "here."
    bk3c "cheers!"
    hide toxc_servedrink
    "he wanders off."
    show toxc toxc08 with Dissolve(1)
    suki "mmm..."
    y "you're not... gonna stop now, are you?"
    suki "relax, i'm not going anywhere..."
    suki "...although pretty soon {i}you'll{/i} be {i}coming{/i}."
    show toxc toxc03 with dissolve
    suki "get it?"
    show toxc toxc04 with dissolve
    y "that's a terrible joke."
    suki "who's telling jokes?"
    show toxc toxc101
    y "hnnngg!" with hpunch
    call pauseInterface
    suki "*gulp!* *sllllllllurp!*"
    y "damn girl!"
    suki "*slurp* *slurp* gagh* *mmgh*"
    call pauseInterface
    y "that's..."
    y "oh, what the hell!"
    y "this stupid customer keeps coming back!"
    show toxc toxc100 with Dissolve(1)
    suki "don't... *slurp...* mess... *gulp...* up..."
    suki "i... *ahhh...* need... *mmmmm...* these... *shhlurp...* customers..."
    call pauseInterface
    y "you're not making this easy."
    suki "*mmmmm....*"
    suki "focus on the job, baby..."
    y "i am."
    suki "i meant that job."
    y "oh."
    call pauseInterface
    suki "i'll just be here... taking my time..."
    suki "...enjoying slobbering on your cock... "
    suki "...while you focus..."
    show toxc toxc103
    y "fuck!"
    call pauseInterface
    bk3c "hey! i-"
    play sound "audio/thud.mp3"
    show toxc_servedrink
    y "here!"
    y "go away!"
    y "something important is happening!"
    bk3c "....."
    bk3c "okay!"
    hide toxc_servedrink
    call pauseInterface
    y "that guy...."
    y "how is he still conscious?"
    show toxc toxc08_1 with Dissolve(1)
    suki "I watered down all the bottles."
    show toxc toxc100 with Dissolve(1)
    call pauseInterface
    y "...i'd give you a promotion if you weren't my only employee."
    y "also, why are you slowing down?"
    show toxc toxc08 with Dissolve(1)
    suki "i can feel you swelling... you're getting close aren't you?"
    y "i... well... yeah..."
    suki "i'm not going to let you cum yet."
    y "...say again?"
    suki "i'm not finished enjoying feeling you throbbing in my mouth."
    show toxc toxc06 with Dissolve(1)
    suki "squeezing you with my throat muscles... pressing my tongue into you..."
    y "Unnnghh...."
    show toxc toxc100 with Dissolve(1)
    suki "*sluuurp*"
    suki "you're not gonna cum from these slurps, are you?"
    suki "*slurp!* *slurp!* *slurp!*"
    suki "just from these slurps here?"
    y "uuuhhhh...."
    y "I'm gonna cu-"
    y "oh, that stupid... that customer is coming up here again!"
    suki "take his order when you drench my throat."
    suki "let it all go, down my throat, while you work."
    show toxc toxc104
    suki "*gag!*"
    call pauseInterface
    y "fuck!"
    bk3c "what?"
    y "no-nothing..."
    y "what do... ah... what... fuck..."
    bk3c "dude, your face is really red."
    bk3c "you're shaking!"
    suki "*slurp!!* *sluuurp!!* *gulp!!*"
    y "ah! fuck!"
    bk3c "shit!"
    bk3c "dude, are you gonna die?"
    y "what... god {i}damn{/i} it! what do you want!? fuck!"
    bk3c "i mean... a guess another shot of tequila."
    bk3c "but it's not my favorite."
    bk3c "i guess i was just thinking that..."
    "the customer starts rambling..."
    "you feel your balls begin to churn, drenched as they are with suki's spit."
    call pauseInterface
    y "(oh, shit, suki!)"
    show toxc toxc105
    "feeling you tense up, suki goes all out, fucking your cock with her face and wet, pouty lips."
    suki "*slurp!!* *slurp!!* *slurp!!*"
    call pauseInterface


    menu:
        "unload on her face!":
            show toxc toxc08_1 with Dissolve(1)
            suki "cover me!"
            bk3c "where's my drink?"
            show expression "bk3/suki/barblow/glass_hand.png" with hpunch
            y "fuck... ing... ah... here!"

            "leaning on the counter, you take one step back just before you blow."

            hide toxc
            show toxc toxc00
            hide expression "bk3/suki/barblow/top.png"
            show expression "bk3/suki/barblow/top.png":
                alpha 0.8
            show toxc_playbody
            with dissolve

            suki "that's it... come on...."

            show expression "bk3/suki/barblow/blink.png":
                xpos 531 ypos 187
            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/spermout_1.png"
            with flash
            suki "....mmmm!"
            call pauseInterface
            y "fuck!"

            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/spermout_2.png"
            with flash
            suki "yes, sexy...."
            call pauseInterface
            bk3c "...what's happening now?"
            suki "hmmm... yes... that's it..."
            call pauseInterface
            bk3c "hey! let go of my drink!"
            suki "that... was a lot of-"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/spermout_3.png"
            hide expression "bk3/suki/barblow/blink.png"
            with flash
            call pauseInterface
            suki "....whoa."
            suki "this... is a lot of semen."
            call pauseInterface
            suki "i don't... even know how i'm gonna get out of here..."
            hide expression "bk3/suki/barblow/glass_hand.png" with dissolve
            "you let go of the drink."

            bk3c "thanks man."
            bk3c "but i think you should get checked for epilepsy."

            call pauseInterface
            y "fuck... that... guy..."
            show expression "bk3/suki/barblow/arm_bitefinger.png"
            suki "that was a huge load..."
            y "you earned it."
            suki "i did, didn't i?"
            suki "Maybe I could use it to make a special girls only {i}cock{/i}tail."
            y "what did i say about your jokes?"
            suki "like i said before... who's joking?"
            call pauseInterface

        "dump it down her throat!":
            bk3c "where's my drink?"
            y "fuck... ing... ah... here!"
            show expression "bk3/suki/barblow/glass_hand.png" with hpunch
            bk3c "that wasn't so hard, right?"
            hide expression "bk3/suki/barblow/glass_hand.png"
            hide toxc
            show toxc toxc09
            show expression "bk3/suki/barblow/floor_torso.png":
                xpos 360 ypos 80

            show expression "bk3/suki/barblow/floor_headsuck.png":
                xpos 360 ypos 90

            show expression "bk3/suki/barblow/desk.png":
                xpos 0 ypos 0 alpha 0.8
            with Dissolve(1.5)

            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/floor_headsuck.png":
                linear 0.3 ypos 30
                linear 1.0 ypos 90
            show expression "bk3/suki/barblow/floor_torso.png":
                xpos 360 ypos 80
                linear 0.3 ypos 60
                linear 1.0 ypos 80

            call pauseInterface
            suki "mmmm!!"
            bk3c "what do i owe you?"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/suki/barblow/floor_headsuck.png":
                linear 0.3 ypos 30
                linear 1.0 ypos 90
            show expression "bk3/suki/barblow/floor_torso.png":
                xpos 360 ypos 80
                linear 0.3 ypos 60
                linear 1.0 ypos 80
            y "I think... hgnh... 25 coins should cover it."
            call pauseInterface
            play sound "audio/gulp2.mp3"
            suki "*gulp!!* *gulp!!* *gulp!!*"
            hide expression "bk3/suki/barblow/floor_torso.png"
            hide expression "bk3/suki/barblow/floor_headsuck.png"
            hide expression "bk3/suki/barblow/desk.png"
            show expression "bk3/suki/barblow/glass_hand.png"
            show toxc toxc07a
            show expression "bk3/suki/barblow/hands_pinch.png":
                xpos 10
            with Dissolve(1.5)
            bk3c "that seems fair."
            "Suki grabs your ass with a vice-like grip and shoves you farther down her throat as you feel the third wave approching."
            call pauseInterface
            bk3c "hey! let go of my drink!"
            play sound "audio/gltch2b.mp3"
            show toxc toxc07a with vshake
            call pauseInterface
            suki "......"
            suki ".............."
            play sound "audio/gulp2.mp3"
            suki "{size=+10}*gulp!!!*" with hpunch

            hide toxc
            hide expression "bk3/suki/barblow/top.png"
            show toxc toxc02
            show expression "bk3/suki/barblow/top.png":
                alpha 0.8

            hide expression "bk3/suki/barblow/hands_pinch.png"

            show expression "bk3/suki/barblow/spermin_1.png"
            with Dissolve(1.5)
            suki "gah!"
            suki "....wow."
            suki "that... was a lot of semen."
            call pauseInterface
            suki "i don't... even know how i'm gonna get out of here..."
            hide expression "bk3/suki/barblow/glass_hand.png" with dissolve
            "you let go of the drink."

            bk3c "thanks man."
            bk3c "but i think you should get checked for epilepsy."

            call pauseInterface
            y "fuck... that... guy..."
            suki "that was a huge load..."
            y "you earned it."
            suki "i did, didn't i?"
            suki "Maybe I could use it to make a special girls only {i}cock{/i}tail."
            y "what did i say about your jokes?"
            show toxc toxc02_3
            suki "like i said before... who's joking?"
            call pauseInterface

    hide expression "bk3/suki/barblow/arm_bitefinger.png"

    suki "come by whenever you need a little work release, and i'll keep my tips!"
    suki "it's a win-win."
    suki "i'm gonna try to sneak to the back..."
    suki "i didn't think there'd be this much cum..."
    y "ahhh... that was fun."
    call pauseInterface

    return

##### [Jo Dee] Titjob
label gallery_joodee_boobjob:
    call gallery_dCharacter_3Common

    scene basingse_home_4
    play music "audio/Unwritten Return.mp3"
    show toob toob01 with vshake

    "...and rip off her bra."
    jd "ayee!"
    call pauseInterface
    y "Isn't that better?"
    jd "no!"
    y "stop complaining!"
    y "if you didn't want this to happen, you shouldn't have tried to kill me in my sleep!"
    jd "I-i'm sorry!"
    ya "{i}sir{/i}."
    jd "i-i'm sorry, sir!"
    y "now, are you going to do your job or not?"
    jd "i'm not sure this is part of my job..."
    y "Sure it is!"
    y "But you know... just as a side thought..."
    y "I think you could easily get a new job if Long Feng fires you."
    jd "What?! No!!"
    jd "I have a mortgage!"
    jd "Being fired is a death sentence in this job market!"
    "you pull out your cock while she's complaining."
    y "Oh, wow... my dick feels a bit cold."
    jd "Maybe if you put your clothes back on..."

    show toob toob02 with Dissolve(1.5)
    "you straddle her chest, slipping between her plump tits."
    "her plush mounds almost completely engulf your cock."
    y "OOoooh.... this is nice and warm!"
    y "So comfy and soft...."
    y "Makes me want to slide up and down."
    show toob toob03
    y "Like this! See?"
    call pauseInterface
    jd "Th-thank you for the demonstration, sir..."
    jd "but... if you could just stop..."
    y "I can almost reach your mouth with the tip of my dick."
    y "I think I should go a bit faster."
    jd "That... that's really not necessary..."
    jd "In fact, I'd prefer it if you wouldn't."
    call pauseInterface
    y "Here I go!"

    show toob toob04
    jd "Ah!"
    call pauseInterface
    y "Oh yeah, this is the stuff."
    jd "This is -ah!-"
    jd "slightly -ah!-"
    jd "uncomfortable -ah!-"
    ya "good!"
    ya "you tried to murder me, joo dee!"
    ya "you think your... ungh... swollen... hng... doughy tits... can make up for trying to fucking kill me?"
    ya "use them to milk out my cum and maybe i won't be so angry any more!"
    ya "you don't want me to be angry any more, do you?"
    jd "i... i don't know!"
    call pauseInterface
    y "well, lucky for you, i'm a kind dom."
    y "so, here, hold your boobs tight and it won't be as uncomfortable."
    show toob toob05
    call pauseInterface
    y "much better right?"
    jd "Y...yeah, but..."
    y "Fuck yeah! You've got some great fucking tits."
    ya "especially for a criminal."
    jd "I'm... i'm not a criminal!"
    ya "what!?"
    jd "i-i mean... i'm a criminal! i'm sorry!"
    jd "please-!"
    call pauseInterface
    y "I've been dying to fuck these...."
    y "Hold tight. I'm going to put some weight behind this!"
    jd "Please don't!"
    ya "I'm going to bang your tits off!"
    jd "Nonononono!"


    show toob toob100
    jd "Aaah!!"
    call pauseInterface
    y "Fuck! this is great stuff!"
    jd "my breasts aren't made for this!"
    y "yes they fucking are!"
    y "We're going to have a lot of fun together, JD!"
    jd "ungh... hmph... ah... unh..."
    ya "beg for my forgiveness!"
    ya "you want this to end?"
    jd "ungh... ah... yes...!"
    ya "then beg!"
    ya "convince me you're sorry!"
    ya "or it won't end here!"
    jd "i-i'm so sorry!"
    jd "take... take out all your anger on me!"
    jd "on my big, fluid tits!"
    jd "forgive me, avatar! forgive me!"
    jd "fuck my big sinful tits and forgive me!"

    ya "oh, i'm feeling forgiving now!"
    ya "I'll go ahead and end this!"
    jd "Yes! Please end this!"

    menu:
        "piss in her mouth!":
            hide toob
            show toob toob101
            with Dissolve(1.5)
            y "nnghh...."
            y "open your mouth, girl!"
            jd "what are-"
            ya "take this, you bitch!"
            show toob_piss:
                xpos 353 ypos 291
            y "ahhhh...."
            jd "*Gurgle gurgle*"
            hide toob_piss
            show expression "bk3/joodee/boobjob/piss4.png"
            with Dissolve(2.0)
            "you fill up joo dee's mouth with piss until it overflows and runs down her cheeks into her hair."
            y "Aaah. All done."
            show toob toob102 with Dissolve(2.0)
            call pauseInterface
            y "I'll let myself out."
            y "you think about what you did."
            y "i'll see you soon, sugar tits."
            jd "gurg..."
            call pauseInterface

        "Cum on her face and boobs!!":
            hide toob
            show toob toob101
            with Dissolve(1.5)
            y "open your mouth, girl!"
            jd "what are-"
            ya "take this, you bitch!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/joodee/boobjob/sperm1.png"

            y "hngh!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/joodee/boobjob/sperm2.png"
            jd "unghhh... you're..."
            y "fuck!"
            play sound "audio/splurt1.ogg"
            show expression "bk3/joodee/boobjob/sperm3.png"
            call pauseInterface
            y "Aaaah... that was sublime."
            show toob toob102 with Dissolve(2.0)
            y "I'll let myself out."
            y "you think about what you did."
            y "i'll see you soon, sugar tits."

            jd "s...sorry..."
            jd "gurg..."
            call pauseInterface

        "Cum on her twat":
            hide toob
            show toob toob06
            "In one fluid motion you flip JooDee's legs up."
            y "let's get rid of those panties."
            jd "nonono! don't!"

            show toob toob07
            "you pull her panties off and spread her legs with no real resistance."
            y "(she must really have to follow orders...)"
            jd "Wha...."
            show toob toob08

            y "just hold still girl."
            jd "what are-"
            ya "take this, you bitch!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/joodee/boobjob/spermtwat1.png"

            jd "unghhh... you're..."
            y "fuck!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/joodee/boobjob/spermtwat2.png"
            jd "no...."
            y "hngh!"

            play sound "audio/splurt1.ogg"
            show expression "bk3/joodee/boobjob/spermtwat3.png"
            call pauseInterface
            y "ahh... that was satisfying."
            y "I'll let myself out."
            y "you think about what you did."
            y "i'll see you soon, sugar tits."
            jd "hurg...."
            jd "I'm... covered in..."
            jd "uhhn...."
            call pauseInterface

    return
##### [Jo Dee] Fuck
label gallery_jd_full_nelson:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    scene hypno_room2
    show toji toji14 with dissolve
    $ totl_penetrate = 'vag'

    jd "will you... wait here for a moment, sir?"
    y "okay..."
    hide toji with dissolve
    y "what are you doing over there?"
    jd "removing my clothes, sir."
    y "neat."
    y "oh, leave on the hat!"
    jd "...of course, sir."

    show totl totl08:
        xpos -10 ypos 20 rotate 20
        linear 2.0 xpos -60 ypos -150 rotate 0
    y "Up you go!"
    hide totl
    show totl totl08
    with Dissolve(1.5)
    jd "oh!"
    y "Hnng... looking good so far!"
    y "Let's do some easy rubbing to prepare you down there."

    show totl totl102
    call pauseInterface
    jd "Ah!"

    show totl totl11
    y "I think you're ready for some parting of the lips."
    show totl totl07 with Dissolve(1.5)
    y "Ready to have me inside you?"
    jd "Yes!"

    show totl totl01
    show totl_faceshock
    with vpunch
    jd "Hnnnggg!"
    y "You okay?"
    jd "*ah...!*"
    jd "...yeeaasssh..."
    hide totl_faceshock with dissolve
    jd "I mean... I'm... I'm super okay!"
    y "I'm going to move now."

    show totl totl100
    call pauseInterface

    y "You're certain this isn't too much for you, right?"
    jd "Ah! Ahbsoluteleeeh!!"
    y "I'm gonna slam it in! Ready?"
    jd "uhhm..."
    y "Here it comes!"
    show totl totl101
    jd "Hiii!!"
    call pauseInterface
    jd "yes!"
    jd "you... ahnn..."
    jd "you must get so... ah... frustrated and pent... ah... pent up..."
    jd "i hate... *mmmngh...* i hate to see that..."
    jd "use my pussy whenever you feel stressed... sir!"
    y "....."
    jd "let out... ohhh... all your frustrations on me!"
    jd "let me fuck them out of you!"
    jd "slam... ahhn... in and out of cunt until you can... unh... finally relax..."

    show totl totl03
    show totl totl07 with Dissolve(1.5)
    y "Gotta take a little breather."
    y "Oh man... pussy is the best thing ever."
    y "Since we're doing this, would you like to switch it up and do some anal too?"
    y "Maybe give your pussy a little rest?"
    show expression "bk3/joodee/nelson/face_uncertain.png"
    jd "What... what would you prefer?"

    menu:
        "vaginal":
            $ totl_penetrate = 'vag'
            y "your juicy pussy."
            show totl totl01
            jd "Thank the spirits..."
            hide expression "bk3/joodee/nelson/face_uncertain.png"
            y "What?"
            jd "Nothing, I'm just happy my pussy is wonderful enough for you to revisit it!"

        "anal":
            y "your juicy ass."
            $ totl_penetrate = 'ass'
            jd "....."
            y "You... don't want to?"
            jd "Nono... anal is... fine, wonderful."
            jd "Let's do that."
            hide expression "bk3/joodee/nelson/face_uncertain.png"

            show totl totl12
            with vpunch

    if totl_penetrate == 'ass':
        jd "Ahh!!!"
        call pauseInterface
        y "You okay, Joodee?"
        jd "I'm fine. I'm fine..."
        jd "Ju-just go ahead."
        show totl totl101
        y "Oh yeahh!"
        y "Visiting misses brown in browntown!"
        y "And here I was thinking your twat was tight!"
        jd "Are you enjoying my little backway?"
        y "Am I?!"

    else:
        show totl totl101
        y "Aaaaand it's back in your tight cunt."
        y "Fuck! I love it in here... it's hot, wet, tight and sucking me in harder than a vacuum!"
        call pauseInterface
        jd "Aaah!"

    jd "sir...!"
    y "yes?"
    jd "think... ah... of me as your at-home sex doll."
    y "um..."
    jd "i'll be discreet, of course!"
    jd "you saved my life, and so i'm yours... whatever you... hnnn... need..."
    jd "sex dolls can't reveal secrets, after all!"
    y "......."
    call pauseInterface
    y "well..."
    y "toph might get grumpy if she finds out one of the services you provide me is endless fucking."
    jd "think.. ah... of it as... unnh... masturbating..."
    jd "just... using my body to do it..."
    jd "instead of cum... cumming... into... *mmm*... tissues or a toilet..."
    jd "...i'm your designated... ah... cum receptacle."
    jd "just when... whenever you need it..."
    y "....i can't argue with that logic!"
    y "fuck, but I'm reaching my limit here."
    y "Outside or inside!?"
    jd "Where... ah!... do you want it... unh!?"


    menu:
        "inside":
            hide totl
            show totl totl04
            y "Fillin you up... right... {size=+6}NOW!"
            play sound "audio/gltch2b.mp3"
            with flash
            pause 1
            play sound "audio/gltch2b.mp3"
            with flash
            pause 1
            play sound "audio/gltch2b.mp3"
            with flash
            pause 1

            show totl totl06

            if totl_penetrate == 'vag':
                show totl_vagspermdrip with Dissolve(1.5)
            else:
                show totl_asspermdrip with Dissolve(1.5)

        "outside":
            hide totl
            show totl totl03
            show totl totl07 with Dissolve(1.5)
            jd "yes, sir!"
            jd "give me your semen!"

            show expression "bk3/joodee/nelson/sperm_onbody_1.png" with vpunch
            play sound "audio/gltch2b.mp3"
            call pauseInterface
            show expression "bk3/joodee/nelson/sperm_onbody_2.png" with vpunch
            play sound "audio/gltch2b.mp3"
            call pauseInterface
            show expression "bk3/joodee/nelson/sperm_onbody_3.png" with vpunch
            play sound "audio/gltch2b.mp3"

    call pauseInterface
    y "That was more than worth it!"
    jd "thank you, sir..."
    jd "let me know... any time..."
    y "oh, i will, joo dee."
    y "i will."
    call pauseInterface
    
    return
##### [Mean Girls] Maze Lick
label gallery_meangirls_maze_licking:
    call gallery_dCharacter_3Common

    show tomg tomg01 with dissolve
    call pauseInterface
    y "Ready to lick yourself some cock girls?"

    "girls" "....yes...."

    y "Good."
    show tomg tomg02 with dissolve
    call pauseInterface

    y "How many times have we done this before?"
    y "I think lots of times, right?"
    y "Time to show me how much you've improved."

    show tomg tomg03 with Dissolve(1.5)
    call pauseInterface

    y "Same smelly cock as last time girls."
    y "No need to hesitate."
    y "Come on, dig in."

    show tomg tomg100
    call pauseInterface

    "*schlurp, schlurp, schlurp*"
    y "Mmmmm, yeah... keep licking the tip, red."
    y "Short little laps."
    y "Yeah, that's it."
    y "Focus on the edge, white and pink."
    y "It might take the three of you working in tandem to get a halfway decent erection..."
    y "...but I can see you're trying your best."
    "The girls keep licking you until you finally start feeling the urge to unload upon them."

    y "Hnng... about to cum..."
    y "turn your faces towards me!"
    show tomg tomg04
    show tomg tomg01 with Dissolve(1.5)
    call pauseInterface
    y "Red gets it first!"
    play sound "audio/splurt2.ogg"
    show expression "bk3/meangirls/maze/sperm1.png"
    y "Pink is up next!"
    play sound "audio/splurt1.ogg"
    show expression "bk3/meangirls/maze/sperm2.png"
    y "And white can have the leftovers."
    play sound "audio/splurt2.ogg"
    show expression "bk3/meangirls/maze/sperm3.png"
    call pauseInterface
    y "AAaaaah, that was nice."
    hide expression "bk3/meangirls/maze/sperm1.png"
    hide expression "bk3/meangirls/maze/sperm2.png"
    hide expression "bk3/meangirls/maze/sperm3.png"
    hide tomg

    return
##### [Mean Girls] Reward
label gallery_meangirls_reward:
    call gallery_dCharacter_3Common

    show bk3_bg_fountain
    "You look around but see nothing of interest, when all of a sudden someone taps you on the shoulder."

    show totu totu03 with Dissolve(1.5)
    "red" "Hey it's us!"
    "red" "thanks again for your help in those horrible tunnels."
    "red" "Let... let's go to that alley there."


    hide bk3_bg_fountain
    show expression "bk3/smellerbee/bj/bg_alley_fountain.jpg"
    hide totu
    show totu totu03

    "red" "Okay, here we are..."
    "The three girls fumble with their clothes and within a few minutes..."

    stop music
    play music "audio/Unwritten Return.mp3"

    show totu totu04 with Dissolve(1.5)
    y "Nice."

    if not mg_reward:
        y "say... aren't you worried about doing this here?"
        "red" "We don't really have anywhere else to do it, and we're guessing you're strong enough to chase anyone away."
        y "True..."
    y "Okay, you just stand there."
    y "I want to make this whole experience slightly better for me."

    $ totu_redgirl = 'neutral'
    $ totu_pinkgirl = 'neutral'
    $ totu_whitegirl = 'neutral'

    hide totu
    show expression "bk3/meangirls/reward/bg_sky.jpg"
    show totu totu01
    with Dissolve(1.5)

    y "I like this... I like this a lot."
    "red" "This is really embarrassing... being stared at from this angle..."
    y "Do you know what would even be more embarrasssing?"
    "red" "...yeah..."
    "red" "Do... do you want me to...?"
    y "absolutely."
    "Hesitantly, she lets her hands slide over her thighs and carefully spreads her lips."
    $ totu_redgirl = 'spread'
    "red" "I... I can't believe I'm doing this..."
    y "Me neither!"
    y "I assumed you were just going to jump up and down and jiggle your titties!"
    y "But this is {i}much{/i} better!"
    y "Hey, pink and yellow."
    y "You're not going to let your friend go through this experience by herself, right?"
    $ totu_pinkgirl = 'spread'
    $ totu_whitegirl = 'spread'

    y "That's nice..."
    y "that's very, very nice."
    y "Why don't you stand around me in a cicle."


    $ totu_redgirl = 'neutral'
    $ totu_pinkgirl = 'neutral'
    $ totu_whitegirl = 'neutral'
    show totu totu02 with Dissolve(1.5)


    y "excellent."
    y "I'd like it a lot if you touch yourself."
    y "I bet you know exactly how it's done, red."
    y "Why don't you show the others how?"
    "red" "I... okay..."
    $ totu_redgirl = 'masturbate'

    "red" "*Hnnnnn...*"
    y "Damn that's hot... "
    y "I'm going to touch myself too."
    "You whip out your erect cock and the girls squeal with surprise as you start stroking it."
    y "Okay, you've seen how it's done, now follow red's lead."
    $ totu_pinkgirl = 'masturbate'
    pause 0.3
    $ totu_whitegirl = 'masturbate'
    "The two other girls join the first one."
    "They're a bit awkward at first but soon enough any difference between them is gone."
    call pauseInterface
    y "Life is good."
    y "Very good."
    "the girls let their hands go up and down, having their fingers follow along the curves of their bodies."
    "Their glistening pussies become wetter with each moment."
    "red" "This... hnnng... this is such a crazy turn-on!"
    "red" "Standing here, stroking ourselves while being watched..."

    y "hold on for a second."

    $ totu_redgirl = 'neutral'
    $ totu_pinkgirl = 'neutral'
    $ totu_whitegirl = 'neutral'


    y "I love seeing you girls enjoy yourselves, but I won't be able to last long as things are."
    y "So before I shoot my load..."

    menu:
        "Piss on me":
            $ totu_redface = 'shock'
            "red" "Piss on you?!?" with hpunch
            y "Yep, that's what I said."
            "red" "Are... are you sure?"
            y "Just empty your bladder all over me."
            $ totu_redface = 'neutral'
            "red" "...okay."
            "red" "Here it comes."
            $ totu_redgirl = 'piss'
            "The salty yellow fluid starts with short uncertain bursts, but within a blink turns into a steady stream."
            y "Red has taken the lead."
            y "What are you waiting for, pink and white?"
            $ totu_whitegirl = 'piss'
            $ totu_pinkgirl = 'piss'
            "Very soon three steady streams are aimed at your face."
            y "*gurgle*"
            call pauseInterface
            "red" "Are we doing it right?"
            y "Just the way I imagined it!"
            $ totu_redgirl = 'spread'
            "Red's stream is the first to slow down to a trickle and stop."
            "The other two girls last a few moments longer but are empty soon enough too."
            $ totu_pinkgirl = 'spread'
            $ totu_whitegirl = 'spread'
            y "Well done!"
            $ totu_redgirl = 'neutral'
            $ totu_pinkgirl = 'neutral'
            $ totu_whitegirl = 'neutral'

        "Spread yourself and walk around me":
            y "I want to have a good look at your lady parts from all possible angles."
            "red" "I'm doing the craziest things today!"
            $ totu_redgirl = 'spread'
            $ totu_whitegirl = 'spread'
            $ totu_pinkgirl = 'spread'

            show totu totu02:
                xanchor 0.5 yanchor 0.5 xpos 500 ypos 360
                linear 40.0 rotate 360
            call pauseInterface
            y "Fuck yeah."
            y "This is the shit!"
            hide totu
            show totu totu02
            show totu totu01 with Dissolve(1.5)

        "Just keep going as you were":
            $ totu_redgirl = 'masturbate'
            pause 0.5
            $ totu_whitegirl = 'masturbate'
            $ totu_pinkgirl = 'masturbate'
            y "That's it."
            y "Rub those pretty little twats!"


    y "Okay!"
    y "Line up, spread those pussies, and get ready for some cum."


    show totu totu01 with Dissolve(1.5)

    $ totu_redgirl = 'spread'
    $ totu_pinkgirl = 'spread'
    $ totu_whitegirl = 'spread'

    y "Hnnnnng!"

    show expression "bk3/meangirls/reward/white.png" with Dissolve(0.5)
    play sound "audio/gltch2b.mp3"
    $ totu_redgirl = 'sperm'
    hide expression "bk3/meangirls/reward/white.png" with Dissolve(1.0)

    pause 0.5

    show expression "bk3/meangirls/reward/white.png" with Dissolve(0.5)
    play sound "audio/gltch2b.mp3"
    $ totu_whitegirl = 'sperm'
    hide expression "bk3/meangirls/reward/white.png" with Dissolve(1.0)

    pause 0.5

    show expression "bk3/meangirls/reward/white.png" with Dissolve(0.5)
    play sound "audio/gltch2b.mp3"
    $ totu_pinkgirl = 'sperm'
    hide expression "bk3/meangirls/reward/white.png" with Dissolve(1.0)

    pause 0.5
    y "That's it for today, girls!"

    return
##### [Jin] Maze Fuck
label gallery_jin_had_mazesex:
    call gallery_dCharacter_3Common

    show expression "bk3/jin/shackles/bg.jpg"
    show tojc tojc00

    menu:
        "Want me to use my dick?":
            jin "Yes! Give me dick!!"

        "Or a dildo?":
            jin "I don't care what it is, just put it in me!"
            jump jin_had_dildo_sex

    $ b3love_jin_mazesex = 1
    $ tojc_face = 'lookdown'
    show tojc tojc100
    jin "Yes! that's it!"
    $ tojc_face = 'lusty'
    jin "Hmmmm, finally!!"
    call pauseInterface
    jin "You have no idea how long I've been wanting this!!"
    jin "Don't hold back! Slam that fucker in me!"
    show tojc tojc101
    jin "Ahh!"
    call pauseInterface
    y "I'm going to cum!!"
    jin "CUM INSIDE ME!!"
    y "...can do!"
    hide tojc
    show tojc tojc08
    show tojc tojc09 with Dissolve(1.5)
    play sound "audio/gltch2b.mp3"
    pause 0.6
    play sound "audio/gltch2b.mp3"

    show expression "bk3/jin/shackles/big_sperm_inside.png":
        alpha 0.0
        linear 2.0 alpha 1.0
    jin "fuuck!!"
    jin "you're drowning my womb in sperm!"
    call pauseInterface
    hide expression "bk3/jin/shackles/big_sperm_inside.png"
    show tojc tojc10
    with Dissolve(1.5)
    jin "Aaaaah! That was great."
    jin "thank you!"
    call pauseInterface
    $ tojc_face = 'neutral'

    return
label gallery_jin_had_dildo_sex:
    call gallery_dCharacter_3Common

    show tojc tojc11
    $ b3love_jin_mazesex = 2
    $ tojc_face = 'lookdown'
    jin "Aaaaah! That's great."
    $ tojc_face = 'lusty'
    show tojc tojc12
    jin "Aawh, i don't know what you're shoving in me but it feels fantastic!"
    show tojc tojc13

    jin "....nhhh!"
    show tojc tojc14 with hpunch
    show tojc tojc15 with Dissolve(1.5)
    jin "Ooooh... fuck, that was great."
    $ tojc_face = 'neutral'

    return
##### [Jin] Blowjob
label gallery_jin_loveblowjob2:
    call gallery_dCharacter_3Common

    scene dressingroom
    play music "audio/Unwritten Return.mp3"
    show toto toto01 with Dissolve(1)
    y "....nice."
    call pauseInterface
    jin "Pffff...."
    jin "i'm just getting comfortable."
    jin "...you've already seen a lot more of mine than just these tits."
    y "i did."
    y "and trust me... i'm thinking about it right now."
    show toto toto01a
    jin "oh, are you...?"
    y "i'm, uh... straining against my pants, here."
    jin "*mmmm...*"
    show toto toto01 with dissolve
    jin "hey, seriously..."
    jin "I'm super grateful for all the things you've been doing for me."

    show toto toto01b
    jin "seriously?!?" with hpunch
    y "well, yeah."
    y "how could i turn that down?"

    jin "awesome!"
    jin "give it here!"

    show toto toto01
    jin "Thank the spirits..."
    jin "i really really want to taste your cock."
    jin "is that... okay?"
    y "i... well... yes."
    show toto toto01a with dissolve
    jin "pull it out."
    y "....are you teasing me?"
    y "this seems very... um... easy."

    show toto toto01 with dissolve
    jin "were... were you joking?"
    jin "sorry."
    jin "i've been feeling super horny since the tunnels."
    jin "I don't know what that ajala chick did, but i'm just so damn horny all the time."
    jin "i was hoping you could help me..."
    jin "besides, i..."
    jin "...i just want to thank you and show you i appreciate you and..."
    jin "i just really want you to fuck my face."
    jin "please?"
    show toto toto01a with dissolve
    y "...i would be thrilled to provide."
    jin "Great!"
    jin "I've been using a dildo but it's just no substitute for the real thing."
    show toto toto01 with dissolve
    jin "come on! whip it out!"
    jin "Show me what you got!"

    show toto toto02
    jin "oh!"

    jin "It's looking really hard."
    jin "I'll start licking the top first."
    jin "That alright with you?"
    y "I have no objections."
    show toto toto03 with Dissolve(1.5)
    "With short little laps she starts licking the top of your penis."
    call pauseInterface
    y "That's... very nice."
    jin "If you think that's nice, watch this."

    show toto toto05
    y "You..."
    y "*hnnng...*"
    y "you {i}have{/i} practiced a lot!"
    call pauseInterface
    jin "*mmgh...*"
    jin "*slurp* *guuulp* *slllurp*"
    call pauseInterface
    y "May I suggest a combo move of licking and sucking?"

    show toto toto04
    jin "shhure!"
    call pauseInterface
    jin "*smack* *slurp* *shlap*"
    y "fuuck..."
    call pauseInterface
    y "That's really effective."

    menu:
        "Please keep doing what you're doing":
            pass

        "Could you go back to just licking?":
            show toto toto03

        "How about only sucking again?":
            show toto toto05

    call pauseInterface
    jin "*Mmmmngh....*"
    call pauseInterface

    show toto toto02 with dissolve
    y "....."
    y "Why did you stop?"
    jin "I just wanted to take another look at him."
    jin "Would mind me getting a little rougher?"
    y "As long as it doesn't come off, go right ahead."
    jin "great!"
    show toto toto06
    call pauseInterface
    jin "*gag* *gulp* *sluurp*"
    y "i... damn, jin..."
    jin "*gaghh* *shhllllup*"
    y "I... I'm gonna cum...."
    jin "*slluurp* *guulp* shmack* *shlurp*"

    menu:
        "Cum in her mouth":
            show toto toto09 with Dissolve(1.5)
            hide toto
            play sound "audio/splurt2.ogg"
            show toto toto09
            with flash
            pause 0.1
            play sound "audio/splurt1.ogg"
            with flash
            "jin sucks hard at the tip, pulling out your sperm as it rockets into her throat."
            "she keeps it steady in her mouth as wave after wave of semen spurt into her mouth."
            show toto toto09
            show expression "bk3/jin/love_bj/spermin_1.png"

        "Cum on her face":
            show toto toto07 with Dissolve(1.5)
            hide toto
            show toto toto07
            jin "come on, then."
            y "ngh!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/love_bj/spermout_1.png"
            with flash
            call pauseInterface
            play sound "audio/splurt1.ogg"
            show expression "bk3/jin/love_bj/spermout_2.png"
            with flash
            call pauseInterface
            play sound "audio/splurt3.ogg"
            show expression "bk3/jin/love_bj/spermout_3.png"
            with flash
            call pauseInterface


    show toto toto08
    with dissolve
    jin "Aahh, now that's something a dildo could never give me!"
    jin "come and visit me whenever you feel you need some relief."
    jin "and... thanks, aang."
    jin "you're the best."
    jin "this is... all i've ever wanted."
    jin "and i'm just so happy."
    jin "thanks."
    y "you... i..."
    y "...i need a nap."

    return
##### [Jin] Fuck & Anal
label gallery_love_jin_sex_anal:
    call gallery_dCharacter_3Common

    scene expression "bk3/tylee/footjob/bg_bedroom.jpg":
        xzoom -1
    show totg totg12
    with dissolve
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    "jin settles on the bed, leaning back and presenting her breasts in full display."
    "a look of promise and begging sexuality radiates from her face."
    call pauseInterface


    jin "so..."
    jin "are you going to fuck me or what?"

    jin "take off your pants."
    "you drop your clothes and stand at attention."
    show totg totg13 with Dissolve(1.5)
    jin "oh, mmmm..."
    jin "you know how to make a girl feel special."
    call pauseInterface

    show totg totg09 with Dissolve(1.5)
    jin "I want it hard."
    jin "and deep."
    jin "i want you to fucking wreck me."
    jin "take me from behind."
    call pauseInterface
    jin "can you do that?"
    y "i think i can manage."
    show totg totg10 with Dissolve(1.5)
    jin "come on then."
    call pauseInterface
    jin "what are you waiting for?"


    show totg totg06 with Dissolve(1.5)
    y "you talk too much."
    y "do you need it?"
    jin "....yes, okay?!"
    jin "I need it bad!"
    jin "I'm in... i'm in fucking {i}heat{/i} here!"
    jin "fucking give it to my pussy!"
    jin "give-"
    $ totg_sex = 'pussy'
    show totg totg07a
    jin "{size=+5}ah!" with hpunch
    call pauseInterface
    show totg totg07 with dissolve
    jin "{i}fuuuuck{/i} yes!"
    y "you convinced me."

    y "You're practically drooling down here, so don't mind me foregoing any pleasantries."
    jin "are you joking?"
    jin "fuck me!"
    y "Here I go!"
    show totg totg102
    jin "uuuhhh.... fuck..."
    call pauseInterface
    jin "it's... ahh... bigger than i remember..."
    jin "mmmmmmhh...."
    jin "you know exactly at what angle to go in."
    jin "Soooo gooooood..."
    jin "you stiff dick is fucking stuffing me!"
    jin "Mmmmh..."
    y "That's good, because I'm going to give you plenty of this."
    call pauseInterface

    show totg totg06 with Dissolve(1.5)
    jin "Awh, don't stop yet!"
    jin "come on!"
    y "Don't worry. I'll put it in again."
    y "But before I do...."
    jin "I want it! i want it!"
    jin "fuck me, aang! fuck me!"
    jin "come on! what are you waiting for?"

    menu:
        y "(where should i fuck her...)"

        "tight pussy!":
            $ totg_sex = 'pussy'
            show totg totg07 with Dissolve(1.5)
            jin "unngh..."
            y "I thought about fucking your ass..."
            y "but decided to concentrate on this tight cunt of yours."
            jin "mmmm... good call..."
            jin "you can stuff my butt later."

        "little asshole":
            $ totg_sex = 'anal'
            show totg totg07a with Dissolve(1.5)
            jin "Ah!!"
            jin "fuck!!!"
            call pauseInterface
            show totg totg07 with Dissolve(1.5)
            jin "....fuck yes!"
            jin "Pound my tight little asshole!"
            jin "Plunge it in deep!"
            show totg totg102
            jin "ungh... uh... fuck... unhh... shit... ungh..."
            jin "Just don't... ahnh... stick it back in my pussy after putting it in my ass."
            y "this ass is all i need right now."
            y "Your pussy is safe... for now."


    jin "You... you can get rough if you want."
    y "Things can get pretty wild when I get rough..."
    jin "Good, I like that."
    y "In that case.... one rough ride coming up!"
    show totg totg05a with hpunch
    show totg totg101
    jin "{size=+6}AAAaaahh!"
    call pauseInterface
    jin "fuck! yes! more!"
    y "more?"
    jin "more!!"
    show totg totg103

    jin "{size=+6}YESSS!! SMASSHH ITT!!!"
    call pauseInterface

    if totg_sex == 'anal':
        jin "{size=+6}SMASH MY ASS TILL IT BREAKS!!! DOO ITTTT!!"

    else:
        jin "{size=+6}BREAK MY CUNT!! SLAM YOUR HARD COCK IN THERE!!"
    call pauseInterface
    y "take this, slut!"
    show totg totg104
    jin "{size=+6}AAAaaahh!"
    jin "{size=+6}fuckfuckfuckfuckfuck!!!"
    call pauseInterface
    y "HNNNGGG!!!"

    menu:
        "unload inside":
            if totg_sex == 'anal':
                y "i'm gonna fill your slut asshole with cum!"
                jin "yes! yes, i'm a slut! i'm your slut!"
                jin "use me! use my ass! give it all to me!"

            else:
                y "i'm gonna fill your slut pussy with cum!"
                jin "yes! yes, i'm a slut! i'm your slut!"
                jin "use me! use my pussy! give it all to me!"
            hide totg
            show totg totg05

            play sound "audio/gltch2b.mp3"
            show totg totg05a with hpunch
            jin "ungh!"
            play sound "audio/gltch2b.mp3"
            with hpunch
            pause 0.7
            show totg totg05 with dissolve
            play sound "audio/gltch2b.mp3"
            with hpunch
            jin "damn..."
            pause 0.7

            if totg_sex == 'anal':
                show totg totg08
                show expression "bk3/jin/analove/sperm_insideass.png"
                with Dissolve(1.5)

            else:
                show totg totg08
                show expression "bk3/jin/analove/sperm_insidepuss.png"
                with Dissolve(1.5)

            jin "there's so much..."

            if totg_sex == 'anal':
                jin "It's flowing out of my ass, even though it's facing up!"

            else:
                jin "it's dripping out of my pussy, even though it's facing up!"

        "outside":
            hide totg
            show totg totg11
            with Dissolve(1.5)
            y "Take this!"
            jin "what are you-"
            show expression "bk3/jin/analove/spermout1.png"
            play sound "audio/gltch2b.mp3"
            show totg totg11a
            with flash
            jin "oh!"
            call pauseInterface

            show expression "bk3/jin/analove/spermout2.png"
            play sound "audio/gltch2b.mp3"
            show totg totg11
            with flash
            jin "ahhh... yeah... cover me..."
            call pauseInterface

            show expression "bk3/jin/analove/spermout3.png"
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface
            jin "mmmmmgh... you came so much!"

    jin "And it's so thick!"
    y "Good girls deserve good sperm."
    y "and lots of it."
    call pauseInterface
    scene black with dissolve

    scene expression "bk3/tylee/footjob/bg_bedroom.jpg":
        xzoom -1
    show tojn tojn22
    with dissolve
    jin "well that was... satisfying."
    jin "i hope you had fun...."
    jin "I know i did."
    jin "i'll just get dressed..."
    hide tojn with dissolve
    show tojn tojn20 with dissolve

    if totg_sex == 'anal':
        jin "my little butt is still pulsing."
    else:
        jin "my little pussy is still pulsing."

    y "nice."
    jin "heehee... i agree."
    jin "i'll see you later, handsome."
    jin "thanks for the date."
    
    return
##### [Ty Lee] Footjob
label gallery_love_ty_footjob:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    show expression "bk3/tylee/footjob/bg_bedroom.jpg"
    show totf_upper up2
    show totf totf10 with dissolve
    ty "hehe!"
    ty "ready?"
    ty "want me to make you cum with my toes?"
    show totf_upper up3
    "you step behind her."
    ty "oh, you're... eager..."
    ty "that's fun..."
    ty "you gonna pull out that big... *giggle*... penis?"

    show totf totf09 with dissolve
    ty "oh, my..."
    ty "you're going to make a lot of cum, aren't you?"
    y "I'm planning on it."
    show totf totf10 with dissolve
    "you step back for a moment."
    y "lift up your legs."
    show totf totf03 with dissolve
    ty "sure!"
    show totf totf04 with dissolve
    ty "can i... start?"
    y "go for it."
    y "use those small agile acrobat feet..."

    show totf totf05 with dissolve
    ty "*giggle*"
    y "what?"
    ty "it's just funny how hot it is."

    show totf totf06
    y "hnngh..."
    call pauseInterface
    ty "*giggle*"
    ty "boys are funny!"
    ty "you like me talented little toes on your thick cock?"
    ty "*giggle!*"
    ty "i'm milking you like a cow!"
    y "yeah... you... are..."
    ty "want it faster?"
    y "....."
    y "yes...."
    ty "okay!"
    show totf totf07
    y "oh, fuuuckk..."
    ty "*giggle!*"
    call pauseInterface
    ty "oh, no!"
    ty "is it working too well?"
    ty "*giggle!*"
    y "you know exactly... fuck... how well it's working..."
    call pauseInterface
    ty "you're getting really stiff..."
    ty "you gonna cum, daddy?"

    menu:
        "cum on ass":
            show totf totf03 with dissolve
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/tylee/footjob/sperm1.png"
            call pauseInterface
            play sound "audio/splurt1.ogg"
            show expression "bk3/tylee/footjob/sperm2.png"
            call pauseInterface
            play sound "audio/splurt3.ogg"
            show expression "bk3/tylee/footjob/sperm3.png"
            call pauseInterface

        "cum on pussy":
            hide totf_upper
            show totf totf08
            with Dissolve(1.5)
            y "oh shit, that's a hot position."
            ty "yeah?"
            ty "does it make you wanna cum?"
            ty "on me?"
            ty "do you want to cum on me?"
            ty "you totally can!"
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/tylee/footjob/sperm4.png"
            call pauseInterface
            play sound "audio/splurt1.ogg"
            show expression "bk3/tylee/footjob/sperm5.png"
            call pauseInterface
            play sound "audio/splurt3.ogg"
            show expression "bk3/tylee/footjob/sperm6.png"
            call pauseInterface
            ty "wow...."
            ty "You can shoot it really far!"
            call pauseInterface

            menu:
                "Get her to eat it":
                    y "you know... sperm is a great non-fattening nutrient."
                    ty "it is?"
                    ty "....."
                    show expression "bk3/tylee/footjob/handonpussy.png" with dissolve
                    "She grabs a scoop of your sperm."
                    ty "hmmm...."
                    hide expression "bk3/tylee/footjob/handonpussy.png"
                    show expression "bk3/tylee/footjob/handinmouth.png"
                    with dissolve
                    ty "*mmmgh...*"
                    ty "I'm not crazy about the taste, but as long as it's healthy...."
                    hide expression "bk3/tylee/footjob/handinmouth.png"
                    show totf_scoopsperm
                    ty "it'd be a waste to just wash it off."
                    ty "*mmmgh...*"
                    ty "gotta stay healthy!"
                    ty "*Burp!*"
                    ty "....there's a lot of it though."

                "Leave":
                    pass

    y "Thanks Ty Lee!"
    ty "any time!"

    return
##### [Ty Lee] Blowjob
label gallery_ty_cabbage_bj:
    call gallery_dCharacter_3Common

    play music "audio/Unwritten Return.mp3"
    $ temp_boolean = False

    scene expression "bk3/tylee/footjob/bg_bedroom.jpg"
    with dissolve

    show toth toth19 with dissolve
    ty "Ready whenever you are!"

    show toth toth12 with dissolve
    ty "Hello mister dick!"
    ty "How do you do?"
    y "uh... dicks can't talk..."
    show toth toth20 with dissolve
    ty "I know that! "
    ty "It's just funny to pretend!"
    y "In that case, he likes to be kissed!"

    show toth toth13 with Dissolve(1.5)
    ty "I Have to know him a lot better before I can do that!"
    y "In that case... we should start with a firm handshake."
    y "a firm... long... handshake."

    show toth toth14
    ty "Teehee! It's a pleasure to meet you!"
    y "Likewise! *you say with a low-pitched voice.*"
    ty "Let's shake on it!"
    y "Yes, please!"

    show toth toth15
    ty "How's life going for you, mr. dick?"
    y "Right now life's hard."
    y "veeery hard."
    ty "I'm sorry to hear that!"
    y "Nonono... for dicks, a hard life isn't that bad."
    y "If taken care of the right way, it makes us cry white tears of joy!"
    ty "That's strange! How can I help?!"
    y "A small kiss on the tip helps."
    ty "I guess one little kiss is fine."

    show toth toth01 with Dissolve(.2)
    ty "*smooch!*"
    show toth toth13 with Dissolve(.2)
    y "Maybe a slightly deeper kiss?"

    show toth toth10 with Dissolve(.2)
    ty "*Smoooooch!*"
    show toth toth13

    y "Maybe a sliightly deeper kiss?"
    show toth toth09 with Dissolve(.2)
    ty "*Smoooooooooooch!*"
    show toth toth13 with Dissolve(.2)

    y "Maybe a sliiiiiightly deeper kiss?"
    show toth toth08 with Dissolve(.2)
    "*Smooooooooooooooooooch!*"
    show toth toth13 with Dissolve(.2)

    show toth toth13 with Dissolve(1.5)
    ty "I've changed my mind, mr. dick!"
    ty "After kissing you, I decided... I'm going to eat you!"
    ty "Swallow you whole because you taste so nice!"
    ty "And if I don't succeed the first time, I'll try again and again and again!!"
    y "YES!"
    y "Uh... I mean... ooooh no... please don't eat me!"
    ty "My mind is made up!"
    ty "Please don't struggle, but you can cry if you need to."

    show toth toth100 with dissolve
    ty "Hmmmmm!"

    call pauseInterface
    ty "*sluurp* *glurp* *gah*"
    y "He's really putting up a fight, isn't he?!"
    ty "*glp* *shlup*"
    show toth toth13 with Dissolve(1.5)
    ty "He is!"
    ty "What should I do?"

    menu:
        "Just keep trying to swallow him!!":
            $ temp_boolean = True
            show toth toth10
            ty "'ere i go!"
            show toth toth101
            ty "*gagh!* *mmg!*"

        "Shake him until he cries!":
            show toth toth16
            ty "Take this! You naughty dick!"
            ty "I need to shake some sense into you!"

    call pauseInterface
    y "fuck!"
    y "Hnnnggg..."
    y "gonna cum... eh, cry... soon!"

    menu:
        "in mouth":
            if temp_boolean == False:
                y "Quick! open your mouth!"
                show toth toth16
                show expression "bk3/tylee/loveblow/openmouth.png":
                    xpos 0 ypos 0

            else:
                hide toth
                show toth toth07

            play sound "audio/gltch2b.mp3"

            if temp_boolean == False:
                show expression "bk3/tylee/loveblow/spermout_5.png"
                with flash
            call pauseInterface

            play sound "audio/gltch2b.mp3"

            if temp_boolean == False:
                show expression "bk3/tylee/loveblow/spermout_6.png"
                with flash
            call pauseInterface

            play sound "audio/gltch2b.mp3"

            if temp_boolean == False:
                show expression "bk3/tylee/loveblow/spermout_7.png"
                with flash

            call pauseInterface
            show toth toth12

            if temp_boolean == False:
                hide expression "bk3/tylee/loveblow/openmouth.png"
                hide expression "bk3/tylee/loveblow/spermout_5.png"
                hide expression "bk3/tylee/loveblow/spermout_6.png"
                hide expression "bk3/tylee/loveblow/spermout_7.png"

            show expression "bk3/tylee/loveblow/sperm_inmouth.png"
            with Dissolve(1.5)
            ty "Hmmm! Delicous tears of joy!"

        "on face":
            hide toth

            if temp_boolean == False:
                show toth toth17

            else:
                show toth toth12

            pause 1
            show expression "bk3/tylee/loveblow/spermout_1.png"
            show toth_blink_temp
            play sound "audio/gltch2b.mp3"
            with flash
            call pauseInterface

            play sound "audio/gltch2b.mp3"
            show expression "bk3/tylee/loveblow/spermout_2.png"
            show toth_blink_temp
            with flash
            call pauseInterface
            show toth toth18

            ty "Are you done crying?"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/tylee/loveblow/spermout_3.png"
            show toth_blink_temp
            with flash
            ty "You must be really happy!"
            y "*pant* he is."

    call pauseInterface
    y "That was divine... Thanks."
    ty "you... really shoot a lot of semen.."
    ty "did you know that?"
    y "I did know that."
    ty "it's so thick... i don't mind though."
    ty "come back again, okay?"
    y "sure thing."
    show toth toth19 with Dissolve(1.5)
    y "Cya later, Ty!"
    show toth toth21 with Dissolve(1.5)
    ty "Bye!"
    
    return
##### [Ty Lee] Fuck
label gallery_tylee_lovefuck:
    call gallery_dCharacter_3Common

    show expression "ebackgrounds/bed_inside.jpg"
    $ toxd_transparent = 'false'
    $ toxd_dildo = False
    ty "i need to get stuffed. now."
    "you watch as ty lee drops her clothes to the floor."
    show toxd_head eyesfront with Dissolve(1.5)
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    ty "sit down, i'm going to give you a penis massage."
    y "a... penis massage?"
    ty "yeah!"
    show toxd toxd00a with Dissolve(1.5)
    hide toxd_head
    show toxd_head eyesfront

    if love_ty_sex_quest < 5:
        ty "i'm so glad we're all alive and safe!"
    ty "i have to thank mr. dick!"
    y "...i have no problem with that."
    ty "I have a nice warm place for him to take a rest and massage him at the same time!"
    ty "And I'm sure he'll be super happy and cry again."
    show toxd toxd00b with Dissolve(1.5)
    "With practiced ease you quickly slide out of your clothes and position yourself beneath Ty Lee."
    show toxd_head eyesdown
    y "Well... he has been playing outside a lot, so I guess he could use some inside relaxing."
    show toxd_head eyesfront
    ty "Then it's decided!"

    show toxd_head eyesdown
    show toxd toxd00c
    ty "I'll just grab him and gently guide him to where he'll need to be."
    show toxd_head lewd
    with Dissolve(1.5)
    ty "MMMMhhh, he's so stiff. "
    ty "I'll really have to massage him hard so he can become soft again."


    show toxd toxd01 with Dissolve(1.5)
    show toxd_head eyesfront
    ty "Are you ready?"
    y "Super ready."
    hide toxd_head
    show toxd toxd02
    with Dissolve(1.5)


    ty "Hmmm, I'll just slowly put him in deeper."
    show toxd toxd03 with Dissolve(1.5)
    ty "He feels really warm all by itself."
    show toxd toxd04 with Dissolve(1.5)
    ty "but it also feels like he's shivering? That's odd!"
    y "Yeah, when he's really looking forward to something he starts pulsating."
    y "Perfectly normal, please go on."
    show toxd toxd05a with Dissolve(1.5)
    ty "Ah!! I don't think he can go deeper. We've hit the ceiling!"
    show toxd_head eyesfront:
        ypos 12
    ty " I think it's tip is about..."
    show expression "bk3/tylee/lovedildo/body_1_armpoint.png":
        ypos 0 xpos 1000
        linear 0.8 xpos 900
        linear 1.2 ypos 100 xpos 800
    show toxd_head eyesdown
    ty "here.."
    hide expression "bk3/tylee/lovedildo/body_1_armpoint.png"
    show toxd toxd01
    hide toxd_head
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "Time for the massage."
    hide toxd_head
    show toxd toxd100
    call pauseInterface
    ty "Hmm I really like massaging you."
    ty "It makes my head feel all fluffy and light."


    menu:
        "x-ray on":
            $ toxd_transparent = 'dick'

        "keep going like this":
            pass
    call pauseInterface
    show toxd toxd01
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "Mmmh... I'm gonna massage you really hard now!"
    ty "So you better be prepared!"

    y "I'm ready!"
    hide toxd_head
    show toxd toxd101
    hide toxd_head

    y "Wohoo! "
    call pauseInterface
    y "Oh, shit!"
    y "gonna cum!!!"
    ty "not in me!"

    menu:
        "inside":
            hide toxd
            show toxd toxd05a

            if toxd_transparent == 'dick':
                show expression "bk3/tylee/lovedildo/womb.png":
                    alpha 0.0
                    linear 1.5 alpha 0.5

            y "Gonna fill you up!"
            show toxd toxd05b
            ty "No! wait!"
            ty "don't-"

            if toxd_transparent == 'dick':
                show expression "bk3/tylee/lovedildo/womb_sperm.png":
                    alpha 0.0
                    linear 4.0 alpha 1.0
            show toxd toxd05a
            play sound "audio/gltch2b.mp3"
            pause 2
            play sound "audio/gltch2b.mp3"
            pause 2
            play sound "audio/gltch2b.mp3"
            ty "unghh... ahh..."

            ty "u-uh spirits... you... you came in me!"


            if toxd_transparent == 'dick':
                hide expression "bk3/tylee/lovedildo/womb.png"
                hide expression "bk3/tylee/lovedildo/womb_sperm.png"

            show toxd toxd00b
            show toxd_spermgush
            show toxd_head eyeshalf
            with Dissolve(1.5)
            ty "you actually... finished in-inside me!"
            y "was i not supposed to?"
            ty "umm... it... it should be fine..."

        "outside":
            show toxd_head eyeshalf
            hide toxd
            show toxd toxd05a
            $ toxd_transparent = 'false'
            show toxd toxd00d with Dissolve(1.5)
            y "hnnnngg!"
            play sound "audio/gltch2b.mp3"
            show expression "bk3/tylee/lovedildo/spermout_1.png"
            call pauseInterface

            play sound "audio/gltch2b.mp3"
            show expression "bk3/tylee/lovedildo/spermout_2.png"
            call pauseInterface

            play sound "audio/gltch2b.mp3"
            show expression "bk3/tylee/lovedildo/spermout_3.png"
            call pauseInterface
            ty "Ooh! All over my boobies!"
            hide toxd_head
            hide expression "bk3/tylee/lovedildo/spermout_1.png"
            hide expression "bk3/tylee/lovedildo/spermout_2.png"
            hide expression "bk3/tylee/lovedildo/spermout_3.png"
            show toxd toxd08 with hpunch
            "Tylee slides off your dick and falls backwards, exhausted from the effort."
            call pauseInterface
            ty "Ah, that felt so nice."
            ty "I feel drenched..."
            y "you are."


    y "We'll do this again soon."
    ty "that sounds... fun."
    
    return
##### [Ty Lee] Dildo Fuck
label gallery_tylee_lovedildo:
    call gallery_dCharacter_3Common

    $ toxd_transparent = 'false'
    $ toxd_dildo = True

    show expression "ebackgrounds/bed_inside.jpg"
    show toxd_head eyesfront with Dissolve(1.5):
        xzoom -1

    ty "Say, Suki told me about this thing she lost in the tunnels."
    ty "She said I could have it if she ever finds it again."
    ty "As a thanks for saving her life."
    ty "Have you found something like a small statue in the tunnels?"
    y "I might... could you describe it?"

    ty "It's green, looks like avatar Kyoshi and is the size of a fairly impressive banana."
    ty "It's for.... fun."
    y "could... could it be this?"
    show toxd_head eyesdown
    show expression "bk3/tylee/lovedildo/solodildo.png" with Dissolve(1.5)
    ty "Ah, yes!"
    ty "That's it!"
    show toxd_head eyesfront
    ty "Thanks for finding it!"
    ty "Would you like me to give you a demonstration of how it's used?"
    ty "As a thanks?"
    y "Well, as long as it doesn't cost me cabbages."
    ty "Of course not!"
    hide toxd_head

    show toxd toxd00b
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "You're supposed to kiss it, but with your \"other lips\"."
    hide expression "bk3/tylee/lovedildo/solodildo.png"
    show toxd toxd00c
    show toxd_head lewd
    with Dissolve(1.5)
    ty "I need to... put it in here... AHH!!" with hpunch

    show toxd toxd01 with Dissolve(1.5)
    show toxd_head eyesfront
    ty "Ehehe... just a second."
    hide toxd_head
    show toxd toxd02 with Dissolve(1.5)
    ty "Mmmh, I'm pushing down now."

    show toxd toxd03 with Dissolve(1.5)
    ty "fuuurther..."
    show toxd toxd04 with Dissolve(1.5)
    ty "I'm eating it all up!!"

    show toxd toxd05a with Dissolve(1.5)

    ty "Ahh!"
    ty "I'm kissing it, but like really deep!"

    show toxd_head eyesfront:
        ypos 12
    show expression "bk3/tylee/lovedildo/body_1_armpoint.png":
        ypos 0 xpos 1000
        linear 0.8 xpos 900
        linear 1.2 ypos 100 xpos 800
    ty "It reaches about... "
    ty "here."
    ty "Do you like the show so far?"
    hide expression "bk3/tylee/lovedildo/body_1_armpoint.png"

    show toxd toxd05a
    y "There's literally no way I can't like this!"
    show toxd toxd01
    hide toxd_head
    show toxd_head eyesdown
    with Dissolve(1.5)
    ty "Good!"
    ty "And that was just the warm up!"
    ty "Now watch closely as I make it disappear and appear again! "
    ty "Like a magician!"

    hide toxd_head
    show toxd toxd100

    call pauseInterface


    ty "Ah!... Aah!!..."
    ty "do you... like this?"
    y "Best damn magic show ever."
    y "All magicians should be pretty girls and this should be their first trick!"

    menu:
        "do some x - ray trickery ":
            $ toxd_transparent = 'dildo'

        "keep going like this":
            pass
    call pauseInterface
    ty "I have one more trick to show you!"
    ty "I call it... rockin the cradle!"
    show toxd toxd101
    y "Fuck this is hot..."
    y "Would you mind me jacking off to this?"
    ty "Not at all!"
    ty "...*Unff!!*... Go a ...*unff!!*... ahead!!"


    ty "Ah... i'm feeling funny!!"

    y "I'm getting there too, just go with it!"

    show toxd toxd05a with hpunch
    show toxd toxd05a with hpunch

    hide toxd
    show toxd toxd06
    with Dissolve(1.5)
    call pauseInterface
    show toxd toxd07 with Dissolve(1.5)
    call pauseInterface

    y "I'll take care of the encore."
    play sound "audio/gltch2b.mp3"
    show expression "bk3/tylee/lovedildo/spermout_dildo1.png"
    call pauseInterface
    play sound "audio/gltch2b.mp3"
    show expression "bk3/tylee/lovedildo/spermout_dildo2.png"
    call pauseInterface
    play sound "audio/gltch2b.mp3"
    show expression "bk3/tylee/lovedildo/spermout_dildo3.png"

    ty "*Pant...* *pant...*"
    ty "that... that was really nice!"
    ty "Suki is a great friend to have!"
    y "Yeah, I like her a lot too."

    return
##### [Naga] Clawjob
label gallery_naga_clawjob:
    call gallery_dCharacter_3Common
    
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"
    show expression "bk3/naga/bj/bg_dream.jpg"

    show toxe toxe00:
        ypos 40 xpos 330

        parallel:
            linear 2.0 ypos 60
            linear 2.0 ypos 40
            repeat

        parallel:
            linear 6.0 xpos 500
            linear 6.0 xpos 330
            repeat

    "{i} Lisssten to me!{/i}" with hpunch
    y "{size=+5}ah!" with hpunch
    y "what the shit?!"
    y "you can't just pop up in my-"
    y "......"
    y "OH my god!!"
    y "You're so cute!"
    "{i} We have seriousss thingsss to talk about...{/i}"
    y "Coochie, coochie, coo!"

    show toxe toxe01 with Dissolve(1.5)
    "{i} SSSilence!!!{/i}" with hpunch
    y "Aaaawhh, you're even cute when you're angry!"
    y "Okay, but seriously now..."
    y "What the flying fuck are you and what are you doing in my mind?"

    show toxe toxe09 with Dissolve(1.5)
    "{i}I wasss born when you took the eyesss..."
    "{i}freed."
    y "So you're not the dreamstealer?"
    "{i} A part of her... small, weak... but strong here... hiding."
    y "Here where? My mind? My dreams?"
    "{i}HISSSS!!!!{/i}"
    "{i}Your mind is unssstable, illusssionsss, hallucinationsss."
    "{i}You're tainted.{/i}"
    y "Really?"
    y "Except for some restless dreams... which YOU could've done for all i know... I feel fine."
    "{i}I've been protecting you, but I can't do much more..."
    "{i}...not unless you allow me within your mind.{/i}"
    "{i}Invite me in.{/i}"
    y "Invite?"
    y "Wow, you certain you're not a vampire?"
    y "Needing permission to enter?"
    y "Anyway, not gonna happen... why would I trust you?"
    y "Why do you even want to help me?"
    y "So far anything with a lisp has caused me nothing but trouble."
    show toxe toxe01 with hpunch
    "{i}HISSSS!!!! Foool!!!{/i}"
    y "You're not winning me over..."
    show toxe toxe00
    "{i}I can do other things for you....{/i}"


    show expression "bk3/naga/clawjob/playerbody.png"
    show expression "bk3/naga/clawjob/dicksolo.png":
        xpos 360 ypos 0
    with Dissolve(1.5)
    y "what the..."
    "{i}...Sssshhhht...{/i}"

    hide toxe
    hide expression "bk3/naga/clawjob/dicksolo.png"
    show toxe toxe03:
        linear 2.0 ypos 10
        linear 2.0 ypos 0
        repeat
    with Dissolve(1.5)
    "{i}Like this... you like thisss... right?{/i}"
    y "....I don't dislike it."
    y "But I still won't let you burrow into my mind."
    "{i}Prreettyy pleasssse?{/i}"
    y "Nope."
    show toxe toxe04

    show expression "bk3/naga/clawjob/tailcover.png":
        xpos 620 ypos 120
        linear 2.0 yzoom 1.0 ypos 300 rotate 0 xpos 630
        linear 2.0 yzoom 0.9 ypos 120 rotate 20 xpos 620
        repeat

    "{i}Prreeeettyy pleasssse?{/i}"
    y "No, you little vixen!"

    hide expression "bk3/naga/clawjob/tailcover.png"
    show toxe toxe01
    show expression "bk3/naga/clawjob/dicksolo.png":
        xpos 360 ypos 0
    with Dissolve(1.5)

    "{i}HIsss!!"
    "{i}Ssstop being ssso ssstubborn!!{/i}"
    "{i}Your sssafety is my sssafety!!{/i}"
    show toxe toxe00:
        xpos 300
    with Dissolve(1.5)
    "{i}SSsorryy, I'm a bit on edge... Let me... continue.{/i}"

    menu:
        "use your tail":
            hide toxe
            show toxe toxe04
            show expression "bk3/naga/clawjob/tailcover.png":
                xpos 620 ypos 120
                linear 2.0 yzoom 1.0 ypos 300 rotate 0 xpos 630
                linear 2.0 yzoom 0.9 ypos 120 rotate 20 xpos 620
                repeat

        "use your little clawhands":
            hide toxe
            hide expression "bk3/naga/clawjob/dicksolo.png"
            show toxe toxe03:
                linear 2.0 ypos 10
                linear 2.0 ypos 0
                repeat
    y "Damn, that's nice."
    y "I'm about to \"pop the cork\"!"

    scene black
    show expression "bk3/naga/bj/bg_dream.jpg"
    show expression "bk3/naga/clawjob/playerbody.png"
    show toxe toxe05
    with Dissolve(1.5)
    "{i}Would you like me to drink your champagne? {/i}"

    menu:
        "No, gonna go for a facial!":
            play sound "audio/gltch2b.mp3"
            show expression "bk3/naga/clawjob/spermout_1.png" with hpunch
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/naga/clawjob/spermout_2.png" with hpunch
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/naga/clawjob/spermout_3.png" with hpunch
            call pauseInterface


            scene black
            show expression "bk3/naga/bj/bg_dream.jpg"


            show toxe toxe08:
                xpos 300
                linear 3.0 ypos 20
                linear 3.0 ypos 40
                repeat
            with Dissolve(1.5)
            "{i}That'sss... thick ssstuff...{/i}"

        "Swallow it all!":
            show toxe toxe06
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            call pauseInterface
            show toxe toxe06
            play sound "audio/gltch2b.mp3"
            call pauseInterface

            scene black
            show expression "bk3/naga/bj/bg_dream.jpg"

            show toxe toxe07:
                xpos 300
                linear 3.0 ypos 20
                linear 3.0 ypos 40
                repeat
            with Dissolve(1.5)
            "{i}Burrp! That'sss... more than I expected.{/i}"
    "{i}I'll leave you alone now..."
    "{i}Do I have your permisssion?{/i}"

    y "Hmmm what? Sure."
    "{i}Thankssss!{/i}"
    hide toxe with Dissolve(1.5)
    y "...wait, I gave you permission to leave! Nothing else!"

    "{i}NO! That totally counted as an invite into your mind!!!{/i}" with hpunch
    y "Nuh-uh!"
    "{i}Yeah-eh!{/i}"
    "{i}Don't worry... It'll be better for both of usss.{/i}"
    "{i}I'm leaving for real now."
    "{i}And I have your permisssion!{/i}"
    y "You're leaving with my permission to leave! That's it!"
    "{i}Lalalalal! "
    "{i}I can't hear you!! {/i}"

    return
##### [Guard] Fuck 
label gallery_guard_fuck:
    call gallery_dCharacter_3Common

    show totq totq00 with Dissolve(1.5)
    hide expression "maze/love_nudeguards.png"

    bk3_g1_b "Hey avatar, nice you could make it!"
    y "You're naked."
    y "....."
    y "wherever this is going, I like where it's starting."
    bk3_g2_b "I'm cold."
    y "so, why did you ask me to come here?"
    bk3_g1_b "Well, first let me ask you a question."
    bk3_g1_b "How do you feel about chicks with dicks?"

    menu:
        "I want to believe they're real":
            $ totq_fucked_with = 'realdick'
            bk3_g1_b "Nice! Because I came into possession of a potion which can grow a dick."
            bk3_g1_b "A few drops will make one which lasts a minute."
            bk3_g1_b "Here, I'll show."

            show totq totq54 with Dissolve(1.0)

            bk3_g1_b "A few drops from this bottle and...."

            show totq totq55 with Dissolve(0.7)
            show totq totq56 with Dissolve(0.7)
            show totq totq57 with Dissolve(0.7)
            show totq totq58 with Dissolve(0.7)
            bk3_g1_b "Presto!"

        "The stuff of nightmares":
            $ totq_fucked_with = 'doubledildo'
            y "There are no chicks with dicks, only men with tits."
            y "But if you're talking about strapons or something, I'm down with those."
            bk3_g1_b "Nice! Because I got one of those double dildo things."
            bk3_g1_b "Here, I'll show."

            show totq totq50
            bk3_g1_b "We take this big floppy pink dildo."
            show totq totq51 with Dissolve(1.5)
            bk3_g1_b "...Hnnnng..."
            bk3_g1_b "...push it in..."
            show totq totq52 with Dissolve(1.5)
            bk3_g1_b "...and we're ready for action."

    y "Okay so what's this all about?"
    bk3_g2_b "While we were \"hanging around\" we figured... hey why haven't we fucked each other?"
    bk3_g1_b "And since you're usually around here, you might as well watch us for that extra kick."
    y "You want me to watch you two bang each other?"
    bk3_g2_b "You seem like the kind of person who'd be down for watching some girl on girl action."
    y "You guessed right, but I want something in return."
    bk3_g1_b "Like what?"
    y "I don't know yet."
    y "But I'll come up with something."
    call gallery_room38_guardfuck_1

    y "Take a break, girls."
    hide totq
    show totq totq00

    if totq_fucked_with == 'realdick':
        show expression "bk3/guards/herma/donedick.png"
    else:
        show expression "bk3/guards/herma/donedildo.png"

    call pauseInterface

    bk3_g1_b "Wow, we worked up quite a sweat."

    if totq_fucked_with == 'realdick':
        bk3_g2_b "Ah, the potion is already losing it's effect."
        hide expression "bk3/guards/herma/donedick.png" with Dissolve(1.7)

    else:
        bk3_g2_b "Ah, let me put this thing aside."
        hide expression "bk3/guards/herma/donedildo.png" with Dissolve(1.7)


    menu:
        "My turn now":
            y "As much fun as it is to watch, participating is even better."
            y "I have quite some experience so I'll give you something to compare against."
            call gallery_room38_guardfuck_2

        "I got things to do":
            y "That was nice, but I have to go now."

    return
label gallery_room38_guardfuck_1:
    hide totq
    $ totq_fucked = 'peanut'

    show totq totq01 with Dissolve(1.5):
        xzoom 0.7 yzoom 0.7
    bk3_g1_b "Enjoy the show, Avatar!"
    bk3_g1_b "No time for foreplay!! In it goes!"
    show totq totq100

    bk3_g2_b "Aaah... it's so big..." with hpunch
    call pauseInterface
    bk3_g2_b "You're splitting my poor pussy open!"
    bk3_g1_b "Don't give me that shit."
    bk3_g1_b "You're loving this!"
    bk3_g1_b "Admit it!"
    bk3_g1_b "You're getting a kick out of me forcefully pushing it in."
    bk3_g2_b "...you're right! Keep plowing!"
    bk3_g2_b "Slam it in there as if the warranty is still valid!"
    bk3_g1_b "You asked for it!"
    show totq totq101
    bk3_g2_b "AAAAAAAH!!!"
    call pauseInterface
    bk3_g1_b "That's it! take it like the bitch you are!"
    bk3_g1_b "Swallow my \"carrot\"!"
    bk3_g2_b "Hhhhnnnngg!! So... big... so... so gooood..."
    bk3_g1_b "You like watching this, avatar!?"
    bk3_g1_b "You like me giving it to this bitch in heat!!"
    bk3_g2_b "Ss...sswitch places with me!"

    if totq_fucked_with == 'realdick':
        bk3_g1_b "Too bad that potion didn't grow balls too or I could've cum inside you."
        bk3_g1_b "Oh whatever."
        bk3_g1_b "Okay, let's switch!"

    else:
        bk3_g1_b "I wish this dildo had some sort of squirt action build in."
        bk3_g1_b "I'd love to \"cum\" inside her and see my seed drip out!"
        bk3_g1_b "Oh whatever. Okay, let's switch!"

    show totq totq01
    show expression "maze/black.png" with dissolve
    hide text
    show text "{color=fff} The girls switch places and immediately get back to work.{/color}"
    call pauseInterface
    hide text
    $ totq_fucked = 'krystal'
    hide totq

    show totq totq101:
        xpos -200
    hide expression "maze/black.png"
    with dissolve

    bk3_g2_b "AAAAAaaaand in it goes!"
    bk3_g1_b "Hnnnnnnngggg!!!"
    call pauseInterface
    bk3_g1_b "You... you could've started out slow you know!!"
    bk3_g2_b "No time for that, we have to entertain our guest."
    bk3_g2_b "Are you enjoying yourself so far, avatar?"
    y "It's always good to see girls explore other girls!"

    return
label gallery_room38_guardfuck_2:
    y "Get on all fours and turn your butt towards me."
    hide totq
    show totq_other
    show totq totq17
    bk3_g1_b "Like this?"
    call pauseInterface
    y "Exactly like that."

    $ totq_fucked = 'krystal'
    show totq totq10

    bk3_g1_b "AAAahhhh!!!" with vpunch
    call pauseInterface
    y "That's right, no waiting in line for you."
    bk3_g1_b "Ah! Ah! You're pushing so hard against my womb!"
    y "Well, that's your fault for having such a shapely behind. "
    y "it wants me to plant my dick deep within it."
    call pauseInterface
    bk3_g2_b "Aaawhh, no fair! I wanted it more."
    $ totq_fucked = 'peanut'
    bk3_g2_b "HHHHHNNNNNGGGG!!!!" with vpunch
    call pauseInterface
    bk3_g2_b "So... so hard and big... *pant* *pant*"
    y "You're clamping down pretty hard on me."
    bk3_g1_b "I can clamp down hard too! Come and see for yourself!"
    bk3_g2_b "Hnnngg... don't... try and steal my dick!"
    bk3_g2_b "It's my turn now."
    call pauseInterface
    $ totq_fucked = 'krystal'
    y "Some for you!" with vpunch
    $ totq_fucked = 'peanut'
    y "For you again!" with vpunch
    $ totq_fucked = 'krystal'
    y "And back to you!" with vpunch
    y "I think both of you are ready for the real deal."
    bk3_g2_b "Do it!!"
    bk3_g1_b "Wait! Wai-"
    show totq totq16
    bk3_g1_b "tttttt!!!" with vpunch
    bk3_g2_b "Hahaha, sissy!"
    $ totq_fucked = 'peanut'
    bk3_g2_b "HIiiiiiiii!!!!" with vpunch
    bk3_g1_b "Hahaha, take that!"
    bk3_g2_b "g-g-gladly!!"
    bk3_g1_b ".....Shit!! Do me! Do me!"

    menu:
        "switch girls":
            $ totq_fucked = 'krystal'
            bk3_g1_b "Yay!"
            bk3_g2_b "Aaaaawwwh!!"
            call pauseInterface

        "stay with this one":
            bk3_g1_b "Awwwh!"
            bk3_g2_b "I win!!!"
            call pauseInterface


    y "I really understand why Ajala loves to reward or punish you with a fingerbang."
    y "It's like I'm being sucked in."
    y "Hmmmmm.... I'm..."
    y "I'm about to cum!"

    menu:
        "On their masks":
            y "Show me your faces!!"
            hide totq
            show totq totq00
            "As soon as the girls turn around you unload in one massive explosion."
            play sound "audio/splurt2.ogg"
            show expression "bk3/guards/herma/sperm_face.png"
            with flash
            y "Ahhh, now that's the way to end things."
            bk3_g2_b "We're feeling kinda tired, maybe we can do this again tomorrow but for today we're done"
            bk3_g1_b "Besides we have to go back to our cell anyway."
            bk3_g1_b "See ya later!"

            show expression "maze/black.png" with Dissolve(1.5)
            show text "The two guards unsteadily waddle out of the room."
            call pauseInterface

            hide totq
            hide expression "bk3/guards/herma/sperm_face.png"

        "Cum inside them":
            $ totq_fucked = 'peanut'
            show totq totq12 with vpunch
            y "ngh!"
            play sound "audio/splurt2.ogg"
            with flash
            y "fuck!"
            $ totq_fucked = 'krystal'
            show totq totq12 with vpunch
            y "take it, whore!"
            play sound "audio/splurt2.ogg"
            with flash

            show totq totq59 with Dissolve(1.5)
            call pauseInterface
            "The sperm you just unloaded has filled up the girls and is now dripping out their pussies."
            bk3_g2_b "So that's how it feels when you're filled with sperm..."
            bk3_g1_b "Creamy!"
            y "And there's more where that came from!"
            y "But not right now."
            y "I need to make more."

            bk3_g1_b "Good because we're feeling kinda tired."
            bk3_g1_b "Maybe we can do this again later, but for today we're done."
            bk3_g1_b "Besides, we have to go back to our cell before anyone finds out we're missing."
            bk3_g1_b "It was fun. Seeya later!"

            show expression "maze/black.png" with Dissolve(1.5)
            show text "The two guards unsteadily waddle out of the room."
            call pauseInterface

    return
##### [Guard] Appa Fuck 
label gallery_appa_tug:
    call gallery_dCharacter_3Common

    show expression "maze/appa_bg.jpg":
        xpos 0 ypos 0

    show expression "maze/appa_body.png"
    hide expression "maze/appa_head3.png"

    show expression "maze/appa_head2.png":
        linear 2.0 ypos 10
        linear 1.0 ypos 0
        repeat


    show toxi toxi01 with Dissolve(1.5)
    "ropegirl" "Ah! You're back!"
    "ropegirl" "Wanna watch me become a sperm propelled rocket with Fluffy's help?"

    hide expression "maze/appa_head2.png"
    show expression "maze/appa_head3.png"
    hide toxi

    show toxi toxi101:
        parallel:
            xpos 50
            linear 4.0 xpos -250
            linear 4.0 xpos 50
            repeat

        parallel:
            ypos 0
            linear 1.0 ypos 15
            linear 1.0 ypos 0
            repeat

    "ropegirl" "First a little dance, to get him in the mood."
    call pauseInterface
    show toxi toxi102
    call pauseInterface
    "ropegirl" "He loves it when I shake my tushy!"
    y "Well, it's a fine tushy."
    hide toxi

    hide expression "maze/appa_body.png"
    hide expression "maze/appa_head3.png"
    hide expression "bk3/appa/tug/appa_tughead.png"
    show expression "bk3/appa/tug/appa_body.png"

    show expression "bk3/appa/tug/appa_tughead.png":
        linear 4.0 ypos -20
        linear 4.0 ypos 0
        repeat
    with Dissolve(1.5)

    "Appa turns over and..."

    show expression "bk3/appa/tug/appa_solodick.png":
        ypos 450 xpos 30
        linear 3.0 ypos 0 xpos 0
    "ropegirl" "Isn't it big!"
    y "Well... you know, it's only normal for an animal his size."

    show toxi toxi01:
        xpos 500
        linear 2.0 xpos 0

    hide toxi
    show toxi toxi101
    "ropegirl" "Now for some light buttocks action while pressing against his shaft..."
    call pauseInterface
    show toxi toxi09a
    play sound "audio/kiss.mp3"
    "ropegirl" "A kiss on the tip"

    hide toxi
    hide expression "bk3/appa/tug/appa_solodick.png"
    show toxi toxi03
    with Dissolve(2.0)
    "ropegirl" "And now that he's nice and hard... I smack his dick!"
    play sound "audio/slap.mp3"
    show toxi toxi04
    pause 0.1
    play sound "audio/deepgrowl.mp3"
    pause 1
    "ropegirl" "like this!"
    $ temp_int = 1

    while temp_int < 8:
        show toxi toxi03
        pause 0.5

        show toxi toxi04
        play sound "audio/slap.mp3"

        pause 0.5
        $ temp_int += 1


    "ropegirl" "He really loves this shit!"
    show toxi toxi05
    "ropegirl" "But his favorite is a handsjob."
    "ropegirl" "Just one hand isn't going to cut it here, so it needs to be a handsjob."
    "ropegirl" "You like that, donchya boy!"
    "ropegirl" "You like having that pillar of flesh you call a penis caressed by my hands."
    "ropegirl" "I'm sad it can't fit inside me, but we can come up with other fun things to do!"
    "ropegirl" "Who's a good boy?! Who's a good boy?!"
    "ropegirl" "How about some fast strokes!"

    show toxi toxi06
    call pauseInterface
    "ropegirl" "It's like jacking a treetrunk!!"
    "ropegirl" "Are you almost there Fluffy?!"
    play sound "audio/deepgrowl.mp3"
    pause 0.5
    play sound "audio/deepgrowl.mp3"
    "ropegirl" "Good, because I can't wait any longer!!"
    show toxi toxi07 with Dissolve(1.5)
    "ropegirl" "Do it Fluffy!!"
    "ropegirl" "Fill me with your cum!! Launch me!!"

    play sound "audio/bigsplurt.mp3"
    show toxi toxi07 with vpunch
    hide toxi
    show toxi toxi08

    hide expression "bk3/appa/tug/appa_solodick.png"

    show expression "bk3/appa/tug/minime.png":
        xanchor 0.5 yanchor 0.5

        xpos 530 ypos 700

        parallel:
            rotate 0
            linear 2.0 rotate 360
            repeat

        parallel:
            linear 5.0 ypos -300

    show expression "bk3/appa/tug/minisperm.png":
        xpos 400 ypos 600
        linear 4.0 ypos -300
    pause 4

    hide expression "bk3/appa/tug/minime.png"
    hide expression "bk3/appa/tug/minisperm.png"


    "ropegirl" "Team rocket blasting off again!"
    "ropegirl" "This is awesome!!"
    "ropegirl" "I can see forever!!"
    "ropegirl" "I'm... still gaining altitude...?"

    hide toxi
    show expression "bk3/appa/tug/appa_solodick.png"
    y "I know you'd like to enjoy that afterglow buddy... but if you want more in the future..."
    y "better go and make sure she doesn't go splat. "
    play sound "audio/deepgrowl.mp3"
    hide expression "bk3/appa/tug/appa_solodick.png"
    hide expression "bk3/appa/tug/appa_body.png"
    hide expression "bk3/appa/tug/appa_tughead.png"
    with Dissolve(1.5)
    pause 1
    "Appa jumps up..."
    show toxi toxi08
    hide toxi_appafly

    show toxi_appafly:
        ypos 300 xpos 200
        linear 9.0 ypos -500 xzoom 0.5 yzoom 0.5
    "...and flies after the girl"
    hide toxi_appafly
    hide toxi toxi08
    show expression "bk3/appa/tug/minime_caught.png"
    show expression "bk3/appa/tug/minime_caught2.png"

    show toxi_appahat:
        xpos 110 ypos 80 xzoom 0.8 yzoom 0.8
        linear 3.0 ypos 90
        linear 3.0 ypos 80
        repeat

    play sound "audio/thud.mp3"
    y "Good boy!" with vpunch
    hide expression "bk3/appa/tug/minime_caught2.png"

    show toxi toxi10:
        ypos 120
    with Dissolve(1.5)

    "ropegirl" "Wow! That was wild!"
    "ropegirl" "I could sell tickets for a ride like this!"
    y "You better not start pimping out my skybison...."
    "ropegirl" "It's just a joke!"

    return
##### [Ending] Toph Fuck
label gallery_bk3_love_final:
    call gallery_dCharacter_3Common

    menu:
        "Pregnant":
            $ katara_cum_inside = True
            $ toxh_preg = True
            $ totk_preg = True
            $ toxk_preg = True
            $ totf_preg = True
        "Not Pregnant":
            $ katara_cum_inside = False
            $ toxh_preg = False
            $ totk_preg = False
            $ toxk_preg = False
            $ totf_preg = False


    scene king_sitting
    show toi toi09
    ek "well, this {i}is{/i} serious!"
    ek "i'll see to it right away!"
    y "thank you, your majestic-ness."
    ek "no, thank you."
    ek "for opening my eyes."
    ek "and exposing the traitor long feng."
    ek "for this...."
    ek "i shall grant you one boon."
    y "a boob?"
    ek "a {i}boon{/i}."
    ek "...though it could be a boob if you'd like."
    ek "i like boobs."
    ek "but i like pretty much everything."
    y "hmmmm...."
    ek "may i make a suggestion?"
    y "sure."
    ek "this beautiful young lady here seems to be infatuated with you."
    y "the feeling is mutual."
    ek "perhaps this would be a good time to... solidify that."
    y "that... is a great idea."
    show toi toi09 with dissolve
    t "what...?"
    ek "then what boon would you have me grant?"

    menu:
        "a wedding":
            $ dressfuck_place = 'palace'
            y "I would ask your highness to grant us..."
            y "...a wedding."
            show toi toi10
            t "a {size=+10}what?!" with hpunch
            y "i love this girl, with all my heart."
            y "i wish to have her by mine, always."
            y "and i wish to be hers."
            t "I... i..."
            ek "very well, if this young lady agrees."
            t "i... you... i... agree..."
            ek "then we must have a ceremony!"
            t "i can't... you... but i..."
            ek "but of course the lady must prepare!"
            ek "and we must have an audience!"
            ek "what is a wedding without a crowd?"
            ek "i'll bring out every single person in this palace!"
            ek "and i'll have my staff assemble all your friends."
            y "thank you, your grace."
            t "bu... bu... bu..."
            ek "avatar, perhaps you could stay and discuss the war in more detail while this \"toph\" goes home to get ready."
            y "it would be a privilege."
            ek "you are correct."
            y "(man, i don't actually know any details...)"
            y "(i really should have paid more attention in history class.)"
            t "i... i need katara."
            hide toi with moveoutleft
            t "katara!!"
            ek "cute. she's a good catch."
            y "thanks, buddy."
            ek "oh, i like that!"
            ek "{size=+6}did you guys hear that?!"
            ek "{size=+6}he called me his buddy!"
            ek "we are buddies now."
            ek "this is decided."
            hide black
            show black
            with dissolve
            "you stay and discuss what you can remember about the day of black sun with the earth king."
            "...but really you end up talking about fuzzy animals and big hats."
            hide black with dissolve
            ek "that was certainly enlightening."
            y "yes, your highness."
            ek "well, we've assembled all of your friends, and pretty much everyone of class in ba sing se."
            ek "so this should be quite the ceremony!"
            show toeg toeg01 with moveinright
            dl "*whisper* "
            ek "mm-hmm... i see..."
            hide toeg with moveoutright
            ek "it has come to my attention that your lady and her friend are here."
            ek "a \"katara\"."
            ek "you may come forward, girl."
            show toki toki01:
                xzoom -1
            with moveinleft
            k3 "thank you, your grace."
            k3 "she is ready if you are."

            if totf_preg:
                k3 "and... i've helped her prepare a surprise for you."
                y "for me?"
            ek "excellent!"
            ek "let's do this thing properly then!"
            ek "stand back, buddy!"
            scene black with dissolve
            show toxk_background toxk_palace:
                xpos 0 ypos 0
            show toki toki01:
                xzoom -1
            with dissolve
            ek "let us begin."
            "a hush falls over the audience."
            k3 "{size=+6}ladies and gentlemen!"
            k3 "i present...."
            show toki toki03
            show toki_smile:
                xzoom -1
            with dissolve
            k3 "miss toph beifong!"
            hide toki
            hide toki_smile
            with moveoutleft

        "a house":
            $ dressfuck_place = 'home'
            y "I would ask your highness to grant us..."
            y "...a house."
            show toi toi10
            t "a {size=+10}what?!" with hpunch
            y "i love this girl, with all my heart."
            y "i wish to grow beside her."
            y "and a little home in the city would be perfect for that."
            t "I... i..."
            ek "very well, if this young lady agrees."
            t "i... you... i..."
            t "yes! of course!"
            ek "very well!"
            ek "you may have the house that was given to you when you first arrived."
            ek "it is yours."
            ek "i wish you much happiness."
            y "thank you, your highness."
            t "that... that house is... is..."
            y "ours."
            y "come."
            t "bu..."
            scene black with dissolve
            "you lightly take toph's stunned hand and direct her through the city and to the house."
            scene basingse_home_1
            show toi toi04
            with dissolve
            y "there it is."
            show toi toi10
            t "that's... ours?"
            t "I can't believe it..."
            y "come on, let's go inside."
            y "i'm feeling... a need."
            show toi toi08
            t "oh?"
            t "it wouldn't be a need to be... inside me, would it?"
            y "it might be."
            show toi toi07
            t "oh, i hope so."
            y "come on!"
            scene black with dissolve
            "you grab her hand and she giggles as you pull her eagerly inside."
            scene basingse_home_2
            show toi toi07
            with dissolve
            t "it's the same as it's always been, but..."
            t "it feels so... different."
            y "...ours."
            show toi toi09 with dissolve
            t "hmm?"
            y "it feels like ours."
            show toi toi04 with dissolve
            t "well said, my love."
            t "I... i can't keep it in anymore!"
            t "i have to tell katara!"
            t "i'll be back in a bit!"
            t "she's gonna be so excited!"
            hide toi with moveoutleft
            y "hahaha... damn she's cute."
            scene black with dissolve
            "you sit for a while, taking in the room."
            "you feel peaceful... and grateful."
            k3 "knock knock!"
            scene black with dissolve
            show toxk_background toxk_home:
                xpos 0 ypos 0
            with dissolve
            show toki toki01:
                xzoom -1
            with moveinleft
            k3 "i hope i'm not interrupting."
            y "no, i'm just having some happy thoughts."
            k3 "well, they're about to get better."
            y "oh? how?"
            k3 "well a certain cute chick came up to me all excited, and asked me to do something for her..."
            k3 "and i think you'll enjoy it."
            k3 "so, without further ado..."
            k3 "i present...."
            show toki toki03
            show toki_smile:
                xzoom -1
            with dissolve
            k3 "miss toph beifong!"
            hide toki
            hide toki_smile
            with moveoutleft

    $ toxk_dress = True
    $ toxk_sex = 'pussy'


    show toxk toxk10:
        xpos 0 ypos 0
    with Dissolve(1.5)
    call pauseInterface

    if dressfuck_place == 'palace':
        "the crowd cheers and toph blushes!"

    if dressfuck_place == 'home':
        "you let out a long, low whistle."
        "she blushes!"

    t "stop..."

    if toxk_preg:
        y "wait..."
        y "i... what..."
        y "your tummy..."
        y "how..."
        t "we had sex."
        t "a lot of it."
        y "no, i mean... you... already..."
        t "how am i already showing?"
        y "yes!"
        y "i just saw you!"
        t "katara."
        t "she gave me a pregnancy speed-up potion."
        t "she thought... she thought you'd like it."
        show toxk toxk12
        t "do you not like it?"
        t "I can't... undo it..."
        t "It's your seed growing inside me."
        t "i'm growing your sperm into a baby... that i'll birth for you."
        t "because... i love you."
        t "is that... okay?"
        y "...of course that's okay!"
        y "that's wonderful!"
        show toxk toxk10
        t "i'm so happy you said that!"

    else:
        y "you deserve that and then some, with how good you look."
        t "oh, aang...."

    y "Hey... you seem taller."

    show toxk toxk12
    t "That... that's probably because of the way I had my hair done."
    t "Katara did it for me."
    y "You look..."
    t "...yes?"

    show toxk toxk10:
        linear 3.0 ypos -260

    if dressfuck_place == 'palace':
        show toxk_background toxk_palace:
            linear 3.0 ypos -230

    else:
        show toxk_background toxk_home:
            linear 3.0 ypos -230
    y "...You look stunning."
    t "...thanks."
    y "Do you have some special underwear to go with it?"
    t "I figured..."
    stop music
    play music "audio/Unwritten Return.mp3"
    show toxk toxk11 with Dissolve(1.5)
    "Toph slowly raises her dress... totally giving away her elevated footwear but doesn't realize it."
    t "well... i figured you'd like it better this way."
    y "You know me so well!"
    y "did you... struggle into your first pair of high heels for me?"
    t "i... wanted to be tall..."
    y "you're so damn cute."
    t "hehehe... so whatcha wanna do now?"

    if dressfuck_place == 'palace':
        ek "a-hem!"
        show toxk toxk10:
            linear 3.0 ypos 0
        show toxk_background toxk_palace:
            linear 3.0 ypos 0
        ek "i believe vows are in order."
        ek "do you promise to forever love each other?"
        ek "through all the fetishes and loud chewing?"
        y "that's... oddly specific, but yes. i do."
        t "i do, too."
        ek "then, using my power as king, i now declare you married!"
        ek "you may consummate!"
        y "yeah, let's-"
        y "wait, what?"
        ek "you must consummate."
        y "here?"
        ek "of course!"
        ek "it is part of the ceremony."
        t "didn't you know that, aang?"
        y "I... guess i didn't."
        t "why did you think i was so shocked?"
        t "but i accept, and i want everyone to see you fill me!"
        t "to prove to everyone that i am your wife!"
        show toxk toxk11 with Dissolve(1.5)
        t "look at me..."
        show toxk toxk11:
            linear 3.0 ypos -260

        show toxk_background toxk_palace:
            linear 3.0 ypos -230
        t "take me."

    else:
        t "I want you to take me."
        t "i want you to fill me."


    y "*gulp....*"


    hide toxk

    if dressfuck_place == 'palace':
        show expression "ebackgrounds/palace_crowd.jpg"

    else:
        show expression "ebackgrounds/basingse_home_zoom.jpg"

    show toxk toxk06
    with fade

    if dressfuck_place == 'palace':
        "toph lays on her back in the center of the throne room."

    if dressfuck_place == 'home':
        "toph lays on her back on the floor."
    y "Sounds like a plan to me."

    if dressfuck_place == 'palace':
        y "...but there are a lot of people here."
        t "i don't see anyone else."
        y "yeah, but you can't see anything."
        t "hahaha!"
        t "well..."

    if dressfuck_place == 'home':
        t "i... i love how intimate this is."
    t "i see you."
    t "I've never seen anyone how i see you."

    if dressfuck_place == 'home':
        y "you've never seen anyone period."
        t "haha..."
        t "well..."
        t "i see {i}you{/i}."
    t "before this goes further... thank you."
    t "for what you are to me."
    y "thank you, toph."
    t "now..."

    if dressfuck_place == 'palace':
        t "don't forget why you're doing this."
        t "you're marking me, in front of everyone."
        t "you're claiming me as owned, by you."
        t "you must prove that i am taken, filled, and permanently marked as yours."

    if dressfuck_place == 'home':
        t "stop fucking around..."
        t "and start fucking into. me."
    y "...i can do that."
    y "Why don't we get that dress out of our way."
    show expression "bk3/toph/dressfuck/head_0_cynic.png"
    t "But sir... I'm a high class lady!"
    t "the only child of the wealthy Beifong family!"
    t "I couldn't do something so indecent as exposing myself and show my... my... "
    t "it's too crude to say!"
    y "...what?"
    y "you already did... just a moment ago."
    hide expression "bk3/toph/dressfuck/head_0_cynic.png"
    show expression "bk3/toph/dressfuck/head_0_angry.png"
    t "Just play along, Aang!"
    t "It's called roleplay."
    y "But you {i}are{/i} a high class lady and the only child of the wealthy Beifong family..."
    t "You want to do this or not?"
    y "Ahum! Don't worry about that, my precious little gem."
    y " Your family must accept me!"
    y "your family will watch as i penetrate you and take you as my love, and my fuckmate for life!"
    y "and if society denies our love then let it burn!!"
    hide expression "bk3/toph/dressfuck/head_0_angry.png"
    t "That's the spirit!"
    y "What?! Where!?"
    t "It's just an expression. Keep doing what you're doing!"
    y "Ah, right of course."
    y "My love for you burns more passionately than the fire of a blacksmith."
    y "I must have you! Allow me to sheath my sword into your forge of love!"

    hide toxk_background

    $ toxk_dress = True

    show toxk toxk00
    t "Is this more to your liking, noble sir?"

    menu:
        "YES! This will do nicely":
            pass

        "No, take it off entirely.":
            $ toxk_dress = False


    show toxk toxk07 with Dissolve(1.5)
    y "It certainly is!"

    show toxk toxk08 with Dissolve(2.0)

    y "Now before I ravish you, let me kiss those lips of yours."

    play sound "audio/kiss.mp3"
    show toxk toxk08 with pflash
    show toxk toxk07 with Dissolve(1.5)
    y "As sweet as strawberries."


    show toxk toxk01 with Dissolve(2.0)
    y "And now... I shall tend to your other lips..."


    show toxk toxk100
    call pauseInterface
    y "Hnn, you're as tight as ever, Toph!"
    y "Just pushing it in makes me afraid I'll break you."
    t "Pffff, as if you could!"
    t "I can clamp down so hard on you, it'd break off."
    y "uh, that's not really helping me in the \"staying hard\" department Toph.. "
    t "Oh... I mean... I'm a frail girl!"
    t "Please don't crush my pussy with your monster cock!"

    if dressfuck_place == 'palace':
        ek "i must say, i'm very much enjoying the drama here."
        ek "are there snacks?"
        ek "for those of us who are a little peckish?"
    y "...."
    y "so! You're challenging me me to crush your pussy!"
    t "I don't think you can, go ahead and try!"
    y "Does that go for your ass too?"

    if dressfuck_place == 'home':
        t "we're going to live together."
        t "so, whenever you need to rut, you can have it."

    else:
        t "well, it belongs to you now doesn't it?"
        t "whenever you need to rut, you can have it."

    t "or my pussy, if you'd prefer."
    t "i want you... however you want to have me."

    if dressfuck_place == 'palace':
        t "i'll finally be a proper married woman!"
        t "happily being fucked... without a say..."
        t "don't you know anything about marriage?"

    menu:
        "pick anal":
            $ toxk_sex = 'anal'

        "keep pounding pussy":
            $ toxk_sex = 'pussy'
    call pauseInterface
    y "I'm going to slam my cock into you so hard you'll be seeing stars!"
    t "Promises, promises."
    y "....better prepare yourself!"
    y "Riiiight now...."
    show toxk toxk101
    call pauseInterface
    t "Hnnff!! Is... is that all you got!"

    menu:
        "inside":
            hide toxk

            show expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)

            show toxk toxk15
            with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"
            show toxk toxk15 with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show toxk toxk15 with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show toxk toxk15 with flash
            call pauseInterface
            show toxk toxk16


            if toxk_sex == 'anal':
                show expression "bk3/toph/dressfuck/spermdrip_top_ass.png"
                with Dissolve(1.5)

            else:
                show expression "bk3/toph/dressfuck/top_spermdrip.png"
                with Dissolve(1.5)

            if toxk_sex == 'pussy':
                t "Did you just give me a creampie?"
                y "Sure did!"

            else:
                t "Filling my ass with your cream... you're a real pervert!"
                t "I love it!"


            y "Now gimme some sugar as a reward."

            if toxk_sex == 'anal':
                hide expression "bk3/toph/dressfuck/spermdrip_top_ass.png"

            else:
                hide expression "bk3/toph/dressfuck/top_spermdrip.png"


            show expression "bk3/toph/dressfuck/side_creampie.png"

        "outside":
            hide toxk

            show expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)

            show toxk toxk15
            with Dissolve(1.5)
            call pauseInterface
            y "Show me that pretty face of yours Toph!!"
            show toxk toxk16 with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/dressfuck/spermout1.png" with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/dressfuck/spermout2.png" with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/toph/dressfuck/spermout3.png" with flash
            t "mmmm.... warm...."
            call pauseInterface
            y "Fuck yeah."
            y "Now gimme some sugar."
            hide expression "bk3/toph/dressfuck/spermout1.png"
            hide expression "bk3/toph/dressfuck/spermout2.png"
            hide expression "bk3/toph/dressfuck/spermout3.png"
            show expression "bk3/toph/dressfuck/spermout4.png"


    hide expression im.Flip("ebackgrounds/basingse_home_4.jpg", vertical=True)


    show toxk toxk13
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show toxk toxk13 with pflash
    call pauseInterface
    show toxk toxk00 with Dissolve(1.5)
    y "I... really love you Toph."
    t "I love you too."

    if dressfuck_place == 'home':
        "you fall asleep in each other's arms."

    else:
        ek "good show!"
        k3 "well done!"
        y "i think they're applauding you."
        t "well {i}i{/i} think they're applauding {i}you{/i}."
        t "you... you rock my whole stupid world."
        ek "alright, can we clean this up now?"
        ek "bring out the royal jizz cleaner!"
        y "...that is a terrible job."

    return


##### [Ending] Katara Fuck
label gallery_katara_pregfuck:
    call gallery_dCharacter_3Common

    menu:
        "Pregnant":
            $ katara_cum_inside = True
            $ toxh_preg = True
            $ totk_preg = True
            $ toxk_preg = True
            $ totf_preg = True
        "Not Pregnant":
            $ katara_cum_inside = False
            $ toxh_preg = False
            $ totk_preg = False
            $ toxk_preg = False
            $ totf_preg = False
            
    stop music
    play music "audio/Unwritten Return.mp3"
    show expression "ebackgrounds/inside_hospital.jpg"
    $ temp_boolean = False


    show toxh toxh09
    k3 "Hey sexy!"

    if toxh_preg == True:
        y "Uuuuh... is that belly signifying what I think it does?"
        k3 "Surprised? With the amount of sperm you release?"
        k3 "It saturates the room so much that simply smelling it could get a girl pregnant!"
        y "Yeah, but usually this kinda thing takes time.."
        k3 "Ba sing Se is a big city with ingredients from all over the world."
        k3 "I figured it was best to move things along faster with the help of some special potions."
        y "But you know I can't stay...."
        k3 "Another reason why I wanted to speed things up."
        k3 "And you will come back for me..."
        k3 "Right?"
        y "It's not like I can buy a ticket and ride the time train whenever I want, but...."
        y "I'll do whatever I can."

    k3 "...do you have to go soon?"
    y "i'm not sure."
    y "i'm starting to get that feeling, though."
    k3 "did you have a good night with toph?"
    y "i had an amazing night."
    y "thanks for your help with that."
    k3 "you're so welcome!"
    k3 "i'm glad you came to visit me... even though you're starting to feel pressed for time."
    y "I love you and I love Toph, but it all started with you."
    k3 "We're sperm sisters! "
    y "Sperm sisters?"
    k3 "it's like eskimo brothers."
    y "so... you wanted to see me?"
    show toxh toxh10 with Dissolve(1.5)
    k3 "I was hoping for a little... something."
    y "have i told you you're pretty, lately?"
    k3 "it's always nice to hear."
    k3 "Have you ever played \"doctor\"?"
    k3 "because...."
    hide toxh with Dissolve(1.5)

    $ toxh_upperbody = 'up_default'
    hide expression "ebackgrounds/inside_hospital.jpg"
    show expression "ebackgrounds/inside_hospital_2.jpg"
    show expression "bk3/katara/pregfuck/braid_solo.png":
        xpos 0 ypos 0
    hide toxh
    show toxh toxh06
    with Dissolve(1.5)
    k3 "I feel like I need a thorough examination."
    show toxh toxh07
    k3 "Down there..."
    y "I can already see you are very, very hot. Feverish even."

    if toxh_preg == True:
        y "But... uuuuh... you sure that's safe with the baby and all?"
        k3 "Don't worry, it's perfectly safe."
        k3 "So safe we could even do this standing up!"
        y "For real?"
        k3 "For real."

        menu:
            "Nah, just stay like you are.":
                y "I kinda like this position better anyway."
                pass

            "Okay let's do it!":
                y "I mean if you're really certain it's safe."
                k3 "I am"
                jump gallery_bk3_katara_pregrub

    y "Let's take a closer look."
    show toxh toxh11 with Dissolve(1.5)
    y "Hmmm... everything looks perfectly fine so far..."
    show expression "bk3/katara/pregfuck/point.png" with Dissolve(1.5)
    k3 "You should especially inspect this part."


    menu:
        "spread pussy":
            hide expression "bk3/katara/pregfuck/point.png"
            show toxh toxh12
            with Dissolve(1.5)

        "kiss pussy":
            hide expression "bk3/katara/pregfuck/point.png" with dissolve
            play sound "audio/kiss.mp3"

            "you tenderly put your lips on Katara's clit and softly kiss it." with pinkflash
    y "This seems like the perfect place to take your temperature."
    y "But let's lick it first."
    show toxh_tongue:
        xpos 630 ypos 400
        easein 1.2 ypos 370
        repeat
    pause 1
    show expression "bk3/katara/pregfuck/spit.png":
        xpos 615 ypos 300 alpha 0.6
        linear 0.6 ypos 150 xpos 600 alpha 0.0
        linear 0.6 ypos 150 xpos 600 alpha 0.0
        repeat
    show expression "bk3/katara/pregfuck/front_blink.png":
        ypos 0
    k3 "Hmmmm... I like how thorough you are."

    hide toxh_tongue
    hide expression "bk3/katara/pregfuck/spit.png"
    y "That should do it."
    show toxh toxh11 with Dissolve(1.5)
    y " Time to take your temperature."
    hide expression "bk3/katara/pregfuck/front_blink.png"

    show toxh toxh00 with Dissolve(1.5)
    k3 "What an impressive thermometer!"
    y "I've already warmed it up for you."
    k3 "I'm not sure it'll fit, doctor!"

    show toxh toxh01
    y "Well, it might sting a little at first, but I'm certain it'll turn out all right."
    k3 "Then please dive right in."


    show toxh toxh100
    $ toxh_upperbody = 'up_blink'
    k3 "OH!" with hpunch

    $ toxh_upperbody = 'up_lewd'
    k3 "That's reaaally nice..."
    k3 "But shouldn't it be left inside for several minutes?"
    y "Its... ahhh... a special one."
    y "It works best when inserted repeatedly."
    y "It's my special thermometer for a very special patient."

    $ toxh_upperbody = 'up_blink'
    k3 "FUUUuuuuuckkk!! "

    $ toxh_upperbody = 'down'
    k3 "I'm goin to lie down for a moment."
    k3 "It's like your dick is handmade for my pussy."
    k3 "I can't understand how I managed to go without it for so long."


    $ toxh_upperbody = 'up_lewd'
    k3 "But you can't be satisfied with this slow pace."
    k3 "Don't hold back! Treat it as if it's the last pussy you'll ever have!"
    y "Don't say scary things like that!!"
    k3 "AAwwh, don't be scared."
    k3 "My little honeypot will always be there for you."
    show toxh toxh01
    y "In that case... make sure you hold your head or you'll end up with whiplash."
    k3 "That seems unlikely."
    y "Dont underestimate me, woman!!!"
    $ toxh_upperbody = 'up_blink'
    k3 "Do it! DO IT NOW!!"
    show toxh toxh101
    k3 "AH!!! THAT'S IT!"
    call pauseInterface
    "You keep slamming in your dick while Katara is making all sorts of appreciative sounds"
    y "HHHNNGG... Can't keep this up much longer!"
    y "Vitamin... shot... coming... your way now!"

    menu:
        "cum inside":
            $ temp_boolean = False
            hide toxh
            show toxh toxh05
            play sound "audio/gltch2b.mp3"
            pause 1
            play sound "audio/gltch2b.mp3"
            pause 1
            play sound "audio/gltch2b.mp3"
            pause 1
            show toxh toxh00
            show expression "bk3/katara/pregfuck/spermin1.png"
            with Dissolve(1.5)
            k3 "mmmm..."

        "cum outside":
            $ temp_boolean = True
            hide toxh
            show toxh toxh00
            play sound "audio/gltch2b.mp3"
            show toxh_spermshot
            show expression "bk3/katara/pregfuck/spermout1.png"
            call pauseInterface

            play sound "audio/gltch2b.mp3"
            show toxh_spermshot
            show expression "bk3/katara/pregfuck/spermout2.png"
            call pauseInterface

            play sound "audio/gltch2b.mp3"
            show toxh_spermshot
            show expression "bk3/katara/pregfuck/spermout3.png"
            $ toxh_upperbody = 'up_lewd'
            call pauseInterface

    scene black
    show expression "ebackgrounds/inside_hospital_2.jpg"
    show expression "bk3/katara/pregfuck/braid_solo.png":
        xpos 0 ypos 0
    show toxh toxh08

    if temp_boolean == True:
        show expression "bk3/katara/pregfuck/spermout4.png"

    else:
        show expression "bk3/katara/pregfuck/spermin2.png"
    k3 "How about a kiss?"
    y "That seems an impropriate thing to do considering you're my patient."
    y "....eh, screw medical ethics!"
    show expression "bk3/katara/pregfuck/shadowkiss.png" with pinkflash

    play sound "audio/kiss.mp3"

    "you let your lips linger on Katara's for a moment and then slowly pull away."
    show expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    hide expression "bk3/katara/pregfuck/shadowkiss.png"
    with Dissolve(1.5)
    y "I... have to go now."
    k3 "Please come back soon!"
    y "Don't worry. I will, but be warned."
    y "When I do... I'm gonna fuck you so hard you'll need a real doctor afterwards!"
    k3 "...that's... disturbing."
    y "Sorry, thought it would sound cool and all."
    y "fuck... can i just sleep here?"
    y "i'm worn out."
    y "I need a nap."
    k3 "of course you can sleep here, love."
    y "oh."
    y "good..."
    y "*yaawn*"
    
    return
##### [Ending] Katara Pregnant Standing
label gallery_bk3_katara_pregrub:
    call gallery_dCharacter_3Common

    $ totk_preg = True
    scene black
    show expression "bk3/katara/rub/floor_tokt.jpg"
    show totk totk03
    with Dissolve(1.5)

    k3 "Ready when you are."
    y "I was ready the first day I saw you."

    show expression "ebackgrounds/ceiling_1.jpg"
    hide totk
    show totk totk17 with Dissolve(1.5)

    call pauseInterface

    y "Wow, you're dripping wet already!"

    show totk totk14 with Dissolve(1.5)
    "You stand behind Katara and slide your hand down over her big belly as she lifts her arms."

    show totk totk11 with Dissolve(1.5)
    call pauseInterface
    y "Just making absolutely certain you're ready to receive me in my full glory."
    "you keeping sliding your two fingers in and out of Katara's pussy."
    "katara" "Hnnn... "
    y "That's my girl."

    show totk totk06 with Dissolve(1.5)
    "You drop your pants and stick your dick in between her legs."
    k3 "That didn't take you long. You couldn't hold back any longer?"
    show totk totk05
    y "Don't underestimate my willpower woman!"
    y "I'm going to rub up against your lips until you go crazy!"

    k3 "You're such a tease."
    k3 "Do you want me to beg for it?"
    k3 "Beg for you to stop rubbing your throbbing cock up against my clit?"
    k3 "Beg to put it in my wet tight-"

    show totk totk06
    y "...."

    k3 "Why did you stop?"

    show totk totk07 with vpunch
    k3 "Ah!"

    show totk totk08 with Dissolve(1.5)
    y "I changed my mind!"
    y "My willpower remains as strong as ever!"
    k3 "I'm loving that hard and thick willpower of yours."
    y "Hnnnnng! I could do this forever."

    k3 "I don't need forever. But... Ah!! ..how does the rest of our lives sound like to you?"
    y "....Pretty good... "
    y " Never ever change Katara."
    k3 "I won't! And if you ever get impotent I can bloodbend your dick all hard again!"
    y "Hah! With such a plump booty in arms reach? No way that'll ever happen."
    y "...please don't bloodbend my dick.."
    y "Or I'll spank you!"

    menu:
        "slap her ass.":
            show totk totk06
            show totk totk19 with Dissolve(1.5)

            $ temp_int = 0

            show expression "bk3/katara/rub/ass_blush.png":
                alpha 0.1 xpos 400 ypos 200

            while temp_int < 7:
                play sound "audio/slap.mp3"


                show totk totk19
                show expression "bk3/katara/rub/ass_blush.png":
                    alpha 1.0
                show expression "bk3/katara/rub/ass_slaphand_1.png":
                    xpos 440 ypos -40
                show expression "bk3/katara/rub/head_surprise3.png":
                    xpos -420 ypos -20
                show text "AH!":
                    xpos 100 ypos 240
                with hpunch

                hide expression "bk3/katara/rub/head_surprise3.png"
                hide text
                show expression "bk3/katara/rub/head_standard.png":
                    xpos -420 ypos -20

                hide expression "bk3/katara/rub/ass_slaphand_1.png"
                show expression "bk3/katara/rub/ass_slaphand_0.png" at Move((700, -250), (900, 0), 0.15 )


                show expression "bk3/katara/rub/ass_blush.png":

                    alpha 1.0
                    xpos 400 ypos 200
                    linear 3.0 alpha 0.1
                call pauseInterface
                $ temp_int += 1

                hide expression "bk3/katara/rub/ass_slaphand_0.png"

                hide expression "bk3/katara/rub/head_standard.png"

            hide expression "bk3/katara/rub/ass_blush.png"
            hide expression "bk3/katara/rub/ass_slaphand.png"

            show expression "bk3/katara/rub/head_standard.png":
                xpos -420 ypos -20


            k3 "I'm not convinced yet."
            k3 "Maybe if you slap me some more..."
            y "...."
            hide expression "bk3/katara/rub/head_standard.png"

            show totk totk07
            k3 "Ah!" with vpunch
            y "Back inside it goes!!"

        "keep going like this":
            call pauseInterface
            pass

    y "Ready or not. I'm gonna split that pussy open with enough force to lift you from the ground!"
    k3 "DO IT!!"
    show totk totk100
    call pauseInterface
    "you start thrusting your cock into Katara just hard enough for her to make small shreeks."
    k3 "Hiii!"
    y "Where do you want it Katara? In or outside!?"
    k3 "Wherever.. unf! you prefer! It's not like you can get me more pregnant!"
    y "Is that a challenge!?!"
    y "gonna cum!"

    menu:
        "Inside!":
            y "Here... it... comes !"
            show totk totk12
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Going once!"
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "Going twice!"
            play sound "audio/gltch2b.mp3"
            show totk totk12 with vpunch
            y "SOOOOLLLLDDDD!!!!"

            hide totk
            show totk totk06
            show expression "bk3/katara/rub/sperm_flowout.png"
            with Dissolve(1.5)
            y "....annndd I'm empty"
            y "I feel completely drained."
            y "You're just too pretty and sexy Katara!"

        "cum outside":
            $ temp_boolean = True
            hide totk
            show totk totk19
            with Dissolve(1.5)
            "You pull out of Katara and.."
            play sound "audio/gltch2b.mp3"
            show expression "bk3/katara/rub/body_butt_sperm1.png" with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/katara/rub/body_butt_sperm2.png" with flash
            call pauseInterface
            play sound "audio/gltch2b.mp3"
            show expression "bk3/katara/rub/body_butt_sperm3.png" with flash
            call pauseInterface
            "..paint her ass white."
            y "You're just too pretty and sexy Katara!"


    k3 "Mmmm, that was fantastic. My legs are feeling wobbly."
    y "Why don't you lie down for a minute?"

    scene black

    show expression "ebackgrounds/inside_hospital_2.jpg"
    show expression "bk3/katara/pregfuck/braid_solo.png":
        xpos 0 ypos 0
    show toxh toxh08
    show expression "bk3/katara/pregfuck/spermin2.png"
    show expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    with Dissolve(1.5)

    k3 "How about a kiss for your sexy watertribe girl?"
    y "I can do better than that!"


    show expression "bk3/katara/pregfuck/zhadkiss_katface.png"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    hide expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png" with pinkflash

    "You softly kiss katara on her lips."

    hide expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png":
        xpos 300 ypos 50
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png" with pinkflash

    "On her belly."


    hide expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png":
        xpos 450 ypos 170
    with Dissolve(1.5)

    play sound "audio/kiss.mp3"
    show expression "bk3/katara/pregfuck/zhadkiss_playerbody.png" with pinkflash


    "And finally between her legs."

    hide expression "bk3/katara/pregfuck/zhadkiss_katface.png"
    hide expression "bk3/katara/pregfuck/zhadkiss_playerbody.png"
    show expression "bk3/katara/pregfuck/eyes_lookat_2.png"
    with Dissolve(1.5)

    y "I... have to go now."
    k3 "Please come back soon!"
    y "Don't worry. I will, but be warned."
    y "When I do... I'm gonna fuck you so hard you'll need a doctor afterwards!"
    k3 "...that's... disturbing."
    y "Sorry, thought it would sound cool and all."
    y "fuck... can i just sleep here?"
    y "i'm worn out."
    y "I need a nap."
    k3 "of course you can sleep here, love."
    y "oh."
    y "good..."
    y "*yaawn*"
    
    return
##### [Ending] Ty Lee Lick
label gallery_tylee_rub:
    call gallery_dCharacter_3Common

    $ toxj_arms = 'down'
    $ toxj_face = 'normal'
    $ toxj_bikini = 'on'
    
    play music "audio/Unwritten Return.mp3"
    play sound "audio/thud.mp3"
    show expression "bk3/toph/party/bg_citystreet1.jpg":
        xpos -1000
    show toxj_ty01
    y "ow!" with sshake
    y "ty lee...?"
    y "fuck, that was like running into a wall."
    y "how did i not knock you over?"
    ty "strong thighs."
    y "....nice."

    ty "What are you doing here?"
    y "I'm actually... leaving."
    ty "For how long?"
    y "Oh, you'll see me soon again."
    y "In fact, I promise I'll help you out in your tavern."
    ty "But I don't have a tavern."
    y "Yet."
    ty "Oh, okay!"
    y "What are you wearing?"
    ty "It's a spanking new swimsuit! How do you like it?"
    y "It's nice."
    hide toxj_ty01
    show toxj_ty03
    ty "You can't just say it like that!"
    y "I... I can't?"
    ty "No, you have to look up and down and say stuff like \"That looks hot\"!"
    y "No prob."
    hide toxj_ty03
    show toxj_ty02:
        xpos 0 ypos 0
        easeout 5.0 ypos -360
        easeout 5.0 ypos 0
    with Dissolve(1.5)
    call pauseInterface
    y "Okay, I got me an eyeful of that."
    ty "And?"
    y "It nicely accents your voluptuous figure and it looks super hot!"
    ty "that's a lot better!"

    hide toxj_ty02
    show toxj_ty01
    with Dissolve(1.5)
    ty "Well, if you're going... Can we do something before you go?"
    y "It has to be quick, but sure I can spare a few minutes."
    ty " I want to waterboard you."
    y "Say what?"
    ty "I want you to lie down so I can squat over your face and rub my pussy all over."
    ty "That's what they call waterboarding right?"
    y "That's... news to me. "
    y "I guess when you're a gusher it can be though."

    menu:
        "Sure let's do this!":
            $ toxj_rub = 'face'
            y "That sounds.. great!"

        "suggest alternative":
            $ toxj_rub = 'dick'
            y "How about my dick instead?"
            ty "I already played lot's with mr. penis I want something new."
            y "Sorry Tylee, but mr. dick misses miss pussy."
            ty "....okay fine."

    hide toxj_ty01
    show toxj_ty05

    with Dissolve(1.5)
    ty "I'll take this off and..."
    y "Eeehh, we might better do this in that alley over there."
    ty "Oh! Good idea!"
    hide toxj_ty05
    show expression "ebackgrounds/nightsky.jpg"
    hide expression "bk3/toph/party/bg_citystreet1.jpg"

    show toxj toxj00

    if toxj_rub == 'face':
        show expression "bk3/tylee/tyrub/face1.png"
    with Dissolve(1.5)

    ty "You have the best seat in the house!"


    "you can already see her moistening in anticipation."
    "she lowers her body and..."
    show toxj toxj03 with Dissolve(1.5)

    if toxj_rub == 'dick':
        "presses her pussy lips again your penis."

        y "A dick carressed by the lower lips of a pretty girl... it doesn't get more comfortable."
        y "Mr. dick is ready to get a full body wash!"
        y "A happy end is unavoidable!"

    else:
        "presses her pussy lips against your face."
        ty "Please give miss pussy a nice fat kiss."
        play sound "audio/kiss.mp3"
        show expression "bk3/tylee/tyrub/face1.png":
            alpha 0.5
        with pinkflash
        show toxj_tongue:
            xpos 420 ypos 320
            easein 1.2 ypos 260
            repeat

        "You give a long kiss and start sliding your tongue between Tylee's labia."

        $ toxj_face = 'lewd'
        ty "Oooh, I like it when you do that!"
        ty "Let's... let's just keep doing that... for a while longer"
        call pauseInterface
        ty "Oooohh, yeah. Make sure to hit all nooks and crannies... *mmm...*"
        ty "Ah... this... is nice but I still have to waterboard you so hold on for a minute."

        hide toxj_tongue
        show toxj toxj03
        show expression "bk3/tylee/tyrub/face1.png":
            linear 7.0 alpha 0.0


    $ toxj_face = 'normal'
    ty "Okay, I'll start rubbing now!"
    show toxj toxj100
    "toxj100"
    ty "Oh! This feels so naughty! I'm a naughty girl!"
    ty "Look at me, rubbing my pussy all over you!"
    $ toxj_face = 'lewd'
    ty "mmmmmm... I really like the rubbing against my clit."
    call pauseInterface
    $ toxj_arms = 'up'
    call pauseInterface
    ty "I'm getting reeaally hot... Gotta take off the top too!"
    $ toxj_bikini = 'off'
    ty "That's better!"
    ty "Gotta go faster! Hold on!"

    show toxj toxj101

    if toxj_rub == 'dick':
        "The super quick rubbing makes you feel like your dick has caught fire."
        "Luckily your dick is drenched in Tylee's juices."

    else:
        "You gasp for air during the small moments you can as Tylee is ferociously goes back and forward."
        "Your face is drenched in Tylee's juices."
    $ toxj_face = 'normal'
    ty "I'm.... I'm about to squirt!"
    ty "Get ready for a flood!"
    $ toxj_arms = 'down'

    if toxj_rub == 'dick':
        y "Right behind you!"

    else:
        y "*mumble*"

    $ toxj_face = 'lewd'
    play sound "audio/gltch2b.mp3"
    show toxj toxj02 with flash
    show expression "bk3/suki/pussyrub/pjuice_1.png"
    ty "Ahh!!"
    play sound "audio/gltch2b.mp3"
    show toxj toxj03 with flash
    show expression "bk3/suki/pussyrub/pjuice_2.png"
    ty "Aaaaah!!"
    play sound "audio/gltch2b.mp3"
    show toxj toxj04 with flash
    show expression "bk3/suki/pussyrub/pjuice_3.png"
    ty "Aaaaah!!"

    hide expression "bk3/suki/pussyrub/pjuice_1.png"
    hide expression "bk3/suki/pussyrub/pjuice_2.png"
    hide expression "bk3/suki/pussyrub/pjuice_3.png"
    with Dissolve(1.5)

    hide toxj
    show toxj toxj00
    with Dissolve(1.5)

    $ toxj_face = 'normal'
    ty "That was fun!"

    mv "TYLEE!!" with hpunch

    hide toxj
    hide expression "ebackgrounds/nightsky.jpg"
    show expression "bk3/toph/party/bg_citystreet1.jpg":
        xpos -1000

    show toxj_ty03:
        xzoom -1.0
    ty "Aaaah! Who's that!"
    show toxj_az02:
        xpos 400
        linear 0.5 xpos 0
    a "what are you doing?!"
    hide toxj_ty03
    show toxj_ty04:
        xzoom -1.0
    ty "uh, oh, hi... Azula..."
    a "You're butt naked! In the streets!" with hpunch
    ty "Uh... I'm wearing a smile?"
    "You slowly crawl away in the commotion."
    "Azula, completely flustered with Tylee's undressed state, hasn't even noticed you. "
    hide toxj_az02
    show toxj_az01:
    with Dissolve(1.5)
    a "I can't believe you... you were... I haven't even... Well, whatever!!"
    a "we got work to do!"
    show toxj_mai01:
        xpos 300
        linear 2.0 xpos 100
    m "Hey Ty!"
    ty "Hey Mai!"
    hide toxj_az01
    show toxj_az01:
        xpos 0
        linear 1.0 xpos -200
    a "Enough!"
    a "put some pants on Ty Lee. We leave now!"
    ty "Okay!"
    $ toxj_bikini = 'on'
    hide toxj_ty04
    show toxj_ty02:
        xzoom -1.0
    ty "What are we going to do?"
    a "Topple a king."
    a "Do you still have that \"fangirl\" outfit? "
    ty "Fangirl? OH the kyoshi warrior outfit! Haha, good one, azula!"
    ty "But I'm afraid I lost it...."
    a "I should have expected this to happen... and I did. I have another one for you."
    a "now let's go."
    hide toxj_az01 with Dissolve(1.5)
    show toxj_mai01:
        xpos 0
    m "Hope you had fun while being away, Azula has been extra touchy lately so we better not make her wait."
    ty "I'll be with you guys in a minute."
    hide toxj_mai01 with Dissolve(1.5)
    hide toxj_ty02
    show toxj_ty01
    with Dissolve(1.5)
    ty "Pssst... Are you still there, Aang?"
    y "Yep."
    ty "I had a lot of fun, but it looks like I gotta go too!"
    y "Don't worry about it. We'll have even more fun in your future!"
    ty "Really?"
    y "I guarantee it! See you later Ty!"
    ty "Bye Bye!!"
    hide toxj_ty01 with dissolve

    return
#
##### [Katara] Handjob
label gallery_bk4l_katara_hj:
    scene image "bk4_love/bg/kathouse_day.jpg":
        pos(0,-300)

    show bfdc bfdc01
    with dissolve
    yon "you said last night that you had a surprise for me?"
    k4 "i did, yes."
    k4 "i wanted to give you a handjob."
    yon "oh. uh..."
    k4 "wait, is that a youth potion?"
    yon "this? well, maybe."
    yon "shady gave it to me."
    k4 "give me that."
    show bfdc bfdc05 with flash
    k4 "did it work?"
    yon "...holy shit."
    k4 "i feel... perkier."
    k4 "ah, back to being young again."
    k4 "so... how about that handjob?"

    menu:
        "jack me off!":
            yon "go for it."
            k4 "wonderful."
            k4 "would you like me to make you cum now, while i'm young?"
            k4 "...or wait until i'm older again?"

            menu:
                "old":
                    $ bk4_katara_age = 'old'
                "young":
                    $ bk4_katara_age = 'young'

            call gallery_bk4l_katara_hj2

        "no thanks":
            yon "I think i'm still gonna pass."
            k4 "ohh... well, that's a shame."

    return

label gallery_bk4l_katara_hj2:
    k4 "lay down."
    k4 "i need to see that cock."
    stop music
    play music "audio/Unwritten Return.mp3"
    scene image "bk4_love/bg/kathouse_day.jpg":
        pos(0,-580)

    show bfdc bfdc16
    show bfdc_top one
    with fade
    k4 "mmmm..."

    call pauseInterface
    "katara's grip is confident but soft."
    "her hand gives you a light squeeze and moves a little in both directions."
    k4 "i can't believe i get to see you again."
    k4 "i missed you."
    yon "well i missed your hands-"
    show bfdc_top two

    call pauseInterface
    "katara begins pulling and pumping your shaft..."
    "her experience is all focused on draining you."
    yon "damn girl..."
    k4 "i can't wait to milk you dry."
    k4 "I want to force you to empty all over my hands."
    show image "bk4_love/misc/proceed.png":
        alpha 1.0 xalign 0.96 yalign 0.96
        linear 0.7 alpha 0.0
        linear 0.7 alpha 1.0
        repeat

    $ temp_int = 0

    while temp_int < 15:
        show bfdc_top one with vpunch
        show bfdc_top two
        pause(0.6)
        $ temp_int += 1

    hide image "bk4_love/misc/proceed.png"
    yon "shit!"
    k4 "yes, i can feel it rising..."
    k4 "swelling..."
    k4 "stiffening..."
    k4 "give it to me... give it all to me..."
    play sound "audio/splurt2.ogg"
    show bfdc_top one
    show bfdc_spermshot with vpunch
    yon "hngh!"
    k4 "yes! cum for me!"
    play sound "audio/splurt1.ogg"
    show bfdc_spermshot with vpunch
    pause(0.4)
    k4 "lovely."
    show bfdc_top three
    k4 "so much!"

    menu:
        "ask her to taste it":
            show bfdc_top four
            k4 "mmmm..."
            k4 "delicious..."

        "don't ask her":
            pass

    yon "now {i}that{/i} is a happy ending."
    k4 "good."
    k4 "please... cum again."

    return
##### [Katara] Sex
label gallery_bk4l_katara_sex1:
    
    play music "audio/Unwritten Return.mp3"
    show image "bk4_love/bg/kathouse_day.jpg":
        pos(0,-580)

    show bfdc bfdc01
    with fade

    menu:
        "old katara":
            $ bk4_katara_age = 'old'
            show bfdc bfdc06 with dissolve

        "young katara":
            $ bk4_katara_age = 'young'
            show bfdc bfdc07 with dissolve

        "nevermind":
            return

    k4 "finally!"
    hide bfdc with dissolve
    show bfdg bfdg00:
        pos(0,10)
    with dissolve
    k4 "bring me your cock!"
    k4 "i want to pleasure you."
    k4 "...and i want to enjoy you."
    pause
    k4 "i want to feel you deep in me..."
    k4 "i want to satisfy you."
    show bfdg bfdg04 with dissolve
    k4 "i want to feel you deep in me..."
    k4 "i want to satisfy you."
    pause
    k4 "yes, take out that cock..."
    k4 "and take me..."
    k4 "give me everything..."
    k4 "use me!"
    show bfdg bfdg05 with vpunch
    k4 "ungh!"
    k4 "yes..."
    show bfdg bfdg02:
        pos(0,0)

    show bfdg_fuck:
        xpos 90 ypos 160
        linear 0.6 ypos 160#-20 180
        linear 0.4 ypos 140#-40
        linear 0.6 ypos 160#-20
        repeat

    k4 "i'm your fucktoy!"
    k4 "use me. use me whenever."
    k4 "you can fill me every time you need to empty your balls."
    k4 "i'm your cumslut."
    hide bfdg
    show bfdg bfdg02 behind bfdg_fuck:
        linear 0.6 ypos 10
        linear 0.4 ypos -30
        linear 0.6 ypos 0
        repeat

    if bk4_katara_age == 'young':
        show bfdg bfdg01a

    else:
        show bfdg bfdg01b

    show bfdg_fuck:
        xpos 90
        easein 0.4 ypos 180 #0
        linear 0.6 ypos 110 # -70  180
        linear 0.6 ypos 160 # -20  180
        repeat

    k4 "yes! yes yes yes!"
    k4 "don't stop!"
    k4 "use me! use this whore cunt!"
    k4 "only yours!"
    k4 "always yours!"

    call pauseInterface
    k4 "fuck! you're so good at that!"
    k4 "did you miss me too?"
    hide bfdg
    hide bfdg_fuck
    show bfdg bfdg09:
        linear 0.0 xpos 0
        linear 0.1 xpos 30
        linear 0.1 xpos 0
        linear 0.1 xpos 30
        linear 0.1 xpos 0
        linear 0.4 xpos 0
        linear 0.4 xpos 0
        linear 0.4 xpos 40
        repeat

    show text "Ah!":
        pos(620,240) alpha 1.0 zoom 1.0
        linear 0.4 alpha 0.0 zoom 2.5 pos(700,240)
        pause(1.2)
        repeat

    if bk4_katara_age == 'young':
        show bfdg bfdg08a
        k4 "i'll... unh... take... that..."
        k4 "as... a... unh... yes..."
        k4 "ahhh..."

    else:
        show bfdg bfdg08b
        k4 "i'll... unh... take... that..."
        k4 "as... a... unh... yes..."
        k4 "ahhh..."

    call pauseInterface
    yon "shit, i'm getting close..."
    k4 "give it to me!"
    k4 "all your cum, my love."
    k4 "empty your balls in me... on me... wherever you need it."

    menu:
        "outside":
            hide text
            hide bfdg
            show bfdg bfdg06 at Move ((0, 0), (30, 0), .20, bounce=True, repeat=False)
            k4 "mmm... beautiful."
            show bfdg_spermshot
            show image "bk4_love/katara/fuck/spermout1.png" with hpunch
            yon "fuck!"
            k4 "ahhh..."
            k4 "yes..."
            show bfdg_spermshot
            show image "bk4_love/katara/fuck/spermout2.png" with hpunch
            k4 "drench me..."
            show bfdg bfdg07 with dissolve
            k4 "you like seeing this slut covered in your spunk?"
            k4 "am i pretty?"
            pause

        "inside":
            hide text
            hide bfdg
            show bfdg bfdg09 with hpunch
            k4 "anhh!"
            k4 "yes!"
            show bfdg bfdg09 with hpunch
            k4 "blow! empty it all into me!"
            show bfdg bfdg06
            show image "bk4_love/katara/fuck/xspermout.png"
            with Dissolve(2.0)
            k4 "you like seeing this slut filled in your spunk?"
            show bfdg bfdg07 with dissolve
            k4 "am i pretty?"
            pause

    k4 "anytime you want to be satisfied..."
    k4 "you know where to find me."

    return
##### [Kya] Masturbation 1
label gallery_bk4l_kya_mast2:
    scene black
    
    play music "audio/Unwritten Return.mp3"
    show image "bk4_love/bg/igloo.jpg":
        pos(0,0)

    show bfda bfda07
    show image "bk4_love/misc/vapor.png"
    show image "bk4_love/kya/bath/wall.png":
        linear 3.0 pos(-150,0)

    pause(4.0)
    yon "(oh spirits yeah, you lesbian slut...)"
    kya "deeper... deeper, korra..."
    kya "push in your tongue..."

    call pauseInterface
    kya "More... faster... deeper..."
    kya "lick my cunt..."
    kya "i want my juices running down your face, korra..."
    kya "mmmmmm...."
    kya "what's that, opal?"
    kya "you want to play with my tits?"
    kya "ahhh... well... ahh..."
    kya "since you asked so nicely..."
    show bfda bfda01 with Dissolve(2)
    kya "here..."
    kya "yes, opal..."
    kya "i know, they're big aren't they?"
    kya "what's that?"
    kya "sure, you can have a closer look..."
    show bfda bfda02 at Move((0, 0), (0, 30), .40, bounce=True)
    kya "they are bouncy aren't they?"
    kya "that's it, bury your face right in them."
    kya "yes opal, suck on my fat tits."
    kya "you cute little whore."

    call pauseInterface
    kya "good girl."
    show bfda bfda03:
        linear 0.8 ypos 10
        linear 0.4 ypos 0
        repeat

    kya "ahhh... it's okay..."
    kya "you can... pinch them..."
    kya "you too, korra..."
    kya "is this your first time with a busty woman?"
    kya "i'll teach you."
    kya "oh, i promise i'll teach you."

    call pauseInterface
    kya "mmmm... ah..."
    kya "ahh... you're both... so good..."
    show bfda bfda04
    kya "ohhh.... oh yes... spirits..."
    kya "rub them... rub me... rub those big tits..."
    kya "you beautiful, sweet-faced little puppy-sluts..."

    call pauseInterface
    kya "oh? what's that?"
    kya "you both want to suck on them?"
    kya "you want to suck on them so hard i get hickies right on my fucking whore nipples?"
    show bfda bfda01:
        pos(0,0)

    kya "here you go, girls."
    kya "suck your young hearts out."
    kya "slobber on them, lick and suck and cover my areolas with both your spit-"
    show bfda bfda05 with vpunch
    kya "-hey!"
    kya "damn it!"
    kya "why are you here again!?"
    yon "aw, but it was getting so good."
    show bfda bfda06
    kya "that's it!"
    kya "i'm not messing around this time!"
    hide image "bk4_love/misc/vapor.png"
    show misc_whirl:
        pos(100,-300) zoom 4.0
        linear 1.0 pos(700,100) zoom 1.0

    kya "you're going down-"
    yon "ah ah ah."
    yon "skimpy bikini? harassing girls?"
    yon "is it really worth it?"
    kya "rrrghh...."
    hide misc_whirl with dissolve
    yon "good girl!"
    kya "good..."
    kya "i'm older than you!"
    yon "I'm aware."
    show bfda bfda05
    kya "oh, fuck you."
    yon "i'm down."
    kya "in your dreams."
    kya "even naked and... shit, wet as fuck... that would never happen."
    yon "i bet your experience makes you amazing on a cock."
    kya "well i've never been with a cock so your fantasies are bullshit."
    yon "wait... really?"
    kya "i'm not having this conversation with you."
    kya "fuck off."
    hide bfda with dissolve
    yon "wait... come back!"
    yon "it was just starting to get good..."

    return
##### [Kya] Masturbation 2
label gallery_bk4l_kya_mast3:
    scene black
    
    play music "audio/Unwritten Return.mp3"
    show image "bk4_love/bg/igloo.jpg":
        pos(0,0)

    show bfdb bfdb03:
        pos(300,50)

    show bfda_wall:
        linear 3.0 pos(-150,0)

    with Dissolve(1)

    kya "hello, tenzin..."
    kya "it's cold and lonely here, isn't it..."
    yon "(what the fuck?)"

    call pauseInterface
    kya "i haven't seen you in ages..."
    show bfdb bfdb04
    kya "mmmm...."
    kya "i wish bumi was here..."
    kya "two brothers..."
    yon "(i thought she was a lesbian?)"
    yon "(this must be a deep fucking fetish...)"

    call pauseInterface

    kya "come here, you two..."

    show bfdb bfdb05
    kya "i wonder... what it would be like..."

    call pauseInterface

    kya "to be ridden..."
    kya "by my two brothers..."

    show bfdb bfdb06:
        linear 1.0 xpos 290
        linear 0.6 xpos 300
        repeat

    kya "yes... mmmh..."
    kya "fuuuck yes."

    kya "take turns with me..."
    kya "ride your whore of a sister..."

    call pauseInterface


    kya "you feel so good in me..."
    show bfdb bfdb07
    kya "ahh you're so good with that... with that tongue..."
    kya "tenzin..."
    kya "yes..."
    kya "keep licking, korra..."
    kya "more..."

    call pauseInterface
    kya "i said, more....."
    kya "hnh..."
    kya "i said..."
    show bfdb bfdb08
    kya "more!"

    call pauseInterface

    kya "use those fucking cocks!"
    kya "fuck me!"
    kya "fuck my pussy, boys!"
    kya "you want me to... ah... to squirt?"
    kya "want me to squirt on your cocks?"
    kya "yes... ah... yes..."
    kya "put it... ah... put it in my ass..."
    kya "the... hnhhgh... the whole thing..."
    kya "and you... unn... uhh... fuck my... my face..."
    kya "and... fuck... fuck... i'm gonna squirt... uhgh..."
    kya "yes, ride me, use me, empty your fucking loads in ah! ah!"
    kya "i'm gonna... uhhn... uhhgh.... ahhhh..."

    show bfdb bfdb09:
        pos(300,0)

    $ temp_int = 0

    while temp_int < 3:
        show bfdb bfdb09a with vpunch
        show bfdb bfdb09a with vpunch
        show bfdb bfdb02 with dissolve
        kya "Aaaah!!"
        $ temp_int += 1

    show bfdb bfdb10 at Move((300, 0), (300, 30), .20, bounce=True)
    kya "oh, spirits..."
    kya "i needed that..."
    kya "drenched in cum..."

    show bfdb bfdb11
    kya "mmm... spunk tastes so sweet and warm..."
    kya "i could eat sperm all day..."
    kya "mmmmgh..."
    kya "i wonder if i should try co-"

    show bfdb bfdb01 with vpunch
    kya "hey!"
    yon "hello!"
    kya "you... damn it!"
    kya "can you stop. fucking. staring?!"
    yon "sorry, i have a medical condition."
    yon "I have to stare at naked women or i might die."
    yon "it's very technical."
    kya "....."
    kya "............"
    hide bfdb
    show bfda bfda06 behind bfda_wall at Move((0, 0), (0, 30), .20, bounce=True)
    pause(0.3)
    show misc_whirl:
        pos(100,-300) zoom 4.0
        linear 1.0 pos(700,100) zoom 1.0

    yon "this again?"
    yon "alright, threaten me, but we both know how this ends."
    yon "you-"
    show misc_whirl:
        pos(700,100) zoom 1.0
        linear 1.0 pos(-350,-500) zoom 6.0

    yon "ah!"with vpunch
    scene black with dissolve
    yon "...."
    yon "ughh..."
    scene
    scene image "bk4_love/bg/compound_night.jpg"
    with fade
    yon "...that bitch attacked me!"
    yon "...."
    yon "...i am so cold."
    yoa "splashing someone with water out here should be prosecuted as a first degree murder attempt!"

    return
##### [Korra] Water Session
label gallery_bk4l_bath_sessions2:
    
    play music "audio/Unwritten Return.mp3"
    show image "bk4_love/bg/kathouse_day.jpg":
        pos(0,-580)

    show bfdl bfdl03
    with fade

    call pauseInterface
    yon "that's hot."
    kn "warmmmm...."
    k4 "welcome."
    k4 "let's get started."
    show bfdl bfdl04

    call pauseInterface
    k4 "easy now..."
    k4 "remember, your body has suffered tremendous damage..."
    kn "i know..."
    show bfdl bfdl05
    show image "bk4_love/korra/heal/glowheal.png":
        alpha 0.3
        linear 2.0 alpha 1.0
        linear 2.0 alpha 0.3
        repeat
    with Dissolve(2.0)

    call pauseInterface
    yon "that's still cool."
    k4 "you're doing well, korra."
    kn "i can feel it... everywhere."
    kn "hn..."
    k4 "alright..."
    show bfdl bfdl03
    k4 "so, [povname]..."
    k4 "are you ready?"
    yon "i am."
    hide image "bk4_love/korra/heal/glowheal.png" with Dissolve(1.5)
    show bfdl bfdl01
    show image "bk4_love/korra/heal/big_water.png"
    with dissolve
    k4 "well first i need to clear the water."
    kn "umm..."
    kn "okay, this again..."

    call pauseInterface
    show bfdl bfdl02
    show misc_whirl:
        pos(400,200) zoom 2.0
        linear 4.0 pos(-400,100)    zoom 1.0

    hide image "bk4_love/korra/heal/big_water.png"
    k4 "and the tub is empty."
    k4 "how do you feel, korra?"
    kn "better."
    kn "i... hurt less."
    k4 "excellent."
    show bfdl bfdl01

    k4 "the next step is the leg massage."
    k4 "[povname], would you get into a good position?"
    yon "sure."
    show bfdl bfdl12
    k4 "korra, you are to sit there until he's done, understand?"
    kn "...i understand."


    k4 "alright."
    k4 "i'll leave you two to it."
    show bfdl bfdl10 at Move((0, 0), (0, 30), .40, bounce=True)
    yon "oof."
    yon "okay, i'm in position."
    yon "how you feeling?"
    kn "embarrassed."
    yon "what? why?"

    show bfdl bfdl11

    call pauseInterface

    kn "because i was a weepy mess last night?"
    yon "nah, you were fine."
    yon "you were just honest with me, which is pretty cool."
    kn "..."
    kn "you really think that?"
    yon "yeah, it just means it's easy when we're together."

    call pauseInterface
    kn "...huh."

    show bfdl bfdl10
    yon "let's just put your leg down."
    yon "and i'll switch sides..."
    show bfdl bfdl10 with Dissolve(1.5):
        xzoom -1.0 xpos 200

    yon "okay, ready for the other leg?"
    kn "but really, i'm totally fine and you don't need to worry."
    yon "oh yeah?"
    kn "yeah, i'm great. really."

    show bfdl bfdl11

    call pauseInterface
    kn "ah... that's... nice."
    kn "it feels... really good?"
    kn "how are you... ah..."
    kn "aammmhhhh...."
    yon "was... did you just moan?"
    kn "maybe..."
    yon "but to return to our convo, i get the sense you're trying to put me at ease."
    yon "you don't have to pretend everything's fine."
    kn "i am fine."
    kn "and... we should probably stop now."
    kn "i'm feeling pretty massaged."

    call pauseInterface

    show bfdl bfdl10:
        xzoom 1.0 pos(0,0)

    kn "okay, that's enough."
    kn "i'm... that's enough for now."
    show bfdl bfdl12 with dissolve
    k4 "how's it going in here?"
    kn "i think i'm finished with his leg massage, katara."
    k4 "well, then..."
    k4 "i'll have to finish it."
    kn "wha-"
    show bfdl bfdl13 at Move((0, 0), (0, 20), .20, bounce=True)
    kn "hey!"
    k4 "let's properly stretch those hammies."

    call pauseInterface
    yon "those are thick ham steaks indeed."
    kn "hey..."

    k4 "you need a proper stretch and haven't been getting it."
    k4 "here we go!"
    show bfdl bfdl14 with dissolve
    kn "ohhhh....."

    call pauseInterface
    kn "i don't know... how to feel... about... hnnnhmmm...."
    yon "you moaned again!"
    kn "hnn...."

    call pauseInterface
    k4 "alright, i think that's enough."
    show bfdl bfdl13 with dissolve
    kn "...."
    kn "can i go...?"

    call pauseInterface
    k4 "yes."
    show bfdl bfdl12 with Dissolve(2)
    k4 "[povname], please take her back."
    yon "with pleasure."


    scene
    scene image "bk4_love/bg/koroom_day_1.jpg"
    show bfdd bfdd02
    with fade
    yon "you really don't have to front with me, you know."
    yon "you can be honest."
    kn "i'm fine, really."
    kn "i'll talk to you later, okay?"
    kn "i want to be alone right now."
    yon "alright."
    hide bfdd with dissolve
    yon "(she's clearly still miserable.)"
    yon "(maybe i can get her a present to cheer her up?)"
    yon "(i'll see what i can find.)"

    return


##### [Korra] Massage
label gallery_bk4l_korra_massage2:
    scene black
    
    play music "audio/Unwritten Return.mp3"
    scene image "bk4_love/bg/korra_bed.jpg" #blue color
    show bfdm bfdm02 with dissolve:
        pos(0,0)

    call pauseInterface
    kn "i'm ready when... whenever you are."
    yon "i'm going to lift your shirt now, okay?"
    kn "okay."
    show bfdm_tits behind bfdm
    show bfdm bfdm04
    with dissolve
    kn "........."

    call pauseInterface
    "you look at korra and she has that strange expression again."
    "vulnerable and submissive, but also a little... afraid?"
    "still, she seems willing to follow your lead."
    yon "i'm going to move you down a little, so i can get better leverage."
    kn "...alright."
    show bfdm bfdm04 with dissolve:
        pos(20,10)

    "you shift korra a little, and she lets you take charge."
    yon "i'm going to start pushing into your back muscles now."
    kn "go for it."
    show bfdm bfdm04 behind bfdm_rub1:
        pos(20,10)
        linear 0.8 pos(0,0)
        linear 0.6 pos(20,10)
        linear 1.0 pos(20,10)
        repeat

    show bfdm_rub1:
        pos(472, 224)

    kn "oh!"

    call pauseInterface
    yon "still feels good?"
    kn "really... really good..."
    kn "wow... i forgot..."
    kn "you're really good at this..."
    "as you feel and caress korra's bare back, that rushing desire to see more of her returns with vengeance."
    "her back is smooth and delicate as you alternate between squeezing pressure and gentle caress."
    kn "mmmmm...."

    call pauseInterface
    kn "ohhh... that's so good..."
    "it's everything you can do not to lean forward and kiss the soft, beautiful skin of her back..."
    hide bfdm_rub1
    show bfdm bfdm04:
        pos(20,10)
    with dissolve
    kn "what's wrong?"
    yon "your..."
    "you try not to swallow as you get the sentence out..."
    yon "...your shirt is in the way."
    "there's a pause as korra makes eye contact with you."
    "there's a moment, just a moment, of total silence."
    kn "...turn around."
    yon "what?"
    kn "i'm going to take off my shirt."
    kn "turn around."
    show image "#000" with dissolve
    pause 1
    show bfdm bfdm06
    hide image "#000" with dissolve
    kn "...there."

    call pauseInterface
    "her uncertainty and willingness make your heart begin to race."
    yon "i'm going to get a better angle."
    "you push your crotch into her behind, and the movement's not subtle."
    show bfdm bfdm05 with Dissolve(0.4)
    kn "mmmmm..."
    "korra relaxes, waits for you to continue."
    yon "okay, here we go again."
    kn "mmkay..."
    show bfdm bfdm05:
        pos(20,10)
        linear 0.8 pos(0,0)
        linear 0.6 pos(20,10)
        linear 1.0 pos(20,10)
        repeat

    show bfdm_rub1:
        pos(472, 224)

    kn "ohhhhh..."

    call pauseInterface
    yon "how's that?"
    kn "so... unhhh... goood..."
    kn "such... relief..."
    yon "your back feels better?"
    kn "very... very... much..."
    kn "mmmmm...."
    kn "i could... sleep..."
    "you press a little harder."
    show bfdm bfdm06
    kn "mghf."
    kn "hey..."
    yon "just working out some knots."
    kn "i wasn't really gonna go... umf... to sleep!"

    call pauseInterface
    hide bfdm_rub1
    hide bfdm
    show bfdm bfdm06
    with dissolve
    kn "hmm?"
    kn "are you done?"
    yon "not just yet."
    "you lean forward and gently, but firmly, grab both her wrists."
    kn "what are you doing..."
    show bfdm bfdm07 with dissolve
    kn "ohhhh...."
    kn "that..."
    show bfdm bfdm08
    kn "ahhhh...."
    kn "oh spirits..."

    call pauseInterface
    kn "yes... yes!"
    kn "oh, my goshhhh!!"
    kn "mmmm..."
    kn "pull... pull me!"
    kn "yes!"
    kn "give... give me what i need..."

    call pauseInterface
    kn "ah... ah..."
    show bfdm bfdm06 with dissolve
    show image "bk4_love/korra/massage/bod_01_sweat.png" with dissolve
    "you let her go, and she collapses onto the bed, breathing heavily."
    kn "that... was... intense..."
    yon "did you enjoy that?"
    kn "I... you took um..."
    kn "it felt great."
    yon "well, i had fun steering you."
    kn "....."
    yon "how's your back?"
    kn "sore, but... in a good way."
    kn "i think you really helped me out."
    kn "thank you so much."
    kn "really."
    kn "for everything."
    yon "pshaw."
    yon "it's cool."
    hide image "bk4_love/korra/massage/bod_01_sweat.png" with dissolve
    kn "would... you stay a little?"
    kn "just lay on the bed with me?"
    yon "yeah. of course."
    kn "...where did you come from?"
    yon "what do you mean?"
    kn "you don't... feel real."
    kn "like... you could disappear at any moment."
    kn "i can't believe i met you here, of all places."
    kn "it feels like...."
    kn "....nevermind."
    kn "it's dumb."
    show bfdm bfdm05 with dissolve
    kn "i'm really tired, but..."
    kn "just stay next to me for a while, okay?"
    yon "i'm not going anywhere."
    "korra sleepily mumbles."
    kn "don't..."
    yon "what?"
    kn "don't go..."
    yon "i'm not going anywhere."
    kn "just... met... you..."
    yon "hm?"
    kn "......"
    "she's passed out."
    "you stay for a little while before tucking her into the bed and heading out."

    return
##### [Jinora] Naked
label gallery_bk4l_jinora_naked:
    scene image "bk4_love/bg/kathouse_day.jpg":
        pos(0,-300)

    show bfdh bfdh12
    with dissolve
    yon "whoa!"
    yon "hey, jinora."
    hide bfdh #have to hid it first or xpos and ypos will get messed up
    show bfdh bfdh10
    with dissolve
    jino "hm?"
    jino "oh, hey [povname]!"
    hide bfdh
    show image "bk4_love/bg/kathouse_day.jpg":
        pos(0,-300)                        
        linear 3.0 pos(0,-580)
    show bfdh bfdh10:
        pos(0,0)
        easeout 3.0 pos(0,-500)
    call bk4l_ctc
    jino "*Ahem*"
    show image "bk4_love/bg/kathouse_day.jpg":
        linear 1.0 pos(0,-300)
    show bfdh bfdh10:
        linear 1.0 pos(0,0)
    jino "Did you get a good look?"
    yon "ahem. um."
    jino "just kidding."
    jino "what are you doing here?"
    yon "just kind of wandering around, to be honest."
    yon "i didn't see you at the training grounds."
    yon "what about you?"
    show bfdh bfdh11 with dissolve
    jino "i was hoping to take a bath and just kinda relax."
    jino "katara is amazing for that."
    yon "yeah, i've seen some of it in session with korra."
    show bfdh bfdh10 with dissolve
    jino "you... attend those, huh?"
    yon "sometimes. i'm still going through therapy myself, and she needs the help."
    yon "Katara asked me to lend a hand with some of it."
    yon "...of course you wouldn't really need that?"                    
    show bfdh bfdh11 with dissolve
    jino "heh, if you want to you can show what you do exactly during those sessions."
    jino "but you'll owe me for the show."
    yon "owe you what, exactly?"
    jino "i'm sure i can come up with something."
    yon "so... i've been wondering..."
    jino "yeah?"
    yon "do those tattoos... go all over?"
    jino "yeah!"
    jino "I got them when I was really young."
    yon "Are you... bragging?"
    jino "I saw you don't have any tattoos, but trust me it's not a pleasant experience."
    jino "They had to be done in such a way that as I get older they don't distort too much."
    jino "you know... because my body was still changing."
    jino "here... let me show you."
    show bfdh bfdh12 with dissolve
    jino "you can see they're all the way down my back."
    yon "i saw that when i came in."
    yon "they run right down into..."
    yon "do they go into your... um..."
    jino "are you staring at my ass there?"
    yon "maybe."
    jino "well, if you {i}really{/i} want to know..."
    jino "I might give you a quick look."
    jino "I mean I've seen you naked, so I guess it would only be fair."                    
    show bfdh bfdh13 with dissolve
    jino "how's that? can you see?"
    call bk4l_ctc
    yon "i can see soooome..."                    
    show bfdc bfdc01:
        xzoom -1
    with dissolve
    k4 "jinora, i'm ready to-"
    show bfdc bfdc08
    k4 "hey!" with vpunch
    k4 "none of that!"
    yon "what?"
    k4 "not with jinora!"
    jino "i'm just showing my tattoos, katara!"
    k4 "you're my granddaughter, you really shouldn't call me by my name."
    k4 "get out of here, you."
    k4 "jinora, let's have that bath."
    yon "but-"
    k4 "scoot!"
    yon "oh, fine..."
    jino "see you later, [povname]!"
    k4 "...."

    return
##### [Asami] Photos
label gallery_bk4l_asami_photos:
    
    scene image "bk4_love/bg/igloo.jpg":
        pos(0,-100)
    show bfdt bfdt08
    with fade

    po3 "alright, fair's fair."
    po3 "here ya go!"
    play sound "audio/win2.mp3"
    "you got a stack of photos!"
    show image "bk4_love/asami/photos/stack.png"
    with dissolve
    call bk4l_ctc
    yon "damn, these are no joke."
    yon "this chick is hot as hell."
    yon "are they all like this?"
    po3 "oh yeah."
    po3 "look through a few."
    yon "don't mind if i do..."
    hide image "bk4_love/asami/photos/stack.png"
    show image "bk4_love/asami/photos/selfie_1.jpg"
    with dissolve
    call bk4l_ctc
    yon "daaaaaaamn."
    hide image "bk4_love/asami/photos/selfie_1.jpg"
    show image "bk4_love/asami/photos/selfie_2.jpg"
    with dissolve
    call bk4l_ctc
    yon "these are awesome."
    hide image "bk4_love/asami/photos/selfie_2.jpg"
    show image "bk4_love/asami/photos/selfie_3.jpg"
    with dissolve
    call bk4l_ctc
    yon "bananas sexy."
    hide image "bk4_love/asami/photos/selfie_3.jpg"
    with dissolve
    po3 "alright, i'm gonna go eat my ice cream."
    hide bfdt with dissolve
    yon "these are definitely saucy."
    yon "i should take them to kya."
    
    return
##### [Opal] Exercise
label gallery_bk4l_opal_exercise:
    
    scene image "bk4_love/bg/your_room.jpg":
        xzoom -1.0 pos(0,-280)


    show bfdq bfdq04:
        pos(0,200)
    call bk4l_ctc
    opal "1 2 3... 10!"
    show bfdq bfdq04:
        linear 3.0 pos(0,40) zoom 0.9
    yon "..."
    yon "......."
    yon "(this is an amazing view!)"
    pause
    show bfdq bfdq05 with Dissolve(1.3)


    opal "hm?"
    opal "[povname]?"
    opal "...."

    hide bfdq
    show bfdq bfdq06 at Move((0, 0), (0, 30), .10, bounce=True)

    yon "What are you doing?"
    opal "they're exercises to stay healthy."
    opal "I... I could show you how to do them..."
    yon "Well, sure why not?"
    show bfdq bfdq08 with dissolve
    opal "Let's start simple."

    show bfdq bfdq02 with Dissolve(1.3)
    opal "you start with this position..."
    pause

    show bfdq bfdq03:
        linear 0.3 pos (30,10)
        linear 1.1 pos (50,10)
        linear 0.6 pos (0,0)
        linear 0.4 pos (0,0)
        repeat

    opal "...then you stretch like this!"
    pause

    show bfdq bfdq08 with dissolve:
        pos(0,0)
    opal "Okay, next exercise."

    show bfdq bfdq00:
        pos(-10,0)
        linear 2.0 pos(20,0)
        linear 0.5 pos(0,0)
        linear 1.5 pos(0,0)
        repeat
    opal "For this you want to get realllll low."
    "you try your best to keep up with the seemingly easy exercises..."
    "but end up trying harder not to fall over than truly mimic opal's movements."
    show bfdq bfdq08 with dissolve:
        pos(0,0)
    opal "Well those are the basics!"
    show bfdq bfdq07 with dissolve
    opal "You did well for someone who is really bad at this!"

    yon "Do you think I can come and do these with you more often?"
    yon "I have very little self discipline and doing them with someone else will keep me on track."
    show bfdq bfdq06
    opal "Oh I don't mind! i still owe you for that... incident..."
    yon "You owe me nothing. The world is the world. Accidents will happen."
    show bfdq bfdq07
    opal "well okay, from now on if you feel like training just come and visit me."
    
    return
##### [Kya] Blowjob
label gallery_bk4l_kya_bj:

    scene image "bk4_love/bg/igloo.jpg":
        pos(0,0)

    show bfde bfde01
    with dissolve
    yon "kya!"
    yon "can you guess what i'm here for?"
    kya "*sigh*"
    kya "are we really doing this?"
    yon "we're definitely doing this."
    kya "guess i'll undress then..."
    hide black
    show black
    with dissolve
    "you take off your clothes as kya does the same."
    hide bfde
    hide black
    show bfda bfda02
    with fade
    kya "alright, let's..."
    kya "....."
    kya "wow."
    kya "that is..."
    show bfda bfda01
    with dissolve
    kya "...wow."
    kya "are they all like that?"
    yon "Like what?"
    kya "um... big."
    show bfda bfda04
    kya "you just... walk around with that?"
    kya "how?"
    yon "to be honest, it's pretty distracting."
    yon "it gets me in all sorts of trouble."
    yon "...pretty much constantly."
    show bfda bfda03
    kya "i bet it does..."
    kya "it's a... a real..."
    kya "...."
    yon "you okay?"
    yon "you trailed off mid-thought."
    kya "i... hmm?"
    yon "you're not horny, are you?"
    yon "for dick?"
    show bfda bfda01
    with dissolve
    kya "what? no.... of course not."
    yon "i thought you were a lesbian?"
    kya "i... shut up."
    kya "i want... i just want to try something."
    kya "i'm going to sit."
    scene
    scene image "bk4_love/bg/igloo.jpg":
        pos(0,-280)


    show bfds bfds00
    with fade
    kya "alright, now that i'm down here..."
    kya "I just want to say..."
    kya "this is all new for me."
    kya "so... let's go slow."
    show bfds bfds06 with dissolve
    kya "okay?"
    yon "sure."
    kya "well, in that case..."
    kya "why don't you come over here?"
    show bfds bfds05 with dissolve
    kya "i guess this is really hapenning."


    show bfds bfds01 with dissolve
    kya "how should we-"

    show bfds bfds02 at Move((0, 0), (-10, 0), .10, bounce=True)
    kya "mm!"
    yon "i'm going to fuck your mouth now."
    kya "hgh?"


    show bfds bfds20
    show bfds_head:
        linear 1.2 pos(-10,0)
        easeout 0.6 pos(0,0)
        repeat

    kya "mmmm..."
    pause
    yon "kya, your mouth feels amazing!"
    kya "hmhm..."
    yon "you're taking it pretty far down, i'm really surprised!"
    pause
    yon "I just... i need..."
    yon "i need more!"

    hide bfds_head
    show bfds bfds02
    with dissolve

    show bfds bfds04
    yon "oh..."
    yon "{size=+10}fuck!" with hpunch
    pause
    kya "mhmm!"
    yon "yes!"
    yon "take it!"
    yon "fuck you! your mouth feels so gooood!!"
    kya "hgnh!"
    yon "what?"
    kya "mmghm!!"
    pause

    hide bfds
    show bfds bfds01
    show image "bk4_love/kya/suck/saliva.png"
    kya "*cough* *cough*"
    yon "sorry, i-"
    kya "that was amazing!"
    yon "you... enjoyed that?"
    kya "absolutely!"
    kya "did you?"
    yon "well, yeah."
    yon "i actually started getting kinda close."
    kya "oh?"
    kya "hmm..."
    kya "can you step back?"
    kya "just for a moment?"
    yon "uh... sure."
    hide image "bk4_love/kya/suck/saliva.png"
    show bfds bfds06
    with dissolve
    kya "great."
    kya "now lay down."
    kya "i want to try a different position."


    scene image "bk4_love/bg/igloo.jpg":
        pos(0,-300)

    show bfds bfds38 with dissolve
    kya "oh yes... i like being in control."
    yon "uh..."
    kya "don't worry, i'm going to take care of you."
    kya "i just want to try something."
    yon "what?"
    kya "well... you were enjoying it, right?"
    yon "yeah, it was awesome."
    kya "i want to see how good i really am."


    show bfds bfds39 with dissolve
    kya "*sshhluuurp*"
    yon "hngh..."

    show bfds bfds40

    show bfds_tits:
        pos(350,180)
        linear 0.5 pos(350,200)
        linear 1.5 pos(350,180)
        repeat
    show bfds_suck4:
        pos(430, 180)
        linear 0.5 pos(430, 100)
        linear 1.5 pos(430, 180)
        repeat
    show bfds_hand:
        pos(500,450)

    kya "*slurp* *mmm*"
    pause
    yon "holy hell... that's..."
    yon "wait, are you... moaning?"
    kya "mmmmmmmm...."
    yon "that's so deep..."
    pause
    hide bfds_suck4
    show bfds_suck3 behind bfds_hand:
        pos(430, 180)
        linear 0.5 pos(430, 100)
        linear 0.5 pos(430, 180)
        repeat
    "kya speeds up, forcing you down her throat with enthusiasm."
    pause
    yon "your moans are vibrating your whole throat!"
    yon "shit, your mouth feels incredible!"
    yon "i'm not gonna last...."
    kya "mmmm...."
    pause
    kya "*slurp* *slurp*"

    menu:
        "cum in mouth":
            yon "fuck, i'm... i'm gonna..."
            scene image "bk4_love/bg/igloo.jpg":
                pos(0,-300)

            show bfds bfds41 with vpunch
            yon "cum!"
            with vpunch
            kya "mmm!!"
            yon "i can feel it filling up your mouth..."
            kya "mmhmmm...."
            with vpunch
            yon "ahh..."
            yon "swallow it."
            kya "........"
            show bfds bfds38
            show image "bk4_love/kya/suck/xspermin.png"
            with dissolve
            kya "ah!"
            kya "wow, that was a lot..."
            kya "and... not bad."
            kya "i thought it'd taste way worse."
            kya "how did i do?"
            yon "you still left kind of a mess..."
            kya "it was a lot!"

        "cum on face":
            yon "sit back, i'm gonna cover your face!"
            scene image "bk4_love/bg/igloo.jpg":
                pos(0,-300)
            show bfds bfds00
            with dissolve

            yon "here it comes! i'm gonna paint your face, kya!"
            kya "i guess-"
            show bfds_spermshot with vpunch
            show image "bk4_love/kya/suck/spermout1.png" with flash
            kya "oh!"
            kya "wow, that-"
            yon "hngh!"
            show bfds_spermshot with vpunch
            show image "bk4_love/kya/suck/spermout2.png" with flash
            kya "....well."
            kya "that was a lot of... mess."
            kya "do you always shoot so much?"
            kya "it's everywhere..."
            yon "usually, yeah."
            yon "i'm like a firehose."
            kya "huh."


    kya "well thank you for a fun night."
    kya "we'll have to see what other kind of... trouble... that cock can get us in."
    kya "goodnight!"

    return
##### [Kora] Kiss
label gallery_bk4l_kora_kiss:

    scene image "bk4_love/bg/koroom_night_1.jpg"
    with fade

    show bfdw bfdw01:
        xpos 600
        linear 2.0 xpos 300
    kn "*hic*"
    kn "helllooo cutie. pie. person."
    yon "...are you okay?"

    show bfdw bfdw01
    kn "*hic* I'm not drunk."
    yon "i didn't say you were."
    yon "but i'm gonna go ahead and guess that you are drunk."
    yon "how did you even get drunk?"
    kn "ittt happens."
    kn "sumimes."
    yon "where'd you get the booze?"
    kn "didjoo know that jinora ish quick?"
    kn "like... shuper quick."
    kn "she stole a thing. a drink. ah alcohol."
    yon "jinora got you drunk?"
    kn "maaayybeee."
    yon "was it on purpose?"
    kn "we were spennin time an' i said i see you some eveningsh and she gave me lotsa alcohol."
    yon "she got you too drunk to hang out with me?"
    yon "hmmm...."
    kn "well we're hangin' now, right??"
    kn "hey! wanna see a trick?"
    yon "... i dunno..."
    show bfdw bfdw02 at Move((300, 0), (300,30), .30, bounce=True)
    pause
    yon "...."
    yon "that is an amazing trick!"

    show bfdw bfdw03 with dissolve
    kn "heehee, that's just the firsh part!"
    kn "thats, thash not even... see!"
    kn "this goes up and then..."


    show bfdw bfdw03:
        linear 1.0 pos(40,0)
    kn "here I go!"

    show bfdw bfdw04:
        xzoom 1.0
        linear 0.2 xpos -20
        linear 0.8 xpos -60
        xzoom -1.0

        linear 0.2 xpos 20
        linear 0.8 xpos 60
        repeat
    call bk4l_ctc
    kn "look at 'em!"
    pause
    kn "just flopping around!"
    kn "they're like... way big but shtill perky sho i can do thish!"
    kn "look at 'em goooo!!"
    pause
    yon "i am not exaggerating when i say i could watch that all night."
    hide bfdw
    show bfdw bfdw03
    kn "aw, you're a shweetie."
    kn "you know... i kinda got drunk on purposh because i-"
    show image "bk4_love/korra/shake/dizzy.png" with dissolve

    kn "...i don't feel so good..."

    hide bfdw
    hide image "bk4_love/korra/shake/dizzy.png"
    show bfdd bfdd01 with vpunch:
        pos(-300,0)
    "korra falls out of wheelchair."
    yon "..."
    yon "yeah, that makes sense."
    "you carry her to bed."

    scene image "bk4_love/bg/korra_bed.jpg" with fade:
        xzoom -1.0 pos(0,0)

    show bfdw bfdw10 at Move((0, 0), (0,30), .30, bounce=True)
    kn "hmn..."
    pause
    yon "maybe i should give you some privacy."
    show bfdw bfdw11 with dissolve
    "you pull down her shirt."

    show bfdw bfdw14
    kn "too warm!!"

    show bfdw bfdw12 at Move((0, 0), (0,30), .30, bounce=True)
    pause
    yon "um... you're in charge."
    yon "and also, i'm not complaining about the view."
    kn "thanks for making thish place less dreary."

    show bfdw bfdw13
    kn "..."
    kn "aren't you going to try and kiss me??"

    menu:
        "maybe when you're less intoxicated?":
            kn "coward... I'm showing you my titties... get a clue."
        "lean forward and...":

            show bfdw bfdw15 with dissolve
            yon "I..."
            pause
            pass

    show text "{size=+5}ZZ{/size}zzzzzz":
        pos(650,180) alpha 0.8
        linear 4.0 pos(500,180) alpha 0.0
        repeat

    show bfdw bfdw10 with hpunch
    kn "*zzzzz*"
    yon "...right."
    yon "Wow, korra is really not into the whole slow approach thing..."
    yon "Me neither, but... she's like basically me in a former life."
    yon "A hot water tribe girl version with very nice round parts, but still..."
    yon "Is this really what I should be doing?"

    show bfdw bfdw11 with dissolve
    yon "sweet dreams, girl me."
    "You kiss her on her cheek and silently leave."
    scene
    scene image "bk4_love/bg/compound_night.jpg"
    show bfdj bfdj02
    with dissolve
    yon "ah!" with vpunch
    yon "opal? why are you outside korra's door?"
    opal "I... I heard some weird noises, I just wanted to make sure everything was alright."
    yon "Don't worry, Korra has gotten her hands on something... strong."
    yon "She'll regret it in the morning, but she's fine."
    opal "oh. okay. good!"
    opal "um..."
    opal "goodnight!"
    hide bfdj with dissolve
    yon "that was kinda weird."

    return
##### [Movers] Nuktuk Outtakes
label gallery_bk4l_ginger_fuck:
    
    scene image "bk4_love/bg/movieset.jpg"
    show bfdu_rollfilmbig
    hide bfdu_rollfilmbig with Dissolve(2.0)

    varrick "Where are the Lights and props! Zhu li!!"
    show image "bk4_love/ginger/fuck/lights.png":
        pos(1000,0)
        linear 2.0 pos(0,0)
    pause(2.0)
    varrick "Okay this is the scene where nuktuk's girlfriend gets drilled!"
    varrick "aaaand action!"
    scene image "bk4_love/bg/drillroom.jpg"
    show bfdv bfdv01
    with dissolve
    "narrator" "oh no! what danger! is there any hope left?!"

    show bfdv bfdv02 with hpunch
    "narrator" "it's nuktuk!"

    show bfdv bfdv03 with dissolve
    "narrator" "with his damsel unable to free herself, nuktuk does the only thing he can!"
    varrick "Cut! Okay drop your pants and get hard, Bolin."


    show bfdv bfdv04

    "bolin" "Wait, what?"
    varrick "This is the drilling scene, so you're going to drill into ginger here!"
    varrick "{size=+20}with your dick!{/size}"
    "bolin" "But... isn't this a children's show?!?"
    varrick "Sure! but we're also shooting a pornmover at the same time!"
    varrick "It's two birds with one stone!"
    varrick "There's people going to do it, so why not us!??"
    varrick "They'd probably call it \"Fukfuk\" or some other idotic name!"
    varrick "With ugly actors who barely look like you guys!!"
    varrick "Bad wigs and no plot to speak of!"
    varrick "We'll just release this as a directors cut, or bloopers or something! I don't care!"
    varrick "Why am I still talking?!?"

    varrick "{size=+20}zhu li!!{/size}" with hpunch
    show image "bk4_love/ginger/fuck/zhuli_1.png":
        pos(300,0)
        linear 1.0 pos(0,0)
    "zhu li" "Yes sir?"
    varrick "do the thing!"
    "zhu li" "Yes sir."

    hide image "bk4_love/ginger/fuck/zhuli_1.png"
    show image "bk4_love/ginger/fuck/zhuli_2.png" at Move((-150, 0), (0,0), .30, bounce=True, repeat = True, delay=1.0)
    pause(1.0)
    show bfdv bfdv08
    with Dissolve(1.0)

    "Zhu li quickly removes the cardboard drill and skirt."
    hide image "bk4_love/ginger/fuck/zhuli_2.png"
    show image "bk4_love/ginger/fuck/zhuli_1.png":
        pos(0,0)
    with dissolve
    "zhu li" "The preparations are done sir."
    varrick "Great! Time for action!"

    show image "bk4_love/ginger/fuck/zhuli_1.png":
        linear 1.0 pos(400,0)
    "bolin" "umm..."
    "bolin" "i don't know if-"
    varrick "Kid. Take a look at ginger."
    varrick "legs in the air and ready to go!"
    varrick "a consummate professional!"
    varrick "now let's consummate this scene!"
    varrick "get over there and be a professional!!"

    show bfdv bfdv06 with Dissolve(1.5)
    "bolin" "Is this... am i doing it right?"
    varrick "you're doing great!"
    varrick "now get in there!"
    show bfdv bfdv07 with Dissolve(1.5)
    "bolin" "okay, but um..."
    "bolin" "Sorry if mess this up... I don't rea-"

    show image "bk4_love/ginger/fuck/ginhead.png"
    "ginger" "Can you hurry this up?!? I have more to do than just this scene today!"
    "bolin" "But..."
    "ginger" "{size=+20}now!!!{/size}"
    hide image "bk4_love/ginger/fuck/ginhead.png"

    show bfdv bfdv09 with hpunch

    varrick "now that's mover magic!!"
    varrick "..."
    varrick "Bolin!! You need to move!"
    varrick "There's no point in making a mover where the actor doesn't move!"
    "bolin" "Sorry"

    show bfdv bfdv10
    show bfdv_fuckani2
    call bk4l_ctc
    varrick "That's it! You're a natural!"
    varrick "Get me a close up of the action!"
    varrick "I want to be able and count her pubes! If she had any!"

    scene bfdv_fuck3
    call bk4l_ctc
    varrick "Excellent! We're going to make a lot of money with this people!"
    varrick "go balls deep, Bolin!"
    varrick "She's not your damn grandmother!"
    scene image "bk4_love/bg/drillroom.jpg"


    show bfdv bfdv10
    show bfdv_fuckani1:


    show bfdv_fuckani1 with hpunch:
        linear 0.2 pos(-10,0)
        linear 0.6 pos(10,0)
        linear 0.2 pos(20,0)
        linear 0.6 pos(25,0)
        repeat
    call bk4l_ctc

    "bolin" "how... are... you... ginger...?"
    "ginger" "you don't have to talk to me to do your job."
    "bolin" "oh..."
    "ginger" "(i can't believe this dork is fucking me...)"
    varrick "Now give her a creampie!"
    "bolin" "but i'm..."
    "bolin" "i'm not there yet..."
    varrick "we're wasting film! give her the nut, bolin!"
    "bolin" "i'm trying!"
    "bolin" "I'm... almost..."
    "bolin" "almost..."
   
    play sound "audio/splurt2.ogg"
    hide bfdv_fuckani1    
    show bfdv bfdv09 with hpunch
    "bolin" "ah!"    
    
    play sound "audio/splurt2.ogg"
    show bfdv bfdv09
    with hpunch
    "bolin" "there's so much!"
    show bfdv bfdv09 with hpunch
    "bolin" "take it all, ginger!"

    show bfdv bfdv06
    show image "bk4_love/ginger/fuck/spermin.png"
    with dissolve
    "bolin" "*pant* *pant*"
    varrick "perfect!"
    show image "bk4_love/ginger/fuck/zhuli_1.png":
        pos(400,400) zoom 0.9
        linear 1.0 pos(160,400)
    "Zhuli" "Actually part of the studio got in the frame, ruining the shot."
    show image "bk4_love/ginger/fuck/zhuli_1.png":
        linear 1.0 pos(400,400)
    varrick "...We're doing it again!!"

    show bfdv bfdv05 with vpunch
    "ginger" "What!?!?"

    return

##### [Captain] Anal
label gallery_bk4l_lotus_anal1:


    scene image "bk4_love/bg/igloo.jpg":
        pos(0,-100)

    show bfdt bfdt07
    po3 "where have you been?!"
    po3 "we had a deal!"
    yon "i spent last night in a cave!"
    po3 "well, don't do it again."
    yon "...."
    yon "okay."
    yon "if i'd known you needed it so badly, i wouldn't have almost frozen to death in the tundra."
    show bfdt bfdt08 with dissolve
    po3 "don't be an ass."
    yon "I'm an ass?"
    yon "What about that logo on your hat... or is it a cap?"
    yon "No matter.. the logo on it looks like a butt."
    po3 "That's not a nice thing to say."
    yon "I'm being very nice by not calling it a clenched anus."
    po3 "...it's a white lotus."
    po3 "It's just a coincidence that it can look like something else."
    po3 "Just like one of those rorshach tests."
    po3 "You should feel bad for seeing something that banal in it."
    yon "are you sure? Also... \"banal\"?  Really?"
    po3 "do you want your reward or not?!"
    po3 "you brought back my guards... for whatever good they are..."
    po3 "and you deserve a little... treat."
    po3 "... oh fuck it, i just want my ass slammed."
    po3 "I haven't had good anal in ages and i'm afraid i've tightened all the way up again."
    yon "i can {i}definitely{/i} help with that."
    po3 "good!"
    po3 "let me just take these pants off..."

    show bfdt bfdt10
    with fade
    po3 "fuck, i'm trembling!"
    po3 "you seeing this?"
    po3 "look at my little legs go."
    yon "um... you sure-"
    po3 "yes!"
    show bfdt bfdt11
    po3 "...oh shit."
    po3 "that is..."
    po3 "go easy at first, it's been a while."
    po3 "i might need a minute to-"
    play sound "audio/spit.mp3"
    show image "bk4_love/lotus/anal/spit.png":
        linear 1.0 alpha 0.0
    pause(1.0)
    show image "bk4_love/lotus/anal/hand.png"
    show bfdt bfdt12
    with dissolve
    po3 "{i}ohhhhhh....{/i}"

    show bfdt bfdt13 with dissolve

    hide image "bk4_love/lotus/anal/hand.png"
    show bfdt_arm
    with dissolve
    po3 "f...fuck."
    po3 "that is... fuck..."
    po3 "spirits, i missed that feeling."
    yon "this is insanely tight!"
    yon "and... your ass is so warm..."
    po3 "You're not exactly sticking a icicle in me either!"
    po3 "I know because I tried that before."
    po3 "Not going to repeat that anytime soon!"
    po3 "Enough sexy talk!"
    po3 "Start digging!"


    hide bfdt
    hide bfdt_arm
    show bfdt bfdt15:
        linear 1.2 pos(10,0)
        linear 0.6 pos(0,0)
        repeat

    show bfdt_legs1:
        linear 1.2 pos(-20,0)
        linear 0.6 pos(0,0)
        repeat
    show bfdt_arm
    call bk4l_ctc
    po3 "*ugh* *ah...*"
    yon "it's like... coming home..."
    yon "It's been some time since I got to stick it in a girls' ass."
    po3 "that's... yes... just like that..."
    po3 "use me... unghh..."
    po3 "yes, just like-"
    yon "i can't take it anymore!"
    yon "Enough of this slow shit!"    

    hide bfdt_legs1
    hide bfdt_arm
    hide bfdt
    show bfdt bfdt18
    po3 "fuck!"
    po3 "yes!"
    
    call bk4l_ctc
    
    po3 "fuck my shithole!"
    po3 "fuck it good!"
    po3 "i'm a good girl!"
    po3 "i'm such a good girl for you daddy!"
    yon "(wha... where did this come from?)"
    po3 "good girls get cum!"
    po3 "they get cum in their ass!"
    po3 "they get their butthole filled with daddy's love liquor!"
    yon "(what the...)"


    menu:
        "cum inside":
            po3 "fill my ass, daddy! dump in your load!"
            show bfdt bfdt17 with hpunch
            yoa "ungh!"
            show bfdt bfdt17 with hpunch
            po3 "yes, daddy!!"
            po3 "ohhh... you're shooting it so deep!!"
            show bfdt bfdt09 with dissolve
            po3 "unnnh..."
            po3 "that was... a huge load, daddy."
            po3 "i'm definitely going to be sore all day."
            po3 "we'll have to do this more... really open me up."

        "cum outside":
            yon "Turn around!"
            hide bfdt
            show bfdt bfdt19
            with dissolve
            po3 "yes, daddy!"

            show bfdt bfdt20 with Dissolve(2.0)
            po3 "drench my little hole!"

            show bfdt_spermshot with hpunch
            show image "bk4_love/lotus/anal/spermout1.png" with flash
            yoa "hng!"
            show bfdt_spermshot with hpunch
            show image "bk4_love/lotus/anal/spermout2.png" with flash
            po3 "daddy!!"
            show bfdt_spermshot with hpunch
            show image "bk4_love/lotus/anal/spermout3.png" with flash
            yoa "get wet, bitch!"

            show bfdt bfdt19 with dissolve
            call bk4l_ctc
            po3 "Have... have I been a good girl?"

            hide image "bk4_love/lotus/anal/spermout1.png"
            hide image "bk4_love/lotus/anal/spermout2.png"
            hide image "bk4_love/lotus/anal/spermout3.png"


    show bfdt bfdt08
    with Dissolve(1.5)
    po3 "well that was fun!"
    po3 "Just like the good old times!"
    yon "soooo... what was that all about?"
    po3 "what?"
    yon "all that... daddy... talk?"
    po3 "i don't know what you're talking about."
    po3 "just sex talk to make things exciting."
    po3 "don't think anything of it."
    po3 "{size=-5}daddy{/size}."
    show bfdt bfdt07 at Move((0, 0), (0, 30), .30, bounce=True)
    po3 "Now get out of here."
    po3 "see you later, punk."
    
    return
#####
#####
#####
#####


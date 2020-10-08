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
#####
###### Declare Characters
label gallery_dCharacters_2Love:
    $ p = Character("lia", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ m = Character("mai", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ t = Character("ty lee", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ oz = Character("Ozai", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ sg = Character("shady guy", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
   
    $ povname = "avatar"
    $ avatar = "player"

    $ y = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_sidebox_neutral.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yg = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_sidebox_grin.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ ya = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_sidebox_angry.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yc = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_sidebox_confused.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yd = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_sidebox_doubtful.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ ys = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_sidebox_smile.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ yn = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_neutral.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yng = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_grin.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yna = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_angry.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ ync = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_confused.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ ynd = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_doubtful.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)
    $ yns = Character("Zuko", color="#000000", show_side_image = Image("zuko/zuko_sidebox/zuko_nude_sidebox_smile.png", xalign = 0, yalign = 0.96), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ a_ = Character('Azula', color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), "azula/a_sidebox_fl_nude.png",
        (0, 0), "azula/a_sidebox_fl_cloth_standard.png",
     ), window_right_padding=280, show_two_window=True, who_xpos=36)

    return
#--

###### Beach Naked
label gallery_beach_naked:
    call gallery_dCharacters_2Love

    show asun asun03 with dissolve
    call pauseInterface
    ys "whoa."
    ys "nice."
    show asun asun03_1 with dissolve
    call pauseInterface
    a "hello, zuko."
    ys "so, uh, what's going on here?"
    t "we were convinced to tan naked!"
    m "no tan lines."
    y "well, i kind of like tan lines..."
    ys "but i have no problem with this."
    yd "i have to say though, aren't you worried about tan lines on your inner thigh?"
    m "...what?"
    yd "with your legs' crossed like that."
    a "hmm... you're right, zuko."
    a "thank you."
    show asun asun04 with dissolve
    call pauseInterface
    "As Azula spreads her legs unashamedly, Ty lee happily follows suit."
    "Mai, looking flustered, surprised, and angry for a split second, hurriedly copies the other two girls."
    "You feel a lot like they're playing \"chicken\"."
    a "*mmmmm...*"
    m "i don't know what i was complaining about...."
    t "right?! this weather is perfect..."
    show asun asun101_1
    show asun_azulablink
    show asun_tyleeblink
    with dissolve
    a "oh, feel that breeze....."
    call pauseInterface
    m "it's so hot, i've got sweat rolling down to my cunt..."
    m "...do you need something, zuko?"
    yd "uhhh...."
    t "yeah, he needs some pussy!"
    t "you two are terrible!"
    a "....."
    m "....."
    m "what is it that you know, ty lee?"
    t "that the weather is nice."
    a "hmm."
    hide asun_azulablink with dissolve
    a "alright, zuko. go on."
    a "you can come back later."
    call pauseInterface

    return
###### Bottle in the Ass
label gallery_truth_or_dare:
    call gallery_dCharacters_2Love

    show azft azft08
    with dissolve

    menu:
        "random spin":
            $ randbottle = renpy.random.randint(1, 3)

            if randbottle == 1:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 60
                pause 5
                call gallery_mai_bottle_butt

            elif randbottle == 2:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 130
                pause 5
                call gallery_ty_bottle_butt

            elif randbottle == 3:
                hide bottle_1
                show bottle_1:
                    xpos 350 ypos 440
                    subpixel True
                    rotate 0
                    linear 1.0 rotate 360
                    rotate 0
                    linear 2.0 rotate 360
                    rotate 0
                    linear 1.0 rotate 200
                pause 5
                call gallery_azula_bottle_butt
            #endif


        "mai":
            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 60
            pause 5
            call gallery_mai_bottle_butt

        "ty lee":
            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 130
            pause 5
            call gallery_ty_bottle_butt

        "azula":
            hide bottle_1
            show bottle_1:
                xpos 350 ypos 440
                subpixel True
                rotate 0
                linear 1.0 rotate 360
                rotate 0
                linear 2.0 rotate 360
                rotate 0
                linear 1.0 rotate 200
            pause 5
            call gallery_azula_bottle_butt

    return
    # --

    label gallery_azula_bottle_butt:
        a "...me?"
        a "oh... goodness..."

        scene black
        show azbb azbb00
        show azbb_azula_getsit
        call pauseInterface
        a_b "....well...."
        show azbb azbb01
        with dissolve
        call pauseInterface
        a_b "here we go..."
        show azbb azbb02 with dissolve
        call pauseInterface
        a_be "ahh...."
        show azbb azbb03 with dissolve
        call pauseInterface
        a_ube "ooohhhh...."
        a_ub "this bottle isn't really..."
        show azbb azbb05 with dissolve
        call pauseInterface
        a_ae "ahhhh.... made for this....."
        t "your pussy is beautiful, though!"
        show azbb azbb100
        call pauseInterface
        a_ube "oohhhhh.... my ass....."
        t "hot!"
        t "you go, azula!"
        m "wow... i'm glad i'm not doing that..."
        a_ab "this was..."
        a_ae "ah!"
        a_ab "your idea..."
        m "faster!"
        show azbb azbb100_1
        a_ae "nnnghhh....."
        a_b "oh!"
        m "it got nice?"
        a_b "it really did."
        a_be "mmmm... ah, that's nice..."
        a_be "smooth...."
        show azbb azbb101
        call pauseInterface
        a_ube "ohhh......"
        t "easy, your highness!"
        a_b "this is great!"
        a_b "mmmm...."
        a_be "alright.... i think i'm done...."
        call pauseInterface

        return
    label gallery_mai_bottle_butt:
        m "...me?"
        m "....that's what i get...."
        scene black
        show azbb azbb00
        show azbb_mai_getsit
        call pauseInterface
        m_l "....well...."
        show azbb azbb01
        with dissolve
        call pauseInterface
        m_l "here we go..."
        show azbb azbb02 with dissolve
        call pauseInterface
        m_l "ahh...."
        show azbb azbb03 with dissolve
        call pauseInterface
        m_l "ooohhhh...."
        m_l "this bottle isn't really..."
        show azbb azbb05 with dissolve
        call pauseInterface
        m_l "ahhhh.... made for this....."
        t "your pussy is beautiful though!"
        show azbb azbb100
        call pauseInterface
        m_l "oohhhhh.... my ass....."
        t "hot!"
        t "you go, mai!"
        a "wow... i am glad i'm not doing that, mai."
        m_l "this was..."
        m_l "ah!"
        m_l "not the best idea..."
        a "faster!"
        show azbb azbb100_1
        m_l "nnnghhh....."
        m_l "oh!"
        a "it got nice?"
        m_l "it really did."
        m_l "mmmm... ah, that's nice..."
        m_l "smooth...."
        show azbb azbb101
        call pauseInterface
        m_l "ohhh......"
        t "easy!"
        m_l "this is great!"
        m_l "mmmm...."
        m_l "alright.... i think i'm done...."
        call pauseInterface

        return
    label gallery_ty_bottle_butt:
        t "...me?"
        t "oh... boy..."
        scene black
        show azbb azbb00
        show azbb_tylee_getsit
        call pauseInterface
        t_l "....well...."
        show azbb azbb01
        with dissolve
        call pauseInterface
        t_l "here we go..."
        show azbb azbb02 with dissolve
        call pauseInterface
        t_l "ahh...."
        show azbb azbb03 with dissolve
        call pauseInterface
        t_l "ooohhhh...."
        t_l "this bottle isn't really..."
        show azbb azbb05 with dissolve
        call pauseInterface
        t_l "ahhhh.... made for this....."
        a "your pussy is beautiful though, ty lee."
        t_l "t-thank you, your highness!"
        show azbb azbb100
        call pauseInterface
        t_l "oohhhhh.... my ass....."
        m "hot!"
        yg "you go, ty lee!"
        m "wow... i am glad i'm not doing that."
        t_l "this was..."
        t_l "ah!"
        t_l "your idea..."
        m "faster!"
        show azbb azbb100_1
        call pauseInterface
        t_l "nnnghhh....."
        t_l "oh!"
        m "it got nice?"
        t_l "it really did."
        t_l "mmmm... ah, that's nice..."
        t_l "smooth...."
        show azbb azbb101
        call pauseInterface
        t_l "ohhh......"
        m "easy, ty lee!"
        t_l "this is great!"
        t_l "mmmm...."
        t_l "alright.... i think i'm done...."
        call pauseInterface
        
        return
###### [Azula] Shower
label gallery_ashower:
    call gallery_dCharacters_2Love

    show azsh azsh112
    show azsh_water
    with dissolve
    call pauseInterface
    yg "damn...."
    call pauseInterface
    show azsh azsh110 with dissolve
    a "*mmmmm...*"
    a "*ah*...*ah*..."
    call pauseInterface
    yg "that's it, sis..."
    a "*mmm*...*ah*...*yes*...."
    show azsh azsh111
    a "zuzu... are you spying again?"
    yc "ah! uh. i..."
    call pauseInterface
    show azsh azsh112 with dissolve
    a "such a pest."
    a "come on in, brother."
    show azsh azsh113 with dissolve
    a "it's not like i've never seen you naked."
    show azsh azsh112 with dissolve
    a "take a seat."
    show azsh azsh110 with dissolve
    a "sit down, you pervert."
    show azsh azsh100
    show azsh_doubt
    with dissolve
    a "poor zuko..."
    a "you don't know women's bodies at all, do you?"
    hide azsh_doubt with dissolve
    a "*mmmmm...*"
    y "you seem to be really enjoying that..."
    show azsh azsh102
    show azsh_lusty
    with dissolve
    a "nonsense, i'm just making sure i'm perfectly clean."
    show azsh_doubt with dissolve
    a "well... let me teach you a bit about our bodies."
    hide azsh_lusty
    show azsh_neutral with dissolve
    a "these are breasts, obviously."
    hide azsh_doubt
    y "why are you... showing me?"
    show azsh_doubt with dissolve
    a "you're clearly struggling. why wouldn't i try to help you?"
    hide azsh_neutral
    a "I'm your sister, after all."
    yd "i guess..."
    hide azsh_doubt with dissolve
    show azsh azsh101 with dissolve
    a "and this is a vagina..."
    show azsh_eyesopen
    show azsh_lusty
    with dissolve
    a "want a closer look?"
    a "just between siblings?"
    menu:
        "show me!":
            show azsh azsh11 with dissolve
            call pauseInterface
            a "why don't you take out your cock?"
            yd "what?"
            a "well... it seems only fair that i get to look at you... while you look at me."
            yd "....."
            show az_mastufbate_1flip at Position (xpos = 0.65, xanchor=0.5, ypos=.5, yanchor=0.5)
            with dissolve
            a "oh... zuzu... that's... large."
            yd "really?"
            a "would you... rub it a bit?"
            a "here, we'll do it... together...."
            show azsh azsh101 with dissolve
            a "like this...."
            show azsh_mastufbate_1flip at Position (xpos = 0.65, xanchor=0.5, ypos=.5, yanchor=0.5)
            hide az_mastufbate_1flip
            a "yes..."
            a "just like that...."
            a "oh! oh, brother!"
            hide azsh_eyesopen
            hide azsh_lusty
            a "brother i'm going to... to cum..."
            show azsh_lusty
            show azsh azsh11
            hide azsh_mastufbate_1flip
            with vshake
            a "ahhh!!"
            a "mmmmmmmmm......"
            show azsh_doubt
            hide azsh_lusty
            with dissolve
            a "why did you stop?"
            a "keep going."
            y "...."
            show azsh_mastufbate_1flip at Position (xpos = 0.65, xanchor=0.5, ypos=.5, yanchor=0.5)
            hide azsh_doubt
            show azsh_eyesopen
            with dissolve
            a "just like that, zuko..."
            y "i'm... i'm..."
            show azsh_lusty with dissolve
            a "yes, brother! let me see it!"
            play sound "audio/splurt3.ogg"
            show a_mindbreak_spermoutside_1 at Position (xpos = 0.5, xanchor=0.5, ypos=.47, yanchor=0.5)
            with flash
            ya "ughh..."
            play sound "audio/splurt2.ogg"
            show a_mindbreak_spermoutside_2 at Position (xpos = 0.5, xanchor=0.5, ypos=.47, yanchor=0.5)
            with flash
            a "oh!"
            play sound "audio/splurt1.ogg"
            hide azsh_mastufbate_1flip
            show a_mindbreak_spermoutside_3 at Position (xpos = 0.5, xanchor=0.5, ypos=.47, yanchor=0.5)
            with flash
            yc "....."
            yc "sorry..."
            a "don't be."
            hide azsh_lusty
            hide azsh_eyesopen
            with dissolve
            "it's exactly what i wanted."
            a "but now i need to rinse off again..."

            menu:
                "lick her clit":
                    show azsh_lick with dissolve
                    y "*slurp*"
                    show azsh_surprised with dissolve
                    a "oh!"
                    hide azsh_eyesopen
                    hide azsh_surprised with dissolve
                    a "mmmmm...."
                    show azsh_lusty with dissolve
                    a "don't stop..."
                    call pauseInterface
                    a "how..."
                    a "how are you so good at this...?"
                    y "*sluurp*"
                    hide azsh_neutral
                    hide azsh_doubt
                    hide azsh_lusty
                    with dissolve
                    a "mmm... hgn..."
                    call pauseInterface
                    show azsh_eyesopen with dissolve
                    a "alright, i think that's enough, don't you?"
                    y "'oh."
                    a "i know, it's delicious. but it's not up to you."
                    hide azsh_lick with dissolve
                    show azsh_lusty with dissolve
                    a "well, you... certainly surprised me."
                    show azsh azsh10 with dissolve
                    a "i hope i won't... catch you in here again."
                    hide azsh_eyesopen
                    hide azsh_lusty with dissolve
                    a "now get out... i really do need to shower."

                "leave":
                    pass
        "nah":
            y "nah, i'm good."
            hide azsh_doubt
            show azsh azsh06
            a "get out."
            
    call pauseInterface
            
    return
label gallery_ashower2:
    call gallery_dCharacters_2Love

    show azsh azsh112
    show azsh_water
    with dissolve
    call pauseInterface
    yg "damn...."
    $ zshower = 3
    call pauseInterface
    show azsh azsh110 with dissolve
    a "*mmmmm...*"
    y "(is she....)"
    a "*ah*...*ah*..."
    yg "(she's masturbating!)"
    call pauseInterface
    yg "that's it, sis... just for me...."
    a "*mmm*...*ah*...*yes*...."
    a "oh, zuko..."
    yd "me?"
    yg "holy-"
    show azsh azsh111
    a "hello, brother."
    yc "ah! uh. i..."
    call pauseInterface
    a "are you spying on me, zuko?"
    show azsh azsh112 with dissolve
    a "such a pest."
    a "you don't have to be shy, zuzu. we're siblings after all."
    show azsh azsh113 with dissolve
    a "it's not like i've never seen you naked."
    yc "you... have?"
    a "of course... we used to take baths together, remember?"
    yc "...not really."
    a "oh right, your memory..."
    show azsh azsh112 with dissolve
    a "well, maybe i can refresh it a little."
    a "take a seat."
    y "oh, i don't know-"
    show azsh azsh110 with dissolve
    a "you wanted a show, i'll give you a show."
    a "sit down, you pervert. i mean, {i}brother."
    show azsh azsh100 with dissolve
    a "so, have you spoken with mai much yet?"
    y "i don't... really know what to say to her."
    a "why not?"
    y "we obviously like each other, but i don't know what to do about it."
    show azsh_doubt with dissolve
    a "oh, poor zuko..."
    a "you really don't understand women."
    hide azsh_doubt with dissolve
    a "*mmmmm...*"
    y "you seem to be really enjoying that..."
    show azsh azsh102
    show azsh_lusty
    with dissolve
    a "nonsense, i'm just making sure i'm perfectly clean."
    show azsh_doubt with dissolve
    a "you should spend some more time with her."
    hide azsh_lusty
    show azsh_neutral with dissolve
    a "trust me, she just wants to see you."
    hide azsh_doubt
    y "why are you being so helpful?"
    show azsh_doubt with dissolve
    a "why wouldn't i help?"
    hide azsh_neutral
    a "I'm your sister, after all."
    yd "i guess..."
    a "i'm almost done here."
    hide azsh_doubt with dissolve
    show azsh azsh101 with dissolve
    a "by the way...."
    show azsh_eyesopen with dissolve
    a "what do you think of my pussy? it's perfect, isn't it?"

    menu:
        "yes, it's perfect":
            y "it's pretty great."
            a "is that so?"
            show azsh_lusty with dissolve
            a "want a closer look?"
            a "just between siblings?"

            menu:
                "show me!":
                    show azsh azsh11 with dissolve
                    call pauseInterface
                    hide azsh_lusty with dissolve
                    a "now i believe it's time for your punishment."
                    y "...you can't punish me."
                    a "father left me in charge."
                    a "so, you get to choose..."
                    a "i think i'll piss on you, help you understand the consequences."
                    a "or... you can give it a good lick."
                    a "your choice."

                    menu:
                        "piss":
                            y "go ahead, i deserve it."
                            a "mmmm... good choice, brother."
                            show azsh_piss
                            hide azsh_eyesopen
                            with vshake
                            a "ahhh...."
                            call pauseInterface
                            yc "*gagghhllagh*"
                            "azula pisses directly into your mouth with surprising accuracy."
                            "her warm, salty spray still manages to drench your face and clothes."
                            a "that's a good brother."
                            a "now i hope i won't catch you back in here."
                            yc "*gagghha*"
                            hide azsh_piss with dissolve
                            show azsh azsh10 with dissolve
                            a "i'm leaving, i'll let you clean up."
                            a "filthy boy."

                        "lick":
                            show azsh_lick with dissolve
                            y "*slurp*"
                            show azsh_surprised with dissolve
                            a "oh!"
                            hide azsh_eyesopen
                            hide azsh_surprised with dissolve
                            a "mmmmm...."
                            show azsh_neutral with dissolve
                            a "keep going brother..."
                            call pauseInterface
                            show azsh_doubt with dissolve
                            a "how..."
                            a "how did you get so good at this?"
                            show azsh_lusty with dissolve
                            y "'eas ah 'achtice"
                            hide azsh_neutral
                            hide azsh_doubt
                            hide azsh_lusty with dissolve
                            a "mmm... don't ruin it with your talking, zuko."
                            call pauseInterface
                            show azsh_eyesopen with dissolve
                            a "alright, i think that's enough, don't you?"
                            y "'oh."
                            a "i know, it's delicious. but it's not up to you."
                            hide azsh_lick with dissolve
                            show azsh_lusty with dissolve
                            a "well, you... certainly surprised me."
                            show azsh azsh10 with dissolve
                            a "i hope you learned your lesson and that i won't... catch you in here again."
                            hide azsh_eyesopen
                            hide azsh_lusty with dissolve
                            a "now i'm leaving."

                "nah":
                    y "nah, i'm good."
                    play sound "audio/slap.mp3"
                    hide azsh_doubt
                    show azsh azsh06
                    with flash
                    a "get out."

        "meh":
            y "it's alright."
            play sound "audio/slap.mp3"
            hide azsh_doubt
            show azsh azsh06
            with flash
            a "get out."


    return
###### [Azula] Handjob
label gallery_za_handjob:
    call gallery_dCharacters_2Love

    scene bg_a_armory
    show ahj7_1
    with dissolve
    a "ah, yes... this magnificent cock. truly fit for a queen."
    a "i... i almost can't stand to wait."
    scene black with dissolve
    "azula pulls down your pants and settles between your legs."
    scene bg_a_armory
    show azhj azhj13
    with dissolve
    a "let's make you cum."
    show azhj azhj01 with dissolve
    a "now, pull it out!"
    show azhj azhj03 with dissolve
    a "my, my."
    a "i never get tired of seeing your cock, brother."
    a "what do you think... should i give you a little tug?"
    show azhj azhj04 with dissolve
    a "well, that didn't take much encouragement."
    a "have you been hoping i'd feel up your cock again?"
    show azhj azhj05 with Dissolve(0.35)
    a "i can't believe you're such a pervert, zuko."
    a "i didn't expect it."
    show azhj azhj08 with Dissolve(0.35)
    a "i almost can't get my hand around it."
    a "is this what you want, you sicko?"
    a "for me to grip your big, handsome cock?"
    show azhj azhj09 with Dissolve(0.35)
    a "i can't believe you."
    show azhj azhj101 with Dissolve(0.35)
    yc "ungh..."
    show azhj azhj105_1 with Dissolve(0.35)
    a "mmm..."
    a "what's wrong, brother?"
    show azhj azhj100 with Dissolve(0.35)
    ya "fuck!"
    a "aw, you're cute when you watch your little sister tug on your cock."
    call pauseInterface
    yc "ngh..."
    yc "you're jacking me off... in mai's shop... i still can't believe this is happening..."
    show azhj_blink with Dissolve(0.35)
    a "hm."
    a "you can't?"
    a "why not?"
    y "well, because, you're my sister."
    show azhj_blush
    hide azhj_blink
    with dissolve
    a "...do you think i'm beautiful?"

    y "i think you're gorgeous."
    show azhj_blink with dissolve
    a "oh."
    a "i've always... been fascinated with you, zuzu."
    a "I know i can be difficult."
    show azhj_lusty with dissolve
    a "but the truth is, these years you've been away..."
    a "i swore that, well..."
    a "if you came back..."
    show azhj_eyesoncock
    hide azhj_blink
    hide azhj_lusty
    with dissolve
    a "i'd do something about it."
    call pauseInterface

    a "...they're all too scared to get close to me."
    hide azhj_eyesoncock
    with Dissolve(0.35)
    a "you're scared too, i know it."
    hide azhj_blush
    show azhj_angry
    show azhj_blush
    with Dissolve(0.35)
    a "and if i have to rule with fear, then i will."
    a "i don't have to be gentle."
    show azhj azhj21
    hide azhj_angry
    hide azhj_blush
    with Dissolve(0.35)
    a "here."
    play sound "audio/fleshslap.mp3"
    show azhj azhj17 with vshake
    a "see?"
    a "did you like that?"
    a "here-"
    show azhj azhj105_2
    a "ah... ah... mm..."
    call pauseInterface
    a "do... ah... you like... this?"
    a "slapping... ah... your cock on my... ah... face?"
    a "your little... ah... sister's face?"
    show azhj azhj17 with Dissolve(0.35)
    a "want me to rub it on my face, brother?"
    show azhj azhj105_3
    a "mmmm...."
    a "how is it?"
    yc "ngh... your face is really soft..."
    a "i know."
    yc "ah..."
    a "your cock is so hot on my face."
    a "see, i can be gentle, too."
    yc "hngh..."
    a "oh no brother, what's wrong? you're not going to make a mess, are you?"
    show azhj azhj103 with dissolve
    "azula leans in close to you. you can feel her breath in your ear as her lips lightly brush against you."
    "her tongue flickers in for a moment as she speaks."
    show azhj azhj105
    a "cum for me, brother. make a fucking mess. i want it all over my hands, understand?"
    a "i want to see what you can do. i want to smell my brother's cum on my hands."
    a "do it."
    a "give me that fucking sperm, brother!"
    "azula gives your earlobe one long suck, her soft, succulent lips slowly tugging at your ear as her tongue briefly runs against you."
    show azhj azhj106
    "Her lips pull off with a small \"pop\" and she begins jacking your cock ferociously, forcing the cum out almost against your wishes."
    a "you gonna cum, brother?"
    a "am i making you cum?"
    a "are you gonna make a big, sticky mess that mai has to clean up?"
    show azhj azhj107 with Dissolve(0.3)
    a "is she gonna have to clean up all the cum?"
    a "cum for me. cum for me."
    show azhj_angry with Dissolve(0.3)
    a "cumformecumformecumforme-"
    yc "hgh-"
    show azhj azhj05
    show azhj_surprised
    hide azhj_angry
    show azhj_sperm_1
    play sound "audio/splurt3.ogg"
    with flash
    a "oh!"
    hide azhj_surprised
    hide azhj_sperm_1
    show azhj_lusty
    show azhj_eyesoncock
    show azhj_sperm_2
    play sound "audio/splurt2.ogg"
    with flash
    a "ahh...."
    a "yes..."
    hide azhj_lusty
    hide azhj_eyesoncock
    hide azhj_sperm_2
    show azhj_blush
    show azhj_sperm_3
    play sound "audio/splurt1.ogg"
    with flash
    a "get it all out, zuko..."
    yc "ungh..."
    show azhj_blink
    show azhj_sperm_1 at Position (xpos = 0.32, xanchor=0.5, ypos=0.53, yanchor=0.5)
    show azhj_sperm_2 at Position (xpos = 0.38, xanchor=0.5, ypos=0.45, yanchor=0.5)
    play sound "audio/splurt2.ogg"
    with flash
    a "mmmm...."
    hide azhj_blink with Dissolve(0.25)
    a "feel better?"
    y "fuck. yes."
    a "did i get it all out?"
    yc "unghh..."
    show azhj_lusty
    show azhj_blink
    hide azhj_sperm_1
    hide azhj_sperm_2
    show azhj_sperm_1 at Position (xpos = 0.32, xanchor=0.5, ypos=0.53, yanchor=0.5)
    show azhj_sperm_2 at Position (xpos = 0.38, xanchor=0.5, ypos=0.45, yanchor=0.5)
    with Dissolve(0.25)
    a "good."
    a "now..."
    hide azhj_lusty
    hide azhj_blush
    show azhj_blush at Position (xpos = 0.54, xanchor=0.5, ypos=0.48, yanchor=0.5)
    hide azhj_blink
    show azhj azhj17

    hide azhj_sperm_1
    hide azhj_sperm_2
    show azhj_sperm_1 at Position (xpos = 0.36, xanchor=0.5, ypos=0.498, yanchor=0.5)
    show azhj_sperm_2 at Position (xpos = 0.43, xanchor=0.5, ypos=0.435, yanchor=0.5)

    with Dissolve(0.25)
    a "that was fun."
    a "now, put your clothes on."
    a "i need to clean my hands."
    show azhj azhj15
    hide azhj_sperm_3
    show azhj_sperm_3 at Position (xpos = 0.57, xanchor=0.5, ypos=1.02, yanchor=0.5)
    with Dissolve(0.25)
    y "and your face."
    a "oh, is there something on my face, zuzu?"
    y "yeah, my cum."
    a "on my face."
    y "...yes."
    a "then why ever would i wash it off?"
    scene black
    scene bg_a_armory
    show afnj
    with dissolve
    a "go ahead, zuko. i'll meet you in the palace later."

    return
###### [Azula] Masturbate
label gallery_zfpalace_night20:
    call gallery_dCharacters_2Love

    $ rand_azula_sleep = 0
    $ tempContinue = True

    while tempContinue:
        menu:
            "Clothed":
                scene black
                show azsl azsl02 with dissolve
                $ rand_azula_sleep = 2
            "Showing Tits":
                scene black
                show azsl azsl03 with dissolve
                $ rand_azula_sleep = 3
            "Showing Pussy":
                scene black
                show azsl azsl04 with dissolve
                $ rand_azula_sleep = 4
            "Showing Both":
                scene black
                show azsl azsl05 with dissolve
                $ rand_azula_sleep = 5
            "Naked":
                scene black
                show azsl azsl01 with dissolve
                $ rand_azula_sleep = 1
            "Continue":
                $ tempContinue = False

        call pauseInterface

    menu:
        "lay down":
            call pauseInterface
            show azsl_eyeshalfopen with dissolve
            a "*sleepily* hey, brother...."
            a "don't be shy, this is your bed now, too."

            menu:
                "cuddle":
                    "you undress and lay next to her."
                    show azsl_eyesopen
                    hide azsl_eyeshalfopen
                    with dissolve
                    "azula runs her fingers down your chest, watching your face with a hungry intensity."
                    "her fingers continue to run down your naked body, until she reaches your cock...."
                    with ushake
                    "....which she grasps and squeezes, causing you to gasp."
                    show azsl_eyeshalfopen
                    hide azsl_eyesopen
                    with dissolve
                    a "mmmm.... i love your cock."
                    a "will you......"
                    y "what?"
                    a "....will you just hold me?"
                    ys "of course."
                    hide azsl_eyeshalfopen with dissolve

                    if rand_azula_sleep == 1:
                        show azsl azsl11 with dissolve

                    if rand_azula_sleep == 2:
                        show azsl azsl12 with dissolve

                    if rand_azula_sleep == 3:
                        show azsl azsl14 with dissolve

                    if rand_azula_sleep == 4:
                        show azsl azsl13 with dissolve

                    if rand_azula_sleep == 5:
                        show azsl azsl15 with dissolve

                    "azula rolls over, and you put your arms around her."
                    a "*mmmm....*"
                    "she moans and presses backwards against you as you settle your member between her cheeks."
                    "you can feel the vibration from her moan against your chest as you grip and press your fingers into her soft, accepting breasts."
                    "you sleep soundly."

                "do you believe in love?":
                    y "do you believe in life after love?"
                    a "....what?"
                    y "i meant... do you think love is real, or is it just pheromones, or-"
                    a "....i don't know."
                    show azsl_eyesopen
                    hide azsl_eyeshalfopen
                    with dissolve
                    a "but i want to be with you."
                    a "and you make me feel safe. and i want to see you happy."
                    show azsl_eyeshalfopen
                    hide azsl_eyesopen
                    with dissolve
                    a "and i don't care what that's called."
                    hide azsl_eyeshalfopen with dissolve
                    a "now, can we sleep?"

                    if rand_azula_sleep == 1:
                        show azsl azsl11 with dissolve

                    if rand_azula_sleep == 2:
                        show azsl azsl12 with dissolve

                    if rand_azula_sleep == 3:
                        show azsl azsl14 with dissolve

                    if rand_azula_sleep == 4:
                        show azsl azsl13 with dissolve

                    if rand_azula_sleep == 5:
                        show azsl azsl15 with dissolve

                    "azula rolls over, and pushes backwards against you."
                    "you sleep soundly."

        "masturbate":
            show azsl_masturbate_1 with Dissolve(0.3)

            menu:
                "be quiet":
                    y "careful...."
                    show azsl azsl06 with dissolve
                    call pauseInterface
                    y "god damn, those are some perfect tits."
                    show azsl_masturbate_1 with Dissolve(0.3)
                    y "that's it, sis."
                    y "if you want to be slathered in cum, stay right there."

                    menu:
                        "cum on tits":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            call pauseInterface
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            show azsl azsl11
                            with dissolve
                            a "*mmghn...*"
                            ys "ahh... i needed that."
                            scene black with dissolve
                            "you sleep next to azula."
                            show azsl azsl01
                            show azsl_spermtits_3
                            with dissolve

                        "cum on pussy":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            call pauseInterface
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3
                            show azsl azsl11
                            with dissolve
                            a "*mmghn...*"
                            ys "ahh... i needed that."
                            scene black with dissolve
                            "you sleep next to azula."
                            show azsl azsl01
                            show azsl_spermvag_3
                            with dissolve

                        "cum on both":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            call pauseInterface
                            ya "(not done yet!)"
                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "(ngh!)"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "(fuck!)"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            call pauseInterface
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            show azsl azsl11
                            with dissolve
                            a "*mmghn...*"
                            ys "ahh... i needed that."
                            scene black with dissolve
                            "you sleep next to azula."
                            show azsl azsl01
                            show azsl_spermtits_3
                            show azsl_spermvag_3
                            with dissolve

                    a "hhmmmm....."
                    show azsl_eyeshalfopen with dissolve
                    a "good morning, broth-"
                    a "......"
                    a "what the..."
                    show azsl_eyesopen
                    hide azsl_eyeshalfopen
                    with dissolve
                    a "did you ejaculate on me during the night, zuzu?"
                    y "...maybe."
                    a "...."
                    a "................"
                    a "well did you have fun at least?"
                    y "oh yeah."
                    show azsl_eyeshalfopen
                    hide azsl_eyes_open
                    with dissolve
                    a "very well. at least wake me next time."
                    a "now i need a shower. you've left me sticky."
                    a "get out."

                "make noise":
                    y "*pant* *pant*"
                    y "that's it..."
                    y "i'm gonna..."
                    show azsl_eyeshalfopen with dissolve
                    y "take th-"
                    y "oh. sorry."
                    show azsl_eyesopen with dissolve
                    a "sigh... go ahead."
                    hide azsl_eyesopen
                    with dissolve
                    a "here."
                    show azsl azsl06 with dissolve
                    a "does this help?"
                    y "fffuuuu...."
                    a "yes, i know."
                    a "go ahead, so i can get some rest."
                    y "well, since you asked..."
                    a "....."
                    y "ngh...."

                    menu:
                        "cum on tits":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            y "there..."
                            a "mmmm... warm."
                            a "all done?"
                            a "good."
                            a "now maybe i can get some sleep."
                            call pauseInterface
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3

                        "cum on pussy":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            y "there..."
                            a "mmmm... warm."
                            a "all done?"
                            a "good."
                            a "now maybe i can get some sleep."
                            call pauseInterface
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3

                        "cum on both":
                            play sound "audio/splurt2.ogg"
                            show azsl_spermtits_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermtits_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermtits_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            ya "not done yet!"
                            play sound "audio/splurt2.ogg"
                            show azsl_spermvag_1
                            with flash
                            y "ngh!"
                            play sound "audio/splurt1.ogg"
                            show azsl_spermvag_2
                            with flash
                            y "fuck!"
                            play sound "audio/splurt3.ogg"
                            show azsl_spermvag_3
                            with flash
                            hide azsl_masturbate_1 with dissolve
                            y "there..."
                            y "there..."
                            a "mmmm... warm."
                            a "all done?"
                            a "good."
                            a "now maybe i can get some sleep."
                            call pauseInterface
                            hide azsl_spermtits_1
                            hide azsl_spermtits_2
                            hide azsl_spermtits_3
                            hide azsl_spermvag_1
                            hide azsl_spermvag_2
                            hide azsl_spermvag_3

                    hide azsl_eyesopen
                    hide azsl_eyeshalfopen
                    show azsl azsl11
                    with dissolve
                    a "get into the bed, idiot."
                    a "and get that blanket."

        "fuck her tits":
            show azsf azsf01 with dissolve
            y "time to take her up on her offer."
            show azsf azsf02 with dissolve
            "you straddle azula's chest and lay your cock on her tits."
            y "yeah, that's nice."
            y "time to bury my cock in your fat tits, sister."
            show azsf azsf03 with Dissolve(0.35)
            yc "oh, fuck..."
            show azsf azsf06 with Dissolve(0.35)
            a "*hsfas...*"
            "azula stretches out a little in her sleep."
            yd "...."
            yg "well, let's get to work."
            show azsf azsf100
            call pauseInterface
            yc "nghh..."
            y "that's it...."
            ys "sshhh... just stay asleep..."
            yg "now, that's some good squish."

            menu:
                "grab her boobs":
                    show azsf azsf12 with dissolve
                    yg "let's pick things up a little..."
                    show azsf azsf101
                    call pauseInterface
                    a "*mmmffshgh.....*"
                    ys "yeah... that's it..."
                    yg "come on, azula... make me cum..."
                    show azsf_sidehead with dissolve
                    show azsf azsf102
                    ya "make me cum... make me cum..."
                    call pauseInterface
                    ya "fuck... fuck... fuck..."
                    show azsf azsf103
                    ya "faster... faster..."
                    call pauseInterface
                    ya "you're gonna make me..."
                    ya "hhngh..."
                    show azsf azsf104
                    call pauseInterface
                    ya "come on! come on!"
                    call pauseInterface
                    show azsf azsf105
                    call pauseInterface
                    ya "ahhh!!"
                    ya "i'm cumming, sis!"
                    ya "take it!"
                    hide azsf_sidehead
                    with dissolve
                    a "*hghngh...?...*"
                    ya "ngh!"
                    play sound "audio/splurt2.ogg"
                    show azsf azsf15

                "stay like this":
                    yg "let's pick things up a little..."
                    show azsf azsf106
                    call pauseInterface
                    a "*mmmffshgh.....*"
                    ys "yeah... that's it..."
                    yg "come on, azula... make me cum..."
                    show azsf_sidehead with dissolve
                    show azsf azsf107
                    ya "make me cum... make me cum..."
                    call pauseInterface
                    ya "fuck... fuck... fuck..."
                    show azsf azsf108
                    ya "faster... faster..."
                    call pauseInterface
                    ya "you're gonna make me..."
                    ya "hhngh..."
                    show azsf azsf109
                    call pauseInterface
                    ya "come on! come on!"
                    call pauseInterface
                    show azsf azsf110
                    call pauseInterface
                    ya "ahhh!!"
                    ya "i'm cumming, sis!"
                    ya "take it!"
                    hide azsf_sidehead
                    with dissolve
                    a "*hghngh...?...*"
                    ya "ngh!"
                    play sound "audio/splurt2.ogg"
                    show azsf azsf09

            show azsf_sperm1
            with flash
            a "*nnghnm...*"
            play sound "audio/splurt2.ogg"
            hide azsf_sperm1
            show azsf_sperm2
            with flash
            yc "nngh..."
            yc "fuck, i think..."
            ya "ungh!"
            play sound "audio/splurt2.ogg"
            hide azsf_sperm2
            show azsf_sperm3
            with flash
            y "damn."
            show azsf azsf00
            show azsf_sperm1:
                xpos -200 ypos 100
            with dissolve
            call pauseInterface
            yg "that's a good look for you, sis."
            show azsf_eyesopen
            show azsf_mouthopen
            hide azsf_sperm3
            show azsf_sperm3
            with dissolve
            a "mmmm.... thank you, love."
            call pauseInterface

            menu:
                "cover her with a blanket":
                    hide azsf_eyeopen
                    show azsf_cover
                    with dissolve
                    a "thank... you..."
                    "you lay next to azula and sleep soundly."

                "no blanket":
                    "you lay next to azula and sleep soundly."

    return
###### [Azula] Fuck her Tits
label gallery_afucktits:
    call gallery_dCharacters_2Love

    show azsf azsf01 with dissolve
    y "time to take her up on her offer."
    show azsf azsf02 with dissolve
    "you straddle azula's chest and lay your cock on her tits."
    y "yeah, that's nice."
    y "time to bury my cock in your fat tits, sister."
    show azsf azsf03 with Dissolve(0.35)
    yc "oh, fuck..."
    show azsf azsf06 with Dissolve(0.35)
    a "*hsfas...*"
    "azula stretches out a little in her sleep."
    yd "...."
    yg "well, let's get to work."
    show azsf azsf100
    call pauseInterface
    yc "nghh..."
    y "that's it...."
    ys "sshhh... just stay asleep..."
    yg "now, that's some good squish."
    menu:
        "grab her boobs":
            show azsf azsf12 with dissolve
            yg "let's pick things up a little..."
            show azsf azsf101
            call pauseInterface
            a "*mmmffshgh.....*"
            ys "yeah... that's it..."
            yg "come on, azula... make me cum..."
            show azsf_sidehead with dissolve
            show azsf azsf102
            ya "make me cum... make me cum..."
            call pauseInterface
            ya "fuck... fuck... fuck..."
            show azsf azsf103
            ya "faster... faster..."
            call pauseInterface
            ya "you're gonna make me..."
            ya "hhngh..."
            show azsf azsf104
            call pauseInterface
            ya "come on! come on!"
            call pauseInterface
            show azsf azsf105
            call pauseInterface
            ya "ahhh!!"
            ya "i'm cumming, sis!"
            ya "take it!"
            hide azsf_sidehead
            with dissolve
            a "*hghngh...?...*"
            ya "ngh!"
            play sound "audio/splurt2.ogg"
            show azsf azsf15
            show azsf_sperm1
            with flash
            a "*nnghnm...*"
            play sound "audio/splurt2.ogg"
            hide azsf_sperm1
            show azsf_sperm2
            with flash
            yc "nngh..."
            yc "fuck, i think..."
            ya "ungh!"
            play sound "audio/splurt2.ogg"
            hide azsf_sperm2
            show azsf_sperm3
            with flash
            y "damn."
            show azsf azsf00
            show azsf_sperm1:
                xpos -200 ypos 100
            with dissolve
            call pauseInterface
            yg "that's a good look for you, sis."
            show azsf_mouthopen
            hide azsf_sperm3
            show azsf_sperm3
            with dissolve
            a "*hnmmfg...*"
            show azsf_sidehead
            hide azsf_sperm3
            show azsf_sperm2:
                xpos 30 ypos -80
            with dissolve
            call pauseInterface
            menu:
                "cover her with a blanket":
                    show azsf_cover with dissolve
                    yg "sleep well...."
                    "you head to your room and sleep."

                "leave":
                    yg "sleep well...."
                    "you head to your room and sleep."
                    
        "stay like this":
            yg "let's pick things up a little..."
            show azsf azsf106
            call pauseInterface
            a "*mmmffshgh.....*"
            ys "yeah... that's it..."
            yg "come on, azula... make me cum..."
            show azsf_sidehead with dissolve
            show azsf azsf107
            ya "make me cum... make me cum..."
            call pauseInterface
            ya "fuck... fuck... fuck..."
            show azsf azsf108
            ya "faster... faster..."
            call pauseInterface
            ya "you're gonna make me..."
            ya "hhngh..."
            show azsf azsf109
            call pauseInterface
            ya "come on! come on!"
            call pauseInterface
            show azsf azsf110
            call pauseInterface
            ya "ahhh!!"
            ya "i'm cumming, sis!"
            ya "take it!"
            hide azsf_sidehead
            with dissolve
            a "*hghngh...?...*"
            ya "ngh!"
            play sound "audio/splurt2.ogg"
            show azsf azsf09
            show azsf_sperm1
            with flash
            a "*nnghnm...*"
            play sound "audio/splurt2.ogg"
            hide azsf_sperm1
            show azsf_sperm2
            with flash
            yc "nngh..."
            yc "fuck, i think..."
            ya "ungh!"
            play sound "audio/splurt2.ogg"
            hide azsf_sperm2
            show azsf_sperm3
            with flash
            y "damn."
            show azsf azsf00
            show azsf_sperm1:
                xpos -200 ypos 100
            with dissolve
            call pauseInterface
            yg "that's a good look for you, sis."
            show azsf_mouthopen
            hide azsf_sperm3
            show azsf_sperm3
            with dissolve
            a "*hnmmfg...*"
            show azsf_sidehead
            hide azsf_sperm3
            show azsf_sperm2:
                xpos 30 ypos -80
            with dissolve
            call pauseInterface
            menu:
                "cover her with a blanket":
                    show azsf_cover with dissolve
                    yg "sleep well...."
                    "you head to your room and sleep."

                "leave":
                    yg "sleep well...."
                    "you head to your room and sleep."

    return
###### [Azula] Piss/Lick
label gallery_zazula_piss:
    call gallery_dCharacters_2Love

    scene bg_a_ceiling with dissolve
    show apiss 1 with dissolve
    "you lay down as azula stands over you."
    call pauseInterface
    a "yes... i'm... so excited, brother."
    show apiss 2 with dissolve
    call pauseInterface
    a_b "i want your tongue on me..."
    show apiss 3 with dissolve
    a_b "i'm going to rub this juicy clit on your face."
    show apiss 2 with dissolve
    a_b "i've also heard about... pissing... from ty lee, if you want that."
    a_b "that would be okay too, if you wanted it."
    a_b "i just... i want to own your face. i want it to be mine."

    menu:
        "piss on me, sis!":
            call gallery_zapiss_cont

        "start licking her":
            call gallery_zapiss_dist
            
    return

    label gallery_zapiss_cont:
        a_b "okay, i'm going to piss on you."
        a_b "i want see my piss flowing into your mouth."
        a_b "you're going to love this."
        a_be "i just know it."
        a_ae "...."
        show apiss an
        "a stream shoots out from azula's lips and immediately drenches your face."
        a_be "ahhhh....."
        call pauseInterface

        menu:
            "struggle":
                a_ab "don't turn your head!"
                "trapped between azula's thighs, there's nothing you can do but accept her warm piss on your face."
                a_b "open your mouth, {i}lover{/i}...."
                show apiss an1 with dissolve
                a_ab "open your fucking mouth and drink your sister's warm salty piss."
                "you open your mouth, and azula's piss flows into it..."
                "filling your mouth until it overflows down your neck."
                a_b "now, swallow some you dirty pervert. swallow my fucking piss."
                show apiss an2 with dissolve
                a_be "ah....."

                menu:
                    "let her finish":
                        a_be "almost...."
                        a_ae "......"
                        show apiss 2 with dissolve
                        a_b "there."
                        a_b "that was nice."
                        a_b "wasn't it?"
                        a_be "nevermind, you can't talk with that mouthful of piss, can you?"
                        a_b "swallow it all."
                        y "..."
                        a_ab "all of it. and thank me."
                        "your mouth is too filled with azula's hot piss to speak, and you end up gurgling."
                        y "*gulp*"
                        a_b "ahh... good boy."
                        show apiss 1 with dissolve
                        a_b "i'm going to sleep now."
                        a_b "mmmm... you smell... strong."
                        a_be "i like it."
                        a_ab "now get out!"
                        a_be "i'm..."
                        hide apiss 1 with dissolve
                        "azula lays down on the floor where she is and immediately passes out."

                    "lick her":
                        show apiss an3 with dissolve
                        a_sb "*ah*!"
                        call pauseInterface
                        show apiss an6 with dissolve
                        a_be "aaahhh..."
                        a_be "mmmmmmmmmmmmm....."
                        call pauseInterface
                        show apiss an3 with dissolve
                        a_ab "you made me stop pissing, zuzu."
                        a_ab "now, i said swallow my piss."
                        a_be "and don't you dare stop licking..."
                        show apiss an7 with dissolve
                        call pauseInterface
                        a_b "that's it..."
                        show apiss an5 with dissolve
                        call pauseInterface
                        a_be "almost...."
                        a_ae "......"
                        show apiss 2 with dissolve
                        a_b "there."
                        a_b "that was nice."
                        a_b "wasn't it?"
                        a_be "nevermind, you can't talk with that mouthful of piss, can you?"
                        a_b "swallow it all."
                        y "..."
                        a_ab "all of it. and thank me."
                        "your mouth is too filled with azula's hot piss to speak, and you end up gurgling."
                        y "*gulp*"
                        a_b "ahh... good boy."
                        show apiss 1 with dissolve
                        a_b "i'm going to sleep now."
                        a_b "mmmm... you smell... strong."
                        a_be "i like it."
                        a_ab "now get out!"
                        a_be "i'm..."
                        hide apiss 1 with dissolve
                        "azula lays down on the floor where she is and immediately passes out."

            "take it":
                a_be "that's it..."
                a_b "good little peasant."
                show apiss an1
                a_be "aaahhh... take azula's piss now..."
                a_b "you like it, don't you? that's it, drink it up..."
                a_b "open your mouth, {i}lover{/i}...."
                show apiss an1 with dissolve
                a_ab "open your fucking mouth and drink your sister's warm salty piss."
                "you open your mouth, and azula's piss flows into it..."
                "filling your mouth until it overflows down your neck."
                a_b "now, swallow some you dirty pervert. swallow my fucking piss."
                show apiss an2 with dissolve
                a_be "ah....."

                menu:
                    "let her finish":
                        a_be "almost...."
                        a_ae "......"
                        show apiss 2 with dissolve
                        a_b "there."
                        a_b "that was nice."
                        a_b "wasn't it?"
                        a_be "nevermind, don't talk, you'll ruin it."
                        a_b "you can't talk with that mouthful of piss anyway, can you?"
                        a_b "swallow it all."
                        y "..."
                        a_ab "all of it. and thank me."
                        "your mouth is too filled with azula's hot piss to speak, and you end up gurgling."
                        y "*gulp*"
                        a_b "ahh... good boy."
                        show apiss 1 with dissolve
                        a_b "i'm going to sleep now."
                        a_b "mmmm... you smell... strong."
                        a_be "i like it."
                        a_ab "now get out!"
                        a_be "i'm..."
                        hide apiss 1 with dissolve
                        "azula lays down on the floor where she is and immediately passes out."

                    "lick her":
                        show apiss an3 with dissolve
                        a_sb "*ah*!"
                        call pauseInterface
                        show apiss an6 with dissolve
                        a_be "aaahhh..."
                        a_be "mmmmmmmmmmmmm....."
                        call pauseInterface
                        show apiss an3 with dissolve
                        a_ab "you made me stop pissing, you pervert."
                        a_ab "now, i said swallow my piss."
                        a_be "and don't you dare stop licking..."
                        show apiss an7 with dissolve
                        call pauseInterface
                        a_b "that's it..."
                        show apiss an5 with dissolve
                        call pauseInterface
                        a_be "almost...."
                        a_ae "......"
                        show apiss 2 with dissolve
                        a_b "there."
                        a_b "that was nice."
                        a_b "wasn't it?"
                        a_be "nevermind, you can't talk with that mouthful of piss, can you?"
                        a_b "swallow it all."
                        y "..."
                        a_ab "all of it. and thank me."
                        "your mouth is too filled with azula's hot piss to speak, and you end up gurgling."
                        y "*gulp*"
                        a_b "ahh... good boy."
                        show apiss 1 with dissolve
                        a_b "i'm going to sleep now."
                        a_b "mmmm... you smell... strong."
                        a_be "i like it."
                        a_ab "now get out!"
                        a_be "i'm..."
                        hide apiss 1 with dissolve
                        "azula lays down on the floor where she is and immediately passes out."

        return
    label gallery_zapiss_dist:
        show apiss an4 with dissolve
        a_sb "*ah*!"
        call pauseInterface
        show apiss an6 with dissolve
        a_be "aaahhh..."
        "azula spreads her plush lips, allowing you deeper access."
        a_be "mmmmmmmmmmmmm....."
        call pauseInterface
        show apiss an3 with dissolve
        "you eagerly run your tongue the full length of her slit, pure and soft as silk."
        a_ube "*ohhh*"
        "azula moans as you lap at her pussy gently, and then roughly, and then gently again."
        "her swollen lips surround her tongue as you flit in and out of her insides, tasting her beginning to run over your tongue."
        "azula speaks softly, almost as if to herself."
        a_ube "{size=-4}that's it..."
        a_ube "{size=-4}yes... zuzu... lick me... taste me... taste my pussy..."
        "she seems almost afraid you'll stop."
        "you press your tongue more firmly, feeling her warm, slick cunt, as she begins humping your face."
        show apiss an6 with dissolve
        a_ae "almost...."
        a_ae "...ah...ah...don't...stop..."
        a_ae "*ngh*...ah...ha...oh!"
        a_ae "oh! don't stop! ah!"
        show apiss 23 with dissolve
        show masturbate_screenfluid_01 with dissolve
        a_ube "oh!"
        show masturbate_screenfluid_02 with dissolve
        a_ube "mmm... ah... yes..."
        "azula creams herself from your efforts, her whole body shaking."
        show apiss 28 with dissolve
        a_b "ah... that was nice... zuzu..."
        a_b "you can... stop licking me now."
        show apiss 2 with dissolve
        a_b "good boy."
        show apiss 1 with dissolve
        a_b "i'm going to sleep now."
        a_b "though i like the view."
        a_ube "now get out..."
        a_ube "i'm..."
        hide apiss 1 with dissolve
        "azula lays down on the floor where she is and immediately passes out."

        return
###### [Azula] Blowjob
label gallery_za_blowjob:
    call gallery_dCharacters_2Love

    scene bg_a_azula_room with dissolve
    show ablj1a with dissolve
    a "well? whip it out, brother."
    show ablj2a with dissolve
    a "haha... oh, my. you're ready, aren't you?"
    hide ablj1a
    show ablj4a with dissolve
    a "..."
    hide ablj2a
    hide ablj3a
    show ablj_tuga with dissolve
    y "ngh..."
    call pauseInterface
    y "that's it, sis..."
    a "..."
    y "you have the best dick-sucking lips in the fire nation."
    y "put them to use."
    show ablj3a with dissolve
    hide ablj_tuga
    hide ablj4a
    a "..."
    show ablj6a with dissolve
    hide ablj3a
    a "okay."
    show ablj7a with dissolve
    hide ablj6a
    a "..."
    show ablj8a with dissolve
    hide ablj7a
    "azula wraps her lips fully around your member."
    y "fuck."
    show ablj9a with dissolve
    hide ablj8a
    "she drops down further, taking it as deeply as she can."
    a "*mghm* *ngh*"
    "she holds it down before coming up sputtering."
    show ablj10a with dissolve
    hide ablj9a
    a "*cough* *cough*"
    show ablj6a with dissolve
    hide ablj10a
    a "how was... that...?"
    y "get. down. there!"
    a "yes, brother! order me!"
    show ablj7a with dissolve
    hide ablj11a
    hide ablj10a
    y "ngh..."
    show ablj8a with dissolve
    hide ablj7a
    show abj_1a
    a "*mmg* *hhngh*"
    y "oh fuck!"
    call pauseInterface
    a "*ngh* *mmmgh*"
    y "deeper..."
    a "*mngh*"
    y "i said \"deeper\"..."
    a "*mmggh*"
    show ablj12a with dissolve
    a "???"
    hide abj_1a
    show ablj13a with vshake
    a "{size=+5}*hhhgghgh!!!!*"
    hide ablj12a
    y "{size=+3}there we go!"
    a "!!!!!"
    a "*ggaghag*"
    y "are you gagging? are you gagging on cock?"
    a "*mmmmmmmm*"
    y "what's that? you like having your throat filled?"
    a "*mmm-hmmmm!!*"
    y "i know you want me to empty my balls in your throat, but i'm just not there yet."
    a "*umph!* *ngh!* *hmmph!*"
    "azula begins moaning into your shaft..."
    show abj_2a with dissolve
    a "*nmgh!*"
    hide ablj8a
    y "i knew you had it in you!"
    y "look how deep you can go!"
    a "*mmnn!*"
    y "what's that?"
    a "*mmmnnn!!!*"
    y "i can't understand a word you're saying... you should really speak up."
    a "{size=+5} *aaaaahgghghhnn!!!!!*"
    y "you're welcome!"

    show ablj33a with dissolve
    a "*gaggh* *hack* *cough*"
    hide abj_2a
    hide ablj13a
    show ablj34a with dissolve
    a "i almost came!"
    hide ablj33a
    a "fuck my mouth again!"
    ya "*rrrrr*"
    show ablj13a with sshake
    "you grab her bangs and pull her all the way down onto your cock again."
    a "*nnghg!!*"
    hide ablj10a
    hide ablj34a
    show abj_2a with dissolve
    a "*umph!* *ngh!*"
    y "look at the prize jewel of the fire nation - azula the whore!"
    y "little dominating sister-princess turned cumslut."
    a "*ggagghh!* *kaghk!*"
    y "that's it, bitch, work that big shaft with your throat."
    y "drain my sack."
    y "suck out all my cum!"
    show ablj34a with dissolve
    a "hey, zuko...."
    hide ablj13a
    yd "what?"
    a "do you... enjoy your time with me?"
    yd "definitely."
    a "...that makes me happy, brother."
    a "i was thinking-"

    show ablj13a with sshake
    a "!!!!"
    show abj_3a with Dissolve(0.2)
    y "come on! come on!"
    hide abj_2a
    y "work that cock, azula!"
    a "!!!"
    a "*nghh!* *nggh!* *aahngh!*"
    ya "oh fuck!"
    a "*??!?!!?*"

    menu:
        "cum in her throat":
            hide ablj13a
            show ablj13a with sshake
            a "!!!!!!"
            hide abj_3a
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            with flash
            a "!!!!!!"
            ya "swallow it, sis!"
            play sound "audio/splurt2.ogg"
            show ablj14a
            with flash
            y "take it down!"
            hide ablj13a
            a "*mmgnh!*"
            play sound "audio/splurt3.ogg"
            show ablj15a
            with flash
            y "down the hatch!"
            hide ablj14a
            play sound "audio/splurt1.ogg"
            show ablj16a
            with flash
            y "{size=+4}oh no you don't!"
            hide ablj15a
            a "*hnghh!*"
            play sound "audio/splurt1.ogg"
            show ablj17a
            with flash
            a "*mmgh!*"
            hide ablj16a
            y "ahh..."
            a "..."
            show ablj35a with dissolve
            a "..."
            show ablj37a with dissolve
            a "that was fun."
            hide ablj35a
            hide ablj17a
            y "yeah, it was."
            show ablj38a with dissolve
            a "don't be afraid to come back."
            a "and... it wouldn't hurt to be nice to me some."
            hide ablj37a
            hide ablj17a
            hide abj_2a
            hide ablj10a
            hide ablj8a
            hide ablj12a
            hide ablj3a
            hide ablj6a
            hide ablj38a with dissolve

        "cum on her face":
            hide ablj13a
            show ablj21a with sshake
            "you shove azula back off your cock."
            a "!!!!!!"
            hide abj_3a
            ya "stroke it!"
            show ablj22a with dissolve
            a "wha-"
            hide ablj21a
            ya "ngh!"
            show ablj23a
            play sound "audio/splurt3.ogg"
            with flash
            a "!!!!!!"
            a "you're-"
            hide ablj22a
            ya "take it, sis!"
            play sound "audio/splurt2.ogg"
            with flash
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            show ablj24a
            with flash
            y "all over your face, azula!"
            hide ablj23a
            play sound "audio/splurt1.ogg"
            show ablj25a
            with flash
            hide ablj24a
            y "ahh..."
            a "...."
            call pauseInterface
            show ablj36a with dissolve
            a "that was fun, but.... i told you to cum in my mouth."
            a "i have an appointment."
            hide ablj25a
            y "so, go like that."
            show ablj25a with dissolve
            a "maybe i will."
            a "don't be afraid to come back."
            a "and... it wouldn't hurt to be nice to me some."
            hide ablj36a
            hide abj_2a
            hide ablj10a
            hide ablj8a
            hide ablj12a
            hide ablj3a
            hide ablj6a
            hide ablj25a with dissolve
            
    return
###### [Azula] Anal
label gallery_za_anal:
    call gallery_dCharacters_2Love

    show ash1 with dissolve
    a "i've been hoping all day that you'd shove your fat cock up my asshole."
    call pauseInterface
    y "damn."
    a "what do you think?"
    y "it's a great ass."
    show ash2 with dissolve
    ab "what, this?"
    hide ash1
    show ash_1 with dissolve
    hide ash2
    call pauseInterface
    show ash3 with dissolve
    hide ash_1
    show ash13 with dissolve
    ab "oh, no... what's that...?"
    y "......"
    show ash14 with dissolve
    abe "ah..."
    ab "easy... ah... when going into my... ah..."
    hide ash13
    show ash15 with dissolve
    asbe "oh!!"
    y "what?"
    hide ash14
    asbe "my... ngh... fuck... oh..."
    show ash13 with dissolve
    y "what's my name?"
    hide ash15
    abe "zuko?"
    show ash_an1
    aae "ah!"
    call pauseInterface
    aae "*ngh!* *ungh!* *ah!*"
    aae "yes, brother! fuck that ass!"
    aab "come on, fuck me!"
    aab "fuck me!"
    aabe "quit being so gentle! pound me like a bitch!"
    y "fine! you want it rough?"
    aab "yes!"
    y "*grr*"
    show ash_an2
    call pauseInterface
    aabe "yes! yes!"
    hide ash_an1
    abe "ugh! ngh! ah... ah... ha..."
    abe "ohhh... ah...."
    y "you're not getting off that easy!"
    aub "wha-"
    show ash_an3
    asb "ah! ah! ah!"
    hide ash_an2
    asbe "wait! wait!"
    aabe "my ass! ow! wait! no!"
    aabe "*ngh!* *mmgh!*"
    y "you asked for it, bitch!"
    aabe "*ah!* *ungh!*"
    menu:
        "cum outside":
            hide ash13
            show ash23 with flash
            aub "wh-"
            hide ash_an3
            play sound "audio/splurt2.ogg"
            show ash20 with flash
            asb "oh!"
            hide ash23
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show ash21 with flash
            asbe "mmm..."
            hide ash20
            y "not done yet!"
            play sound "audio/splurt2.ogg"
            show ash22 with flash
            abe "ahh...."
            hide ash21
            y "fuck..."
            abe "i'm soaked..."
            abe "i can feel it dripping down my legs..."
            ab "that was great."
            ab "maybe we'll do it again sometime."
            call pauseInterface
            hide ash13
            hide ash22 with dissolve

        "cum inside":
            show ash14 with dissolve
            aub "wh-"
            hide ash_an3
            play sound "audio/splurt2.ogg"
            show ash17 with flash
            asb "ah!"
            hide ash14
            y "fuck!"
            play sound "audio/splurt2.ogg"
            show ash18 with flash
            asbe "ngh..."
            hide ash17
            y "not done yet!"
            play sound "audio/splurt2.ogg"
            show ash19 with flash
            abe "ahh...."
            hide ash18
            y "fuck..."
            abe "i'm so full..."
            ab "that was great."
            ab "maybe we'll do it again sometime."
            call pauseInterface
            hide ash13
            hide ash19 with dissolve

    return
###### [Azula] Sex
label gallery_za_sex:
    call gallery_dCharacters_2Love

    scene bg_a_threesome_03
    show azrr azrr01 with dissolve
    show azrr azrr02 with dissolve
    a "perfect."
    a "are you ready, brother?"
    y "like you wouldn't believe."
    "azula presses down on your cock, expecting it to slide in easily."
    "the tip of your cock stops at the entrance to her pussy for a half-second before the pressure from azula forces you suddenly inside her."
    play sound "audio/gltch2.mp3"
    show azrr azrr06
    with pflash

    a "fff...fuck!"
    call pauseInterface
    "azula immediately stops applying weight onto your cock, and you hold there, throbbing in the warmth of her pussy."
    "you can tell she's taken aback at the resistance."

    a "fuck, fuck, fuck...."
    a "it's... it's too tight, i don't think..."
    a "ah...."
    a "fuck!"
    a "no! i'm going to take this fucking cock!"
    show azrr azrr05 with dissolve
    call pauseInterface
    a "ah... ah... ha... oh, fuck, zuko...."
    a "how do... how do you fuck any girls with this..."
    show azrr azrr06 with dissolve
    a "fuck... i need a second..."
    a "......"
    a "okay.... okay...."
    a "here we go...."
    show azrr azrr10 with dissolve

    call pauseInterface
    show azrr azrr09 with Dissolve(0.3)
    a "mmnghh..."
    call pauseInterface
    a "ngh..."
    show azrr azrr08 with Dissolve(0.3)
    a "hhnggh... mgh... ah..."
    call pauseInterface
    a "just that... that little bit was... shit...."
    show azrr azrr04 with dissolve
    yg "you really are tight, little sis."
    a "shut... shut up... zuko..."
    yg "is big brother's dick too big?"
    a "no... you're... ah... i just... i want to fuck.... you.... ah..."
    show azrr azrr03 with vshake
    a "ah!"
    a "fuck!"
    show azrr azrr07 with Dissolve(0.3)
    call pauseInterface
    a "damn it! shit!"
    a "ahhh..... shhh..... don't... don't say a fucking.... ahh...."
    show azrr azrr03 with Dissolve(0.3)
    a "don't... don't move..."
    show azrr azrr106
    call pauseInterface
    a "ah.... ah.... ah...."
    a ".......i think we can do this, zuko."
    a "i just..."
    a "give me... a second..."
    a "okay..."
    a "okay... here we go..."

    show azrr azrr107

    call pauseInterface
    a "ah!"
    a "yes!"
    show azrr azrr100
    a "ohhh...."
    call pauseInterface
    a "*ngh*... *mmph*... *ah*..."
    a "yes... ngh... final... finally...."
    a "how... how is it, brother?"
    a "is it good? is your sister's pussy good?"
    call pauseInterface
    show azrr azrr04 with Dissolve(0.3)
    a "oh, fuck..."
    show azrr azrr08 with Dissolve(0.4)
    a "oh, fuck!"
    show azrr azrr108
    call pauseInterface
    a "zuzu.... oh, zuzu.... keep... just keep fucking me...."
    a "the palace is ours.... the nation is ours...."
    a "no one can stop us...."
    a "just keep... keep fucking me...."
    a "we can do this for whenever... forever..."
    call pauseInterface
    a "tell me you love it... tell me!"
    yg "you feel fucking amazing..."
    a "more... i need more...!"
    show azrr azrr101
    call pauseInterface
    a "yes! yes!"
    a "oh, big brother! oh, zuzu!"
    a "let me ride you! baby sis will always be here to ride your big cock!"

    show azrr azrr109 with dissolve

    a "i can't stop watching it...."
    a "i've wanted this, but i've been so afraid..."
    a "afraid of how good it would feel..."
    a "fuck... fuck... you're so thick..."
    
    show azrr azrr103 with dissolve

    a "i'm never letting you leave... never!"

    call pauseInterface
    show azrr azrr104 with dissolve
    call pauseInterface
    a "you'll never leave me, right, zuko?"
    a "you'll stay and let me fuck you over and over and over and over again?"
    a "right? won't you?"
    a "i love you, zuko."
    a "i love you so much."
    if not zuko_end:
        a "i want to bear your children."

    a "this feels good, right?"
    a "doesn't this feel perfect?"
    a "tell me you love me."
    show azrr azrr102 with dissolve
    call pauseInterface
    a "tell me, zuko..."
    a "tell me that you love me...!"
    a "i need to hear it...."
    a "tell me!"
    y "i-"
    a "look me in the eyes!"
    a "tell me!"
    call pauseInterface
    y "i love you."
    a "of course..."
    a "of course you love me..."

    show azrr azrr104 with dissolve
    a "how could you not?"
    a "i know you love how this feels... watching me..."
    a "this right here."
    a "feel me squeezing out that cum?"
    a "i know you're desperate to fill me up with sperm, brother."
    a "fill up your little sister. your filthy slut of a little sister."
    a "azula, your personal family slut."

    show azrr azrr101 with dissolve

    a "fuck yes.... i'm fucking the firelord..."
    a "i'm zuzu's...."
    a "my life is so good.... so fucking good..."
    show azrr azrr109 with dissolve
    a "and this cock... this fucking cock..."
    a "yes... yes... i feel you swelling..."
    show azrr azrr103 with dissolve
    a "i feel you in there..."
    a "give me that load.... that big fucking load..."
    a "fill my pure, ready pussy...."
    a "it's okay. you can cum, zuzu."
    a "i need this. we need this."
    a "cum in me. give me your seed."
    a "yes... yes... fuck, you're getting... getting too.. ah... ah..."
    a "cum for me! cum on, brother! cum!"

    menu:
        "impregnate azula":
            y "ngh!"
            show azrr azrr07
            show azzr_xray
            with Dissolve(1.0)
            play sound "audio/splurt2.ogg"
            show azzr_xray_spermshot
            pause 0.3
            hide azzr_xray_spermshot
            show azzr_xray_sperm1
            a "yes!"
            show azrr azrr12 with dissolve
            play sound "audio/splurt2.ogg"
            show azzr_xray_spermshot
            pause 0.3
            hide azzr_xray_spermshot
            hide azzr_xray_sperm1
            show azzr_xray_sperm2
            if not zuko_end:
                a "give me babies, zuzu!"
            y "fuck!"

            show azrr azrr03 with dissolve
            play sound "audio/splurt1.ogg"
            show azzr_xray_spermshot
            pause 0.3
            hide azzr_xray_spermshot
            hide azzr_xray_sperm2
            show azzr_xray_sperm3
            a "mmmm..."
            hide azzr_xray_sperm2
            show azrr_fertilize
            call pauseInterface
            a "wow...."
            a "that... that was a huge load, zuko."
            
        "superheat and kill your sperm":
            "as your begin to ejaculate, you heat your sperm just high enough to kill them."
            y "ngh!"
            show azrr azrr07
            show azzr_xray
            with Dissolve(1.0)
            play sound "audio/splurt2.ogg"
            show azzr_xray_spermshot
            pause 0.3
            hide azzr_xray_spermshot
            show azzr_xray_sperm1
            a "yes!"
            show azrr azrr12 with dissolve
            play sound "audio/splurt2.ogg"
            show azzr_xray_spermshot
            pause 0.3
            hide azzr_xray_spermshot
            hide azzr_xray_sperm1
            show azzr_xray_sperm2
            if not zuko_end:
                a "give me babies, zuzu!"
            y "fuck!"
            show azrr azrr03 with dissolve
            play sound "audio/splurt1.ogg"
            show azzr_xray_spermshot
            pause 0.3
            hide azzr_xray_spermshot
            hide azzr_xray_sperm2
            show azzr_xray_sperm3
            a "mmmm..."
            call pauseInterface
            a "wow...."
            a "that... that was a huge load, zuko."
            a "and... very warm..."

    show azrr azrr03 with dissolve
    play sound "audio/splurt1.ogg"
    show azzr_xray_spermshot
    pause 0.3
    hide azzr_xray_spermshot
    hide azzr_xray_sperm2
    show azzr_xray_sperm3
    a "mmmm..."
    show azrr_fertilize
    call pauseInterface
    a "wow...."
    a "that... that was a huge load, zuko."

    show azrr azrr12 with dissolve
    a "mmmm...."
    call pauseInterface
    show azrr azrr14 with dissolve
    show azrr azrr15 with dissolve
    a "don't forget this moment."
    a "we're going to have a lifetime of them."
    call pauseInterface
    show azrr azrr105
    hide azzr_xray
    hide azzr_xray_sperm3
    with dissolve
    a "mmm..."
    a "look at all the cum...."
    a "now..."
    a "i'll let you relax...."
    call pauseInterface

    return
###### [Azula] Beach Rub
label gallery_za_beachrub:
    call gallery_dCharacters_2Love

    stop music
    play music "audio/Unwritten Return.mp3"
    show azbr azbr02 with dissolve

    call pauseInterface
    y "oh, fuck yes."
    a "now, remember..."
    show azbr azbr06 with Dissolve(0.35)
    a "act natural."
    call pauseInterface
    a "ready?"
    ys "definitely."
    a "say please."
    ya "get to it!"
    a "......"
    a "mmmmm....."

    show azbr azbr100 with Dissolve(0.35)
    call pauseInterface
    "azula smoothly straddles and cups your cock with her cheeks."
    "she's surprisingly light, and yet presses down firmly, burying your cock deeply in her crevice."
    "her soft cheeks surround and squeeze you as she grinds her ass down onto you, keeping her pressure constant."
    call pauseInterface
    a "now you should wave to those curious people over there."
    a "so they don't think anything suspicious."
    "you smile and wave at the beach-goers, who smile and wave back."
    call pauseInterface
    a "so, you wanted something to do..."
    a "how's my ass? fun?"
    show azbr azbr101 with Dissolve(0.35)
    a "i know i'm having fun."
    call pauseInterface
    a "we really should spend more time together."
    show azbr_blink with Dissolve(0.35)
    a "isn't this nice?"
    call pauseInterface
    a "bonding like this?"
    hide azbr_blink
    show azbr azbr100
    with Dissolve(0.35)
    a "I can't imagine what father would say."
    call pauseInterface
    show azbr azbr101 with Dissolve(0.35)
    call pauseInterface
    "ty lee suddenly gets out of the water and starts walking towards you."
    yc "oh, shit! we should... we should stop..."
    show azbr_sultry with Dissolve(0.35)
    a "nonsense, zuzu."
    a "i can handle ty lee."
    call pauseInterface

    yc "i... guess... ah... you can... deal with her..."
    hide azbr_sultry with Dissolve(0.35)
    a "you're such a good big brother."
    show azbr azbr105 with Dissolve(0.35)
    call pauseInterface

    a "you just enjoy yourself, now."

    call pauseInterface
    show azbr azbr02_1 with dissolve
    t "hey, guys!"

    call pauseInterface
    a "hello, ty lee. are you having fun?"
    t "i really am!"
    t "what are you guys up to?"
    show azbr azbr03_1 with dissolve
    call pauseInterface
    ya "hngh..."
    a "oh, just catching up."
    t "that's great!"
    show azbr azbr03_2 with dissolve
    t "i hope the weather stays nice..."
    a "i am sure that..."
    show azbr azbr04_2 with dissolve
    call pauseInterface
    a "*mmmmm*"
    a "...that it will stay fine."
    show azbr azbr105_1
    call pauseInterface
    ya "(shit!)"
    show azbr azbr105_2
    t "are... are you okay?"
    call pauseInterface
    a "why, yes. what makes you ask?"
    t "well, you're... rocking... on zuko..."
    a "i have a bit of a... well, a wedgie."
    show azbr azbr105_3
    a "i don't mean to be crude, but it feels like there's something shoved in my ass cheeks."
    show azbr azbr102_1
    show azbr_sultry
    with Dissolve(0.35)
    a "you don't mind, do you, brother?"
    call pauseInterface

    yc "uuungh....."
    call pauseInterface
    a "it looks like he doesn't mind."
    a "if that's the case, sorry about this zuko, i'm gonna wiggle extra hard to try to get it out."
    show azbr azbr104_1
    call pauseInterface
    ya "ahh... f-fuck..."
    show azbr azbr104_2
    t "what's wrong, zuko?"
    hide azbr_sultry with dissolve
    a "yes, what {i}is{/i} the matter, zuzu?"
    yc "i, uh... i think i'm about to cum..."
    yc "...down with something."
    yd "and i think it's going to be... messy..."
    call pauseInterface
    show azbr_sultry with dissolve
    a "you're certainly not going to make a mess right now, are you?"
    a "not with me on your lap?"
    a "i hope i'm not the cause."
    a "i promise i'm almost done... I think i'm about to get it out."
    call pauseInterface
    ya "oh, fuck!"
    play sound "audio/splurt3.ogg"
    show azbr azbr07_2
    hide azbr_sultry
    show az_mai_sperm_9:
        xpos -420 ypos 300
    with flash
    call pauseInterface
    t "prince, are you okay!"
    a "oh, {i}no{/i}..."
    ya "y-yes, i..."
    play sound "audio/splurt3.ogg"
    hide az_mai_sperm_9

    show a_pussrub_holdcock_sperm01:
        xpos -266 ypos 138
    show az_mai_sperm_10:
        xpos -420 ypos 300

    with flash
    call pauseInterface
    ya "hgh!"
    t "i'll go get a bucket!"
    hide a_pussrub_holdcock_sperm01
    hide az_mai_sperm_10
    show azbr azbr07
    show a_pussrub_holdcock_sperm01:
        xpos -266 ypos 138
    show az_mai_sperm_10:
        xpos -420 ypos 300
    with dissolve
    a "what are you doing, brother?"
    play sound "audio/splurt3.ogg"
    hide azbr_sultry
    hide az_mai_sperm_10
    show az_mai_sperm_11:
        xpos -420 ypos 300
    with flash
    call pauseInterface
    yc "ghgh...."
    a "you shouldn't be cumming on me in front of ty lee."
    show azbr azbr04 with Dissolve(0.35)
    call pauseInterface
    a "mmmm...."
    a "warm..."
    show azbr azbr07
    with Dissolve(0.35)
    a "but it's nice, isn't it brother?"
    call pauseInterface
    a "you can rely on me... to take care of you."
    show azbr_sultry with Dissolve(0.35)
    a "but now... i think you might need a dip in the ocean."
    yd "don't you?"
    a "i'll just wipe it off in my swimsuit."
    hide azbr_sultry with dissolve
    a "i'll rinse it out later."
    a "i don't think i'll need it for a while."
    a "we {i}should{/i} get up before ty lee comes back, though."
    yd "good plan."
    y "......."
    yd "......."
    yd "you're not moving..."
    show azbr_sultry with dissolve
    a "well, it's nice."
    hide azbr_sultry with dissolve
    a "oh, all right."

    return
###### [Azula] Anal over Mai
label gallery_sleepy_azula_anal:
    call gallery_dCharacters_2Love

    stop music
    play music "audio/Unwritten Return.mp3"
    scene black
    scene bg_a_2beds
    show amsl amsl23
    with dissolve
    show amsl amsl22 with dissolve
    "you walk in and azula immediately opens her eyes."
    "almost like she's been waiting for you."
    a "welcome. brother."
    "the way she says it is definitive. like the tolling of a bell."
    "a sense of understanding is heavy in the room. neither of you speak. there's no need."
    show amsl amsl00 with dissolve
    "azula moves slowly, fluidly, cat-like."
    "naked and delicate in the small, shared room, she crouches over mai."
    show amsl amsl12 with dissolve
    call pauseInterface
    
    "you take off your clothes with ease and purpose, as if pulled by gravity."
    "The sight and scent of her, waiting, patiently, is intoxicating."
    "she smells clean; ever so lightly of lilacs and vanilla."
    "your heart races as she presents her ass to you. there is no hurry. you both know why you came."
    show amsl amsl03 with dissolve
    "you approach her and rest your member lightly against her anus."
    show amsl amsl104
    "azula presses back into you... with mild hesitation."
    "you begin to press forward, and she stops all movement."
    "understanding, you wait for her to adjust."
    "after a moment, she moves again."
    show amsl amsl105
    pause 0.2
    with pflash
    a "*mmmh*"
    call pauseInterface
    "and in that moment you're inside of her."
    "azula, your sister."
    "bitter. vengeful. calculating. desperate."
    "you can feel her trying to adjust to the unfamiliar presence of your cock."
    "her anus squeezes you in quick, rapid succession as if trying to force you out, but only serving to make you harder."
    show amsl amsl106
    call pauseInterface
    a "ahhh..."
    "small, involuntary noises escape her throat as she pushes to welcome you deeper into her."
    "unable to take it any more, you move violently, thrusting your full mass inside of her."
    show amsl amsl11 with vshake
    call pauseInterface
    a "*ahh....*"
    "she holds herself there, but you can tell from the increasing quivering that she is struggling to keep her composure."
    show amsl amsl07 with dissolve
    "azula pulls herself off of your cock enough to gain reprieve from your size."
    show amsl amsl05 with dissolve
    "she slides again until she has almost completely pulled herself off..."
    show amsl amsl100
    "and slides back down, her determination overcoming her discomfort, and growing more confident with every stroke."
    "she begins to pick up speed, pulling out as she fucks you with her ass... making sure to fully stimulate the tip of your cock."
    a "ohhh...."
    "her moans become more frequent, pushing out of her as you enter her..."
    "almost as if each thrust of your cock knocks breath out of her."
    a "yes.... yes.... oh, zuzu... yes....."
    show amsl amsl101
    "her thrusts grow more desperate, her voice becomes more animal, and she skewers herself wildly on your cock."
    a "yes! yes! ngh! fuck! yes!"
    call pauseInterface
    a "fuck me, zuko! fuck me like the fucking whore i am!"
    ync "but mai...."
    a "fuck her! and {i}fuck. me."
    ync "wait, shhh...."
    show amsl amsl102
    a "if you don't give me what i fucking need, i'll wake her myself!"

    menu:
        "give her what she wants... some violence!":
            yna "you want it? take it!"
            play sound "audio/fleshslap.mp3"
            show amsl amsl101_1
            with flash
            a "{i}aahhh{/i}..."
            "you slap azula so hard her face turns back down as you beginning slamming her ass, all caution abandoned."
            "she matches your thrusts with violent eagerness."
            a "that's it, brother! show me who's really in charge!"
            yna "i'm gonna make you {i}hurt{/i}, you sick, manipulative bitch!"

        "go straight to giving it to her hard!":
            yna "you want it? take it!"
            show amsl amsl101_1
            with flash
            a "{i}aahhh{/i}..."
            "you beginning slamming her ass, all caution abandoned."
            "she matches your thrusts with violent eagerness."
            a "that's it, brother! show me who's really in charge!"
            yna "you're going to fucking {i}cry{/i}, azula."

    call pauseInterface

    a "yes! own me! own my ass! show me!"
    a "prove my ass belongs to-"
    show amsl amsl101_2
    a "unghh! fuck!"
    call pauseInterface
    a "i'm a fuckpig!"
    a "fuck me! fuck my little ass! my poor little ass!"
    a "it's been waiting for big brother to come fill it!"
    ynd "(she seems really into degradation...)"

    menu:
        "spit on her back":
            play sound "audio/spit.mp3"
            show amsl amsl101_3
            with flash
            a "oh!"
            show amsl amsl11_1 with vpunch
            a "ah!"
            a "f...fuck..."
            a "...fuck!"
            a "don't... don't just leave it... oh, fuck it's deep..."
            show amsl amsl11_2 with dissolve
            a "what are... you... doing, broth... ah... brother...?"
            yna "put your head down!"
            show amsl amsl11_1 with dissolve
            a "w... why am i... ah..."
            yn "beg for it, whore."
            a "*mmmm....*"
            a "please, zuko... zuzu... don't make me suffer..."
            a "treat me right.... make me cry from your cock...."
            a "mo... move it... p... please... have mercy..."
            ynd "mercy?"
            yn "coming from you, i know exactly what kind of mercy to give, sis."

            yna "you're going to follow my orders, understand?"
            ynd "now..."
            yna "up!"
            show amsl amsl101_4 with dissolve
            a "unh..."
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "ah!"
            a "ow.... *mmmmmm*....."
            yna "up!"
            show amsl amsl101_4 with dissolve
            yn "who are you?"
            a "a... i'm... az... azula..."
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "unngh...."
            yna "now... {i}what{/i} are you?"
            a "y...your whore..."
            yna "up!"
            show amsl amsl101_4 with dissolve
            yn "what are you?"
            a "i'm a-"
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "ahh...."
            a "b... bitch..."
            yna "up!"
            show amsl amsl101_4 with dissolve
            yn "and?"
            a "a-"
            yna "down!"
            show amsl amsl11_1 with vpunch
            a "s... stupid... cocksleeve..."
            a "who should be beaten."
            show amsl amsl101_4 with dissolve
            a "with precision."
            a "in a steel, soundproof room."
            a "i deserve to have my hair pulled and wear-"
            ynd "uh."
            show amsl amsl18_1 with dissolve
            a "what?"
            yn "shut up."
            show amsl amsl103 with dissolve

        "bury it and hold there":
            show amsl amsl11 with vpunch
            a "ah!"
            a "f...fuck..."
            a "...fuck!"
            a "don't... don't just leave it... oh, fuck it's deep..."
            show amsl amsl11_3 with dissolve
            a "what are... you... doing, broth... ah... brother...?"
            yna "put your head down!"
            show amsl amsl11 with dissolve
            a "w... why am i... ah..."
            yn "beg for it, whore."
            a "*mmmm....*"
            a "please, zuko... zuzu... don't make me suffer..."
            a "treat me right.... make me cry from your cock...."
            a "mo... move it... p... please... have mercy..."
            ynd "mercy?"
            yn "coming from you, i know exactly what kind of mercy to give, sis."
            yna "you're going to follow my orders, understand?"
            ynd "now..."
            yna "up!"
            show amsl amsl101_6 with dissolve
            a "unh..."
            yna "down!"
            show amsl amsl11 with vpunch
            a "ah!"
            a "ow.... *mmmmmm*....."
            yna "up!"
            show amsl amsl101_6 with dissolve
            yn "who are you?"
            a "a... i'm... az... azula..."
            yna "down!"
            show amsl amsl11 with vpunch
            yna "now... {i}what{/i} are you?"
            a "y...your whore..."
            yna "up!"
            show amsl amsl101_6 with dissolve
            yn "what are you?"
            a "i'm a-"
            yna "down!"
            show amsl amsl11 with vpunch
            a "ahh.... b... bitch..."
            yna "up!"
            show amsl amsl101_6 with dissolve
            yn "and?"
            a "a-"
            yna "down!"
            show amsl amsl11 with vpunch
            a "s... stupid... cocksleeve..."
            a "who should be beaten."
            a "with precision."
            a "in a steel, soundproof room."
            a "i deserve to have my hair pulled and wear-"
            ynd "uh."
            show amsl amsl18 with dissolve
            a "what?"
            yn "shut up."
            show amsl amsl103

    show amsl amsl11 with vpunch
    a "nngh...."
    a "...fuck."
    yn "...."
    yna "get to it!"
    show amsl amsl04 with dissolve
    a "....yes, brother...."

    show amsl amsl101_1
    call pauseInterface
    yn "do you like getting your asshole fucked ruthlessly over your friend?"
    a "yes!"
    a "pound my ass over your sleeping girlfriend!"
    a "mai... that frigid bitch... can suck it..."
    a "{i}i{/i} know what you need, brother..."
    yn "oh, fuck, azula... your ass is unreal..."
    a "yes, that's it... enjoy it, zuzu."
    a "it's all yours."
    a "i'm going to..."
    a "i'm going to make you cum."
    a "...oh my god."
    a "......."
    a "...i can't believe it."
    a "i can't believe it!"
    a "you're going to cum in me!"
    a "oh my god!"
    show amsl amsl101_2
    call pauseInterface
    a "do it!"
    a "*ah!*"
    a "cum for me!"
    a "cum!"
    a "i don't... *ah!*... i don't think i can do much more..."
    yna "you want my cum, azula?"
    a "yes! *ngh!* please!"
    yna "you want it, sis?"
    a "*ah!* give it to *unh!* me!"
    yna "fuck.. fuck.. fuck!"
    yna "here it cums!"
    yna "i'm fucking cumming! take my load, sis!"
    a "yes! pound *ah!* my fucking asshole, brother!"
    a "{size=+5}cum for me!"

    menu:
        "cum inside":
            $ azula_in_ass = True
            show amsl amsl10 with vpunch
            a "fuck!"
            play sound "audio/splurt3.ogg"
            show amsl_sperminass_1
            with flash
            a "yes!"
            play sound "audio/splurt2.ogg"
            show amsl_sperminass_2
            with flash
            a "big brother!"
            play sound "audio/splurt3.ogg"
            show amsl_sperminass_2
            with flash
            a "{size=+6}cum in me, zuko!"

        "cum outside":
            $ azula_on_ass = True
            show amsl amsl12 with vpunch
            a "fuck!"
            play sound "audio/splurt3.ogg"
            show amsl_spermonbutt_1
            with flash
            a "yes!"
            play sound "audio/splurt2.ogg"
            show amsl_spermonbutt_2
            with flash
            a "big brother!"
            play sound "audio/splurt3.ogg"
            show amsl_spermonbutt_3
            with flash
            a "{size=+6}cum on me, zuko!"


    show az_mai_eyesopen with vshake
    call pauseInterface
    m "what..."
    m "what's going on...?"
    play sound "audio/splurt3.ogg"
    with flash
    yna "ngh!"
    ync "......"
    a "........."
    ync "you're, uh, you're having a dream."
    play sound "audio/splurt3.ogg"
    with flash
    a "yes, a dream, mai."
    m "zuko...?"
    if azula_in_ass:
        m "are... you cumming in azula right now?"
    m "....are you two having sex?"
    yn "ssshhhhh.... sh."
    yn "that's just crazy."
    play sound "audio/splurt3.ogg"
    with flash
    a "it's all a dream, mai."
    a "i fell over is all."
    a "go to sleep."
    m "oh... okay..."
    hide az_mai_eyesopen with dissolve
    call pauseInterface
    ync "......"
    a "well, that was close."
    a "...you came a lot."
    ync "yeah... her waking up in the middle just..."
    ync "it was the fear."
    ynd "adrenaline, maybe?"
    yn "either way, i just had a fucking great orgasm."
    a "well... i feel like you've earned some rest."
    a "i know i have..."
    yng "have you?"
    if azula_in_ass:
        show az_azula_turnhead4 with dissolve
    else:
        show az_azula_turnhead1 with dissolve

    a "don't confuse who's really in charge here, brother."

    if azula_in_ass:
        show amsl amsl12
        show amsl_spermonbutt_0
        hide az_azula_turnhead4
        hide amsl_sperminass_2
        hide amsl_sperminass_1
        hide amsl_sperminass_3
        with dissolve
    if azula_on_ass:
        hide az_azula_turnhead1 with dissolve
    a "i think it's time for you to leave."
    ynd "...what? you're kicking me out?"
    a "you did your job."
    ynd "i feel used."
    a "oh, you were."
    a "...and so was i, unless you've already forgotten..."
    a "we used each other."
    a "in this cold, dark world."
    a "family, brother."
    a "get some rest."

    "azula, cum dripping out and down her ass, crawls away from you on all fours."
    "it's a pleasure to watch."
    show amsl amsl22
    hide amsl_spermonbutt_0
    hide amsl_spermonbutt_1
    hide amsl_spermonbutt_2
    hide amsl_spermonbutt_3
    with dissolve
    a "goodnight... brother."
    show amsl amsl23 with dissolve
    a "I'm exhausted."
    a "i'll see you in the morning."
    
    return
###### [Ursa] Blowjob
label gallery_ursa_zuko:
    call gallery_dCharacters_2Love

    scene bg_a_smallpalaceroom
    show usbj usbj01_1
    with Dissolve(1)
    ursa "zuko, baby, i'm sorry."
    zu "mother?"
    ursa "i've... done something tonight."
    ursa "you're too young to understand, but i have to leave."
    ursa "but i love you."
    zu "mother, i'm scared!"
    show usbj_blink with dissolve
    ursa "oh, don't be scared."
    ursa "i'm going to give you something to remember me by."
    zu "you are?"
    ursa "don't tell your sister, okay?"
    aa "oh, and you didn't have to."
    aa "i saw it all......."
    zu "if you love me why are you going?"
    hide usbj_blink with dissolve
    ursa "shhh, baby."
    ursa "mommy's going to kneel down now, okay?"
    show usbj usbj01
    with vshake
    ursa "my sweet boy."
    ursa "i don't want you to ever forget me, okay?"
    ursa "come closer."
    show usbj usbj02 with dissolve
    zu "okay..."
    ursa "i want you to always remember just how much i love you."
    ursa "i'm going to show just how deeply i care for you."
    ursa "do you feel that, zuko? do you feel my hand?"
    zu "ah... mmmm... it's..."
    ursa "that's natural. that's what happens when i do that."
    ursa "i'm going to pull my hand away now..."
    zu "i'm..."
    show usbj usbj03 with dissolve
    zu "don't look!"
    ursa "you've already grown so much, zuko."
    ursa "i'm sorry i won't be able to see you grow more..."
    show usbj usbj04 with dissolve
    zu "ohhh...."
    show usbj usbj05 with dissolve
    ursa "mmmm...."
    show usbj usbj06 with dissolve
    zu "nnnmmmm...."
    show usbj usbj07 with dissolve
    ursa "*gagghh*"
    zu "mother!"
    show usbj usbj08 with dissolve
    ursa "*gaghh* *slurp* *mmmgh*"
    zu "ughn! it feels good!"
    ursa "*slurp* *mmgh*"
    show usbj usbj04 with dissolve
    ursa "*shluuuurp*"
    show usbj usbj03
    show usbj_eyesup
    with dissolve
    ursa "*pop*"
    ursa "is that nice, darling?"
    zu "y-yes, mother."
    ursa "good."
    show usbj usbj04
    hide usbj_eyesup
    with dissolve
    ursa "relax, honey."
    show usbj usbj100
    zu "ohhh...."
    ursa "that's it baby, that's it."
    call pauseInterface
    zu "mother, i... i feel strange."
    zu "i don't know what's happening..."
    show usbj usbj101
    call pauseInterface
    zu "something's happening!"
    ursa "*slurp* *mmmgh* *gltch*"
    ursa "*mmm* *mmmm* *mmm*"
    show usbj usbj102
    zu "m-mother!"
    call pauseInterface
    ursa "let it happen, baby. my sweet boy. right here in mommy's mouth. it's okay."
    zu "mother, i can't... it feels so good!"
    ursa "*mmph* *mmph* yes my baby, i love you so much!"
    play sound "audio/splurt3.ogg"
    show usbj usbj10
    with flash
    zu "nnghh!"
    play sound "audio/splurt3.ogg"
    show usbj usbj11
    with flash
    ursa "*ghagh!!!*"
    ursa "*gulp* *gulp*"
    play sound "audio/splurt3.ogg"
    show usbj usbj12
    with flash
    ursa "*sluurp* *gagh*"
    play sound "audio/splurt3.ogg"
    show usbj usbj13
    with flash
    zu "ah!"
    ursa "*gulp* *gulp* *gulp*"
    ursa "*slurp* *gulp*"
    call pauseInterface
    show usbj usbj03
    show usbj_dripsperm
    with dissolve
    ursa "was that fun, zuko?"
    zu "yes, mother!"
    zu "we should do it again!"
    show usbj_eyesup with dissolve
    ursa "i would love to, sweetie."
    ursa "but this was only once."
    ursa "a gift."
    ursa "now what do you say to gifts?"
    zu "thank you!"
    ursa "good boy..."

    return
###### [Ursa] Images
label gallery_ursa_pics:
    screen black

    while True:
        menu:
            "look at first picture":
                hide usa_bw_sketch2
                show usa_bw_sketch
                
            "look at second picture":
                hide usa_bw_sketch
                show usa_bw_sketch2
                
            "finished":
                return

        call pauseInterface
###### [Ty Lee] Vibrator
label gallery_tylee_vibrator:
    call gallery_dCharacters_2Love

    show azst azst03 with dissolve
    call pauseInterface
    y "oh, that's the good shit."
    "{i}zzzt! zzzt! zzzt!"
    "the toy continues to vibrate and move in her pussy, clearly keeping her asleep."
    call pauseInterface
    y "fun."
    show azst_eyesopen with dissolve
    t "oh! hello, prince."
    y "good morning."
    y "time to get up."
    t "okay!"
    call pauseInterface
    y "......"
    y "alright, i'm going."

    return
###### [Ty Lee] Masturbation
label gallery_tylee_dickwatch:
    call gallery_dCharacters_2Love

    scene bg_a_tavern1
    show ty_idle_ff_nude
    with dissolve
    "ty lee gets out of her clothes with surprising speed."
    t "there!"
    t "and just taking a look should be alright."
    t "besides, now you've seen mine, i should see yours!"
    y "sound logic."
    t "i want a closer look!"
    scene bg_a_tavern2
    show azdw azdw100
    with dissolve
    call pauseInterface
    t "whenever you're ready!"
    show azdw_dick with dissolve
    t "are-"
    show azdw azdw03
    show azdw_eyesdown
    with dissolve
    t "oh!"
    t "........."
    t "oooh... wow..."
    show azdw azdw01 with dissolve
    t "it looks nothing like bzzbzz."
    yd "bzzbzz?"
    hide azdw_eyesdown
    show azdw azdw100
    with dissolve
    t "my pink sleeping aid!"
    yd "......"
    yd "okay, are you done?"
    show azdw_eyesdown
    show azdw azdw01
    with dissolve
    t "ehmm... can you... move it a bit?"
    yd "like... masturbate?"
    hide azdw_eyesdown with dissolve
    t "yeah!"
    show azdw_eyesdown with dissolve
    y "well... all right."
    show azdw_masturbate
    hide azdw_dick
    with dissolve
    t "oh, wow......"
    yd "......"
    t "and maybe...."
    t "maybe you could cum in my mouth?"
    yd ".....why?"
    t "i just... want the whole experience..."
    t "does... that make sense? is it too weird?"
    y "nah, it's fine."
    yg "i'll do it. for you."
    yg "if you thank me."
    t "oh, yes! thank you, prince!"
    show azdw azdw02 with dissolve
    t "......."
    t "can you hurry up a little?"
    ya "it takes as long as it takes!"
    hide azdw_eyesdown with dissolve
    t "would it help to see my pussy and ass?"
    t "I'm really flexible."
    yd "i mean, maybe...."
    t "well, let me just-"
    show azdw azdw04 with sshake
    t "ah!"
    "ty lee slips as she tries to show you her bare ass."
    call pauseInterface
    t "i'm going to sit up again."
    t "but did... did it help...?"
    menu:
        "get back on your knees":
            show azdw_masturbate_fast
            hide azdw_masturbate
            ya "get back up here!"
            t "coming!"
            show azdw azdw02 with dissolve
            t "ready!"
            yd "you sure you want me to cum?"
            t "you can make new sperm, right?"
            t "just aim at my face!"
            show azdw_mouthopen with dissolve
            t "aaa...."
            ya "fuck!"
            play sound "audio/splurt2.ogg"
            hide azdw_masturbate_fast
            show azdw_mastur4

            show azdw_sperm0
            show azdw_sperm1
            pause 0.02
            hide azdw_sperm0
            t "oh!"
            show azdw_eyesdown with dissolve
            ya "right in your fucking mouth!"
            call pauseInterface
            hide azdw_eyesdown with dissolve
            play sound "audio/splurt1.ogg"
            hide azdw_eyesdown
            show azdw_sperm0
            show azdw_sperm2
            pause 0.02
            hide azdw_sperm0
            hide azdw_sperm1
            ya "fuck!"
            call pauseInterface
            t "s'warm!"

            play sound "audio/splurt3.ogg"
            show azdw_sperm0
            show azdw_sperm3
            pause 0.02
            hide azdw_sperm0
            hide azdw_sperm2
            ya "ngh!"
            t "*gurgle*"
            "ty lee has trouble speaking with all of the cum in her mouth, so gurgling is the best she can do."

            call pauseInterface

            t "......."
            yd "you should probably swallow that."
            t "*gugugule*"
            show azdw azdw06
            hide azdw_mouthopen
            hide azdw_sperm3
            with dissolve
            t "........."
            play sound "audio/gulp2.mp3"
            t "{size=+5}*gulp!*"
            show azdw azdw01
            show azdw_sperm2
            with dissolve
            t "did i get it all?"
            yd "....."
            y "good enough."
            t "'cause i have customers..."
            y "i'm sure you'll be fine."
            t "thanks, zuko!"
            yd "well, i'll leave you to it then."

        "stay there!":
            show azdw_masturbate_fast
            hide azdw_masturbate
            ya "stay there!"
            t "wh-what?"
            ya "just like that!"
            t "but then i can't see-"
            ya "here it comes!"
            t "what? where?!"
            ya "ahhhh!!!"
            t "aaaahhhh!!!!!"
            play sound "audio/splurt2.ogg"
            hide azdw_masturbate_fast
            show azdw_mastur4
            show azdw_sperm0
            show azdw_spermass1
            pause 0.02
            hide azdw_sperm0
            t "oh!"
            ya "right on your fucking asshole!"
            call pauseInterface
            play sound "audio/splurt1.ogg"
            show azdw_sperm0
            show azdw_spermass2
            pause 0.02
            hide azdw_sperm0
            hide azdw_spermass1
            ya "fuck!"
            call pauseInterface
            t "thats... hot..."
            t "right... right on my ass!"
            t "are you fin-"
            play sound "audio/splurt3.ogg"
            show azdw_sperm0
            show azdw_spermass3
            pause 0.02
            hide azdw_sperm0
            hide azdw_spermass2
            ya "ngh!"
            t "oh!"
            call pauseInterface
            t "um..."
            t "this is... a lot."
            t "i, um... have customers..."
            y "bummer."
            hide azdw_mastur4 with dissolve
            ys "alright, well."
            ys "see ya around."
            t "oh... okay..."
            call pauseInterface
            "you leave ty lee there, upside down, cum dripping into her pussy, ass, and all over the carpet."
            y "nice."

    return
###### [Mei] Boob Massage
label gallery_zem_boob:
    call gallery_dCharacters_2Love

    show mabo mabo01 with dissolve
    m "....."
    show mabo mabo02
    show mabo_blush
    with dissolve
    m "here."
    show mabo_blink with dissolve
    m "...."
    show mabo mabo03 with dissolve
    call pauseInterface
    m "go ahead, love."
    show mabo mabo04
    hide mabo_blink
    hide mabo_blush
    show mabo_surprise
    show mabo_blush
    show mabo_eyesdown
    with dissolve
    m "oh!"
    hide mabo_surprise
    hide mabo_blush
    hide mabo_eyesdown
    show mabo_smile
    show mabo_blush
    show mabo_eyesdown
    show mabo mabo100
    m "mmmmm....."
    call pauseInterface
    hide mabo_eyesdown
    m "having... ah... fun?"
    y "you have the softest tits..."
    hide mabo_smile
    show mabo mabo101
    with Dissolve(0.2)
    m "ohhh... easy..."
    call pauseInterface
    show mabo_blink with Dissolve(0.2)
    m "ahh..."
    show mabo mabo102
    y "yeah... perfect fucking pillows..."
    m "mmmm...."
    show mabo mabo106
    m "easy, zuko...."
    m "be... be gentle..."
    call pauseInterface
    hide mabo_blink
    m "zuko... ah... ah.... you're making me wet..."
    show mabo mabo19
    show mabo_surprise
    show mabo_eyesdownleft
    hide mabo_blush
    show mabo_blush
    with Dissolve(0.35)
    m "ahhh... oh, zuko..."
    show mabo mabo104
    show mabo_surprise
    show mabo_blink
    hide mabo_blush
    show mabo_blush
    with Dissolve(0.35)
    call pauseInterface
    m "ahh... it feels so nice..."
    hide mabo_blink with Dissolve(0.3)
    m "i'm... oh, i'm wet...."
    hide mabo_surprise
    show mabo_blink
    with Dissolve(0.3)
    m "i'm dripping..."
    y "you're dripping here, too."
    show mabo mabo105
    show mabo_smile
    hide mabo_blush
    show mabo_blush
    with Dissolve(0.3)
    m "nnnghhh.... fuck, zuko...."
    m "mmmmmm...."
    hide mabo_eyesdownleft
    show mabo_eyesdownleft with Dissolve(0.3)
    call pauseInterface
    m "yes, zuko... baby... suck my tits..."
    m "my breasts are yours..."
    m "oh fuck, i'm fucking wet...."
    m "keep sucking...."
    m "i think... ah... i think i'm going to... ah... cum... zu..."
    m "i'm gonna cum, zuko... i'm gonna cum from you sucking my tits..."
    hide mabo_smile
    show mabo_blink
    hide mabo_eyesdownleft
    with vshake
    m "{size=+4}zuko!!"
    call pauseInterface

    show mabo_smile
    show mabo_blush
    show mabo_blink
    with Dissolve(0.3)
    m "thank you..."
    call pauseInterface
    m "okay..."
    m "easy...."
    hide mabo_blink
    show mabo mabo03
    with Dissolve(0.3)
    m "will i see you later?"
    y "of course."
    show mabo mabo01 with Dissolve(0.3)
    play sound "audio/kiss.mp3"
    hide mabo_blush
    show mabo_surprise
    show mabo_blush
    with pflash
    m "mmm!"
    hide mabo_surprise
    show mabo_smile
    hide mabo_blush
    show mabo_blush
    m "that was nice...."

    return
###### [Mei] Blowjob 
label gallery_zem_blowjob:
    call gallery_dCharacters_2Love

    stop music fadeout 2
    play music "audio/Unwritten Return.mp3" fadein 2
    scene black
    show mabj mabj22
    with dissolve
    m "mmmm...."
    show mabj mabj23 with dissolve
    m_l "i hope no one sees..."
    scene black with dissolve
    "mai lays down in the sand in front of you..."
    show mabj mabj01 with Dissolve(0.8)
    m "{size=-4}(wow... i'm always amazed...)"
    show mabj_eyesup with dissolve
    m "zuko..."
    m "i'm..."
    hide mabj_eyesup with dissolve
    m "...happy i'm here with you."
    m "this almost doesn't seem real, does it?"
    show mabj_eyesup with dissolve
    m "we're finally together..."
    m ".........."
    hide mabj_eyesup
    show mabj mabj02
    with dissolve
    m "i want to do this for you forever."
    show mabj mabj100
    call pauseInterface
    show mabj_smile
    hide mabj_unsure
    with dissolve
    m "oh, zuko..."
    m "are you ready?"
    show mabj_unsure
    hide mabj_smile
    with dissolve
    yn "that... is a dumb question."
    show mabj mabj05
    hide mabj_smile
    hide mabj_unsure
    with dissolve
    m "....."
    play sound "audio/lick_b.mp3"
    m "*lick*"
    m "......"
    play sound "audio/gulp2.mp3"
    show mabj mabj06 with dissolve
    m "*gulp*"
    show mabj mabj101
    call pauseInterface
    m "*slurp* *gulp*"
    ync "hnngh..."
    m "*mmmmmm*"
    ync "your mouth feels incredible, mai...."
    m "*mmmm* *sluurp* *gltch*"
    m "*slurp* *gulp* *slurp*"
    ync "i want to fuck your mouth every day from now on...."
    m "o'ay..."
    show mabj mabj102
    m "how's it 'eel, prince?"
    yn "unbelieveable!"
    m "'ood..."
    call pauseInterface
    ync "hgh..."
    yn "you're so good at this!"
    m "*slurrp* *gulp* *slurrp*"
    m "'aiting..."
    m "'or you..."
    yn "you're sucking it right out--"
    show mabj mabj103
    call pauseInterface
    yna "fuck, mai!"
    m "you like this right?"
    show mabj_unsure with dissolve
    m "you like when i jack your cock?"
    m "am i milking you right?"
    show mabj_angry
    hide mabj_unsure
    with dissolve
    m "i'm going to get this cum out."
    m "you're mine, zuko."
    m "no one else's."
    show mabj_unsure
    hide mabj_angry
    with dissolve
    m "right?"
    ync "hhgngh..."
    m "this feels great, right? and you're mine, right?"
    ync "y-yes..."
    hide mabj_unsure with dissolve
    m "fine."
    show mabj mabj104
    call pauseInterface
    m "'um 'or 'ee!"
    yn "w-what?"
    m "'um!"
    yn "i don't..."
    m "{size=+4}cum!!"
    m "'um in my 'outh!"
    m "i 'ant it!"
    m "i'll suck it 'ight out!!"
    yn "oh, shit... i think... i think some people are watching..."
    m "'um 'ickly!"
    m "*mmmmmm!!!*"
    "mai relentlessly bobs and gulps on your cock, determined to suck the load out of you..."
    "her lips and tongue slide lightly down your shaft and {i}sluuurp{/i} hard on the way up."
    m "*slurrrp* *slurrp* *gltch* *slurp* *gulp*"
    "she forces your cock down her throat without break as her wet, sloppy suction brings you to the brink."
    m "*gulp* *slurp* *sluuurrrp*"
    yna "ohhh... here it comes!"
    "as a little of her spit dribbles down your shaft, mai moans and sucks mercilessly, repeatedly plunging your full length into her mouth."
    yna "i'm gonna fucking nut!"
    m "*mmmm!!!* *mmmmmmm!!!!!!*"

    menu:
        "cum in mouth":
            show mabj mabj08 with Dissolve(0.2)
            show mabj mabj09 with Dissolve(0.2)
            show mabj mabj10 with Dissolve(0.2)
            show mabj mabj11 with Dissolve(0.2)
            yna "ngh!"
            play sound "audio/splurt2.ogg"
            show mabj mabj12
            with flash
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp*"
            play sound "audio/splurt3.ogg"
            show mabj mabj13
            with flash
            play sound "audio/gulp2.mp3"
            m "*mmmm!!!!!*"
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp* *gulp* *gulp*"
            play sound "audio/splurt3.ogg"
            show mabj mabj14
            with flash
            call pauseInterface
            play sound "audio/splurt1.ogg"
            with flash
            yna "fuck! i can't stop!"
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp* *gulp* *gulp*"
            play sound "audio/gulp2.mp3"
            m "*gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp* *gulp*"
            m "...................."
            show mabj mabj15 with dissolve
            m "*gasp*"
            m "so 'uch 'um!"
            m "can't breathe...."
            show mabj_blink with Dissolve(0.2)
            play sound "audio/gulp2.mp3"
            m "{size=+5}*gulp!*"
            show mabj_eyesup
            hide mabj_blink
            with dissolve
            m "that... was so much..."
            m "i wasn't... i didn't... i wasn't expecting that..."
            show mabj mabj15_1 with dissolve
            m "do you... feel better?"
            m "did i do well?"
            yn "that was amazing...."
            show mabj mabj15_3 with dissolve

        "cum on face":
            show mabj mabj103
            m "are you-"
            yna "ngh!"
            play sound "audio/splurt2.ogg"
            show mabj mabj16
            with flash
            m "oh!"
            play sound "audio/splurt3.ogg"
            show mabj mabj17
            with flash
            m "*mmmmm* ....that's it, my prince..."
            m "get it all out..."
            m "use my face... like..."
            m "...like a cumrag, zuko!"
            play sound "audio/splurt3.ogg"
            show mabj mabj18
            with flash
            play sound "audio/splurt3.ogg"
            show mabj mabj18
            with flash
            call pauseInterface
            yna "fuck! it's so good!"
            m "...................."
            show mabj_eyesup
            with dissolve
            m "there's... so much on me..."
            m "i wasn't... i didn't... i wasn't expecting that..."
            m "it's... so warm. and sticky."
            m "...i can feel it dripping down my cheeks."
            show mabj mabj15_2 with dissolve
            m "do you... feel better?"
            m "did i do well?"
            yn "that was amazing...."
            show mabj mabj15_5 with dissolve

    m "good."
    m "i loved it, too."
    return
###### [Mei] Anal
label gallery_zem_anal:
    call gallery_dCharacters_2Love
    
    play music "audio/Unwritten Return.mp3" fadein 2
    show maan maan00 with sshake
    yng "whoa!"
    yng "you're ready, huh?"
    show maan maan08
    m "like you have no idea."
    ynd "watcha doing there?"
    m "...."
    yng "you're not getting cold feet are you, beautiful?"
    m "i'm preparing."
    m "...."
    play sound "audio/gltch2.mp3"
    show maan maan07
    with pflash
    m "{size=+6}ah!"

    yna "fuck!"
    call pauseInterface
    m "ahh... yes..."
    m "ah... ah..."
    yn "you okay?"
    m "it's... fine... i just need..."
    m "ah... need to adjust..."
    m "give me a minute to..."
    m "............"
    play sound "audio/gltch2.mp3"
    show maan maan102
    with vshake
    m "{size=+6}yes!"
    ync "ungh!"
    call pauseInterface
    m "yes, zuko!"
    show maan maan103
    call pauseInterface
    ync "ohhh..."
    m "yes... yes... yes!... yes!"
    ync "you're... ah... being a little... ah... rough..."
    m "don't be a baby, zuko..."
    m "i know you... ah... wanted this."
    m "you're so... easy to... ah... read."
    call pauseInterface
    m "i need more!"
    show maan maan104
    call pauseInterface
    ync "ah! what's gotten into you, mai?!"
    m "fuck... ah... \"slow\"..."
    m "i want you... ah... in..."
    m "in my fucking... ah... asshole..."
    call pauseInterface
    ync "mai, i can't last much longer..."
    scene maan19
    show maan maan101
    m "yeah, that's it, zuko! that's it!"
    call pauseInterface

    m "i'm gonna squeeze out every fucking drop when you cum."
    m "every fucking drop is going in my asshole, zuko."
    m "i don't even care what you want... i want an asshole full of cum."
    m "got it?"
    m "i'm not gonna slow down until you fill me up!"
    m "i want it! i want it!"

    menu:
        "stay with the close up":
            show maan maan101
            call pauseInterface
            m "i... mmph... feel you in there, zuko."
            m "my... ah... ass is very... ah... sensitive."
            m "you're swelling up... you're... ah... going to cum, aren't you?"
            m "cum zuko! cum for me!"
            m "fill my ass!"
            yna "here it comes!"
            m "yes, baby! cream in me!"
            play sound "audio/splurt3.ogg"
            show maan maan14
            with flash
            m "yes!"
            play sound "audio/splurt2.ogg"
            show maan maan15
            with flash
            m "oh zuko... ohh..."
            play sound "audio/splurt2.ogg"
            with flash
            m "it's... ah... wait..."
            play sound "audio/splurt3.ogg"
            show maan maan16
            with flash
            m "ah... st... stop... ah..."
            play sound "audio/splurt2.ogg"
            with flash
            m "mmmm... ah... so... satisfying... ahhh...."
            play sound "audio/splurt2.ogg"
            with flash
            m "......"
            m "it's... so.... there's so much..."
            yn "fuck..."
            ynd "what got into you?"
            m "well... i think... you did."
            show maan maan18
            show maan_spermdrip_closeup
            with dissolve
            m "i really needed that."
            m "...wow...look at that..."
            m "oh, that's... a lot... of... um..."
            call pauseInterface
            show maan maan08
            hide maan_spermdrip_closeup
            show maan_spermdrip
            with dissolve

        "zoom out":
            show maan maan104
            call pauseInterface
            m "i... mmph... feel you in there, zuko."
            m "my... ah... ass is very... ah... sensitive."
            m "you're swelling up... you're... ah... going to cum, aren't you?"
            m "cum zuko! cum for me!"
            m "fill my ass!"
            yna "here it comes!"
            m "yes, baby! cream in me!"
            play sound "audio/splurt3.ogg"
            show maan maan09
            with flash
            m "yes!"
            play sound "audio/splurt2.ogg"
            show maan maan10
            with flash
            m "oh zuko... ohh..."
            play sound "audio/splurt2.ogg"
            with flash
            m "it's... ah... wait..."
            play sound "audio/splurt3.ogg"
            show maan maan11
            with flash
            m "ah... st... stop... ah..."
            play sound "audio/splurt2.ogg"
            with flash
            m "mmmm... ah... so... satisfying... ahhh...."
            play sound "audio/splurt2.ogg"
            with flash
            m "......"
            m "it's... so.... there's so much..."
            yn "fuck..."
            ynd "what got into you?"
            m "well... i think... you did."
            show maan maan08
            show maan_spermdrip
            with dissolve
            m "i really needed that."
            m "...wow...look at that..."
            m "oh, that's... a lot... of... um..."

            call pauseInterface

    yn "that's a pretty view."
    call pauseInterface
    m "amazing."
    show maan maan00
    hide maan_spermdrip
    show nude_mai_fl_flip:
        xpos 100
    with dissolve
    
    return
###### [Mei] Sex
label gallery_zem_sex_start:
    call gallery_dCharacters_2Love

    $ maikup_spread = False
    $ maikup_pussylick = False
    $ maikup_anallick = False

    call gallery_zem_sex_foreplay
    call gallery_zem_sex
    call gallery_zem_sex_menu
    return

label gallery_zem_sex_foreplay:
    while not maikup_spread and not maikup_pussylick and not maikup_anallick:
        scene black
        scene bg_a_armory_1
        show azmu azmu15
        with Dissolve(0.35)

        menu:
            "spread her lips" if not maikup_spread:
                $ maikup_spread = True
                show azmu_pussyclosed
                with dissolve
                call pauseInterface
                show azmu azmu00 with dissolve
                m "what are you doing back there, zuko?"
                y "just getting a closer look."
                show azmu_pussyopen
                hide azmu_pussyclosed
                show azmu_blink
                with dissolve
                m "ohhh...."
                call pauseInterface
                menu:
                    "lick her pussy":
                        show azmu_pussylicking
                        show azmu_surprised with dissolve
                        m "oh!"
                        m "zuko...."
                        hide azmu_blink
                        call pauseInterface
                        menu:
                            "lick a little more":
                                call pauseInterface

                            "back to options":
                                pass
                    "back to options":
                        pass

            "lick her pussy" if not maikup_pussylick:
                $ maikup_pussylick = True
                show azmu_pussylicking
                call pauseInterface
                show azmu azmu00
                show azmu_surprised
                with dissolve
                m "oh!"
                call pauseInterface

                m "oh, my!"
                hide azmu_surprised
                show azmu_blink
                with dissolve
                m "*mmmmmm*"
                m "i didn't realize i needed a tongue bath."
                hide azmu_blink with dissolve
                m "was i getting messy back there?"
                call pauseInterface
                menu:
                    "lick a little more":
                        call pauseInterface

                    "back to options":
                        pass


            "lick her ass" if not maikup_anallick:
                $ maikup_anallick = True
                show azmu_pussylicking:
                    ypos -130 xpos -10

                show azmu azmu00
                show azmu_surprised
                hide azmu_pussylicking
                show azmu_pussylicking:
                    ypos -130 xpos -10
                with dissolve

                m "oh!"
                m "zuko, i don't know if-"
                show azmu_blink
                hide azmu_surprised
                with dissolve
                m "ohhh..."
                m "mmmmmm....."
                hide azmu_blink with dissolve
                m "you're really being... thorough back there."
                m "....don't stop."
                menu:
                    "lick a little more":
                        call pauseInterface
                    
                    "back to options":
                        pass

    return
label gallery_zem_sex:
    scene black
    scene bg_a_armory_1
    show azmu azmu00
    with dissolve
    m "zuko...."
    m "please.... put your cock inside me."
    show azmu azmu01 with dissolve
    call pauseInterface
    "you rest the tip of your cock against her lips."
    m "yes... that's it, baby..."
    yg "you want it? come get it."
    m "*mmmm*"
    m "that's my naughty prince."
    show azmu azmu08 with Dissolve(0.3)
    show azmu azmu02 with Dissolve(0.3)
    call pauseInterface
    "mai slides a little into your cock, pushing it just past her pussy lips."
    m "is that what you want?"
    y "fuck. yes."
    play sound "audio/gltch2.mp3"
    show azmu azmu03
    with pflash
    m "{i}ohhhh...."
    "with a slow, determined push, mai presses your cock into her hot, welcoming pussy."
    call pauseInterface
    m "fuck...."
    m "now you stay right there...."
    m "i'm going to do all the work, baby."
    show azmu azmu100
    call pauseInterface
    m "i've waited so long for you..."
    m "is it everything you wanted?"
    m "it's better than i dreamed of... and i've been dreaming of this since we were kids."
    show azmu azmu102
    m "i can't believe your perfect, fat cock is inside me."
    m "zuko, i can't...."
    show azmu azmu100_1
    call pauseInterface
    y "fuck..."
    m "i need you."
    m "i'm so happy here with you."

    show azmu azmu102_1
    m "i promise to give you anything you need."
    call pauseInterface
    m "stay with me and i promise to give you whatever you want, whenever you want it."
    m "because...."

    show azmu azmu101
    call pauseInterface
    m "i want it, too."
    call pauseInterface
    m "i'm going to take care of you, baby. my poor baby. you have such needs."
    m "i'm here to make them... easier."

    return
label gallery_zem_sex_menu:
    m "how do you want it?"

    while True:
        menu:
            "fast - smooth":
                show azmu azmu100_2
            "fast - hard":
                show azmu azmu101_1
            "fast - hard (No Shake)":
                show azmu azmu101_3
            "slow - smooth":
                show azmu azmu100
            "slow - hard":
                show azmu azmu101_2
            "slow - hard (No Shake)":
                show azmu azmu101_4
            "cum":
                show azmu azmu100_3
                call pauseInterface
                m "yes, baby fuck this cunt!"
                m "cum for me!"
                m "i wanna feel your hot load, zuko!"

                menu:
                    "cum inside":
                        show azmu azmu06
                        m "yes, nut in me, my prince!"
                        m "empty that fat cock in my hot little pussy!"
                        ya "ngh!"
                        play sound "audio/splurt2.ogg"
                        show azmu_inpussperm1
                        with flash
                        m "oh!"
                        m "it's warm!"
                        play sound "audio/splurt2.ogg"
                        show azmu_inpussperm2
                        hide azmu_inpussperm1
                        with flash
                        m "*mmmmm* yes, zuko, you're doing so good...."
                        m "...don't stop..."
                        ya "fuck!"
                        play sound "audio/splurt3.ogg"
                        show azmu_inpussperm3
                        hide azmu_inpussperm2
                        with flash
                        call pauseInterface
                        show azmu azmu00
                        hide azmu_inpussperm3
                        show azmu_inpussperm4
                        show azrr_fertilize
                        with dissolve

                    "cum outside":
                        show azmu azmu00
                        show azmu_masturbate
                        with dissolve
                        call pauseInterface
                        m "yes, nut on me, my prince!"
                        m "empty that fat cock on my hot little pussy!"
                        ya "ngh!"
                        play sound "audio/splurt2.ogg"
                        show azmu_buttsperm1
                        show azmu_surprised
                        with flash
                        m "oh!"
                        m "it's warm!"
                        play sound "audio/splurt2.ogg"
                        show azmu_buttsperm2
                        hide azmu_buttsperm1
                        hide azmu_surprised
                        with flash
                        m "*mmmmm* yes, zuko, you're doing so good...."
                        m "...don't stop..."
                        ya "fuck!"
                        play sound "audio/splurt3.ogg"
                        show azmu_buttsperm3
                        hide azmu_buttsperm2
                        hide azmu_masturbate
                        with flash
                        call pauseInterface

                m "thank you, zuko."
                m "and i... i'm so happy with you."
                m "I love you."
                
                return

        m "ah, fuck yes baby..."
        call pauseInterface

image azmu azmu101_3:
    "azmu azmu01"
    0.12
    "azmu azmu08"
    0.12
    "azmu azmu10"
    0.12
    "azmu azmu12"
    0.12
    "azmu azmu22"
    0.3
    "azmu azmu05"
    0.15
    "azmu azmu03"
    0.15
    repeat
image azmu azmu101_4:
    "azmu azmu01"
    0.2
    "azmu azmu08"
    0.2
    "azmu azmu10"
    0.2
    "azmu azmu12"
    0.2
    "azmu azmu22"
    0.7
    "azmu azmu05"
    0.3
    "azmu azmu03"
    0.3
    repeat
###### [Mei] Lick Azula
label gallery_lick_azula:
    call gallery_dCharacters_2Love

    $ mai_azula_lick = True

    scene bg_a_armory_2_1
    show azml azml02
    show windowlickscene
    with Dissolve(.35)
    call pauseInterface
    yd "what the..."
    a "now, that's better."
    show azml azml04 with Dissolve(.35)
    a "i have no patience tonight."
    call pauseInterface
    show azml azml03 with Dissolve(.35)
    call pauseInterface
    a "now..."
    a "get. started."
    ya "that bitch! who the fuck is she-"
    show azml_licking with Dissolve(.35)
    yg "oh... hot damn!"
    yg "this is super hot, but.... what the hell!?"
    call pauseInterface
    yg "now {i}that's{/i} a pretty sight."
    a "{i}ahh{/i}... yes..."
    a "....right there..."
    a "you're getting better, mai."
    show azml azml01 with Dissolve(.35)
    a "it's almost a shame."
    a "i so enjoyed your scared, tentative licks."
    a "of course... this is... mmmm... very... ah... nice as well..."
    m "....."
    call pauseInterface
    show azml azml02 with Dissolve(0.35)
    a "ah... damn it, mai..."
    a "tongue my cunt... lick me clean..."
    a "i've had such a... difficult... day...."
    a "guards not doing what they're told..."
    a "the wrong peasants rioting...."
    yd "(wrong peasants?)"
    a "i... fuuck... i need this so badly..."
    a "it's so difficult being royalty..."
    a "and i've wanted you to lick my pussy for so long..."
    show azml azml04 with Dissolve(0.35)
    a "you're having.... mmmm.... fun aren't you?"
    m "......"
    a "{i}aren't you?"
    m "mmhmm... yes....."
    a "that's a good girl, mai..."
    show azml azml03 with Dissolve(0.35)
    a "now, eat up..."
    show azml azml01 with Dissolve(0.35)
    a "and pleasure your princess."
    m "i... thought we were friends..."
    a "oh, but we are..."
    a "this is what friends do, mai."
    a "and it's.... mmmgh fuck!... what friends of {i}princesses{/i} do."
    a "get in there!"
    a "eat that fucking cunt!"
    a "oh! i'm going to... i'm fucking... ah.... ah.......ah... ah..ah..ah..ah...."
    show azml azml01 with Dissolve(0.35)
    show azml_small_pussyjuice
    with vshake
    a "ah!!!"
    call pauseInterface
    hide azml_licking
    show mai_1
    hide azml_small_pussyjuice
    show azml_small_pussyjuice
    with Dissolve(0.35)
    m "azula? are we-"
    show azml azml04 with Dissolve(0.35)
    a "that's {i}princess{/i} azula to you right now, mai."
    a "and who told you to stop?"
    m "i just... i thought since you-"
    a "get back in there!"
    show azml azml02 with Dissolve(0.35)
    a "i'm not finished creaming on your pretty face."
    a "now do as your princess commands!"
    m "........"
    hide mai_1
    show azml_licking
    hide azml_small_pussyjuice
    show azml_small_pussyjuice
    with Dissolve(0.35)
    call pauseInterface
    yg "that's it, i need a closer look."
    scene black with dissolve
    "there's a side door next to the window that's unlocked."
    "you enter."

    show azml azml01
    show azml_licking
    show azml_small_pussyjuice
    with Dissolve(0.35)
    yg "hello, girls."
    hide azml_small_pussyjuice
    hide azml_licking
    show azml_maifacesyou
    with Dissolve(0.35)
    m "zuko! what-!"
    call pauseInterface
    show azml azml03
    show azml_lookatplayer
    with Dissolve(0.35)

    a "hello, zuko. enjoying the view?"
    a "i was just giving mai her bedtime snack."
    m "I wasn't... it's not..."
    hide azml_lookatplayer with Dissolve(0.35)
    a "did i tell you to stop, mai?"
    a "you know what happens if you do."

    a "and zuko.... this might be just the thing I need to forgive you."
    m ".........."
    y "tell you what, how about you go ahead and fuck her face."
    y "as a peace offering."
    m "hey...."
    y "i'll let you use her mouth to your content and then you and i are square."
    y "deal?"
    a "....oh very well."
    a "i just can't stay mad at you."
    a "we're family, after all."
    a "now, get to it, mai!"


    m ".........."
    hide azml_maifacesyou
    show azml_licking
    hide azml_small_pussyjuice
    show azml_small_pussyjuice
    with Dissolve(0.35)
    yd "so what happens if she stops?"
    show azml_lookatplayer with Dissolve(0.35)
    a "oh, that's between mai and i."
    a "very rude of you to ask, zuzu. tut tut."

    y "so when-"
    show azml azml02
    hide azml_lookatplayer
    with Dissolve(0.35)
    a "if you're going to stay, you're not allowed to talk."
    a "this is just a couple girls having fun."
    hide azml_licking
    hide azml_small_pussyjuice
    show azml_maifacesyou
    with Dissolve(0.35)
    m "it's really not-"
    a "quiet, mai."
    a "if you stop-"
    a "look what you've done."
    a "you'll have to wet me again."
    hide azml_maifacesyou
    show azml_licking
    with Dissolve(0.35)
    a "well, zuzu, this is where i go to vent, in any case."

    show azml azml100
    hide azml_licking
    with Dissolve(0.35)
    call pauseInterface
    a "you have no idea how difficult it is to be the ruling family."
    a "not just of the fire nation, but of the world, soon."
    a "besides..."
    show azml azml101
    call pauseInterface
    a "oh, fuck... i think..."
    a "i think i'm going to... ah... cream again....."
    a "...nnngh...."
    a "fuck!"
    show azml azml100
    show azml_big_pussyjuice
    with vshake
    a "angh...."
    a "don't... stop..."
    a "what..."
    a "ah...! ah...."
    call pauseInterface
    a "....what was i saying?"
    m "something about the ruling family?"
    a "right... ah... interbreeding is an ancient royal tradition."
    a "you knew that, didn't you?"
    m "....."
    a "mai...."
    m "...yes."
    a "mmmm..."
    a "love that vibration."
    a "only other royalty understand the stresses and responsibilities of ruling."
    a "and in the pursuit of keeping royal blood pure, certain... actions... are required."
    a "usually between brother and sister."
    m "i... i guess i haven't thought about..."
    a "mmmm.... no, you haven't, have you?"
    a "very.... ah... fuck me... selfish."
    scene black
    scene bg_a_armory_2_1
    show azml azml01
    show azml_licking
    show azml_small_pussyjuice
    with dissolve
    a "I think... i have one left in me..."
    a "moan for me."
    m "...mm...."
    a "no. do better."
    m "......"
    m "mmmmmmmmmmm......"
    a "yes... more... more..."
    m "mmmhmmmhmmmm...."
    a "fuck, fuck, fuck!"
    m "mmmmmmmhhhhhhmmmmmmmmmhmmhhhhmmmmmm"
    a "aaaahhhh...!!!"
    with vshake
    a "fuck!"
    a "stop!"
    a "...i said stop!!!"
    show mai_1
    hide azml_licking
    hide azml_small_pussyjuice
    show azml_small_pussyjuice
    with dissolve
    a "ohh... mmm..."
    show azml azml04
    with dissolve
    a "very well done, mai."
    a "now, stay still."
    scene black with dissolve
    "azula leans back and slowly rubs her cunt down mai's face."
    scene bg_a_armory_2_1
    show azml azml13
    show azml_big_pussyjuice:
        xpos 62 ypos -80
    show azml_small_pussyjuice:
        xpos -40 ypos -100
    with dissolve
    a "perfect. stay just like that until i leave."
    m "*pant*-*pant*"
    call pauseInterface
    "azula dresses herself as mai tries to regain her breath, soaked, on the floor."
    call pauseInterface
    scene black
    scene bg_a_armory_2_1
    show a_blink:
        xpos -350
    show mfn
    show azml_small_pussyjuice:
        xpos 80 ypos -231
    with dissolve

    a "good night, zuko."
    return
###### [Ending] Fuck Mai
label gallery_mai_ring_on:
    call gallery_dCharacters_2Love

    menu:
        "Pregnant":
            $ mai_preg = True
        "Not":
            $ mai_preg = False;

    scene bg_maiend_beach1
    show b2ma b2ma05 with dissolve
    "mai's clothes split and drop to the floor."
    call pauseInterface
    m "now for yours."
    yc "aw man... i liked these pants."
    yc "they're the only ones i own."
    with vshake
    "mai slices off your clothing with quick precision."
    y "remind me to never get on your bad side when there are knives around."
    m "don't worry... i will."
    sg "well, by the power vested in me by two old witches that live in the shack on the dock and seem to run everything..."
    sg "i now pronounce you husband and wife!"
    sg "you may now fuck the bride!"
    y "grea-"
    yd "what."
    m "we consumate our love, zuko."
    m "you really don't know anything."
    yd "uh. here? in public?"
    m "there are only a few stragglers. it's normal."
    yd "......."
    yd "well, a man's gotta do what a man's gotta do...."
    scene black with dissolve
    show bg_maiend_beach2
    show b2ma b2ma07
    with dissolve
    call pauseInterface
    m "my pussy is your responsibility now, zuko."
    m "you have to beat it, take care of it.... {i}own{/i} it. starting now."
    show b2ma b2ma08 with dissolve
    call pauseInterface
    m "don't be shy, husband."
    y "one thing i'm not is shy."
    show b2ma b2ma09 with dissolve
    m "mmm... that's my big, thick, man."
    m "give me your love."
    show b2ma b2ma11 with dissolve
    m "yes...."
    show b2ma b2ma100
    call pauseInterface
    m "yes, zuko... make love to me..."
    m "make me yours, forever and always..."
    m "i'll be-"
    show b2ma b2ma101
    m "oh!"
    m "getting a little rougher, i see...."
    call pauseInterface
    m "ngh! ah!"
    m "i'll be your partner, your sex toy, your-"
    show b2ma b2ma102
    show b2ma_blink with dissolve
    call pauseInterface
    m "ah... ah... maid... ah... fuck... ah..."
    m "....friend....ah...."
    hide b2ma_blink with dissolve
    show b2ma b2ma104
    call pauseInterface
    m "f...fuck...."
    m "yes..."
    m "oh, zuko....."
    m "harder... harder..."
    show b2ma b2ma103
    call pauseInterface
    m "yes... yes... fuck me! fuck me, zuko!"
    m "fuck me, husband!"
    ya "i'm cumming, wife!"
    m "cum, husband! cum!"
    m "mark me!"
    m "let them all know i'm taken!"
    call pauseInterface
    m "take me!"
    menu:
        "cum inside":
            if not mai_preg:
                play sound "audio/splurt2.ogg"
                show b2ma b2ma17
                with flash
                m "yes!"
                play sound "audio/splurt1.ogg"
                with flash
                ya "take my jizz, wife!"
                m "please!"
                play sound "audio/splurt1.ogg"
                with flash
                m "ohh...."
                show b2ma b2ma09
                show azrr_fertilize
            else:
                play sound "audio/splurt2.ogg"
                show b2ma b2ma17
                with flash
                m "yes!"
                play sound "audio/splurt1.ogg"
                with flash
                ya "take my jizz, wife!"
                m "please!"
                play sound "audio/splurt1.ogg"
                with flash
                m "ohh...."
                show b2ma b2ma09

            show b2ma_sperm4
            with flash
            call pauseInterface
            m "oh, zuko...."
        "cum outside":
            show b2ma b2ma09 with Dissolve(0.2)
            play sound "audio/splurt2.ogg"
            show b2ma_spermshot
            pause 0.3
            hide b2ma_spermshot
            show b2ma_sperm1
            call pauseInterface
            m "mmmm...."
            play sound "audio/splurt3.ogg"
            show b2ma_spermshot
            pause 0.3
            hide b2ma_spermshot
            show b2ma_sperm2
            call pauseInterface
            ya "take my jizz, wife!"
            m "please!"
            hide b2ma_sperm1
            play sound "audio/splurt2.ogg"
            show b2ma_spermshot
            pause 0.3
            hide b2ma_spermshot
            show b2ma_sperm3
            call pauseInterface
            m "ohh...."
            hide b2ma_sperm2
            call pauseInterface
    play sound "audio/applause.mp3"
    "there's a very polite burst of applause that takes you by surprise."
    y "i... forgot that there were people there...."
    m "you did very well, hunny."
    m "walking is going to... be difficult."
    scene black with dissolve
    scene bg_maiend_beach1
    show b2ma b2ma05
    with dissolve
    y "well, that was something." 

    return
###### [Ending] Azula Blowjob
label gallery_azula_blowjob:
    call gallery_dCharacters_2Love

    menu:
        "Pregnant":
            $ azula_preg = True
        "Not":
            $ azula_preg = False;

    scene bk2_night01
    show b2az b2az04
    with dissolve

    y "i love you, azula."
    y "i think we may both be monsters...."
    y "but god help me, i love you."
    show b2az_blush with dissolve
    a "oh...."
    a "i...."
    a "...i love you too."
    a "now stop fucking around and work my mouth."
    hide b2az_solodick
    show b2az_openmouth
    show b2az_solodick
    hide b2az_handson
    with dissolve

    ys "you want it?"
    a "ple-"

    hide b2az_solodick
    hide b2az_openmouth
    show b2az_bj_ani
    a "mmm!"
    call pauseInterface
    y "oh, sis... it's so perfect... "
    y "your mouth is so warm...."

    hide b2az_bj_ani
    show b2az_bj_ani2
    show b2az_blink with dissolve
    call pauseInterface
    a "*slurp* *gulp*"
    y "yes... yes..."
    hide b2az_bj_ani2
    show b2az_bj_ani3
    hide b2az_blink with dissolve
    call pauseInterface
    y "fuck... fuck..."
    a "hngh! mmngh! *sluurp*"
    hide b2az_bj_ani3
    show b2az_bj_ani4
    show b2az_blink with dissolve
    call pauseInterface
    "azula slurps and gags obediently as you slam your cock against the back of her throat."
    "her soft lips surround and suck at your shaft as you hump her unresisting face."
    a "*gltch* *gulp*"
    y "angh! i'm gonna cum!"
    hide b2az_blink with dissolve
    a "*slurp* mgh! *slurp* *gulp*"

    menu:
        "in her mouth":
            play sound "audio/splurt2.ogg"
            hide b2az_bj_ani4
            show az_knee_d4
            show b2az_blink
            with flash
            a "mgh!"
            a "*gulp* *gulp*"
            if azula_preg:
                a "feed my baby!"
            play sound "audio/splurt3.ogg"
            with flash
            hide b2az_blink with dissolve
            a "*gulp* *gulp* *gulp*"
            hide az_knee_d4
            show b2az_openmouth
            with dissolve
            play sound "audio/splurt2.ogg"
            hide b2az_blink
            show c_fuck_spermoutside_01 at Position (xpos = 0.42, xanchor=0.5, ypos=0.3, yanchor=0.5)
            with flash
            a "yes!"
            call pauseInterface
            hide b2az_openmouth with dissolve
            a "i wanted to taste it all..."
            a "...but at least my face is warm."
            
        "on her face":
            hide b2az_bj_ani4
            hide b2az_solodick
            show b2az_openmouth
            with dissolve
            a "give me your cum, brother!"
            if azula_preg:
                a "feed my baby!"
            play sound "audio/splurt2.ogg"
            hide b2az_blink_ani
            show c_fuck_spermoutside_01 at Position (xpos = 0.42, xanchor=0.5, ypos=0.21, yanchor=0.5)
            with flash
            a "fuck yes!"
            play sound "audio/splurt3.ogg"
            hide c_fuck_spermoutside_01

            show c_fuck_spermoutside_02 at Position (xpos = 0.42, xanchor=0.5, ypos=0.2, yanchor=0.5)
            show c_fuck_spermoutside_01 at Position (xpos = 0.42, xanchor=0.5, ypos=0.5, yanchor=0.5)
            with flash
            a "ohh....."
            call pauseInterface
            hide b2az_openmouth with dissolve
            a "i wanted to taste it..."
            a "...but at least my face is warm."

    call pauseInterface

    $ azula_preg = False;
    return
###### [Ending] Throne Fuck
label gallery_zthronebone1:
    call gallery_dCharacters_2Love

    show aztr aztr01 with dissolve
    t "hey guys, has it start- oh, my!"
    m "yeah."
    scene aztr aztr05 with Dissolve(0.7)
    "the people stand around and watch in anticipation."
    "it's clear this will be a very unorthodox ceremony...."
    show aztr aztr06 with dissolve
    y "before we begin...."
    y "from now on, this day shall be known as..."
    y "....blow the firelord day!"
    "there are some murmurs in the crowd as not everyone agrees..."
    "...but some people unexpectedly kneel in case you walk by and smack them with your dick."
    ys "neat."
    y "now, i'd like to introduce azula, my...."

    y "....azula, my wife."
    show aztr aztr07 with dissolve
    y "she rules by my side and is subject only to myself and my cock."
    y "you will obey me... and thus, her."

    show aztr aztr08 with Dissolve(1.0)
    pause 0.8
    call pauseInterface
    y "azula!"
    a "my lord?"
    y "you will alway ride me during judgements, and-"
    yd "...."
    yd "look at me, woman!"
    show aztr aztr09 with Dissolve(0.8)
    a "yes, dear?"
    y "you will ride me during every throneroom session, is that understood?"
    a "of course, my love."
    a "would you like me to get started? to help you enjoy the ceremony?"
    y "yes, i believe i would."
    show aztr aztr08 with Dissolve(0.8)
    a "very well, my lord."
    call pauseInterface

    show aztr aztr19 with Dissolve(0.8)
    call pauseInterface
    show aztr aztr100_1
    pause 0.9
    play sound "audio/gltch2.mp3"
    with pflash
    call pauseInterface
    "azula slips your cock into her soaking pussy in one fluid motion."
    with ushake
    "you can feel her pussy grip you and quiver slightly, and can tell she's putting on a good show...."
    "....but is struggling to take you."
    show aztr aztr100
    call pauseInterface
    y "that's it, dear."
    y "now.... i believe we were here to celebrate something?"
    "the crowd murmurs, stunned, as azula's pussy slurps and slaps against you, engulfing your cock repeatedly."
    "the sounds of wet, hard fucking reverberate throughout the throne room."
    y "come now.... where's that crown?"
    "crowd" "they're siblings! what the fuck!?"
    "a ripple runs through the people as a new face emerges...."
    show aztr aztr01 with dissolve
    pause 0.5
    show aztr aztr02 with dissolve
    pause 0.5
    oz "what-"
    show aztr aztr04 with dissolve
    oz "......"
    oz "hgnh..."
    m "she's actually doing an impressive job of-"
    show aztr aztr03 with dissolve
    oz "shut up!"
    oz "what the {i}hell{/i} is going on here!?"
    y "ah, father.... welcome."
    show az_player_body_0
    show aztr aztr100
    with dissolve
    y "have you come to congratulate me?"
    oz "con.... congratulate you!?"
    oz "you're fucking your sister in front of the whole city!"
    y "yeah.... isn't it great?"
    oz "......no!"
    "crowd" "you gotta admit though, zuko's got style..."
    oz "shut up, you!"
    hide az_player_body_0 with dissolve
    a "i'm right here, father."
    a "there's no need to talk around me."
    call pauseInterface
    oz "i see you slamming on your older brother's.... member, azula."
    oz "get off of him right now."
    a "i have to get {i}him{/i} off first."
    oz "that's not what i meant!"
    a "well, how about this-"
    show aztr aztr100_2
    call pauseInterface
    yc "oh... fuck...."
    "azula speeds up as the slurping, smacking sounds of your cock plunging into her cunt get louder and more wild."
    oz "stop it! stop!"
    y "what's wrong, {i}ozai{/i}?"
    y "come firebend."
    ys "oh, did you forget how?"
    oz "it.... it was taken from me...."
    y "well.... i can still firebend."
    ya "so, why don't you come over here, so i can burn your fucking face while i fuck your perfect daughter?"
    oz "......"
    yd "what, no clever comment?"
    ya "the fire nation is mine, you vicious, bitter, insane old shit."
    oz "you-"
    ya "that's it!"
    show aztr aztr101
    "you snap your fingers and azula immediately responds."
    call pauseInterface
    "she changes pace to slam violently into your cock."
    "every time she pulls her pussy up, she squeezes, milking your shaft with a hard, calm determination."
    "azula has clearly learned to channel her ruthlessness into making you orgasm."
    call pauseInterface
    ya "speak again, {i}ozai{/i}."
    ya "say something else."
    ya "i {i}beg{/i} you."
    oz "........."
    oz "zu-"
    show aztr aztr101_1
    "you snap your fingers again, and azula picks up her pace."
    call pauseInterface
    y "do you like that, father?"
    ys "i'm fucking your precious azula on your throne."
    yd "well... she's fucking me..."
    ys "on my throne, now."
    y "why don't you tell him, azula?"
    a "fuck me harder, daddy!"
    oz "what."
    a "zuzu is my daddy, now."
    a "i belong to him."
    call pauseInterface
    a "he is my man, my lover, my daddy, the father of my soon-to-be child."
    a "i am his, and he is mine."
    a "i will fuck him, forever, and you disgust me."
    y "well said."
    ya "guards!"
    ys "i'm done. take him away."
    show aztr aztr04 with dissolve
    oz "wh...what?"
    show aztr aztr03 with dissolve
    oz "you can't do this!"
    ys "tell him, azula."
    a "fuck you, ozai!"
    show aztr aztr101_1
    call pauseInterface
    a "zuzu and i don't want you around! i want his thick, painful cock in my all the time!"
    yd "pain... painful?"
    a "well, you're too big right now.... i hope i adjust eventually..."
    yg "i hope you don't. tight is good."
    a "yes, my lord!"
    oz "no!"
    "the guards take ozai away to the prison."
    yc "oh fuck, azula.... i think i'm going to cum...."
    a "yes! do it! cum for me! in front of everyone!"
    "crowd" "yeah! make him cum, queen azula!"
    "crowd" "fill that cunt, firelord zuko!"
    "crowd" "our new rulers are the best!"
    menu:
        "cum in pussy":
            play sound "audio/splurt2.ogg"
            show aztr aztr15
            show aztr_sperminpuss_1
            with flash
            call pauseInterface
            yc "fuck!"
            a "yes, baby!"
            play sound "audio/splurt2.ogg"
            show aztr_sperminpuss_2
            hide aztr_sperminpuss_1
            with flash
            call pauseInterface
            a "don't leave room in there for anything but your thick, sticky load!"
            play sound "audio/splurt3.ogg"
            show aztr_sperminpuss_3
            hide aztr_sperminpuss_2
            with flash
            call pauseInterface
            yc "dammit, azula.... you feel too good..."
            show aztr aztr08
            show aztr_spermonass_0
            hide aztr_sperminpuss_3
            with dissolve
            call pauseInterface
            
        "cum on ass":
            play sound "audio/splurt2.ogg"
            show aztr aztr08
            show aztr_spermonass_1
            with flash
            call pauseInterface
            yc "fuck!"
            a "yes, baby!"
            play sound "audio/splurt2.ogg"
            show aztr_spermonass_2
            hide aztr_spermonass_1
            with flash
            call pauseInterface
            a "don't leave room in there for anything but your thick, sticky load!"
            play sound "audio/splurt3.ogg"
            show aztr_spermonass_3
            hide aztr_spermonass_2
            with flash
            call pauseInterface
            yc "dammit, azula.... you feel too good..."

    a "mmmm...."
    a "well, now that is certainly a mess."
    a "maids! i expect you to come clean us!"
    a "with your tongues! that's an order!"
    yc "man, i am spent...."
    
    return
###### [Ending] Foursome
label gallery_zuko_true_end:
    call gallery_dCharacters_2Love

    scene bg_a_threesome_02 with dissolve
    show az3sm az3sm07 with dissolve
    call pauseInterface
    y "whoa, hey mai. why are you here?"
    m "...azula asked me here. naked."
    y "and you just came?"
    m "she's been different lately."
    "*knock knock*"
    y "i'll get it."
    show tf with dissolve
    t "oh, hey you! azula asked me to come by."
    y "you too?"
    t "yeah! hold on..."
    hide tf with dissolve
    show az3sm az3sm08 with dissolve
    y "Uh..."
    y "what's-"
    show a_blink with dissolve
    a "oh, i see you're already here."
    y "what's going on?"
    a "well... since you've been so wonderful..."
    a "we thought we'd have a little fun..."
    hide a_blink with dissolve
    show az3sm az3sm09 with dissolve
    a "how does that sound?"
    y "sweet!"
    a "excellent."
    a "in that case...."
    scene black
    show b2te b2te01
    show b2te_azeyesonyou
    with dissolve
    call pauseInterface
    a "get behind me, zuko."
    y "behind... you?"
    a "i want you to rub my clit with that big cock."
    show b2te_solodick
    hide b2te_azeyesonyou
    with dissolve
    y "like this?"
    a "ahh..."
    a "can you... rub it?"

    show b2te b2te104
    show b2te_azcumface
    hide b2te_solodick
    hide b2te_azeyesonyou
    with dissolve
    a "ahh... mmmnh...."
    call pauseInterface
    a "i love this big fucking....."
    show b2te_azeyesonyou
    hide b2te_azcumface
    with dissolve
    a "you deserve a little more pleasure, i think..."
    a "ty lee!"

    hide b2te_azeyesonyou
    show b2te b2te11_1
    with dissolve
    a "get down here..."
    a "you're going to suck his cock!"
    a "under my supervision, of course..."
    show b2te b2te02
    show b2te_azblink_ani
    hide b2te_solodick
    with dissolve
    call pauseInterface
    show b2te b2te03 with dissolve
    t "i see you, zuko!"
    t "don't be shy!"
    show b2te b2te100 with dissolve
    show b2te_tyleeblink_ani
    call pauseInterface
    t "*sluurrp*"
    t "mmmm... you taste nice, azula!"
    show b2te_azcumface with dissolve
    "azula shivers with pleasure as you rub against her."
    a "yes... oh, zuzu...."
    call pauseInterface
    show b2te b2te06 with Dissolve(0.2)
    t "mmm!"
    t "*slurp* *gulp*"
    hide b2te_azcumface
    show b2te_azeyesonyou
    with dissolve
    a "is something wrong?"
    t "*gulp* *sluuurp*"
    y "i just feel like mai is missing out."
    a "hmmm... you have a point..."
    hide b2te_azeyesonyou with dissolve
    a "switch!"
    hide b2te_tyleeblink_ani
    show b2te b2te01
    with dissolve
    a "mai, come here..."
    show b2te b2te10 with dissolve
    show b2te_maiblink_ani
    call pauseInterface
    m "i'm ready, love."
    m "let me lick azula's juices off of you."
    show b2te b2te101
    m "mmngh.... *slurrp*"
    call pauseInterface
    a "you look good down there, mai."
    a "it's nice to still be in charge where it counts."
    show b2te_azeyesonyou with dissolve
    a "how are you, sexy?"
    y "i'm doing-"
    hide b2te_azeyesonyou
    show b2te_azblink
    with dissolve
    y "...."
    y "how are {i}you{/i}, sis?"
    a "ahh.... mmmh...."
    a "so... so good...."
    a "ah...ha... i'm ... ah..."
    y "are you gonna cum?"
    a "I'm... i'm gonna..."
    show b2te_azcumface
    hide b2te_azblink
    with dissolve
    a "ohhh... fuck!"
    $ truend_fluid = True
    with vshake
    a "nngh...."
    call pauseInterface
    hide b2te_azcumface
    show b2te_azeyesonyou
    with dissolve
    a "are you close?"
    y "fffuuuckk....."
    a "now, {i}that's{/i} a yes...."
    a "should they switch?"
    hide b2te_azeyesonyou with dissolve

    menu:
        "cum on ty lee":
            show b2te b2te103
            hide b2te_maiblink_ani

            with dissolve
            t "I'm ready!"
            call pauseInterface
            y "fuck... fuck... fuck...!"

            show b2te b2te04
            show b2te_tyleemouth
            with dissolve

            t "go ahead, zuko!"
            t "cum for me!"
            play sound "audio/splurt2.ogg"
            show b2te_spermshot
            show b2te_sperm1
            pause 0.3
            hide b2te_spermshot
            a "ahh...!"
            play sound "audio/splurt1.ogg"
            show b2te_spermshot
            show b2te_sperm2
            pause 0.3
            hide b2te_spermshot

            hide b2te_sperm1
            t "mmgh!"
            t "*gulp!*"
            play sound "audio/splurt2.ogg"
            show b2te_spermshot
            show b2te_sperm3
            pause 0.3
            hide b2te_spermshot
            hide b2te_sperm2

            call pauseInterface
            a "that's a good look for you, ty lee."
            t "mmghagh...."
            a "swallow when you're ready..."
            a "we'll wait."
            t "......."
            show b2te b2te04
            hide b2te_sperm3
            show b2te_sperm1
            hide b2te_tyleemouth
            with dissolve
            t "*gulp!*"
            hide b2te_sperm1
            show b2te_sperm1
            show b2te_tyleemouth
            with dissolve
            t "yum!"

        "cum on mai":
            show b2te b2te102

            hide b2te_maiblink_ani
            with dissolve
            m "i'm ready!"
            call pauseInterface
            y "fuck... fuck... fuck...!"
            show b2te b2te11
            show b2te_maimouth
            with dissolve
            m "go ahead, baby!"
            m "cum for me!"
            play sound "audio/splurt2.ogg"
            show b2te_spermshot
            show b2te_sperm1
            pause 0.3
            hide b2te_spermshot
            a "ahh...!"
            play sound "audio/splurt1.ogg"
            show b2te_spermshot
            show b2te_sperm2
            pause 0.3
            hide b2te_spermshot

            hide b2te_sperm1
            m "mmgh!"
            m "*gulp!*"
            play sound "audio/splurt2.ogg"
            show b2te_spermshot
            show b2te_sperm3
            pause 0.3
            hide b2te_spermshot
            hide b2te_sperm2

            call pauseInterface
            a "that's a good look for you, mai."
            m "mmghagh...."
            a "swallow when you're ready..."
            a "we'll wait."
            m "......."
            show b2te b2te11
            hide b2te_sperm3
            show b2te_sperm1
            hide b2te_maimouth
            with dissolve
            m "*gulp!*"
            hide b2te_sperm1
            show b2te_sperm1
            show b2te_maimouth
            with dissolve
            m "yum."

    a "very nice."
    a "you two get cleaned up... i want to go for a walk with zuko."
    show b2te_azeyesonyou with dissolve
    a "is that okay?"
    y "sure..."
    y "i'm feeling pretty accepting right now."
    a "alright... let's put on some clothes and step outside..."
    a "go ahead, i'll meet you outside in a minute."
    call pauseInterface

    return
#--
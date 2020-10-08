label gallery_dCharacter_3Common:
    $ k3 = Character("Katara", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ jd = Character("joo dee", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ t = Character("toph", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ mv = Character("mysterious voice", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ girl = Character("girl", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ju = Character("june", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ jin = Character("jin", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ct = Character("Ajala", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)

    $ povname = "avatar"
    $ avatar = "player"
    $ bk3name = 'Aang'
    $ trigger = "buttsluts"

    $ y = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), ConditionSwitch(
            "avatar == 'jack'", "pumpkin/p_fr_sidebox_neutral.png",
            "avatar == 'player'", "p_fr_sidebox_neutral.png",),
        (0, 0), ConditionSwitch(
            "avatar == 'player'", "p_fr_sidebox_mask.png",
            "avatar == 'jack'", "transparent.png",),), 
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ya = Character("[povname]", color="#000000", show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), ConditionSwitch(
                "avatar == 'jack'", "pumpkin/p_fr_sidebox_angry.png",
                "avatar == 'player'", "p_fr_sidebox_angry.png",),
            (0, 0), ConditionSwitch(
                "avatar == 'player'", "p_fr_sidebox_mask.png",
                "avatar == 'jack'", "transparent.png",),),
            window_left_padding=220, show_two_window=True, who_xpos=36)
    
    return
#--

###### [Katara] Lake Blowjob
label gallery_after_store_train:
    call gallery_dCharacter_3Common

    $ katara_blowjob_holdhead = False
    $ toph_top_nude = True
    
    stop music fadeout 1
    play music "audio/Unwritten Return.mp3"
    scene lake_laogai_2
    show tokb tokb00
    with dissolve
    y "Umm...."
    show tokb tokb01 with dissolve
    k3 "i'm ready to... kiss you now."
    y "......"
    y "are you sure?"
    k3 "yes..."
    show tokb tokb02 with dissolve
    y "...you really sure?"
    show tokb tokb04 with dissolve
    call pauseInterface
    show tokb tokb05 with dissolve
    y "I guess that answers that."
    show tokb tokb07 with dissolve
    k3 "mmm..."
    show tokb tokb100
    call pauseInterface
    k3 "*sluurp*"
    t "what's going on?"
    t "are you really kissing?"
    show toi toi212:
        ypos -100
        xpos -200
        ease 6.0 xpos 0
    show expression "bk3/toph/swim_idles/water_standin.png":
        xpos -200
        ease 6.0 xpos 0

    k3 "*gulp* *mmmm* *slurp*"
    t "aang! is she really kissing you!?"
    $ katara_blowjob_blink = True
    menu:
        "hold her head":
            $ katara_blowjob_holdhead = True
        "keep going like this":
            $ katara_blowjob_holdhead = False
    y "...in a manner of speaking."
    t "....what?"
    k3 "*gltch* *sluuurp*"
    t "that's... some really noisy kissing."
    t "are... are you using tongue or something?"
    y "yeah, she... ah... she's using tongue.... ah..."
    $ katara_blowjob_blink = False
    y "she could use a little more tongue though... right... ah...."
    $ katara_blowjob_blink=True
    pause 1
    $ katara_blowjob_blink=False
    pause 1
    $ katara_blowjob_blink=True
    pause 1
    $ katara_blowjob_blink=False
    y "yes... ahh... fuck... i can't believe..."
    t "guys?"
    y "ngh..."
    show tokb tokb101
    k3 "*mmngh...* *ahh....* *mngh...*"
    t "Umm...."
    t "katara...? can we talk for a second?"
    y "her mouth is busy right now, toph."
    k3 "*slurp* *slurp* *gulp*"
    y "ah... ah... she's almost free..."
    menu:
        "cum on face":
            show tokb tokb05 with dissolve
            y "fuck..."
            play sound "audio/splurt2.ogg"
            show tokb_sperm1
            with flash
            k3 "aahhh....!"
            play sound "audio/splurt1.ogg"
            hide tokb_sperm1
            show tokb_sperm2
            with flash
            y "hgnh! fuck!"
            k3 "yes, baby!"
            t "...what...?"
            y "ngh!"
            hide tokb_sperm2
            show tokb_sperm3
            with flash

        "cum in mouth":
            show tokb tokb10 with vshake
            y "fuck..."
            show tokb tokb11
            with vshake
            play sound "audio/splurt2.ogg"
            with flash
            k3 "aahhh....!"
            show tokb tokb11
            with vshake
            play sound "audio/splurt1.ogg"
            with flash
            y "hgnh! fuck!"
            k3 "yes, baby!"
            t "...what...?"
            y "ngh!"
            show tokb tokb04
            show tokb_sperm4
            with flash

    play sound "audio/splurt2.ogg"
    y "ohh...."
    k3 "mmmmm....."
    t "guys! stop ignoring me!"
    t "I'm feeling kind of... left out..."

    call pauseInterface
    
    return
###### Fight Fuck
label gallery_winnerfuckall_menu:
    show frape frape0
    $ bk3_girlhead = 'bk3_girlhead_1'

    while True:
        hide expression 'bk3_girlhead_1ani'
        hide expression 'bk3_girlhead_2ani'
        hide expression 'bk3_girlhead_3ani'
        hide expression 'bk3_girlhead_4ani'
        hide expression 'bk3_girlhead_5ani'

        if bk3_girlhead == 'bk3_girlhead_1':
            show expression 'bk3_girlhead_1ani'
        elif bk3_girlhead == 'bk3_girlhead_2':
            show expression 'bk3_girlhead_2ani'
        elif bk3_girlhead == 'bk3_girlhead_3':
            show expression 'bk3_girlhead_3ani'
        elif bk3_girlhead == 'bk3_girlhead_4':
            show expression 'bk3_girlhead_4ani'
        elif bk3_girlhead == 'bk3_girlhead_5':
            show expression 'bk3_girlhead_5ani'

        menu:
            "Girl 1":
                $ bk3_girlhead = 'bk3_girlhead_1'
            "Girl 2":
                $ bk3_girlhead = 'bk3_girlhead_2'
            "Girl 3":
                $ bk3_girlhead = 'bk3_girlhead_3'
            "Girl 4":
                $ bk3_girlhead = 'bk3_girlhead_4'
            "Girl 5":
                $ bk3_girlhead = 'bk3_girlhead_5'
            "Continue":
                call gallery_winnerfuckall
                return

label gallery_winnerfuckall:
    call gallery_dCharacter_3Common

    show expression "bk3_fight/eyebrow_angry.png"
    girl "What? You want to put your filthy dick inside me ?!" with Dissolve(1.0)
    y "Ah, I was hoping you'd stay unconscious a bit longer."
    show frape frape1 with Dissolve(1.0)
    girl "So what'll be, ass or pussy? Wait, let me see your stampcard first."

    menu:
        "ass":
            girl "Fine you faggot, put it in my ass."

            show frape frape2
            show frape_analgape
            with Dissolve(1.3)
            girl "come on, this isn't a peepshow."
            show frape_dick
            girl "put it in."
            show frape_analoverlay

            hide frape_dick
            show frape_dick:
                ypos 60
                linear 1.0 ypos 0
                linear 1.5 ypos 60
                repeat
            hide frape_analoverlay
            show frape_analoverlay


            girl "What? you think that does anything for me?"
            girl "Hah! A nice cock but you've got no idea what to do with it!"
            girl "harder!"

            girl "Tickle my throat with that long shlong of yours!"

            show frape_dick:
                ypos 60
                linear 1.0 ypos -80
                linear 1.5 ypos 60
                repeat
            with vpunch


            girl "Faster!!"
            show frape_dick:
                ypos 60
                linear 0.5 ypos -80
                linear 1.0 ypos 60
                repeat
            with vpunch

            girl "that's more like it!"

            show frape_dick:
                ypos -100
            with vpunch
            play sound "audio/gltch2b.mp3"
            hide expression "bk3_fight/eyebrow_angry.png"
            show expression "bk3_fight/eyebrow_happy.png"
            girl "oh."
            hide frape_dick
            show frape2_dick2 with Dissolve(1.3)
            girl "That's quite a bit."
            y "I'm ready for that pussy now."

            hide expression "bk3_fight/eyebrow_happy.png"
            show expression "bk3_fight/eyebrow_angry.png"

            girl "After you've just been in my ass?! No way!"
            y "Aaawh."

        "pussy":
            girl "Ah, excellent choice. Let's see if you have what it takes to satisfy me."

            hide frape_openpuss
            show frape_openpuss:
                ypos 4
                linear 1.0 ypos -3
                linear 1.5 ypos 4
                repeat

            hide frape_dick
            show frape_dick:
                ypos -10
                linear 1.0 ypos -50
                linear 1.5 ypos -10
                repeat

            show frape_pussoverlay

            girl "What? you think that does anything for me?"
            girl "Hah! A nice cock but you've got no idea what to do with it!"
            girl "Go harder, you piece of shit!"

            girl "Kiss my womb with your fat dick!"

            show frape_dick:
                ypos -10
                linear 1.0 ypos -180
                linear 1.5 ypos -10
                repeat


            girl "Faster!!"
            show frape_dick:
                ypos -10
                linear 0.5 ypos -180
                linear 1.0 ypos -10
                repeat


            girl "that's more like it!"

            show frape_dick:
                ypos -140
            play sound "audio/gltch2b.mp3"
            hide expression "bk3_fight/eyebrow_angry.png"
            show expression "bk3_fight/eyebrow_happy.png"
            girl "oh."

            play sound "audio/gltch2b.mp3"
            girl "Aaaah. That's a nice amount. I can feel it flowing inside me."
            $ bk3_inseminations += 1
            hide frape_dick
            hide frape_openpuss
            hide frape_pussoverlay
            with Dissolve(0.8)

            show frape_dick2

            y "Ready for round two?"
            girl "Nah not now, spreading loads has a better chance of getting me pregnant."
            y "....Say wut?!?"
            hide frape_dick2
            show frape_heldopenpuss with Dissolve(1.3)
            hide expression "bk3_fight/eyebrow_happy.png"
            show expression "bk3_fight/eyebrow_angry.png"

            girl "With this much cum inside me you can't really be surprised about that possibility, right?"


    return
###### Fist some Guard 
label gallery_fist_some_guard:
    call gallery_dCharacter_3Common

    show expression "images/maze/fistbox/fistbox.jpg" with Dissolve (1.5)
    "a plump behind presses against the hole in the box."
    "...Eagerly awaiting what will come."
    y "Well fuck... don't mind if I do!"
   
    image fistherbox:
        "images/maze/fistbox/fistbox_0.png"
        0.3
        "images/maze/fistbox/fistbox_1.png"
        0.3
        "images/maze/fistbox/fistbox_2.png"
        0.3
        "images/maze/fistbox/fistbox_3.png"
        0.3
        "images/maze/fistbox/fistbox_4.png"
        0.3
        "images/maze/fistbox/fistbox_3.png"
        0.3
        "images/maze/fistbox/fistbox_2.png"
        0.3
        "images/maze/fistbox/fistbox_1.png"
        0.3
        repeat
    hide fistbox_0
    show fistherbox
    hide expression "images/maze/black.png"
    show expression "images/maze/black.png"
    hide expression "images/maze/black.png" with Dissolve(1.5)

    "... you have your entire hand sliding in and out at a feverish pace."
    "The girl's moaning gets louder and louder."
    mv "AAhh, yes! Faaaster! Faster!"
    mv "{size=+10}Fuuuck me up!!{/size}"
    mv "{size=+15}{b}Fuuuuuuck meee uuuup!!!{/b}{/size}"

    hide fistherbox

    show expression "images/maze/fistbox/fistbox_3.png" with hpunch
    show expression "images/maze/fistbox/fistbox_3.png" with hpunch
    "With a scream of satisfaction the girl faints as she climaxes."

    hide expression "images/maze/fistbox/fistbox_3.png"
    hide expression "images/maze/fistbox/fistbox.jpg"
    hide expression "maze/box_inside.jpg"
    with Dissolve(2.0)

    return
###### PornLove (Slave)
label gallery_pornlove_bk3_slave:
    while True:
        menu:
            "Smellerbee Cowgirl":
                scene expression "maze/grate_pornlove1.jpg" with dissolve
            "Smellerbee Creampie":
                scene expression "maze/grate_pornlove2.jpg" with dissolve
            "Smellerbee Blowjob":
                scene expression "maze/grate_pornlove3.jpg" with dissolve
            "Yue Fuck":
                scene pornlove_yue with dissolve
            "Exit":
                return

        call pauseInterface
###### PornLove (Love)
label gallery_pornlovebk3_love:
    while True:
        menu:
            "First Page":
                scene pornlove_old_1 with dissolve
            "Second Page":
                scene pornlove_old_2 with dissolve
            "Third Page":
                scene pornlove_old_3 with dissolve
            "Exit":
                return

        call pauseInterface
###### PornLove (Love) Smellerbee
label gallery_pornlove_bk3_love_2:
    while True:
        menu: 
            "First Page":
                scene smeller_dp1 with dissolve
            "Second Page":
                scene smeller_dp2 with dissolve
            "Third Page":
                scene smeller_dp3 with dissolve
            "Exit":
                return

        call pauseInterface
###### [Toph] Dancing
label gallery_toph_drinking:
    call gallery_dCharacter_3Common

    show expression "ebackgrounds/inside_tavern_day.jpg"
    show totd totd03:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat

        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat
    call pauseInterface
    t "Isss... kinda hot in here isn't it?"
    t "le-lemme try somethin..."

    show totd totd05 with Dissolve(1.5)

    t "Aaaah, much... better!"
    t "*hick*"
    call pauseInterface
    t "Sss...soooo..."
    t "...I like your dick, man!!"
    $ toph_drunk = 'angry'
    t "When will my parents finally..."
    t "*hick*"
    t "...finally gonna..."
    t "gonna... treat me like an adult.."
    $ toph_drunk = 'sad'
    t "I wish I was taller..."


    show totd totd06
    call pauseInterface
    y "(she's bouncing all over the place...)"
    y "(hopefully this rolls back to happy-time drunk and away from throw-up drunk...)"

    show totd totd05
    t "*sniff...*"
    call pauseInterface
    "You hear cheering and turn your head to look at the commotion."
    hide totd with Dissolve(1.5)

    show totd_crowd

    show totd totd25:
        parallel:
            xpos 0
            linear 3.0 xpos 100
            linear 3.0 xpos -100
            linear 3.0 xpos 0
            repeat

        parallel:
            ypos 0
            linear 0.5 ypos 10
            linear 0.5 ypos 0
            repeat
    with dissolve
    "A highly intoxicated Suki is shaking her tits while walking up and down."
    call pauseInterface
    "A small crowd has formed around her."
    show totd totd26
    suki "Oh..."
    suki "*hick*"
    suki "...hey Aang!"
    suki "Do you you come here, too?"
    y "Girl, I come everywhere!"

    y "(damn, iroh is selling some potent stuff!)"
    y "(i wonder if he's making a profit on this...)"
    y "(he's probably just giving it away to see tits...)"

    show totd totd25
    suki "Look at my titties!"

    y "(yup.)"
    suki "Aren't they wonderful!?"
    y " \"wonderful\"? Have you been talking with Joo Dee?"
    suki "what?"
    y "it's just that she says it all the time and- nevermind."
    "You turn your attention back to Toph."

    hide totd_crowd
    hide totd
    with Dissolve(1.5)


    show totd totd100:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat

        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat
    with dissolve

    $ toph_drunk = 'angry'
    t "That stupid cow!"
    t "She thinks she's special just because of some stoopit tits?"
    t "I'll show what a..."
    t "*hick*"
    t "...what a real woman can doo..."
    t "Hold my bottle, Aang!!"
    hide totd

    show totd totd101:
        linear 3 xpos 5
        easeout 3.3 xpos -5
        repeat
    with Dissolve(1.5)
    t "Lalalalla..."
    t "*hick*"
    t "...lalaallaa...."
    t "Imma superstar!!"
    t "lalallaaa..."

    menu:
        "Watch Toph":
            y "You're the most sexy of 'em all Toph!"
            y "Now come down from there before you break something."
            hide totd totd101 with dissolve
            show totd totd100 with dissolve
            t "Se... seee!"
            t "I'm twice the woman she is!"
            hide totd

            show totd totd05:
                ypos 0
                linear 2 ypos 5
                linear 2.3 ypos 0
                repeat
            t "I... I know what ya want Aang!"
            y "You do?"
            t "Yeaah!!!"
            t "You..."
            t "*hick*"
            t "you want to stick your dick in my pooper!!"
            y "I don't think I'd phrase it like that..."
            y "but yeah, sure, when given the opportunity I'd absolutely do that."
            t "Well... you can't!!"
            t "That's foooor pooping!"
            t "Not for dicks!"
            t "You dick!!"
            y "...i feel like you're projecting."
            y "i literally have not even mentioned it."
            y "i think."
            t "But...butt maybe maybe if you ask me nicely..."
            y "oh?"
            t "I'm tired..."
            t "I'm just..."
            t "...just gonna close my eyes for a second..."
            y "nonono, wait-"
            hide totd
            show totd totd00 with hpunch
            y "......"
            y "...sure."

        "Watch Suki":
            hide totd with dissolve
            show totd_crowd

            show totd totd25:
                parallel:
                    xpos 0
                    linear 3.0 xpos 100
                    linear 3.0 xpos -100
                    linear 3.0 xpos 0
                    repeat

                parallel:
                    ypos 0
                    linear 0.5 ypos 10
                    linear 0.5 ypos 0
                    repeat

            y "Shake'em girl!"
            show totd
            show totd_crowd
            with hpunch

            "Suddenly you hear a crash behind you."
            hide totd
            hide totd_crowd
            show totd totd00
            with dissolve
            y "Oh shit..."
            y "Are you okay Toph?"
            t "unghh... you just.. butts..."
            y "....what?"
            t "you wan' ma bu... duncha...?"
            y "do i... want your butt? um, i mean, yeah."
            t "can... can't have it..."
            t "for... poops!"
            t "but... curi... curious... maybe..."
            t "ask... ask nice..."
            y "are you saying that you want anal, but i have to ask-"

    t "*SNOOOORRRE*"
    y "Oh man... she's out cold."

    menu:
        "do nothing":
            pass

        "lick Toph":
            y "hmmmm....."
            show totd totd35 with dissolve
            y "it seems a shame not to have a taste..."
            show totd totd36 with Dissolve(1.5)
            y "just relax...."
            t "hnghaba..."
            show totd totd37 with Dissolve(1.5)
            y "*slick*"
            y "mmmm...."
            t "ahn... ahh... gahn..."
            call pauseInterface
            "you pass your tongue up and down her parted lips..."
            "with suki distracting the rest of the drunk patrons, you take your time."
            "her sweet, unresisting pussy leaks onto your tongue as you take your fill."
            call pauseInterface
            show totd totd38 with Dissolve(1.5)
            y "i think that's enough."
            t "higah..."
            show totd totd35 with Dissolve(3.5)
            "you wait a moment for her drenched cunt to finish leaking onto the table."


    show totd totd00

    hide totd
    show totd_crowd

    show totd totd25:
        parallel:
            xpos 0
            linear 3.0 xpos 100
            linear 3.0 xpos -100
            linear 3.0 xpos 0
            repeat

        parallel:
            ypos 0
            linear 0.5 ypos 10
            linear 0.5 ypos 0
            repeat

    "accompanied by the snoring of Toph, you watch Suki until you yourself black out."
    scene black with Dissolve(2.0)


    show expression "ebackgrounds/inside_tavern_day.jpg"
    show totd totd00
    with Dissolve(1.5)
    t "Oooh...my head. Where am I?"
    y "Mornin' Toph."
    show totd totd07 with dissolve
    t "What happened!!?"
    y "I think we got a little tipsy."
    y "I vaguely remember you dancing on the table."
    t "Oh shit, oh shit, oh shit!"

    return
#--
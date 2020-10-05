###### Declare Characters
label gallery_dCharacter_2Slave:
    $ p = Character("lia", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ m = Character("mai", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ t = Character("ty lee", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ oz = Character("Ozai", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)

    $ povname = "avatar"
    $ avatar = "player"
    
    $ y = Character("you", color="#000000", 
        show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), "player/base_neutral.png",
            (0, 0), ConditionSwitch(
                "tnose == 'small'", "player/nose_small.png",
                "tnose == 'medium'", "player/nose_mediocre.png",
                "tnose == 'big'", "player/nose_big.png",),
            (0, 0), ConditionSwitch(
                "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
                "textra2 == 'glasses'", "player/xtra_glasses.png",
                "textra2 == 'none'", "transparent.png"),
            (0, 0), ConditionSwitch(
                "textra3 == 'scar'", "player/xtra_scar.png",
                "textra3 == 'none'", "transparent.png",
                ),
            (0, 0), ConditionSwitch(
                "tchin == 'none'", "transparent.png",
                "tchin == 'beard'", "player/xtra_beard.png",
                "tchin == 'round'", "player/xtra_chinround.png",
                "tchin == 'square'", "player/xtra_chinsquare.png",
                ),
            (0, 0), ConditionSwitch(
                "thair == 'blonde1'", "player/hair_straightblond.png",
                "thair == 'bald'", "player/hair_bald.png",
                "thair == 'brown1'", "player/hair_darkwild.png",
                "thair == 'blonde2'", "player/hair_blondcurly.png",
                "thair == 'brown2'", "player/hair_darkcurly.png",
                "thair == 'brown3'", "player/hair_darkponytail.png",
                ), ), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ya = Character("you", color="#000000", 
        show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), "player/base_angry.png",
            (0, 0), ConditionSwitch(
                "tnose == 'small'", "player/nose_small.png",
                "tnose == 'medium'", "player/nose_mediocre.png",
                "tnose == 'big'", "player/nose_big.png",),
            (0, 0), ConditionSwitch(
                "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
                "textra2 == 'glasses'", "player/xtra_glasses.png",
                "textra2 == 'none'", "transparent.png"),
            (0, 0), ConditionSwitch(
                "textra3 == 'scar'", "player/xtra_scar.png",
                "textra3 == 'none'", "transparent.png",
                ),
            (0, 0), ConditionSwitch(
                "tchin == 'none'", "transparent.png",
                "tchin == 'beard'", "player/xtra_beard.png",
                "tchin == 'round'", "player/xtra_chinround.png",
                "tchin == 'square'", "player/xtra_chinsquare.png",
                ),
            (0, 0), ConditionSwitch(
                "thair == 'blonde1'", "player/hair_straightblond.png",
                "thair == 'bald'", "player/hair_bald.png",
                "thair == 'brown1'", "player/hair_darkwild.png",
                "thair == 'blonde2'", "player/hair_blondcurly.png",
                "thair == 'brown2'", "player/hair_darkcurly.png",
                "thair == 'brown3'", "player/hair_darkponytail.png",
                ), ), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ yc = Character("you", color="#000000", 
        show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), "player/base_confused.png",
            (0, 0), ConditionSwitch(
                "tnose == 'small'", "player/nose_small.png",
                "tnose == 'medium'", "player/nose_mediocre.png",
                "tnose == 'big'", "player/nose_big.png",),
            (0, 0), ConditionSwitch(
                "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
                "textra2 == 'glasses'", "player/xtra_glasses.png",
                "textra2 == 'none'", "transparent.png"),
            (0, 0), ConditionSwitch(
                "textra3 == 'scar'", "player/xtra_scar.png",
                "textra3 == 'none'", "transparent.png",
                ),
            (0, 0), ConditionSwitch(
                "tchin == 'none'", "transparent.png",
                "tchin == 'beard'", "player/xtra_beard.png",
                "tchin == 'round'", "player/xtra_chinround.png",
                "tchin == 'square'", "player/xtra_chinsquare.png",
                ),
            (0, 0), ConditionSwitch(
                "thair == 'blonde1'", "player/hair_straightblond.png",
                "thair == 'bald'", "player/hair_bald.png",
                "thair == 'brown1'", "player/hair_darkwild.png",
                "thair == 'blonde2'", "player/hair_blondcurly.png",
                "thair == 'brown2'", "player/hair_darkcurly.png",
                "thair == 'brown3'", "player/hair_darkponytail.png",
                ), ), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ym = Character("you", color="#000000", 
        show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), "player/base_grin.png",
            (0, 0), ConditionSwitch(
                "tnose == 'small'", "player/nose_small.png",
                "tnose == 'medium'", "player/nose_mediocre.png",
                "tnose == 'big'", "player/nose_big.png",),
            (0, 0), ConditionSwitch(
                "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
                "textra2 == 'glasses'", "player/xtra_glasses.png",
                "textra2 == 'none'", "transparent.png"),
            (0, 0), ConditionSwitch(
                "textra3 == 'scar'", "player/xtra_scar.png",
                "textra3 == 'none'", "transparent.png",
                ),
            (0, 0), ConditionSwitch(
                "tchin == 'none'", "transparent.png",
                "tchin == 'beard'", "player/xtra_beard.png",
                "tchin == 'round'", "player/xtra_chinround.png",
                "tchin == 'square'", "player/xtra_chinsquare.png",
                ),
            (0, 0), ConditionSwitch(
                "thair == 'blonde1'", "player/hair_straightblond.png",
                "thair == 'bald'", "player/hair_bald.png",
                "thair == 'brown1'", "player/hair_darkwild.png",
                "thair == 'blonde2'", "player/hair_blondcurly.png",
                "thair == 'brown2'", "player/hair_darkcurly.png",
                "thair == 'brown3'", "player/hair_darkponytail.png",
                ), ), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ yd = Character("you", color="#000000", 
        show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), "player/base_doubtful.png",
            (0, 0), ConditionSwitch(
                "tnose == 'small'", "player/nose_small.png",
                "tnose == 'medium'", "player/nose_mediocre.png",
                "tnose == 'big'", "player/nose_big.png",),
            (0, 0), ConditionSwitch(
                "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
                "textra2 == 'glasses'", "player/xtra_glasses.png",
                "textra2 == 'none'", "transparent.png"),
            (0, 0), ConditionSwitch(
                "textra3 == 'scar'", "player/xtra_scar.png",
                "textra3 == 'none'", "transparent.png",
                ),
            (0, 0), ConditionSwitch(
                "tchin == 'none'", "transparent.png",
                "tchin == 'beard'", "player/xtra_beard.png",
                "tchin == 'round'", "player/xtra_chinround.png",
                "tchin == 'square'", "player/xtra_chinsquare.png",
                ),
            (0, 0), ConditionSwitch(
                "thair == 'blonde1'", "player/hair_straightblond.png",
                "thair == 'bald'", "player/hair_bald.png",
                "thair == 'brown1'", "player/hair_darkwild.png",
                "thair == 'blonde2'", "player/hair_blondcurly.png",
                "thair == 'brown2'", "player/hair_darkcurly.png",
                "thair == 'brown3'", "player/hair_darkponytail.png",
                ), ), window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ys = Character("you", color="#000000", 
        show_side_image = LiveComposite(
            (1000, 720),
            (0, 0), "player/base_smile.png",
            (0, 0), ConditionSwitch(
                "tnose == 'small'", "player/nose_small.png",
                "tnose == 'medium'", "player/nose_mediocre.png",
                "tnose == 'big'", "player/nose_big.png",),
            (0, 0), ConditionSwitch(
                "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
                "textra2 == 'glasses'", "player/xtra_glasses.png",
                "textra2 == 'none'", "transparent.png"),
            (0, 0), ConditionSwitch(
                "textra3 == 'scar'", "player/xtra_scar.png",
                "textra3 == 'none'", "transparent.png",
                ),
            (0, 0), ConditionSwitch(
                "tchin == 'none'", "transparent.png",
                "tchin == 'beard'", "player/xtra_beard.png",
                "tchin == 'round'", "player/xtra_chinround.png",
                "tchin == 'square'", "player/xtra_chinsquare.png",
                ),
            (0, 0), ConditionSwitch(
                "thair == 'blonde1'", "player/hair_straightblond.png",
                "thair == 'bald'", "player/hair_bald.png",
                "thair == 'brown1'", "player/hair_darkwild.png",
                "thair == 'blonde2'", "player/hair_blondcurly.png",
                "thair == 'brown2'", "player/hair_darkcurly.png",
                "thair == 'brown3'", "player/hair_darkponytail.png",
                ), ), window_left_padding=220, show_two_window=True, who_xpos=36)

    return
#--


###### [Ty Lee] Drink Piss
label gallery_tylee_drinkpiss:
    call gallery_dCharacter_2Slave

    show bety bety102 with dissolve
    t "oh. um..."
    call pauseInterface
    t "do i... should i..."
    t "There sure are a lot of you..."
    g1 "are you ready, girl?"
    g2 "hngh-"
    play sound "audio/pissing.mp3"
    show bety bety100
    call pauseInterface
    t "oh... there's... so much..."
    g1 "ahh... i really needed a good piss from that ale."
    show bety bety102 with dissolve
    g2 "that should do it."
    t "i'm just... going to drink this now..."
    t "....."
    show bety bety101 with dissolve
    call pauseInterface
    t "*gulp* *gulp* *gulp*"
    show bety bety102 with dissolve
    t "*ah!*"
    t "it's so hot and salty..."
    t "and there's so much..."
    t "....."
    show bety bety101 with dissolve
    call pauseInterface
    t "*gulp* *gulp* *gulp*"
    t "it's so... rough..."
    t "why do you want this?"
    show bety bety102 with dissolve
    t "*ah!*"
    t "that's enough, right?"

    menu:
        "a little more":
            g1 "nah, we've been drinking a lot."
            g1 "i think we've all got a bit left, don't we boys?"
            g2 "hngh-"
            show bety bety100
            call pauseInterface
            t "oh... there's... so much..."
            g1 "ahh... there we go..."
            g2 "that should do it."
            show bety bety102 with dissolve
            t "i'm just... going to drink this now..."
            t "....."
            show bety bety101 with dissolve
            call pauseInterface
            t "*gulp* *gulp* *gulp*"
            show bety bety102 with dissolve
            t "*ah!*"
            t "it's so hot and salty..."
            t "and there's so much..."
            t "....."
            show bety bety101 with dissolve
            call pauseInterface
            t "*gulp* *gulp* *gulp*"
            t "it's so... rough..."
            t "why do you want this?"
            show bety bety102 with dissolve
            t "*ah!*"
            t "that's enough, right?"
            g1 "yeah, that should do it."

        "done":
            g1 "yeah, that should do it."

    g2 "here's your gold."
    t "thank... thank you."

    return
###### [Ty Lee] Blowjob
label gallery_tylee_blowjob:
    call gallery_dCharacter_2Slave

    scene bg_a_tavern1 with dissolve
    show tf2 with dissolve
    hide bg_a_tavern
    hide tf
    y "take off your clothes."
    t "of course!"
    hide tf2 with dissolve
    show tfn with dissolve
    call pauseInterface
    y "very nice."
    t "hee hee."
    y "get down on your knees."
    show tfn2 with dissolve
    hide tfn
    t "okay!"
    hide tfn2 with dissolve
    show tys1 with dissolve
    call pauseInterface
    t "like this?"
    y "oh, yeah."
    y "why don't you play with my cock?"
    show tys_an3 with dissolve
    t "like this, daddy?"
    y "...oh fuck, that's a good girl."
    call pauseInterface
    t "..."
    show tys4 with dissolve
    y "ah..."
    hide tys_an3
    show tys5 with dissolve
    t "...."
    show tys_an1 with dissolve
    call pauseInterface
    y "hngh..."
    y "your mouth feels amazing..."
    show tys_an2 with dissolve
    y "damn girl, you know how to work a cock."
    hide tys_an1
    hide tys10
    show tys10 with dissolve
    t "thank you, daddy!"
    hide tys_an2
    y "...fuck that's hot."
    t "yes sir!"
    show tys_an2 with dissolve
    t "mmm..."
    hide tys10

    menu:
        "facefuck her!":
            y "well, i'm getting a little bored."
            show tys15 with dissolve
            t "i'm sorry..."
            hide tys_an2
            t "please, i'll do whatever you like!"
            y "hmm... are you sure?"
            t "oh, yes, sir!"
            y "hmm... get back on that cock."
            show tys_an21 with dissolve
            t "..."
            hide tys15
            y "...very well."
            show tys8 with dissolve
            t "(what is he-)"
            hide tys_an21
            show tys13 with dissolve
            t "???"
            hide tys8
            show tys_an4 with dissolve
            t "!!!!!"
            hide tys7
            y "ngh! that's it, baby!"
            y "suck that dick, ty lee!"
            y "earn that paycheck!"
            t "...!!!"
            y "how about we speed it up?"
            y "really work that mouth out?"
            show tys_an5
            t "mmmghh!!!"
            hide tys_an4
            y "yeah! that's it, whore!"
            y "oh fuck, here it comes!"

            menu:
                "finish on her face":
                    y "here's the first half of your payment!"
                    y "open wide!"
                    show tys23 with dissolve
                    t "huh?"
                    hide tys_an5
                    y "ngh!"
                    play sound "audio/splurt3.ogg"
                    show tys24
                    with flash
                    t "oh!!"
                    y "fuck!"
                    play sound "audio/splurt1.ogg"
                    show tys25 with flash
                    t "what is-"
                    y "agghh your face deserves this!"
                    play sound "audio/splurt2.ogg"
                    show tys26 with flash
                    t "......"
                    y "open your eyes."
                    show tys27 with dissolve
                    t "'ow 'oo ah 'ook?"
                    show tys28 with dissolve
                    call pauseInterface
                    y "great."
                    y "clean up and get back to work."
                    y "i'll visit you again soon."
                    t "o'ay!"
                    hide tys23
                    hide tys24
                    hide tys25
                    hide tys26
                    hide tys27
                    hide tys28

                "finish in her mouth":
                    y "here's the first half of your payment!"
                    show tys14 with dissolve
                    t "???"
                    hide tys_an5
                    y "ngh!"
                    play sound "audio/splurt3.ogg"
                    show tys16
                    with flash
                    t "mmmngh!!!"
                    y "fuck!"
                    play sound "audio/splurt1.ogg"
                    show tys17 with flash
                    t "*gagh!?*"
                    y "agghh fuck this throat of yours!"
                    play sound "audio/splurt2.ogg"
                    show tys18 with flash
                    t "......"
                    y "show me!"
                    show tys19 with dissolve
                    t "..."
                    hide tys18
                    y "swallow."
                    show tys20 with dissolve
                    t "*gulp*"
                    show tys22 with dissolve
                    t "did..."
                    hide tys19
                    hide tys20
                    t "did i do well?"
                    y "oh yes..."
                    show tys20 with dissolve
                    t "yay!"
                    y "well, clean up and get back to work."
                    y "i'll visit you again soon."
                    hide tys20 with dissolve
                    t "okay!"
                    hide tys14
                    hide tys16
                    hide tys17
                    hide tys22

        "lean back and let her work":
            scene bg_a_tavern2 with dissolve
            show tys29 with dissolve
            y "go ahead... show me what you can do."
            t "mm-ay!"
            show tys_an6 with dissolve
            t "mm! mm!"
            call pauseInterface
            y "damn, girl...."
            hide tys29
            show tys29 with dissolve
            t "this is fun!"
            hide tys_an6
            t "thank you again!"
            y "get back on that cock, ty lee!"
            t "yes, siree!"
            show tys_an7 with dissolve
            call pauseInterface
            y "oh fuck, here it comes!"

            menu:
                "finish on her face":
                    y "here's the first half of your payment!"
                    y "open wide!"
                    show tys23 with dissolve
                    t "huh?"
                    hide tys_an5
                    hide tys_an7
                    y "ngh!"
                    play sound "audio/splurt3.ogg"
                    show tys24
                    with flash
                    t "oh!!"
                    y "fuck!"
                    play sound "audio/splurt1.ogg"
                    show tys25 with flash
                    t "what is-"
                    y "agghh your face deserves this!"
                    play sound "audio/splurt2.ogg"
                    show tys26 with flash
                    t "......"
                    y "open your eyes."
                    show tys27 with dissolve
                    t "'ow 'oo ah 'ook?"
                    show tys28 with dissolve
                    call pauseInterface
                    y "that was great."
                    t "'ay!"
                    y "well, clean up and get back to work."
                    y "i'll visit you again soon."
                    t "o'ay!"
                    hide tys23
                    hide tys24
                    hide tys25
                    hide tys26
                    hide tys27
                    hide tys28

                "finish in her mouth":
                    y "here's the first half of your payment!"
                    show tys32 with dissolve
                    t "???"
                    hide tys_an5
                    hide tys_an7
                    y "ngh!"
                    play sound "audio/splurt3.ogg"
                    show tys33
                    with flash
                    t "mmmngh!!!"
                    y "fuck!"
                    play sound "audio/splurt1.ogg"
                    show tys34 with flash
                    t "*gagh!?*"
                    y "agghh fuck this throat of yours!"
                    play sound "audio/splurt2.ogg"
                    show tys35 with flash
                    t "......"
                    y "show me!"
                    show tys19 with dissolve
                    t "..."
                    hide tys34
                    y "swallow."
                    show tys20 with dissolve
                    t "*gulp*"
                    show tys22 with dissolve
                    t "did..."
                    hide tys19
                    hide tys20
                    t "did i do well?"
                    y "oh, yes..."
                    show tys20 with dissolve
                    t "oh yay!"
                    y "well, clean up and get back to work."
                    y "i'll visit you again soon."
                    hide tys20 with dissolve
                    t "okay!"
                    hide tys22
                    hide tys29
                    hide tys32
                    hide tys33
                    hide tys35

    hide tys_an1
    hide tys1
    hide tys2
    hide tys3
    hide tys4
    hide tys5
    hide tys13

    return
###### [Ty Lee] Fuck
label gallery_tylee_sex:
    call gallery_dCharacter_2Slave

    show drty drty34 with dissolve
    call pauseInterface
    t "hey, it's still pretty comfy."
    show drty drty35 with dissolve
    t "wanna see my pussy?"
    show drty drty105 with dissolve
    call pauseInterface
    y "...."
    y "that is fucking fantastic."
    show drty drty05 with dissolve
    t "i like my pussy."
    show drty drty06_1 with dissolve
    t "...."
    show drty drty07 with dissolve
    t "you do too, right?"
    show drty drty104 with dissolve
    call pauseInterface
    t "you should watch me rub it."
    show drty drty106 with dissolve
    call pauseInterface
    t "ahhn... nnnhh..."
    t "i have such a pretty pussy, don't i daddy?"
    t "ah...oh... don't you wanna come here...?"
    t "don't you, daddy?"
    show drty drty104 with dissolve
    t "heehee."
    y "that's it! ready or not, here i... come."
    show drty drty06_1 with dissolve
    t "heehee."
    y "spread your lips, girl."
    t "of course, daddy!"
    show drty drty10 with dissolve
    t "like this?"
    t "do you want it?"
    t "you wanna put that big, thick-"
    show drty drty02 with dissolve
    t "...."
    t "i'm... nervous."
    y "i told you to spread them."
    show drty drty01 with dissolve
    t "......"
    y "are you ready?"
    t "....."
    t "{size=-5}yes..."
    y "alright, just relax."
    show drty drty02 with dissolve
    t "o-okay."
    t "....."
    show drty drty12 with dissolve
    t "oohhh....."
    call pauseInterface
    show drty drty13_1 with dissolve
    t "ahh..."
    call pauseInterface
    show drty drty15 with dissolve
    t "*ah!*"
    show drty drty100_1 with dissolve
    call pauseInterface
    t "*ah!* *oh!* *mmm*"
    t "it's... *ah*... so... *ngh*... good!"
    show drty drty100 with dissolve
    call pauseInterface
    t "i can't - *ah* - believe you're - *ngh* - fucking my - *mmph!* - pussy, daddy!"
    t "aahhhhh... i feel so right-"
    show drty drty103_2
    t "ah!"
    call pauseInterface
    t "eas- easy!"
    show drty drty103_3
    call pauseInterface
    t "what... *ah!*... did... *oh*... i... *ngh!*..."
    t "do... *agh!*... to... *ugh!*... you... *gah!*...!?"
    show drty drty103_4 with dissolve
    t "mmm...."
    y "you love it."
    y "you're a perfect whore."
    t "thank - *ah!* - you, daddy!"
    show drty drty12 with dissolve
    t "hmm?"
    show drty drty08_1 with dissolve
    t "don't... take it away..."
    show drty drty107 with dissolve
    t "ah... ah...."
    t "daddy... baby... sir..."
    t "please..."
    call pauseInterface
    show drty drty108 with dissolve
    call pauseInterface

    menu:
        "keep fucking her pussy":
            y "i'm not done yet!"
            t "what-"
            show drty drty15 with vshake
            t "*ahh!*"
            show drty drty103_6
            t "yes! yes! yes, baby!"
            t "fuck that tight little cunt!"

            menu:
                "cum inside pussy":
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show drty drty16 with flash
                    t "oh!"
                    play sound "audio/splurt3.ogg"
                    show drty drty17 with flash
                    y "slut!"
                    play sound "audio/splurt1.ogg"
                    show drty drty18 with flash
                    t "oh, wow!"
                    show drty drty19 with flash
                    t "........."
                    t "look how much there is!"
                    t "i'm like a... a... creampie!"
                    show drty drty32 with dissolve
                    t "am i pretty?"
                    t "did i do good?"
                    y "very."
                    show drty drty32 with dissolve
                    t "yay!"
                    t "well, i've gotta get back to work, so i'm just going to wipe off my pussy quickly..."
                    t "and now i'm going to take a nap!"
                    show drty drty34 with dissolve
                    t "with cum-filled pussy!"
                    t "see ya around!"
                    
                "cum outside pussy":
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show drty drty28 with flash
                    t "oh!"
                    play sound "audio/splurt3.ogg"
                    show drty drty29 with flash
                    y "slut!"
                    play sound "audio/splurt1.ogg"
                    show drty drty30 with flash
                    t "oh, wow!"
                    show drty drty31_1 with flash
                    t "........."
                    t "look how much there is!"
                    t "it's so... warm!"
                    show drty drty32 with dissolve
                    t "am i pretty?"
                    t "did i do good?"
                    y "very."
                    show drty drty32 with dissolve
                    t "yay!"
                    t "well, i've gotta get back to work, so i'm just going to wipe off my pussy quickly..."
                    t "and now i'm going to take a nap!"
                    show drty drty34 with dissolve
                    t "see ya around!"

        "fuck her ass":
            show drty drty20 with dissolve
            t "ohh...."
            t "mmm...."
            show drty drty21_1 with dissolve
            t "ah...!!"
            t "that's... ah...."
            show drty drty23 with dissolve
            t "you're in my-!"
            t "you've put it in my butt!"
            y "of course."
            show drty drty23_1 with dissolve
            t "is it-"
            show drty drty23_2 with ushake
            t "ngh!"
            show drty drty23_1 with dissolve
            t "nice?"
            y "it's fucking tight."
            t "i'm gla-"
            show drty drty102
            t "oh!"
            call pauseInterface
            y "that's it... fucking your tight little ass..."
            y "tight little butthole..."
            y "with your legs in the fucking air..."
            y "how's it feel?"
            show drty drty102_1
            t "it... it's... filling..."
            y "and?"
            t "i... i like it...."
            y "that's good, because i'm about to cum..."
            y "ready for your reward?"
            y "your salty, gooey treat?"
            t "oh! yes!"
            t "please!"
            t "you're so good to me... please... give me whatever you want!"
            t "i'm so lucky!"
            t "you're so sexy, and handsome, and amazing!"
            y "here... it... fucking...."
            play sound "audio/splurt2.ogg"
            show drty drty24 with flash
            t "*ah!*"
            play sound "audio/splurt3.ogg"
            show drty drty25 with flash
            y "ngh!"
            play sound "audio/splurt3.ogg"
            show drty drty26 with flash
            t "my bottom!"
            show drty drty27 with dissolve
            t "I'm... so full..."
            call pauseInterface
            t "it's... so much..."
            t "well, i've gotta get back to work soon..."
            t "so i'm going to take a quick nap!"
            show drty drty34 with dissolve
            t "with cum-filled ass!"
            t "see ya around!"

    return
###### [Azula + Lia] Blowjob
label gallery_lia_azula_bj:
    call gallery_dCharacter_2Slave

    scene bg_a_prisonroom
    show azli azli01
    with dissolve
    call pauseInterface
    a "this is exciting, [acallme]!"
    y "well, lia, why don't you get started?"
    show azli azli02 with dissolve
    p "yes, sir!"
    a "that's so mean! i wanna go!"
    show azli azli12 with dissolve

    call pauseInterface
    p "hhmm..."
    a "come on, i can do better than that!"
    show azli azli13 with dissolve
    call pauseInterface
    p "nngh..."
    "lia's mouth is hot and eager against you. with a gentle moan, she presses her tongue up against the underside of your shaft."
    y "that's it, slave."
    show azli azli104 with dissolve
    call pauseInterface
    p "hhmmmmgh..."
    y "ngh... you've trained her well."
    a "please let me have a turn, [acallme]."
    y "it'll be your turn soon enough."
    show azli azli02 with dissolve
    y "alright. now wet it some more for azula."
    a "yes, slobber on his cock for me! i wanna taste your spit."
    show azli azli104 with dissolve
    call pauseInterface
    p "mmmgh...."
    y "alright, i think that's enough."
    show azli azli02 with dissolve
    call pauseInterface
    y "suck her spit off my cock, azula."
    a "thank you, [acallme]!"
    show azli azli03 with dissolve
    call pauseInterface
    "her lips wrap carefully around the head, clearly happy to have your cock in her mouth."
    "she sucks savoringly, enjoying the tip."
    a "*slurp* *shlup*"
    show azli azli04 with dissolve
    a "hmmgh!"
    call pauseInterface
    p "yes, your highness... that's it..."
    a "mmmgh...."
    "azula's brow furrows in concentration as she holds herself there."
    show azli azli03 with dissolve
    a "*sluuurp*"
    show azli azli101_1 with dissolve
    call pauseInterface
    y "ngh..."
    y "you're doing pretty well, princess."
    a "mmmm....."
    p "she seems to really enjoy cock in her mouth."
    a "'es."
    y "ah. well, we have a problem."
    a "mm?"
    y "you can still talk."
    a "*mmm!*"
    show azli azli05 with ushake
    a "*nngh!* *gaghh*"
    "azula pushes her face into your cock, deeply burying your shaft in her throat."
    "you can feel her throat muscles try to swallow around your cock."
    p "oh, wow! mistress! you're amazing!"
    show azli azli03 with dissolve
    a "sllluuuurrrppp.... *gulp*"
    show azli azli101 with dissolve
    call pauseInterface
    "azula speeds up, making sure to place you deep in her throat with every headbob."
    a "*gaggh* *slurp* *gltch*"
    a "mmmm-mmm-mmmm..."
    p "yes, mistress... slurp that fat cock. slurp it right in front of me."
    p "you're amazing!"
    show azli azli101_2 with dissolve
    "The adulation seems to encourage azula, who sucks you with increasing determination."
    call pauseInterface
    a "mngh! ungh!"
    a "*slurp-gagh*"
    p "faster, your highness!"
    show azli azli102 with dissolve
    call pauseInterface
    y "azula, you dirty little slut... look at you go."
    a "*gugh* *slurp*"
    p "that looks like fun..."
    menu:
        "stay with azula":
            y "come on!"
            show azli azli102_1
            call pauseInterface
            "azula forces your cock down and milks you aggressivly with her throat."
            y "Fuck! here it comes!"
            play sound "audio/splurt3.ogg"
            show azli azli06
            with flash
            a "yes!"
            play sound "audio/splurt2.ogg"
            show azli azli07
            with flash
            a "cum for me [acallme]!"
            p "oh, wow..."
            play sound "audio/splurt1.ogg"
            show azli azli08
            with flash
            a "mmmmm......."
            show azli azli09 with dissolve
            "azula puts your cock back into her mouth and sucks out the remaining dribble of cum."
            show azli azli10 with dissolve
            call pauseInterface
            show azli azli11 with dissolve
            call pauseInterface
            show azli azli08 with dissolve
            a "you aren't done, are you?"
            menu:
                "let lia in on the fun":
                    y "not quite yet."
                    y "lia-"
                    p "yes!"
                    y "you didn't think i forgot you, did you?"
                    p "well..."
                    y "suck out what azula missed."
                    a "i didn't miss any!"
                    p "yes, sir."
                    show azli azli14 with dissolve
                    call pauseInterface
                    p "mmmm...."
                    show azli azli105 with dissolve
                    call pauseInterface
                    p "*slurp* *gltch*"
                    y "you're so cute when you're bobbing up and down on my cock."
                    p "mmmm...."
                    p "*gulp* *shlup*"
                    y "you're actually getting me close."
                    show azli azli105_1 with dissolve
                    call pauseInterface
                    y "oh, fuck. you're determined, aren't you?"
                    p "mm! mm!"
                    y "ngh... here it comes!"
                    p "*slurp!* *gulp!* *slurp!*"
                    play sound "audio/splurt2.ogg"
                    show azli azli107 with flash
                    p "mmmmmmmm....!!!"
                    play sound "audio/splurt3.ogg"
                    with flash
                    y "ngh!"
                    play sound "audio/splurt1.ogg"
                    with flash
                    call pauseInterface
                    y "easy..."
                    show azli azli107_1 with dissolve
                    call pauseInterface
                    y "i think that's enough."
                    show azli azli22 with dissolve
                    y "you look a little wet, azula."
                    a "you always know just what to say, [acallme]."
                    y "you're cute with my jizz dripping down your face."
                    a "thank you."
                    y "alright, i'll see you girls later."
                    show azli azli21 with dissolve
                    
                "leave":
                    y "yeah."
                    y "i'll see you girls later."

        "move to lia":
            y "azula... you're a disappointment."
            a "hgh!"
            y "why don't you just sit there and watch how lia does it."
            show azli azli02 with dissolve
            a "i'm so sorry! i can do better!"
            show azli azli12 with dissolve
            y "show her how it's done, lia."
            show azli azli104
            call pauseInterface
            a "that's not better than me!"
            a "i'll prove it!"
            y "You had your turn"
            p "ngh! hmm!"
            p "*sluurp*"
            a "you're not as good as me, peasant. don't listen to him."
            p "*slurp* *gulp*"
            a "you're nothing. you're worthless."
            p "*gltch* *shlurp*"
            a "you may be pleasing him..."
            a "but your whole purpose in life is a fucktoy, so you had better be good at it."
            show azli azli104_1
            p "*slurp* mmmm..."
            a "but i'm still better than you. you're just a peasant slave, you can't possibly compete."
            y "oh, fuck. you're determined, aren't you?"
            p "mm! mm!"
            y "ngh... here it comes!"
            p "*slurp!* *gulp!* *slurp!*"
            play sound "audio/splurt2.ogg"
            show azli azli106 with flash
            p "mmmmmmmm....!!!"
            play sound "audio/splurt3.ogg"
            with flash
            y "ngh!"
            play sound "audio/splurt1.ogg"
            with flash
            call pauseInterface
            y "easy..."
            show azli azli106_1 with dissolve
            call pauseInterface
            y "i think that's enough."
            show azli azli02 with dissolve
            a "you're not done are you?"
            menu:
                "let azula in on the fun":
                    y "not quite."
                    y "finish the job, azula."
                    a "thank you, [acallme]!"
                    show azli azli101_2 with dissolve
                    "azula dives on your cock, sucking deeply and fiercely, cleaning out whatever cum lia missed."
                    call pauseInterface
                    a "*slurp!* *gagh!*"
                    y "that's a good little whore."
                    y "ngh... you're about to get seconds..."

                    a "*gltch* *slurp*"
                    a "....?"
                    y "ngh!"
                    show azli azli102_1
                    call pauseInterface
                    "azula forces your cock down and milks you aggressivly with her throat."
                    y "Fuck! here it comes!"
                    play sound "audio/splurt3.ogg"
                    show azli azli06
                    with flash
                    a "yes!"
                    play sound "audio/splurt2.ogg"
                    show azli azli07
                    with flash
                    a "thank you so much!"
                    p "oh, wow..."
                    play sound "audio/splurt1.ogg"
                    show azli azli08
                    with flash
                    a "i love it!"
                    show azli azli09 with dissolve
                    "azula puts your cock back into her mouth and sucks out the remaining dribble of cum."
                    show azli azli10 with dissolve
                    call pauseInterface
                    show azli azli11 with dissolve
                    call pauseInterface
                    show azli azli08 with dissolve
                    a "i do hope you're finished now."
                    y "yeah. bye."
                    show azli azli21 with dissolve
                    
                "leave":
                    y "yeah."
                    y "i'll see you girls later."

    a "bye!"
    p "bye!"

    return
###### [Azula] Piss
label gallery_apissjob:
    call gallery_dCharacter_2Slave
    
    scene bg_a_smallpalaceroom with dissolve
    show a_blink with dissolve
    a "hellooo... bish...."
    show ae with dissolve
    a "you shtupid bish..."
    hide a_blink
    show aa with dissolve
    a "the fuck are you doing... inna room?"
    hide ae
    y "are... you drunk?"
    show aae with dissolve
    a "...."
    hide aa
    a "show what if i am?"
    show ad with dissolve
    a "i deserve to get drunk!"
    hide aae
    show ade with dissolve
    a "like everybody else! gets too!"
    hide ad
    y "wow, you are really fucked up."
    show ad with dissolve
    a "no, {i}you're{/i} the one who's {i}fucked up."
    hide ade
    show aue with dissolve
    a "the... the things you make me do..."
    hide ad
    show ad with dissolve
    a "i hate you... you know i hate you, right?"
    hide aue
    y "yeah, i know. let's-"
    show aue with dissolve
    a "and i like it...."
    hide ad
    y "come again?"
    show aa with dissolve
    hide aue
    a "you make me... so... angry!"
    a "i just..."
    show au with dissolve
    a "I need to piss."
    hide aa
    a "i'm gonna get naked now."
    y "uh-"
    hide au with dissolve
    show alnub with dissolve
    a "lay down."
    y "wait, no, why?"
    show alnab with dissolve
    a "I am your princess! you will do as i command."
    hide alnub
    hide alnab with dissolve
    scene bg_a_ceiling with dissolve
    show apiss 1 with dissolve
    a "you bish."
    a "you shupid, i hate you... i'm so horny... and i need to..."
    show apiss 2 with dissolve
    call pauseInterface
    y "wait..."
    a_b "you see this pussy...?"
    show apiss 3 with dissolve
    a_b "you see it?"
    a_b "this pretty, soft, small little pussy?"
    a_b "it will never be yours..... EVER!"
    a_be "hahh... ha... i know, i know you want it! i know!"
    a_ab "but i'm the princess! I'm princess azula!"
    a_be "and you can't have it! ha!"
    show apiss 2 with dissolve
    a_b "i want to..."
    a_b "i'm going to piss on your face, thief."
    menu:
        "Accept your fate":
            call gallery_apiss_cont
            
        "Distract her with oral":
            call gallery_apiss_dist

    return

    label gallery_apiss_cont:
        a_b "i want to piss so bad."
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
                a_ab "open your fucking mouth and drink your slut's warm salty piss."
                "you open your mouth, and azula's piss flows into it..."
                "filling your mouth until it overflows down your neck."
                a_b "now, swallow some you dirty pervert. swallow my fucking piss."
                show apiss an2 with dissolve
                a_be "ah....."
                menu:
                    "let her finish":
                        a_be "almost...."
                    
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

            "take it":
                a_be "that's it..."
                a_b "good little peasant."
                show apiss an1
                a_be "aaahhh... take azula's piss now..."
                a_b "you like it, don't you? that's it, drink it up..."
                a_b "open your mouth, {i}lover{/i}...."
                show apiss an1 with dissolve
                a_ab "open your fucking mouth and drink your slut's warm salty piss."
                "you open your mouth, and azula's piss flows into it..."
                "filling your mouth until it overflows down your neck."
                a_b "now, swallow some you dirty pervert. swallow my fucking piss."
                show apiss an2 with dissolve
                a_be "ah....."
                menu:
                    "let her finish":
                        a_be "almost...."
                        
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
        scene bg_a_city_night with dissolve

        return
    label gallery_apiss_dist:
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
        a_ube "{size=-4}yes... peasant... thief... lick me... taste me... taste my pussy..."
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
        a_b "ah... that was nice... thief..."
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
###### [Azula] Footjob
label gallery_afootjob4:
    call gallery_dCharacter_2Slave

    show aft1 with dissolve
    a_ "come here, [acallme]."
    a_ "i want to feel your cum dripping down my little toes."
    show aft2 with dissolve
    a_ "mmmmm..."
    hide aft1
    a_ "i see you're ready."
    show aft3 with dissolve
    a_ "oh, no..."
    hide aft2
    show aft4 with dissolve
    a_ "i'm... so happy."
    hide aft3
    y "i-"
    show aft5 with dissolve
    a_ "ssh."
    hide aft4
    y "ohh..."
    show aft8 with dissolve
    a_ "*ohh*... mmmm..."
    hide aft5
    show aft6 with dissolve
    a_ "yes, that's it..."
    hide aft8
    show aft with dissolve
    a_ "i like feeling your cock with my soft feet."
    a_ "don't you?"
    call pauseInterface
    a_ "mmm..."
    show aft_fast with dissolve
    call pauseInterface
    a_ "i want you to ejaculate on my pretty little toes."
    hide aft
    a_ "are you getting close?"
    play sound "audio/splurt2.ogg"
    show aft9
    with flash
    y "ngh!"
    hide aft
    hide aft6
    play sound "audio/splurt3.ogg"
    show aft10 with flash
    a_ "yes!"
    hide aft9
    play sound "audio/splurt1.ogg"
    show aft11 with flash
    a_ "more!"
    y "aahhhh...."
    call pauseInterface
    show aft13 with dissolve
    a_ "so good..."
    hide aft11
    a_ "thank you, [acallme]... thank you so much..."
    hide bg_a_smallpalaceroom
    hide aft12

    return
###### [Azula] Boobjob
label gallery_aboobjob4:
    call gallery_dCharacter_2Slave

    show atf1a with dissolve
    call pauseInterface
    y "good girl."
    y "do you like being on your knees?"
    a "yes... because then i get cock."
    y "lift your shirt."
    show atf2a with dissolve
    call pauseInterface
    ab "is this right, [acallme]?"
    hide atf1a
    ab "do you want to see your breasts?"
    y "oh hell yes."
    ab "...."
    y "i'd hate to see those beautiful tits go to waste."
    ab "thank you."
    ab "please don't keep me waiting, [acallme]."
    show atf3a with dissolve
    call pauseInterface
    hide atf2a
    y "i'm going to fuck your tits properly."
    ab "mmm..."
    y "squeeze them around my cock."
    show atf4a with dissolve
    call pauseInterface
    y "ahh... good girl..."
    hide atf3a
    y "how long have you been waiting to do this?"
    ab "all day, [acallme]."
    y "keep squeezing."
    show atf_1a
    call pauseInterface
    y "oh fuck... that's right."
    show atf_2a
    ab "thank you [acallme], thank you [acallme], thank you [acallme]..."
    hide atf_1a
    ab "am i pleasing you?"
    y "it'd be better if you weren't so lazy."
    ab "i'm so sorry, [acallme]!"
    show atf_3a
    call pauseInterface
    ab "*umph*"
    ab "is this better?! please say it's better!"
    ab "fuck my titties! fuck my titties!"
    hide atf_2
    ab "i love your big strong cock between my fat titties, [acallme]."
    ab "this is their purpose! this is why i have them!"
    ab "fuck my titties, [acallme]! fuck them, fuck them!"
    ab "*uhn-umph-ungh*"
    y "do you need some encouragement?"
    ab "yes, [acallme]!."
    play sound "audio/slap.mp3"
    show atf9a
    hide atf_3a
    with flash
    asu "!!!"
    aab "yes!"
    play sound "audio/slap.mp3"
    show atf10a
    hide atf9a
    with flash
    aab "yes! slap your bitch!"
    y "shut up, slave."
    ab "mmm... thank you [acallme]."
    y "are you going to be a good girl and keep rubbing those warm, soft breasts around my cock?"
    show atf_5a
    ab "everything for you, [acallme]."
    hide atf10a
    y "what are you doing right now?"
    ab "i'm jacking you off with my breasts."
    ya "faster!"
    show atf_6a
    call pauseInterface
    "azula speeds up, her soft mounds enveloping your cock as the inside of her tits are lubricated with precum."
    y "ngh... feel that?"
    y "i'm getting close, so you know what's going to happen?"
    hide atf_5a
    ab "will you cum on me?"
    y "remember how you made me cum on poor lia's face?"
    ab "yes...!"
    y "well i'm going to return the favor."
    ab "oh, yes! thank you!"
    play sound "audio/splurt3.ogg"
    show atf11a
    with flash
    asu "!!!"
    hide atf_6a
    play sound "audio/splurt1.ogg"
    show atf12a
    with flash
    ab "yes! shoot it on my f-"
    hide atf11a
    show atf13a
    play sound "audio/splurt3.ogg"
    with flash
    ab "there's so m-"
    hide atf12a
    play sound "audio/splurt2.ogg"
    with flash
    call pauseInterface
    ab "*mmmmmm* you ejaculated on my face..."
    ab "i love it."
    y "i'll see you around, slut."
    ab "*mmmmmmm*"
    hide atf4a
    show atf14a with Dissolve(0.3)
    hide atf13a
    call pauseInterface

    return
###### [Azula] Buttjob
label gallery_abuttjob4:
    call gallery_dCharacter_2Slave

    hide a_blink with dissolve
    scene bg_a_smallpalaceroom
    show ash1 with dissolve
    call pauseInterface
    y "now that's a great ass."
    show ash2 with dissolve
    ab "thank you, [acallme]!"
    show ash_1 with dissolve
    hide ash1
    hide ash2
    call pauseInterface
    show ash3 with dissolve
    hide ash_1
    
    menu:
        "put a finger in her ass":
            show ashf1 with dissolve
            au "hm-?"
            hide ash3
            show ashf2 with dissolve
            ab "aahhh..."
            hide ashf1
            y "that's right, there's a finger in your ass."
            show ashf1 with dissolve
            ab "oh-"
            hide ashf2
            show ash_f
            ab "ahh...."
            hide ashf1
            ab "it feels... nice..."
            show ash3 with dissolve
            hide ash_f
            aub "please... do... what you'd like..."
            y "well, i'd like to fuck these voluptuous ass cheeks of yours."
            y "back up into my cock."
            show ash4 with dissolve
            y "good girl!"
            hide ash3
            aub "..."
            y "i'm gonna rub my cock between your cheeks until i cum."
            ab "mmmm....."
            ab "please let me feel that cock."
            show ash_2
            y "you want it bad, don't you?"
            ab "mmhmm."
            y "does slutty mcbitchface want a cock between her perfect cock-press?"
            au "yes... please, yes..."
            ab "{size=-4}*mmmm...*"
            y "how many cocks have you jacked off with this perfect little ass?"
            aa "only yours, lord."
            y "ohhh... fuck, your ass feels good."
            y "you're trying to make me cum, aren't you?"
            ab "of course, [acallme]..."
            y "that's fine, because i'm going to cum all over your ass."
            ab "please and thank you, [acallme]."
            y "oh fuck, you feel so gooood..."
            y "that's right... use that bubble butt to make me cum, whore."
            y "it's what you're here for."
            y "you love it, don't you, whore?"
            ab "yes...."
            hide ash_2
            ab "thank you..."
            y "now tell me what you're doing."
            show ash_2
            ab "i'm rubbing my asscheeks up and down on your cock."
            y "you feel me twitching between your buttcheeks?"
            abe "...yes..."
            y "a little faster..."
            show ash_3
            y "yes... oh fuck..."
            hide ash_2
            y "are you ready to have your pretty little ass drenched in cum, azula?"
            ab "so much sir, i want to cry..."
            ab "i need it, i haven't had any cum on me all day..."
            y "ungh....."
            hide ash_3
            play sound "audio/splurt3.ogg"
            show ash6
            with flash
            y "fuck!"
            hide ash4
            play sound "audio/splurt1.ogg"
            show ash7
            with flash
            a "*mmmm*... thank you!"
            hide ash6
            play sound "audio/splurt3.ogg"
            show ash8
            with flash
            y "ahh..."
            hide ash7
            call pauseInterface
            y "look at the pretty little fire princess's ass, covered in spunk."
            abe "..."
            y "Look how soiled you are."
            y "you'll never be clean again."
            y "but you know that, don't you?"
            ab "*mmmmmm*"
            hide ash2
            hide ash3
            show ash10 with dissolve
            y "stay right there."
            ab "hmm...?"
            y "guard!"
            asu "oh?"
            g1 "yes, sir."
            ab "..."
            y "call her a slut."
            g1 "your high... azula. you're a disgusting slut."
            ab "mmmmm....."
            y "want to cum on it, too?"
            g1 "uh..."
            ab "it's okay, really. bring a friend."
            g1 "it's like a dream come true..."
            aub "please cum on me, guard..."
            ab "it's what [acallme] wants."
            g1 "...i hate watching your shapely, demanding, bitchy ass!"
            g1 "i'm gonna glaze you like a donut!"
            y "heh."
            g1 "ugh!"
            show ash11 with dissolve
            asu "oh!!!"
            hide ash10
            g2 "can i get in on this?"
            y "definitely."
            g2 "say please, whore."
            ab "...please..."
            g2 "ugh!"
            show ash12 with dissolve
            hide ash11
            abe "ahh...mmm..."
            y "i think that's enough for now. you guys can go."
            "the two guards scurry off, but take a good long look before they round the corner."
            y "see you next time... princess."
            abe "thank you for everything, [acallme]."
            call pauseInterface
            hide ash12
            hide ash8

        "put your cock between her buttcheeks":
            y "well, i'd like to fuck these voluptuous ass cheeks of yours."
            y "back up into my cock."
            show ash4 with dissolve
            y "good girl!"
            hide ash3
            aub "..."
            y "i'm gonna rub my cock between your cheeks until i cum."
            ab "mmmm....."
            ab "please let me feel that cock."
            show ash_2
            y "you want it bad, don't you?"
            ab "mmhmm."
            y "does slutty mcbitchface want a cock between her perfect cock-press?"
            au "yes... please, yes..."
            ab "{size=-4}*mmmm...*"
            y "how many cocks have you jacked off with this perfect little ass?"
            aa "only yours, lord."
            y "ohhh... fuck, your ass feels good."
            y "you're trying to make me cum, aren't you?"
            ab "of course, [acallme]..."
            y "that's fine, because i'm going to cum all over your ass."
            ab "please and thank you, [acallme]."
            y "oh fuck, you feel so gooood..."
            y "that's right... use that bubble butt to make me cum, whore."
            y "it's what you're here for."
            y "you love it, don't you, whore?"
            ab "yes...."
            hide ash_2
            ab "thank you..."
            y "now tell me what you're doing."
            show ash_2
            ab "i'm rubbing my asscheeks up and down on your cock."
            y "you feel me twitching between your buttcheeks?"
            abe "...yes..."
            y "a little faster..."
            show ash_3
            y "yes... oh fuck..."
            hide ash_2
            y "are you ready to have your pretty little ass drenched in cum, azula?"
            ab "so much sir, i want to cry..."
            ab "i need it, i haven't had any cum on me all day..."
            y "ungh....."
            hide ash_3
            play sound "audio/splurt3.ogg"
            show ash6
            with flash
            y "fuck!"
            hide ash4
            play sound "audio/splurt1.ogg"
            show ash7
            with flash
            a "*mmmm*... thank you!"
            hide ash6
            play sound "audio/splurt3.ogg"
            show ash8
            with flash
            y "ahh..."
            hide ash7
            call pauseInterface
            y "look at the pretty little fire princess's ass, covered in spunk."
            abe "..."
            y "Look how soiled you are."
            y "you'll never be clean again."
            y "but you know that, don't you?"
            ab "*mmmmmm*"
            hide ash2
            hide ash3
            show ash10 with dissolve
            y "stay right there."
            ab "hmm...?"
            y "guard!"
            asu "oh?"
            g1 "yes, sir."
            ab "..."
            y "call her a slut."
            g1 "your high... azula. you're a disgusting slut."
            ab "mmmmm....."
            y "want to cum on it, too?"
            g1 "uh..."
            ab "it's okay, really. bring a friend."
            g1 "it's like a dream come true..."
            aub "please cum on me, guard..."
            ab "it's what [acallme] wants."
            g1 "...i hate watching your shapely, demanding, bitchy ass!"
            g1 "i'm gonna glaze you like a donut!"
            y "heh."
            g1 "ugh!"
            show ash11 with dissolve
            asu "oh!!!"
            hide ash10
            g2 "can i get in on this?"
            y "definitely."
            g2 "say please, whore."
            ab "...please..."
            g2 "ugh!"
            show ash12 with dissolve
            hide ash11
            abe "ahh...mmm..."
            y "i think that's enough for now. you guys can go."
            "the two guards scurry off, but take a good long look before they round the corner."
            y "see you next time... princess."
            abe "thank you for everything, [acallme]."
            call pauseInterface
            hide ash12
            hide ash8

        "fuck her ass":
            show ash13 with dissolve
            ab "mmmm.... sir... what are you..."
            y "trying something."
            show ash14 with dissolve
            abe "ah..."
            ab "you're... ah... going into my... ah..."
            hide ash13
            show ash15 with dissolve
            asbe "*ohhhhh!!*"
            abe "yes!!!"
            y "your what?"
            hide ash14
            asbe "my... ngh... fat, stupid, whore ass..."
            show ash13 with dissolve
            y "what's my name?"
            hide ash15
            abe "[acallme]."
            show ash_an1
            aae "ah!"
            call pauseInterface
            aae "*ngh!* *ungh!* *ah!*"
            aae "yes, [acallme]! fuck that ass!"
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
            aabe "my ass! ngh! fuck, yes!"
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
                    ab "that was so wonderful, [acallme]."
                    ab "thank you."
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
                    ab "that was so wonderful, [acallme]."
                    ab "thank you."
                    call pauseInterface
                    hide ash13
                    hide ash19 with dissolve

        "fuck her pussy":
            show ash13_1 with dissolve
            ab "mmmm.... sir... that's my pussy..."
            y "i know."
            show ash14_1 with dissolve
            abe "ah..."
            ab "you're... ah... my... ah..."
            hide ash13_1
            show ash15_1 with dissolve
            asbe "*mmmmm...*"
            abe "yes!!!"
            y "your what?"
            hide ash14_1
            asbe "my... ngh... tight cunt..."
            show ash13_1 with dissolve
            y "what's my name?"
            hide ash15_1
            abe "[acallme]."
            show ash_an1_1
            aae "ah!"
            call pauseInterface
            aae "*ngh!* *ungh!* *ah!*"
            aae "yes, [acallme]! fuck my cunt!"
            aab "come on, fuck me!"
            aab "fuck me!"
            aabe "pound that tight fucking cunt!"
            y "fine! you want it rough?"
            aab "yes!"
            y "*grr*"
            show ash_an2_1
            call pauseInterface
            aabe "yes! yes!"
            hide ash_an1_1
            abe "ugh! ngh! ah... ah... ha..."
            abe "ohhh... ah...."
            y "you're not getting off that easy!"
            aub "wha-"
            show ash_an3_1
            asb "ah! ah! ah!"
            hide ash_an2_1
            asbe "wait! wait!"
            aabe "my pussy! ah! fuck yes!"
            aabe "it hurts so fucking good!"
            aabe "*ngh!* *mmgh!*"
            y "you asked for it, bitch!"
            aabe "*ah!* *ungh!*"
            menu:
                "cum outside":
                    hide ash13_1
                    show ash23_1 with flash
                    aub "wh-"
                    hide ash_an3_1
                    play sound "audio/splurt2.ogg"
                    show ash20_1 with flash
                    asb "oh!"
                    hide ash23_1
                    y "fuck!"
                    play sound "audio/splurt2.ogg"
                    show ash21_1 with flash
                    asbe "mmm..."
                    hide ash20_1
                    y "not done yet!"
                    play sound "audio/splurt2.ogg"
                    show ash22_1 with flash
                    abe "ahh...."
                    hide ash21_1
                    y "fuck..."
                    abe "i'm soaked..."
                    abe "i can feel it dripping down my legs..."
                    ab "that was so wonderful, [acallme]."
                    ab "thank you."
                    call pauseInterface
                    hide ash13_1
                    hide ash22_1

                "cum inside":
                    show ash14_1 with dissolve
                    aub "wh-"
                    hide ash_an3_1
                    play sound "audio/splurt2.ogg"
                    show ash17_1 with flash
                    asb "ah!"
                    hide ash14_1
                    y "fuck!"
                    play sound "audio/splurt2.ogg"
                    show ash18_1 with flash
                    asbe "ngh..."
                    hide ash17_1
                    y "not done yet!"
                    play sound "audio/splurt2.ogg"
                    show ash19_1 with flash
                    abe "ahh...."
                    hide ash18_1
                    y "fuck..."
                    abe "i'm so full..."
                    ab "that was so wonderful, [acallme]."
                    ab "thank you."
                    call pauseInterface
                    hide ash13_1
                    hide ash19_1
                    
    return
###### [Azula] Blowjob
label gallery_ablowjob4:
    call gallery_dCharacter_2Slave

    show ablj1a with dissolve
    a "please give me your cock, [acallme]."
    a "i'll suck out all your cum."
    a "i haven't eaten anything today."
    show ablj2a with dissolve
    hide ablj1a
    show ablj4a with dissolve
    a "..."
    hide ablj2a
    hide ablj3a
    show ablj_tuga with dissolve
    y "ngh..."
    call pauseInterface
    y "that's it, princess..."
    a "..."
    y "you have the best dick-sucking lips in the fire nation."
    y "put them to use."
    show ablj3a with dissolve
    hide ablj_tuga
    hide ablj4a
    a "thank you master!"
    show ablj6a with dissolve
    a "..."
    hide ablj3a
    a "i will."
    show ablj7a with dissolve
    hide ablj6a
    a "*mmmmm*"
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
    a "i love the feel of you in my throat..."
    y "get. down. there!"
    a "sorry, [acallme]!"
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
    a "i almost came, sir!"
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
    y "little dominating princess turned cumslut."
    a "*ggagghh!* *kaghk!*"
    y "that's it, bitch, work that big shaft with your throat."
    y "drain my sack."
    y "suck out all my cum!"
    show abj_3a with Dissolve(0.2)
    y "come on! come on!"
    hide abj_2a
    y "work that cock, bitch!"
    a "!!!"
    a "*nghh!* *nggh!* *aahngh!*"
    ya "oh fuck!"
    a "*mmmmmmmmmm*"
    menu:
        "piss in her throat":
            hide ablj13a
            show ablj13a with sshake
            a "*mmmm!!!*"
            y "ahh...."
            "while azula's warm mouth is wrapped around your member, you relieve yourself."
            "you empty your bladder in her hot, accepting mouth, and she swallows continuously."
            a "*mmmmmm......*"
            "she moans into your cock, continuing to suck your shaft tightly as she gulps it down."
            "as you finish pissing, she comes up for air with a gasp, smacking her lips."
            show ablj34a with dissolve
            a "ah! yes!"
            hide ablj13a
            a "that was delicious, master! thank you!"
            a "piss in my mouth, like the filthy whore i am!"
            show ablj33a with dissolve
            a "i'm your personal toilet. use my mouth whenever you need to piss."
            hide ablj34a
            a "i'll swallow it all."
            a "i'm so happy. thank you. thank you. thank you!"
            y "but that's not all!"
            show ablj34a with dissolve
            a "hmm-?"
            hide ablj33a

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
                    ya "swallow it, bimbo bitch!"
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
                    a "thank you [acallme], that was very filling."
                    hide ablj35a
                    hide ablj17a
                    show ablj38a with dissolve
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
                    a "yes!"
                    hide ablj22a
                    ya "take it, bitch!"
                    play sound "audio/splurt2.ogg"
                    with flash
                    ya "ngh!"
                    play sound "audio/splurt3.ogg"
                    show ablj24a
                    with flash
                    y "all over your fucking face, slave!"
                    hide ablj23a
                    play sound "audio/splurt1.ogg"
                    show ablj25a
                    with flash
                    hide ablj24a
                    y "ahh..."
                    a "..."
                    call pauseInterface
                    show ablj36a with dissolve
                    a "thank you, [acallme]. i haven't had a facial all day."
                    hide ablj25a
                    show ablj25a with dissolve
                    hide ablj36a
                    hide abj_2a
                    hide ablj10a
                    hide ablj8a
                    hide ablj12a
                    hide ablj3a
                    hide ablj6a
                    hide ablj25a with dissolve

        "cum in her throat":
            hide ablj13a
            show ablj13a with sshake
            a "!!!!!!"
            hide abj_3a
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            with flash
            a "!!!!!!"
            ya "swallow it, bimbo bitch!"
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
            a "thank you [acallme], that was very filling."
            hide ablj35a
            hide ablj17a
            show ablj38a with dissolve
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
            a "yes!"
            hide ablj22a
            ya "take it, bitch!"
            play sound "audio/splurt2.ogg"
            with flash
            ya "ngh!"
            play sound "audio/splurt3.ogg"
            show ablj24a
            with flash
            y "all over your fucking face, slave!"
            hide ablj23a
            play sound "audio/splurt1.ogg"
            show ablj25a
            with flash
            hide ablj24a
            y "ahh..."
            a "..."
            call pauseInterface
            show ablj36a with dissolve
            a "thank you, [acallme]. i haven't had a facial all day."
            hide ablj25a
            show ablj25a with dissolve
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
label gallery_aanal5:
    call gallery_dCharacter_2Slave

    hide a_blink
    show aan1a with dissolve
    menu:
        "use anal beads":
            show aan2a with dissolve
            hide aan1a
            a "oh, yes! i love those!"
            show aan3a with dissolve
            hide aan1a
            y "and in goes number one!"
            show aan4a
            hide aan3a
            with flash
            a "*ah*"
            show aan5a
            hide aan4a
            a "hngh..."
            show aan4a
            hide aan5a
            with flash
            a "mmmm!"
            a "it's..."
            show aan5a with dissolve
            hide aan4a
            a "so good..."
            show aan6a with dissolve
            hide aan5a
            y "number three!"
            show aan4a
            hide aan5a
            with flash
            a "ah....ahhh...."
            show aan5a with dissolve
            hide aan4a
            y "here's several more."
            show aan4a
            hide aan5a
            with flash
            a "nnnngghh...."
            y "now here comes the fun part."
            show aan7a with dissolve
            hide aan4a
            a "pull them!"
            show aan8a with dissolve
            hide aan7a
            y "here we go!"
            show aan9a with dissolve
            hide aan8a
            a "be gen-"
            show aan10a
            hide aan9a
            with flash
            a "ah-"
            show aan11a
            hide aan10a
            with flash
            a "oh..."
            a "that's... ah..."
            show aan12a
            hide aan11a
            with flash
            y "...nice?"
            show aan13a with dissolve
            hide aan12a
            a "mmm... yes..."
            show aan14a
            hide aan13a
            with flash
            a "ah...ha..."
            show aan_beadsa with dissolve
            a "mmmm..."
            call pauseInterface
            show aan17a with dissolve
            hide aan_beads
            hide aan14a
            a "ohh..."
            a "..."
            a "...again?"
            y "you enjoyed that, huh?"
            show aan18a with dissolve
            hide aan17a
            a "i almost came..."
            y "but no, it's time for the main event."
            show aan19a with dissolve
            hide aan18a
            a "the main..."
            y "you have such a nice ass.."
            show aan20a with dissolve
            hide aan19a
            a "yes... yes [acallme]... you know you want to..."
            a "please...."
            call gallery_aanal4_cont

        "fuck her ass":
            show aan19a with dissolve
            hide aan18a
            y "you have such a nice ass.."
            show aan20a with dissolve
            hide aan19a
            a "yes... yes [acallme]... you know you want to..."
            a "please...."
            call gallery_aanal4_cont

        "fuck her pussy":
            show aan19a with dissolve
            hide aan18a
            y "you have such a nice pussy.."
            show aan20a_1 with dissolve
            hide aan19a
            a "yes... yes [acallme]... you know you want to..."
            a "please...."
            call gallery_aanal5_cont

    return

    label gallery_aanal4_cont:
        show aan21a with dissolve
        hide aan20a
        a "yes, [acallme]! take that asshole!"
        a "it's yours! it's all yours!"
        show aan22a with dissolve
        hide aan21a
        a "ah-"
        show aan23a with dissolve
        hide aan22a
        a "let me-"
        show aan24a with ushake
        hide aan23a
        a "aaahh....!!!"
        show aan25a with ushake
        hide aan24a
        a "fuck!!"
        show aan26a with ushake
        hide aan25a
        a "it's so... fucking... thick!"
        y "ngh... yeah..."
        a "*ngh!*"
        show aan25a with dissolve
        hide aan26a
        a "wait-"
        show aan27a with vshake
        hide aan25a
        a "{size=-4}oww...."
        show aan28a with dissolve
        hide aan27a
        a "hnngh...."
        show aan29a with dissolve
        hide aan28a
        a "don't st-"
        show aan30a with vshake
        hide aan29a
        a "ah...!!"
        show aan_anala with dissolve
        call pauseInterface
        y "you've got such a tight fucking ass, azooba."
        a "*umph!*...that's...*ngh!*...right...*ugh!*"
        a "thank...*ungh!*....you...*umph!*...[acallme]!"
        y "are you a sick fucking whore?"
        a "ahh... ha... yes... sir..."
        call pauseInterface
        y "your ass feels so good..."
        a "ah! *ungh!* ah!"
        a "thank... *ngh!*"
        a "thank you!!"
        a "*ah!* *ungh!*"
        y "oh shit, i'm gonna cum."
        a "ah! yes! cum for me! ah!"
        a "cum in my little butthole... it's so soft and delicate... and..."
        y "...and?"
        a "it needs to be full of cum!"
        play sound "audio/splurt3.ogg"
        show aan31a
        with flash
        y "bitch!"
        hide aan_anala
        hide aan30a
        a "aah...."
        play sound "audio/splurt1.ogg"
        show aan32a
        with flash
        a "my little butt...."
        hide aan31a
        y "ngh!"
        play sound "audio/splurt2.ogg"
        show aan33a
        with flash
        a "yes..."
        hide aan32a
        play sound "audio/splurt2.ogg"
        with flash
        a "ahh... that was so wonderful..."
        show aan34a with dissolve
        a "you imbecile..."
        show aan35a with dissolve
        hide aan34a
        y "...."
        y "so azula, how does a cum-filled ass feel?"
        show aan34a with dissolve
        hide aan35a
        a "amazing..."
        y "i can actually feel your pulse around my cock - that's how tight you are."
        a "mmmm....."
        y "alright fine, i'll leave you and your tight little ass, cumdump."
        a "aw...."
        y "watch your mouth slave, or i'll fuck it."
        hide aan34a with dissolve
        a "mmmm...."
        hide aan34a with dissolve
        hide bg_a_smallpalaceroom
        
        return

    label gallery_aanal5_cont:
        show aan21a_1 with dissolve
        hide aan20a_1
        a "yes, [acallme]! take that pussy!"
        a "it's yours! it's all yours!"
        show aan22a_1 with dissolve
        hide aan21a_1
        a "ah-"
        show aan23a_1 with dissolve
        hide aan22a_1
        a "let me-"
        show aan24a_1 with ushake
        hide aan23a_1
        a "aaahh....!!!"
        show aan25a_1 with ushake
        hide aan24a_1
        a "fuck!!"
        show aan26a_1 with ushake
        hide aan25a_1
        a "it's so... fucking... thick!"
        y "ngh... yeah..."
        a "*ngh!*"
        show aan25a_1 with dissolve
        hide aan26a_1
        a "wait-"
        show aan27a_1 with vshake
        hide aan25a_1
        a "{size=-4}oww...."
        show aan28a_1 with dissolve
        hide aan27a_1
        a "hnngh...."
        show aan29a_1 with dissolve
        hide aan28a_1
        a "don't st-"
        show aan30a_1 with vshake
        hide aan29a_1
        a "ah...!!"
        show aan_anala_1 with dissolve
        call pauseInterface
        y "you've got such a tight fucking cunt, azooba."
        a "*umph!*...that's...*ngh!*...right...*ugh!*"
        a "thank...*ungh!*....you...*umph!*...[acallme]!"
        y "are you a sick fucking whore?"
        a "ahh... ha... yes... sir..."
        call pauseInterface
        y "your pussy feels so good..."
        a "ah! *ungh!* ah!"
        a "thank... *ngh!*"
        a "thank you!!"
        a "*ah!* *ungh!*"
        y "oh shit, i'm gonna cum."
        a "ah! yes! cum for me! ah!"
        a "cum in my little cunt... it's so ready... and..."
        y "...and?"
        a "it needs to be full of cum!"
        play sound "audio/splurt3.ogg"
        show aan31a_1
        with flash
        y "bitch!"
        hide aan_anala_1
        hide aan30a_1
        a "aah...."
        play sound "audio/splurt1.ogg"
        show aan32a_1
        with flash
        a "my little pussy...."
        hide aan31a_1
        y "ngh!"
        play sound "audio/splurt2.ogg"
        show aan33a_1
        with flash
        a "yes..."
        hide aan32a_1
        play sound "audio/splurt2.ogg"
        with flash
        a "ahh... that was so wonderful..."
        show aan34a_1 with dissolve
        a "*mmmm*..."
        show aan35a_1 with dissolve
        hide aan34a_1
        y "...."
        y "so azula, how does a cum-filled pussy feel?"
        show aan34a_1 with dissolve
        hide aan35a_1
        a "amazing..."
        y "alright fine, i'll leave you and your tight little pussy."
        a "aw...."
        y "watch your mouth slave, or i'll fuck it."
        hide aan34a_1 with dissolve
        a "mmmm...."
        hide aan34a_1 with dissolve
        hide bg_a_smallpalaceroom

        return
###### [Azula] Pussy Grind
label gallery_agrind4:  
    call gallery_dCharacter_2Slave

    scene bg_a_azula_room with dissolve
    show azg2a with dissolve
    a "you're so good to me!"
    show azg3 with dissolve
    a "i'm going to cum all over your nice cock."
    hide azg2a
    a "*mmmm*"
    show azg2a with dissolve
    y "you like that cock, slave?"
    hide azg3
    show azg3 with dissolve
    a "yes, [acallme]! it's so good on my clit!"
    hide azg2a
    show azg2 with dissolve
    a "it's rubbing... ah... on my clit... so... ah..."
    hide azg3
    y "...."
    show azg4 with dissolve
    a "....."
    hide azg2
    show azg_an1 with dissolve
    call pauseInterface
    a "ah...."
    a "yes....."
    a "rubbing a big... ah... big cock..."
    a "so fucking... ah... warm... feel... so g... ah... ha..."
    show azg_an2 with dissolve
    hide azg_an1
    call pauseInterface
    a "ah! ah! ah!!"
    a "yes... yes... it feels so good, so fucking good..."
    a "i'm so lucky... you're so handsome..."
    a "you're perfect... and smart... and ruthless..."
    a "and... and..."
    a "and i'm... i'm..."
    a "ah... ah... {size=+4}ah... {size=+6} ah..."
    show azg7 with flash
    with ushake
    a "{size=+6}aaah!!"
    hide azg_an2
    show azg8 with dissolve
    a "unghh...."
    a "oh, [acallme]...."
    call pauseInterface
    hide azg7
    show azg9 with dissolve
    a "mmmm..."
    hide azg8
    hide azg4
    show azg4 with dissolve
    a "......"
    show azg_an2
    a "........"
    y "(oh fuck...)"
    a_b "that's it, [acallme]..."
    a_b "feel these warm, soft pussy lips."
    a_be "mmm... i'm rubbing my sopping wet pussy on your cock."
    a_b "you feel how wet it is?"
    a_b "i squirted all over your cock."
    a_be "and now i'm rubbing it into you."
    a_b "do you enjoy it [acallme]? please enjoy it..."
    a_b "i want to feel you cum from my soaking wet pussy lips."
    a_ab "cum for me, [acallme]! cum for me!"
    a_ab "cum from fucking my sloppy wet cunt lips!"
    y "i can't take it! i'm gonna cum!"
    a_ab "yes! yes!"
    show azg10 with dissolve
    a_ab "cum for me!"
    a_ab "give me that hot, thick cum!"
    hide azg_an2
    play sound "audio/splurt3.ogg"
    show azg11 with flash
    a_ab "that's it!"
    a_ab "cum in my hand!"
    hide azg10
    play sound "audio/splurt2.ogg"
    with flash
    a_b "let it all out..."
    play sound "audio/splurt2.ogg"
    show azg12 with flash
    y "hngh...."
    hide azg11
    call pauseInterface
    a_b "it's so warm."
    hide azg4
    hide azg9
    hide azg1
    scene bg_a_azula_room with dissolve
    hide azg12
    show afnb with dissolve
    a "mmmm... thank you [acallme]!"
    a "it's a perfect moisturizer."
    show afnbe
    a "*mmmmmm*"
    show afnab with dissolve
    a "thank... you..."

    return
###### [Azula] Tentacle Anal
label gallery_tentacle_training:
    call gallery_dCharacter_2Slave

    scene bg_a_swamp_2 with dissolve
    show azswrp swrp07 with dissolve
    y "oh. fuck. that's why."
    show azswrp swrp06 with dissolve
    y "that's... not good."
    a "don't just stand there! help me!"
    "as you step forward, vines wrap around your arms and legs, holding you firmly in place."
    y "fuck!"
    cr "{b}you will go nowhere, human."
    show azswrp swrp101 with dissolve
    a "ahh!"
    call pauseInterface
    a "no! it's...!"
    a "stop!"
    a "my a-"
    show azswrp swrp100 with dissolve
    "overwhelmed by shock, azula passes out."
    cr "{b}aw... did the little bitch pass out?"
    cr "{b}did she pass out from getting her ass slammed by a monster?"
    call pauseInterface
    y "azula! wake up!"
    show azswrp swrp101 with dissolve
    a "wha-"
    show azswrp swrp103 with dissolve
    a "ahh! my- my ass!"
    a "t-they're in my asshole!"
    call pauseInterface
    a "stop this at... at once!"
    show azswrp swrp104 with dissolve
    call pauseInterface
    "*sblurp* *gltch* *glop*"
    aae "ngh!"
    aae "my *ah* little *ugh* ass!"
    aa "it's *mngh* being filled! do *ha* something!"
    show azswrp swrp105 with dissolve
    call pauseInterface
    aae "*ngh!* *agh!*"
    aae "it's thick and slimy in my asshole!"
    "the creature growls and pulls out."
    show azswrp swrp25 with dissolve
    call pauseInterface
    aub "oh, thank-"
    show azswrp swrp108 with dissolve
    call pauseInterface
    asu "oh!"
    aae "ow..."
    au "my... my poor pussy!"
    show azswrp swrp109 with dissolve
    call pauseInterface
    au "why?!"
    aae "ow-how!"
    au "why are you doing this?!"
    cr "{b}I want you to suffer, bitch!"
    show azswrp swrp17 with dissolve
    asu "oof!"
    aue "you're... pulling too h-"
    show azswrp swrp19 with dissolve
    aub "wait-"
    show azswrp swrp21 with dissolve
    aube "ah! no!"
    show azswrp swrp22 with dissolve
    aae "hngh!"
    cr "{b}yes! that's it! feel my wrath!"
    show azswrp swrp23 with dissolve
    asu "aaah!!"
    aae "stop, stop!"
    show azswrp swrp106 with dissolve
    call pauseInterface
    asu "AAAAAHHHH!"
    aae "ah! thief! ow! help!"
    y "just give him what he wants! maybe it'll leave us alone when it's finished!"
    show azswrp swrp107 with dissolve
    aa "i don't-"
    asu "ah!"
    aa "want him to \"finish\"!"
    show azswrp swrp24 with sshake
    asu "aaaah!"
    y "looks like he finished anyway..."
    au "w-what even is this...?"
    cr "{b}you are full of spirit cum. congratulations, you're a cross-dimensional whore."
    show azswrp swrp20 with dissolve
    aue "ohhh....."
    show azswrp swrp110 with dissolve
    call pauseInterface
    aue "annghh...."
    y "at least he saved your pussy for me...."
    aa "what?!"
    y "noth-"
    show azswrp swrp07 with dissolve
    y "oh. uh... azula?"
    aa "what!"
    y "i don't think it's... uh..."
    aa "spit it out, you idiot!"
    show azswrp swrp112
    asu "ah!!"
    y "...done."
    call pauseInterface
    y "you're just gonna have to ride it out, i think."
    y "why are you doing this?"
    y "why do you hate azula?"
    cr "{b}i... can't help it. we pick up our host's feelings... don't we?"
    y "what are you talking about?"
    show azswrp swrp111
    call pauseInterface
    show azswrp swrp102 with dissolve
    cr "{b}but tell me, what do you think, human male?"
    cr "{b}where should I finish on this female?"
    cr "{b}this {i}azula?"
    y "(oh shit, it knows azula. how? and why does it hate her?)"
    "{b}answer quickly, human!"
    auce "shouldn't i get a say...?"

    menu:
        "inside":
            y "no."
            y "fill up that slut's ass, weird... magic tree."
            cr "{b}hmmmm!"
            play sound "audio/splurt3.ogg"
            show azswrp swrp13 with vshake
            auce "......"
            play sound "audio/splurt1.ogg"
            show azswrp swrp14 with vshake
            cr "{b}yes, indeed..."
            play sound "audio/splurt2.ogg"
            show azswrp swrp15 with vshake
            auce "*whimper*"
            show azswrp swrp15_1 with dissolve
            auc "my poor asshole...."
            auc "i'm so sore...."
            auce "hhn..."
            show azswrp swrp15 with dissolve
            "worn out by the merciless assfucking, azula faints."

        "outside":
            y "no."
            y "drench that slut, you giant vegetable."
            cr "{b}hmmmm!"
            play sound "audio/splurt3.ogg"
            show azswrp swrp10 with dissolve
            auce "......"
            play sound "audio/splurt1.ogg"
            show azswrp swrp11 with dissolve
            cr "{b}yes, indeed..."
            play sound "audio/splurt2.ogg"
            show azswrp swrp12 with dissolve
            auce "*whimper*"
            show azswrp swrp12_1 with dissolve
            auc "my poor asshole...."
            auc "i'm so sore...."
            auce "hhn..."
            show azswrp swrp12 with dissolve
            "worn out by the merciless assfucking, azula faints."

    return

###### [Azula] Pussy Lick
label gallery_aprison_lick:
    call gallery_dCharacter_2Slave

    show azmb mb47_3 with dissolve
    a "hmm...?"
    show azmb mb108 with dissolve
    a "ah...."
    a "............"
    a "master..."
    show azmb mb108_1 with dissolve
    a "mmm....."
    show azmb mb109 with dissolve
    a "i'm... i'm gonna...."
    a "ah... ah....."
    a "I'm gonna...."
    show azmb mb52_1 with dissolve
    with vshake
    a "*ah!*"
    show azmb mb51 with dissolve
    a "......"
    a "thank you, master..."
    show azmb mb48_1 with dissolve
    call gallery_prision_fuck
    return

###### [Azula] Prision Fuck
label gallery_prision_fuck:
    show azmb mb17 with dissolve
    a "m... master?"
    show azmb mb18 with dissolve
    a "ahh....."
    show azmb mb22 with ushake
    a "*aaahhh....!!*"
    show azmb mb103 with dissolve
    a "yes, master!"
    call pauseInterface
    y "what are you?"
    show azmb mb103_2 with dissolve
    a "a stupid bitch, master."
    y "sing me a song."
    a "i'm just a dumb bitch, short and stout..."
    show azmb mb103_1 with dissolve
    call pauseInterface
    a "here is my pussy, here is my mouth..."
    a "well i get all horny, here me shout..."
    a "fill me up, let it drain out!"
    y "that's good girl."
    show azmb mb103_3 with dissolve
    a "thank you, master..."

    menu:
        "turn her around":
            call gallery_prision_fuck_turn_around
        "keep going":
            call gallery_prision_fuck_keep_going

    call gallery_prision_fuck_cum_menu
    return

    label gallery_prision_fuck_turn_around:
        show azmb mb57 with dissolve
        y "stick your ass out."
        a "yes, master..."
        show azmb mb56 with dissolve
        y "good girl."
        show azmb mb58 with dissolve
        a "please... i can't wait-"
        show azmb mb59 with dissolve
        a "*ahh...!*"
        show azmb mb112 with dissolve
        call pauseInterface
        a "do you like looking at my ass, master?"
        a "it's yours. all yours."
        a "please... *ngh!*... pound my pussy, master."
        call pauseInterface
        y "alright, let's turn you around, i have one last thing to do."
        show azmb mb26 with dissolve
        a "wh..."
        a "please don't tease me, master..."
        a "I promise i'll be good."
        a "please-"
        show azmb mb105_3 with dissolve
        a "*ohh...*"
        call pauseInterface
        a "mmmm.... i'm squeezing your cock with my pussy... do you like that, master?"
        a "*ah*...*ngh*..."
        a "do you like getting your cock squeezed by my tight little cunt?"
        a "i feel you thick and throbbing in there."
        show azmb mb104_1 with dissolve
        a "i know you want to fill good little azula up with your fat load of jizz."
        a "ah...ha...mmmm..."
        a "you do, don't you?"
        show azmb mb104 with dissolve
        a "go ahead, baby. let it out. whenever you want."
        a "let it all out. until i'm dripping out your hot, sticky, cumload."
        
        return
    label gallery_prision_fuck_keep_going:
        show azmb mb26 with dissolve
        a "wh..."
        a "please don't tease me, master..."
        a "I promise i'll be good."
        a "please-"
        show azmb mb105_3 with dissolve
        a "*ohh...*"
        call pauseInterface
        a "mmmm.... i'm squeezing your cock with my pussy... do you like that, master?"
        a "*ah*...*ngh*..."
        a "do you like getting your cock squeezed by my tight little cunt?"
        a "i feel you thick and throbbing in there."
        show azmb mb104_1 with dissolve
        a "i know you want to fill good little azula up with your fat load of jizz."
        a "ah...ha...mmmm..."
        a "you do, don't you?"
        show azmb mb104 with dissolve
        a "go ahead, baby. let it out. whenever you want."
        a "let it all out. until i'm dripping out your hot, sticky, cumload."

        return

    label gallery_prision_fuck_cum_menu:
        menu:
            "cum inside":
                call gallery_prision_fuck_cum_inside
            "cum outside":
                call gallery_prision_fuck_cum_outside

        return
    
        label gallery_prision_fuck_cum_inside:
            y "ngh!"
            a "yes! give it to me!"
            play sound "audio/splurt3.ogg"
            show azmb mb38 with flash
            y "bitch!"
            a "{size=+5}yes!!!"
            play sound "audio/splurt2.ogg"
            show azmb mb39 with flash
            a "*ah!* i-i'm cumming!!"
            play sound "audio/splurt3.ogg"
            show azmb mb40 with flash
            a "ahhh...."
            a "*mmmmm*..."
            a "am i a good cumrag, master?"
            y "yes, you are."
            show azmb mb40_3 with dissolve
            a "thank you master."
            
            return

        label gallery_prision_fuck_cum_outside:
            y "ngh!"
            a "yes! give it to me!"
            play sound "audio/splurt2.ogg"
            show azmb mb35 with flash
            y "bitch!"
            a "{size=+5}yes!!!"
            play sound "audio/splurt3.ogg"
            show azmb mb36 with flash
            "*ah!* i-i'm cumming!!"
            play sound "audio/splurt1.ogg"
            show azmb mb37 with flash
            call pauseInterface
            a "ahhh...."
            a "*mmmmm*..."
            a "am i a good cumrag, master?"
            y "yes, you are."
            show azmb mb37_1 with dissolve
            a "thank you master."
            
            return
###### [Ending] Group Sex
label gallery_fpalace_day10:
    call gallery_dCharacter_2Slave

    $ azula_four = False
    $ tylee_four = False
    $ mai_four = False


    scene bg_a_threesome_02 with dissolve
    show az3sm az3sm07 with dissolve
    call pauseInterface
    y "whoa, hey mai. why are you here?"
    m "...azula asked me here. naked."
    y "and you just came?"
    m "she's been different lately, so it's fine. thanks to you i guess."
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
    a "well, the cows escaped from the farm, and apparently had weapons-"
    m "my weapons...."
    a "anyway, everybody's out dealing with that so we thought we'd have a little fun..."
    a "and put on a show for you."
    hide a_blink with dissolve
    show az3sm az3sm09 with dissolve
    menu:
        a "wanna watch us have a little girl time?"
        "oh hell yeah":
            y "girls, azula is now an all-you-can-eat buffet."
            t "ooo! dibs on her pussy!"
            a "mmmm..."
            m "alright."
            show az3sm az3sm100 with dissolve
            a "*aahhhh.....*"
            call pauseInterface
            t "mmmm.... *shlick* *shlick*"
            a "oh yes! lick my cunt!"
            m "mmngh mngh..."
            a "ah... ah... suck my nipples..."
            a "don't be shy! suck them! i wanna cum!"
            show az3sm az3sm101 with dissolve
            t "you having fun over there? you're the expert on azula's pussy."
            y "i am. now give me a good fucking show."
            a "get back on my clit, ty lee!"
            t "heehee, yes ma'am!"
            show az3sm az3sm100 with dissolve
            t "*lick* *mm*"
            t "you have the sweetest, prettiest pussy, azula!"
            m "mmhmm..."
            a "ah! yes! don't... don't stop....."
            a "this is for you. this is for you, [acallme]. do you like it? are you happy?"
            y "maybe i should-"
            show az3sm az3sm102 with dissolve
            m "stay right there."
            m "azula needs to cum and you're not allowed over here."
            m "you just have to watch."
            y "that's-"
            m "shut up. azula needs her titties sucked."
            a "i really do... come back..."
            show az3sm az3sm100 with dissolve
            a "yes... that's it..."
            a "good little sluts... take care of your princess..."
            a "ah... ah-ha... ty lee... i'm gonna cream on your face..."
            a "keep tonguing my cunt... keep your tongue... ah... yes..."
            a "oh, mai... mai suck harder... suck harder! own my fucking tit!"
            a "oh fuck! fuck! i'm gonna fucking... girls, keep sucking and licking your princess!"
            a "you're going to get a gift... ah... ah... ah! ah!!!"
            call pauseInterface
            with vshake
            show az3sm az3sm17 with dissolve
            a "ohhhh...."
            with vshake
            "...fuck that was so nice...."
            a "....get your tongue out."
            t "bu' oo oh 'asty..."
            a "i know i'm tasty. get your tongue out of my cunt."
            t "aww...."
            show az3sm az3sm22 with dissolve
            t "that was fun!"
            a "mmm...."

        "Fuck them instead.":
            call gallery_fpalace_day11

    return

    label gallery_fpalace_day11:
        show az4sm az4sm34 with dissolve
        call pauseInterface
        a_ub "so. would you like to fuck my friends?"
        a_ube "...and me?"
        y "you know... I think I might."
        a_be "then i need you to drink something."
        y "what?"
        a_b "there's potion on the table. it will... satisfy all of us."
        y "...alright, fine."
        scene black with dissolve
        "you drink the potion."
        "your cock immediately engorges... you feel pent up like you never have before."
        show az4sm az4sm34 with dissolve
        y "what the hell was that?"
        a_be "that... was to make sure we all have a chance at some fun."
        show az4sm az4sm35 with dissolve
        "your cock throbs as you stare at the three pussies in front of you."
        y "oh, i'm ready now."
        t_ "whatcha doing back there?"
        play sound "audio/gltch.mp3"
        show az4sm az4sm36 with pflash
        t_l "ah..."
        call pauseInterface
        m_l "mmmm... {i}finally."
        play sound "audio/gltch.mp3"
        show az4sm az4sm37 with dissolve
        t_l "ooohhhhh....."
        a_b "you just dig in, don't you?"
        a_be "that's why you're in charge."
        t_ "he really owns it..."
        y "girls? i'm right here."
        show az4sm az4sm106 with dissolve
        t_l "ah...ah...ha...easy...easy..."
        m_l "oh... fuck... yes..."
        "mai's pussy soaks your fingers as ty lee tries to manage you slamming into her."
        a_be "mmmmm.... you like my cunt don't you?"
        a_ub "i love your fingers in me, but..."

        call gallery_foursome_fuck1
        call gallery_foursome_fuck2
        call gallery_foursome_fuck3
        call gallery_foursome_fuck4
        return

        label gallery_foursome_fuck1:
            menu:
                "fuck azula":
                    $ azula_four = True
                    show az4sm az4sm01 with dissolve
                    a_b "i knew you'd come around."
                    a_be "my pussy is irresistable."
                    "you lightly prod her with the tip, enjoying watching her pussy lips swallow the head."
                    a_ab "don't tease-"
                    play sound "audio/gltch.mp3"
                    show az4sm az4sm02 with pflash
                    a_ube "nngh..."
                    a_b "ahh... i love your thick cock..."
                    show az4sm az4sm03 with dissolve
                    a_ube "{i}aahh....."
                    show az4sm az4sm100 with dissolve
                    call pauseInterface
                    a_ube "ngh... fuck... fuck..."
                    "you slam into azula repeatedly as she moans loudly into ty lee's ear."
                    t_ "that's not fair! i want some!"
                    m_ "and least you've had some so far..."
                    a_be "yes... use my cunt, [acallme]."
                    a_b "ngh... it's sooo goood...."
                    "azula's cunt squishes and squeezes you until you can no longer hold out."
                    y "here it comes, whore!"
                    a_ub "give it to me..."
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show az4sm az4sm31 with flash
                    a_ub "yes, baby..."
                    play sound "audio/splurt1.ogg"
                    show az4sm az4sm32 with flash
                    a_b "cover me in it, master..."
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm33 with flash
                    a_ube "mmm... your jizz is so warm..."
                    y "ah... wait..."
                    "your cock remains firmly hard."
                    a_b "did you think that we were going to let you cum only once?"
                    a_b "you have a lot more in there for us."

                "fuck ty lee":
                    $ tylee_four = True
                    show az4sm az4sm09 with dissolve
                    t_ "me!?"
                    t_ "you gonna give me a workout?"
                    "you rub the tip against ty lee, and she pushes into you instictively."
                    play sound "audio/gltch.mp3"
                    show az4sm az4sm10 with pflash
                    t_l "*mmmmm*."
                    t_l "you have such a perfect cock..."
                    show az4sm az4sm11 with dissolve
                    t_l "{i}aahh....."
                    show az4sm az4sm102 with dissolve
                    call pauseInterface
                    t_l "it's... ah... maybe... a... little... ah... big..."
                    m_ "i'm so jealous..."
                    a_ub "can you... finger us again? i'm so wet..."
                    y "shut up! you'll take what i give you!"
                    t_l "yes... pay attention to only me, daddy..."
                    a_ab "that's not fair..."
                    "ty lee's cunt grips you tighter as she maons in time with your thrusts."
                    y "here it comes, whore!"
                    t_l "give me your cum!"
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show az4sm az4sm28 with flash
                    t_l "yes, daddy..."
                    play sound "audio/splurt1.ogg"
                    show az4sm az4sm29 with flash
                    t_l "drench me in it..."
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm30 with flash
                    t_l "oh god my pussy is sore..."
                    y "ah... wait..."
                    "your cock remains firmly hard."
                    a_b "did you think that we were going to let you cum only once?"
                    a_b "you have a lot more in there for us."

                "fuck mai":
                    $ mai_four = True
                    show az4sm az4sm17 with dissolve
                    m_ "....."
                    "you press into mai's soft lips as she moans in anticipation."
                    m_ "yes..."
                    play sound "audio/gltch.mp3"
                    show az4sm az4sm18 with pflash
                    "mai's cunt almost fights you, seemingly too small to fit you."
                    m_l "uunnhh...."
                    m_l "wait, be... be gentle... i'm the only one that hasn't... ah..."
                    "ignoring her hesitation, you push a little harder..."
                    show az4sm az4sm19 with dissolve
                    m_l "{i}aahh..... fuck!!"
                    "you hold there inside her as she grips and flexes and her fingers grip the sheets."
                    m_l "my... ah... you're... ah..."
                    show az4sm az4sm104 with dissolve
                    call pauseInterface
                    m_l "ah... ngh... ungh... ah... ha..."
                    m_l "you're.... you're big..."
                    t_ "you're doing so good, mai!"
                    y "how's your first taste of this cock?"
                    m_l "....hard...."
                    "mai moans louder as she squeezes you desperately..."
                    m_l "i'm cumming!"
                    y "fuck, me too!"
                    m_l "i... empty... it on me..."
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show az4sm az4sm25 with flash
                    m_l "it's warm..."
                    play sound "audio/splurt1.ogg"
                    show az4sm az4sm26 with flash
                    m_l "cover my fat ass... it's yours..."
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm27 with flash
                    m_l "that was so good..."
                    y "ah... wait..."
                    "your cock remains firmly hard."
                    a_b "did you think that we were going to let you cum only once?"
                    a_b "you have a lot more in there for us."
            
            
            return
        label gallery_foursome_fuck2:
            menu:
                "fuck azula" if not azula_four:
                    $ azula_four = True
                    if tylee_four:
                        show az4sm az4sm01_t with dissolve
                    if mai_four:
                        show az4sm az4sm01_m with dissolve
                    a_b "i knew you'd come around."
                    a_be "my pussy is irresistable."
                    "you lightly prod her with the tip, enjoying watching her pussy lips swallow the head."
                    a_ab "don't tease-"
                    if tylee_four:
                        play sound "audio/gltch.mp3"
                        show az4sm az4sm02_t with pflash
                    if mai_four:
                        play sound "audio/gltch.mp3"
                        show az4sm az4sm02_m with pflash

                    a_ube "nngh..."
                    a_b "ahh... i love your thick cock..."
                    if tylee_four:
                        show az4sm az4sm03_t with pflash
                    if mai_four:
                        show az4sm az4sm03_m with dissolve
                    a_ube "{i}aahh....."
                    if tylee_four:
                        show az4sm az4sm100_t with pflash
                    if mai_four:
                        show az4sm az4sm100_m with dissolve
                    call pauseInterface
                    a_ube "ngh... fuck... fuck..."
                    "you slam into azula repeatedly as she moans loudly into ty lee's ear."
                    t_ "i want some more!"
                    a_be "yes... use my cunt, [acallme]."
                    a_b "ngh... it's sooo goood...."
                    "azula's cunt squishes and squeezes you until you can no longer hold out."
                    y "here it comes, whore!"
                    a_ub "give it to me..."
                    y "ngh!"

                    if tylee_four:
                        play sound "audio/splurt2.ogg"
                        show az4sm az4sm31_t with flash
                    if mai_four:
                        play sound "audio/splurt2.ogg"
                        show az4sm az4sm31_m with flash

                    a_ub "yes, baby..."

                    if tylee_four:
                        play sound "audio/splurt1.ogg"
                        show az4sm az4sm32t with flash
                    if mai_four:
                        play sound "audio/splurt1.ogg"
                        show az4sm az4sm32m with flash

                    a_b "cover me in it, master..."

                    if tylee_four:
                        play sound "audio/splurt3.ogg"
                        show az4sm az4sm33t with flash
                    if mai_four:
                        play sound "audio/splurt3.ogg"
                        show az4sm az4sm33m with flash

                    a_ube "mmm... your jizz is so warm..."
                    "your cock still remains firmly hard."
                    y "...how..."
                    a_b "i told you."
                    a_b "you're going to need to cum a lot."

                "fuck ty lee" if not tylee_four:
                    $ tylee_four = True

                    if mai_four:
                        show az4sm az4sm09m with dissolve
                    if azula_four:
                        show az4sm az4sm09a with dissolve

                    t_ "me!?"
                    t_ "you gonna give me a workout?"
                    "you rub the tip against ty lee, and she pushes into you instictively."
                    play sound "audio/gltch.mp3"

                    if mai_four:
                        show az4sm az4sm10m with pflash
                    if azula_four:
                        show az4sm az4sm10a with pflash

                    t_l "*mmmmm*."
                    t_l "you have such a perfect cock..."

                    if mai_four:
                        show az4sm az4sm11m with dissolve
                    if azula_four:
                        show az4sm az4sm11a with dissolve
                    t_l "{i}aahh....."

                    if mai_four:
                        show az4sm az4sm102m with dissolve
                    if azula_four:
                        show az4sm az4sm102a with dissolve
                    call pauseInterface
                    t_l "it's... ah... maybe... a... little... ah... big..."
                    m_ "i'm so jealous..."
                    a_ub "can you... finger us again? i'm so wet..."
                    y "shut up! you'll take what i give you!"
                    t_l "yes... pay attention to only me, daddy..."
                    a_ab "that's not fair..."
                    "ty lee's cunt grips you tighter as she maons in time with your thrusts."
                    y "here it comes, whore!"
                    t_l "give me your cum!"
                    y "ngh!"
                    play sound "audio/splurt2.ogg"

                    if mai_four:
                        show az4sm az4sm28m with flash
                    if azula_four:
                        show az4sm az4sm28a with flash

                    t_l "yes, daddy..."
                    play sound "audio/splurt1.ogg"
                    if mai_four:
                        show az4sm az4sm29m with flash
                    if azula_four:
                        show az4sm az4sm29a with flash
                    t_l "drench me in it..."
                    play sound "audio/splurt3.ogg"
                    if mai_four:
                        show az4sm az4sm30m with flash
                    if azula_four:
                        show az4sm az4sm30a with flash
                    t_l "oh god my pussy is sore..."
                    "your cock still remains firmly hard."
                    y "...how..."
                    a_b "i told you."
                    a_b "you're going to need to cum a lot."

                "fuck mai" if not mai_four:
                    $ mai_four = True
                    if tylee_four:
                        show az4sm az4sm17t with dissolve
                    if azula_four:
                        show az4sm az4sm17a with dissolve
                    m_ "....."
                    "you press into mai's soft lips as she moans in anticipation."
                    m_ "yes..."
                    play sound "audio/gltch.mp3"

                    if tylee_four:
                        show az4sm az4sm18t with pflash
                    if azula_four:
                        show az4sm az4sm18a with pflash
                    "mai's cunt almost fights you, seemingly too small to fit you."
                    m_l "uunnhh...."
                    m_l "wait, be... be gentle... i'm the only one that hasn't... ah..."
                    "ignoring her hesitation, you push a little harder..."
                    if tylee_four:
                        show az4sm az4sm19t with dissolve
                    if azula_four:
                        show az4sm az4sm19a with dissolve
                    m_l "{i}aahh..... fuck!!"
                    "you hold there inside her as she grips and flexes and her fingers grip the sheets."
                    m_l "my... ah... you're... ah..."
                    if tylee_four:
                        show az4sm az4sm104t with dissolve
                    if azula_four:
                        show az4sm az4sm104a with dissolve
                    call pauseInterface
                    m_l "ah... ngh... ungh... ah... ha..."
                    m_l "you're.... you're big..."
                    t_ "you're doing so good, mai!"
                    y "how's your first taste of this cock?"
                    m_l "....hard...."
                    "mai moans louder as she squeezes you desperately..."
                    m_l "i'm cumming!"
                    y "here it comes, whore!"
                    m_l "i... empty... that on me..."
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    if tylee_four:
                        show az4sm az4sm25t with flash
                    if azula_four:
                        show az4sm az4sm25a with flash
                    m_l "it's warm..."
                    play sound "audio/splurt1.ogg"
                    if tylee_four:
                        show az4sm az4sm26t with flash
                    if azula_four:
                        show az4sm az4sm26a with flash
                    m_l "cover my fat ass... it's yours..."
                    play sound "audio/splurt3.ogg"
                    if tylee_four:
                        show az4sm az4sm27t with flash
                    if azula_four:
                        show az4sm az4sm27a with flash

                    m_l "that was so good..."
                    "your cock still remains firmly hard."
                    y "...how..."
                    a_b "i told you."
                    a_b "you're going to need to cum a lot."

            return
        label gallery_foursome_fuck3:
            menu:
                "fuck azula" if not azula_four:
                    $ azula_four = True
                    show az4sm az4sm01b with dissolve
                    a_b "i knew you'd come around."
                    a_be "my pussy is irresistable."
                    "you lightly prod her with the tip, enjoying watching her pussy lips swallow the head."
                    a_ab "don't tease-"
                    play sound "audio/gltch.mp3"
                    show az4sm az4sm02b with pflash

                    a_ube "nngh..."
                    a_b "ahh... i love your thick cock..."
                    show az4sm az4sm03b with dissolve
                    a_ube "{i}aahh....."
                    show az4sm az4sm100b with dissolve
                    call pauseInterface
                    a_ube "ngh... fuck... fuck..."
                    "you slam into azula repeatedly as she moans loudly into ty lee's ear."
                    t_ "i want some more!"
                    a_be "yes... use my cunt, [acallme]."
                    a_b "ngh... it's sooo goood...."
                    "azula's cunt squishes and squeezes you until you can no longer hold out."
                    y "here it comes, whore!"
                    a_ub "give it to me..."
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show az4sm az4sm31b with flash
                    a_ub "yes, baby..."
                    play sound "audio/splurt1.ogg"
                    show az4sm az4sm32b with flash

                    a_b "cover me in it, master..."

                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm33b with flash
                    a_ube "mmm... your jizz is so warm..."
                    "your cock still remains firmly hard."
                    y "is it... gonna stay like this?"
                    a_b "you probably have..."
                    a_b "one left in you."

                "fuck ty lee" if not tylee_four:
                    $ tylee_four = True
                    show az4sm az4sm09b with dissolve

                    t_ "me!?"
                    t_ "you gonna give me a workout?"
                    "you rub the tip against ty lee, and she pushes into you instictively."
                    play sound "audio/gltch.mp3"
                    show az4sm az4sm10b with pflash

                    t_l "*mmmmm*."
                    t_l "you have such a perfect cock..."

                    show az4sm az4sm11b with dissolve
                    t_l "{i}aahh....."
                    show az4sm az4sm102b with dissolve
                    call pauseInterface
                    t_l "it's... ah... maybe... a... little... ah... big..."
                    m_ "i'm so jealous..."
                    a_ub "can you... finger us again? i'm so wet..."
                    y "shut up! you'll take what i give you!"
                    t_l "yes... pay attention to only me, daddy..."
                    a_ab "that's not fair..."
                    "ty lee's cunt grips you tighter as she maons in time with your thrusts."
                    y "here it comes, whore!"
                    t_l "give me your cum!"
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show az4sm az4sm28b with flash

                    t_l "yes, daddy..."
                    play sound "audio/splurt1.ogg"
                    show az4sm az4sm29b with flash
                    t_l "drench me in it..."
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm30b with flash
                    t_l "oh god my pussy is sore..."
                    "your cock still remains firmly hard."
                    y "is it... gonna stay like this?"
                    a_b "you probably have..."
                    a_b "one left in you."

                "fuck mai" if not mai_four:
                    $ mai_four = True
                    show az4sm az4sm17b with dissolve
                    m_ "....."
                    "you press into mai's soft lips as she moans in anticipation."
                    m_ "yes..."
                    play sound "audio/gltch.mp3"
                    show az4sm az4sm18b with pflash
                    "mai's cunt almost fights you, seemingly too small to fit you."
                    m_l "uunnhh...."
                    m_l "wait, be... be gentle... i'm the only one that hasn't... ah..."
                    "ignoring her hesitation, you push a little harder..."
                    show az4sm az4sm19b with dissolve
                    m_l "{i}aahh..... fuck!!"
                    "you hold there inside her as she grips and flexes and her fingers grip the sheets."
                    m_l "my... ah... you're... ah..."
                    show az4sm az4sm104b with dissolve
                    call pauseInterface
                    m_l "ah... ngh... ungh... ah... ha..."
                    m_l "you're.... you're big..."
                    t_ "you're doing so good, mai!"
                    y "how's your first taste of this cock?"
                    m_l "....hard...."
                    "mai moans louder as she squeezes you desperately..."
                    m_l "i'm cumming!"
                    y "here it comes, whore!"
                    m_l "i... empty... that on me..."
                    y "ngh!"
                    play sound "audio/splurt2.ogg"
                    show az4sm az4sm25b with flash
                    m_l "it's warm..."
                    play sound "audio/splurt1.ogg"
                    show az4sm az4sm26b with flash
                    m_l "cover my fat ass... it's yours..."
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm27b with flash

                    m_l "that was so good..."
                    "your cock still remains firmly hard."
                    y "is it... gonna stay like this?"
                    a_b "you probably have..."
                    a_b "one left in you."

            return
        label gallery_foursome_fuck4:
            a_b "so..."
            a_ub "who do you want to finish in?"
            y "finish in?"
            m_ "well, you should probably cum in one of us."
            a_b "so, who gets the honor?"
            menu:
                "azula":
                    show az4sm az4sm01all with dissolve
                    a_be "i knew you couldn't stay away."
                    show az4sm az4sm101b with dissolve
                    call pauseInterface
                    a_ub "yes, baby..."
                    a_ub "give it to me..."
                    a_ube "give me everything..."
                    a_ube "ah... ah... fuck..."
                    y "what are you?"
                    a_b "your personal fucktoy, [acallme]."
                    a_be "for you to unload in and drench at your pleasure."
                    y "here it comes, bitch!"
                    a_ube "yes!"
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm05d with flash
                    call pauseInterface
                    a_be "mmmmm...."
                    a_b "thank you..."
                    "you feel your body returning to normal."
                    y "fuck that was great..."

                "ty lee":
                    show az4sm az4sm09all with dissolve
                    t_ "i knew you couldn't stay away."
                    show az4sm az4sm103b with dissolve
                    call pauseInterface
                    t_l "yes, daddy..."
                    t_l "give it to me..."
                    t_l "give me everything..."
                    t_l "ah... ah... fuck..."
                    y "what are you?"
                    t_l "your sugar baby..."
                    t_l "for you to unload in and drench at your pleasure."
                    y "here it comes, slut!"
                    t_l "yes!"
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm15d with flash
                    call pauseInterface
                    t_l "mmmmm...."
                    t_l "thank you..."
                    "you feel your body returning to normal."
                    y "fuck that was great..."

                "mai":
                    show az4sm az4sm17all with dissolve
                    m_ "i knew you couldn't stay away."
                    show az4sm az4sm105b with dissolve
                    call pauseInterface
                    m_l "yes..."
                    m_l "give it to me..."
                    m_l "give me everything..."
                    m_l "ah... ah... fuck..."
                    y "what are you?"
                    m_l "whatever you want me to be..."
                    m_l "unload in and drench me at your pleasure!"
                    y "here it comes, slut!"
                    m_l "yes!"
                    play sound "audio/splurt3.ogg"
                    show az4sm az4sm23d with flash
                    call pauseInterface
                    m_l "mmmmm...."
                    m_l "thank you..."
                    "you feel your body returning to normal."
                    y "fuck that was great..."

            return
###### [Ending] Tower Fuck
label gallery_fpalace_day12:
    call gallery_dCharacter_2Slave

    scene bg_a watchtower_day
    show afnl
    with dissolve
    a "[acallme]!"
    y "what are you doing up here? why are you naked?"
    a "i've been waiting for you for hours."
    y "here? why?"
    
    show afnub with dissolve
    a "didn't... mai tell you?"
    hide afnl
    y "no, i never saw her. i just ended up here by chance."
    a "oh..."
    show afnbe with dissolve
    a "well, there's a bit of an event today..."
    hide afnub
    y "yeah, i kind of noticed."
    a "i thought it might be fun if..."
    a "well..."
    show afnl with dissolve
    a "you fucked me in the window?"
    hide afnbe
    y "what?"
    show afnub with dissolve
    a "i want... i want the people to know. that i belong to you."
    hide afnl
    show afnl with dissolve
    a "that you belong to me... as my master."
    hide afnub
    y "i'm not sure how i feel about that."
    show afnub with dissolve
    a "it would make me so happy, [acallme]!"
    a "please!"
    hide afnl
    y "that's not for you to decide."
    show afnube with dissolve
    a "i'm sorry, [acallme]. you're right."
    hide afnub
    a "....."
    y "....."
    y "you're such a fucking whore."
    show afnl with dissolve
    a "yes, [acallme]."
    hide afnube
    y "you really want to fuck in front of the city?"
    a "...yes..."
    y "alright. what do you hate?"
    show afnub with dissolve
    a "um... the earth kingdom. and waterbenders."
    hide afnl
    a "and being insulted. by anyone other than you, of course [acallme]."
    y "....alright, what else?"
    a "um... i really hate doing jumping jacks."
    y "perfect. you know what you're going to do now, slut?"
    show afnube with dissolve
    a "jumping jacks."
    hide afnub
    y "correct."
    a "....anything for you, master."
    hide afnube with dissolve
    show azet azet100 with dissolve
    call pauseInterface
    y "that's it whore, bounce those big fucking titties."
    a "yes, [acallme]."
    y "do you hate doing this?"
    a "...yes, [acallme]..."
    a "but i'll do anything for you."
    y "tell me about yourself."
    a "i'm a stupid whore with a stupid, slut face and a body made for fucking."
    a "i'm desperate to have cum anywhere inside me."
    a "i'm nothing. i'm an embarrasment. i'm useless."
    a "i love your cock."
    call pauseInterface
    y "that's a good girl. now get in the window."
    a "really?!"
    a "thank you!"

    scene black with dissolve
    show azet azet13 with dissolve

    pause 1
    show azet azet14 with dissolve
    a "yes...."
    a "i am your princess..."
    a "give me a moment, [acallme]."
    y "sure."
    show azet azet11 with dissolve
    "as azula squats in the window, a crowd slowly gathers..."
    show azet azet12 with dissolve
    "crowd" "is that..."
    "crowd" "that's azula! a...azula's naked in the window!"
    "crowd" "holy shit! what is she doing?"
    show azet azet14 with dissolve
    a "yes... that's it..."
    a "see me..."
    show azet azet15 with dissolve
    t "oh... my..."
    m "figures."
    r "well... i can certainly appreciate that."
    p "she can really get away with anything..."
    t "well yeah, with a pussy like that..."
    t "wait... is she..."
    m "yup."
    t "oh my gosh."
    show azet_bg
    show azet_door:
        ypos 0
        linear 4 ypos 720
    show azet_plaster:
        ypos -720
        linear 4 ypos 0
        repeat
    pause 3
    hide azet_door
    m "she's at it now..."
    t "do you... think she knows... we can see her....?"

    show azet_bg_azwindow:
        ypos -920
        linear 4 ypos 0

    m "definitely."
    pause 3
    a "yes! yes!"
    show azet azet101
    hide azet_plaster
    hide azet_bg_azwindow
    hide azet_bg
    "crowd" "what a slut!"
    a "fuck me, [acallme]!"
    "crowd" "what did she call him?"
    a "i love cock! i love your cock!"
    a "i'm so happy!"
    a "*mmmmm* *ahhhh*"
    a "watch me fuck, everybody!"
    a "watch your princess fuck!"
    a "it's so good!!"
    call pauseInterface
    show azet azet15 with dissolve
    t "she knows what's she's doing at least..."
    oz "where is everyone?!"
    oz "who took my crowd?"
    a "*ungh* *mmm*"
    oz "and where is azula?"
    oz "excuse me. excuse me!"
    a "*ah* *mmmgh*"
    oz "move, people! i am your ruler!"
    oz "what is going on up front? what is that noise?"
    show azet azet16 with dissolve
    oz "what-"
    show azet azet17 with dissolve
    with vshake
    oz "hgnh..."
    m "don't worry sir, she's doing a good job."
    "crowd" "look at that royal slut! maybe we can take turns with her later!"
    g "i came on her ass once."
    show azet azet18 with dissolve
    oz "......"
    show azet azet101 with dissolve
    a "*mmmm* ah.... ah..."
    a "you want it harder, [acallme]?"
    a "you want azula to make you cum so good?"
    show azet azet102 with dissolve
    call pauseInterface
    a "yes, baby! own my stupid cunt with your perfect cock!"
    "crowd" "she's disgusting!"
    "crowd" "she's amazing!"
    "crowd" "i got next!"
    a "is this what you all wanted? to see my bare tits?"
    a "to see my pussy slammed?"
    a "i don't have to worry about ruling anymore!"
    a "I can be a happy cocksleeve!"
    show azet azet18 with dissolve
    oz "azula!!!"
    oz "get down this instant!"
    show azet azet102 with dissolve
    a "father's here! hi, father!"
    oz "stop this!"
    a "no! i'm a slut, father! and i don't care who knows!"
    oz "i'd say everyone knows!"
    a "you're just *ah!* jealous because you can't fuck me!"
    a "*mmmm!*"
    a "i bet i fuck better than mother did!"
    oz "get down here right now!"
    a "you wouldn't have made mother leave if she fucked like this, would she?"
    show azet azet101 with dissolve
    a "*ah!* *mmmm!*"
    a "she didn't love me! you don't love me! i don't need you! i have [acallme]!"
    a "i'm full, daddy! i'm full of cock! let me be full of cock!"
    show azet azet18 with dissolve
    m "she's gone insane...."
    t "no, she's perfect..."
    show azet azet101 with dissolve
    call pauseInterface
    a "how about this, daddy?"
    show azet azet102 with dissolve
    a "how about i slam on some cock for you? for this whole nation?"
    a "we lost it, by the way! we lost our nation!"
    oz "what..."
    y "it's true, you're fucked."
    y "well, your daughter's fucked. as you can see. you're just out of luck."
    show azet azet101 with dissolve
    oz "azula! this is crazy! stop it!"
    a "how about this, daddy?"
    show azet azet103 with dissolve
    call pauseInterface
    a "i'm gonna make him cum!"
    a "i want his cum! i want a hot, sticky cunt, daddy!"
    a "[acallme], cum for me!"
    a "you wanna watch, daddy?"
    a "you're gonna watch!"
    a "you're gonna watch your daughter get filled up with cum?"
    a "cum for me, [acallme]! cum for me!"
    y "you stupid fucking whore!"
    play sound "audio/splurt3.ogg"
    show azet azet19 with vshake
    a "yes!"
    play sound "audio/splurt2.ogg"
    show azet azet20 with vshake
    a "fill me up, [acallme]!"
    play sound "audio/splurt3.ogg"
    show azet azet21 with vshake
    a "it's sooo goood!!!"
    play sound "audio/gltch.mp3"
    show azet azet22 with dissolve
    a "look at all this cum, father!"
    call pauseInterface
    "crowd" "*cheers*"
    a "we did it!"
    a "he came! he came in me!"
    "crowd" "good job, azula!"
    a "everybody, look at my cunt! my cummy cunt!"
    y "we should get back inside."
    a "yes, [acallme]."
    a "thank you all!"
    "crowd" "thank you!"
    show azet azet13 with dissolve
    a "bye!"
    show azet azet18 with dissolve
    oz "where did she-"
    r "ozai, you are under arrest."
    show azet azet16 with dissolve
    oz "don't be ridiculous girl."
    r "oh, i'm not."
    r "it gives me great pleasure to tell you that you are no longer in control of your nation."
    r "guards!"
    g "you're under arrest, ozai."
    show azet azet17 with dissolve
    oz "i lost my firebending, and my daughter, now my nation...."
    show azet azet16 with dissolve
    oz "very well."
    r "let's go."
    scene black with dissolve
    scene bg_a watchtower_day
    show afnl
    with dissolve
    a "that was amazing."
    y "it was... a little crazy."
    show pgfull with dissolve
    s "avatar."
    y "oh. hey."
    s "we're leaving now."
    hide pgfull with dissolve
    show afnub with dissolve
    a "what... what was that?"
    hide afnl
    y "yeah... i've got to go."
    show afnubc with dissolve
    a "no... no, you can't...."
    hide afnub
    a "where are you going?"
    y "fuck if i know."
    a "when are you coming back?"
    y "don't know that either."
    "you begin to feel yourself lifted up, even as your body stays still."
    show afnabc with dissolve
    a "no! you can't go!"
    hide afnubc
    y "hey, chin up! you'll be sucking my cock again before you know it."
    y "so you better not turn into a fat slob while i'm gone. understood?"
    show afnl with dissolve
    "Azula wipes the tears from her face and tries to smile."
    a "I'll keep everything neat and tight until you return!"
    y "That's my girl! Okay I'm off!"
    hide afnl with dissolve
    "you lift up and into the sky."
    hide afnabce with dissolve
    scene black with dissolve
    show pgfull with dissolve
    s "you have learned much."
    y "yeah, yeah. where to now?"
    s "you will see."
    hide pgfull with dissolve
    
    return
#--
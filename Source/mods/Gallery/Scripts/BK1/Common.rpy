###### Declare Characters
label gallery_dCharacters_1:
    $ sk = Character('Nami', color = "#000000", image = "shopkeeper", window_right_padding=250, show_two_window=True, who_xpos=36)
    $ k = Character('Katara', color="#000000", image = "katara", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ac = Character('Alley Cat', color="#000000", window_right_padding=250, show_two_window=True, who_xpos=36)
    $ st = Character('Una', color="#000000", image = "Una", window_right_padding=250, show_two_window=True, who_xpos=36)
    $ kya = Character('kya', color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)


    $ ya = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), ConditionSwitch(
            "avatar == 'jack'", "pumpkin/p_fr_sidebox_angry.png",
            "avatar == 'player'", "p_fr_sidebox_angry.png",),
        (0, 0), ConditionSwitch(
            "avatar == 'player'", "p_fr_sidebox_mask.png",
            "avatar == 'jack'", "transparent.png",),),
        window_left_padding=220, show_two_window=True, who_xpos=36)


    $ y = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), ConditionSwitch(
            "avatar == 'jack'", "pumpkin/p_fr_sidebox_neutral.png",
            "avatar == 'player'", "p_fr_sidebox_neutral.png",),
        (0, 0), ConditionSwitch(
            "avatar == 'player'", "p_fr_sidebox_mask.png",
            "avatar == 'jack'", "transparent.png",),), 
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ yc = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), ConditionSwitch(
            "avatar == 'jack'", "pumpkin/p_fr_sidebox_confused.png",
            "avatar == 'player'", "p_fr_sidebox_confused.png",),
        (0, 0), ConditionSwitch(
            "avatar == 'player'", "p_fr_sidebox_mask.png",
            "avatar == 'jack'", "transparent.png",),), 
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ ym = Character("[povname]", color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (0, 0), ConditionSwitch(
            "avatar == 'jack'", "pumpkin/p_fr_sidebox.png",
            "avatar == 'player'", "p_fr_sidebox.png",),
        (0, 0), ConditionSwitch(
            "avatar == 'player'", "p_fr_sidebox_mask.png",
            "avatar == 'jack'", "transparent.png",),), 
        window_left_padding=220, show_two_window=True, who_xpos=36)

    $ avatar = "player"
    
    return
#--

###### [Katara] Breasts Size
label gallery_katara_breasts:
    call gallery_dCharacters_1

    hide knbe
    show knb at Position (xpos = 0.9, xanchor=0.5, ypos=.6, yanchor=0.5)
    with dissolve

    while True:
        menu: 
            "Tiny" if "Tiny Breasts" in mods:
                $ boobs = "tiny"
            "Small":
                $ boobs = "small"
            "Medium":
                $ boobs = "medium"
            "Big":
                $ boobs = "big"
            "Continue":
                return

        #"Katara now has [boobs] breasts!"
        #"(She'll need to be naked for you to tell, obviously.)"
        #call pauseInterface

###### [Nami] Blowjob
label gallery_shop_bj_scene:
    call gallery_dCharacters_1

    #scene bg_n_insideshop_01
    scene n2bg with fade
    show nbj1 at right
    with dissolve
    sk "oh my god..."
    sk "i can't believe I'm going to get to suck the avatar's cock!"
    y "heh."
    show nbj2 at right
    with dissolve
    hide nbj1
    sk "*sniff*"
    sk "it smells so good..."
    show nbjt at right
    with dissolve
    hide nbj2
    sk "i'm sorry, i just... can't believe it!"
    sk "..."
    y "um..."
    sk "..."
    y "i'm still here, you know."
    show nbj5 at right
    with dissolve
    hide nbjt
    sk "sorry!"
    show nbj6 at right
    with dissolve
    hide nbj5

    sk "mmm..."
    show nbj7 at right
    with dissolve
    hide nbj6
    sk "*mphh!*"
    show nbj5 with dissolve
    hide nbj7
    show nbjt2 at right
    with dissolve
    hide nbj5
    sk "what a tasty cock!"
    show nbj6 at right
    with dissolve
    sk "mmm..."
    hide nbjt2
    y "okay, that's it."
    show nbj8 at right
    with dissolve
    hide nbj7
    sk "hmm?"
    sk "wh-"
    show nbj9 at right
    with dissolve
    sk "!!!"
    hide nbj8
    sk "*mmghm!*"
    show nbj8 at right
    with dissolve
    hide nbj9
    sk "..."
    show nbj5 at right
    with dissolve
    hide nbj8
    show nbjt2 at right
    with dissolve
    hide nbj5
    sk "aw... why'd you stop..."
    y "oh, you little bitch."
    show nbj8 at right
    with dissolve
    hide nbjt2
    sk "mmm..."
    show nbj9 at right
    with dissolve
    sk "*mmghn!*"
    hide nbj8
    show nbj8 at right
    with dissolve
    hide nbj9
    show nbjd at right
    with dissolve
    hide nbj8
    sk "*mmm!*"
    sk "*slurp-slurp-slurp*"
    y "you're nothing but a cocksucking whore, aren't you?"
    sk "*mngh!*"
    y "you live for dick don't you?"
    sk "ngh!"
    y "say it."
    sk "mm im a ik!"
    show nbj2 at right
    with dissolve
    hide nbjd
    sk "*gasp-gasp*"
    sk "you poor thing, you must really need a fuckable mouth."
    show nbjt at right with dissolve
    sk "let me take care of you."
    hide nbj2
    show nbjs at right with dissolve
    sk "mmmm..."
    sk "*slurp-slurp-slurp*"
    sk "*gahhkg*"
    hide nbjs
    show nbjt at right with dissolve
    sk "you like that?"
    sk "you like when i choke on your thick cock?"
    show nbjs at right with dissolve
    sk "*slurp-slurp*"
    hide nbjt
    show nbjt at right with dissolve
    sk "your cock tastes so good."
    hide nbjs
    show nbj7 at right with dissolve
    sk "*gagghh*"
    show nbj2 at right with dissolve
    sk "*cough-cough*"
    hide nbj7
    show nbj3 at right with dissolve
    sk "I'm choking on your fat cock."
    hide nbj2
    show nbjs at right with dissolve
    sk "*slurp-slurp-ggahgh*"
    hide nbj3
    sk "Mmm, ah..."
    hide nbjs
    show nbjt at right with dissolve
    sk "You like fucking my little throat?"
    y "Fuck yes..."
    sk "Mmm yeah you do."
    show nbjs at right with dissolve
    "*slurp-slurp*"
    hide nbjs
    show nbjt at right with dissolve
    sk "You like how wet and warm my mouth is?"
    sk "How about seeing these pretty lips around your cock?"
    show nbjs at right with dissolve
    hide nbjt
    sk "*slurp-slurp*"
    sk "*mmm-mmph-gnh*"
    show nbjt at right with dissolve
    sk "Come on, give me that load."
    hide nbjs
    sk "Mmmm... I can feel your balls tightening..."
    sk "Are you gonna give me a big load?"
    sk "Fill up this little slut's mouth with your cum?"
    sk "Gonna make me choke on all your cum?"
    show nbjs at right with dissolve
    y "(Here it comes...)"
    hide nbjt

    menu:
        y "where should i cum?"
        "throat":
            call gallery_shop_throat
        "face":
            call gallery_shop_face

    return
    
    label gallery_shop_throat:
        show nbj8 at right
        with dissolve
        hide nbjs
        y "{size=30}fuck!{/size=30}"
        hide nbj8
        show nbj9 at right
        with dissolve
        with flash
        sk "!!!!!"
        hide nbj8
        sk "*gulp-gulp-gulp*"
        show nbjd2 at right
        with dissolve
        pause 0.5
        with flash
        show n_xxx_stance02_cheek at right
        sk "..."
        sk "*gulp-gulp*"
        with flash
        sk "*gulp-gulp-gulp-gulp*"
        with flash
        hide nbjd2
        hide n_xxx_stance02_cheek
        show nbj8 at right
        with dissolve
        pause 0.5
        with flash
        show n_xxx_stance01_sperm_1 at right
        with dissolve
        hide nbj9
        sk "............"
        with flash
        show n_xxx_stance01_sperm_2 at right
        with dissolve
        hide n_xxx_stance01_sperm_1
        with flash
        sk "*gulp-gulp-gulp*"
        show n_xxx_stance01_sperm_3 at right
        with flash
        hide n_xxx_stance01_sperm_2
        show n_xxx_stance01_cheek at right
        with dissolve
        with flash
        sk "..."
        hide n_xxx_stance01_cheek with dissolve
        play sound "audio/gulp2.mp3"
        sk "{size=+5}*gulp!*"
        hide nbjd2
        hide nbj8
        hide nbj5
        hide nbj6
        show nbj19 at right
        hide n_xxx_stance01_sperm_3
        with flash
        sk "..."
        sk "*gasp-gasp*"
        sk "mmm..."
        sk "what a load..."
        show nbj16 at right
        with dissolve
        hide nbj19
        sk "that was great!"
        show nbj17 at right
        with dissolve
        sk "come back again, 'kay?"
        sk "..."
        hide nbj3
        hide nbj6
        hide nbj9
        hide nbj5
        hide nbj4
        hide nbj16
        hide nbj17
        show nbj18 at right
        with dissolve
        y "hey! easy!"
        show nbj17 at right
        with dissolve
        hide nbj18
        sk "sorry!"
        hide nbj17
        with Fade(0.7, 0.0, 0.7)
        hide n2bg
        return


    label gallery_shop_face:
        show nbj13 at right
        with dissolve
        y "{size=30}take it, whore!{/size=30}"
        hide nbjs
        show nbj20
        hide nbj13
        show n_xxx_stance01_onface_1 at right
        with flash
        sk "!!!!!"
        with flash
        sk "yes baby!"
        show n_xxx_stance01_onface_2 at right
        hide n_xxx_stance01_onface_1
        with flash
        sk "cover my pretty face in your hot cum!"
        with flash
        sk "aahhh..."
        hide nbj13 with dissolve
        show n_xxx_stance01_onface_3 at right
        hide n_xxx_stance01_onface_2
        with flash
        with flash
        sk "............"
        sk "..."
        show nbj21 at right
        with Dissolve(0.7)
        sk "*gasp-gasp*"
        sk "oh my god..."
        sk "what a load..."
        sk "that was great!"
        show nbj22 at right
        with dissolve
        hide nbj21
        sk "come back again, 'kay?"
        hide n_xxx_stance01_onface_3
        hide n_xxx_stance01_onface_2
        hide n_xxx_stance01_onface_1
        hide nbj22
        with Fade(0.7, 0.0, 0.7)
        hide n2bg
        return
###### Alley Fuck
label gallery_yue_bj:
    call gallery_dCharacters_1
    
    show cat1 with dissolve
    call pauseInterface
    
    show cat
    with dissolve
    call pauseInterface
    y "..."
    y "how often are they out here?"
    y "..."
    y "i wonder how close-"
    ac "{size=+5}*!!!!mmmmm!!!!*"
    y "well that answers that. better figure out how to get home."
    call pauseInterface
    
    return
###### [Magazine] PornLove 23
label gallery_magazine_1:
    while True:
        menu:
            y "which should I jerk off to?"
            "Cover":
                scene sokka_dirtymagazine_00 with dissolve

            "(page 23) batgirl getting creampied!!":
                scene sokka_dirtymagazine_01 with dissolve

            "(page 39) ariel introduced to a new world...":
                scene sokka_dirtymagazine_02 with dissolve

            "(page 55) spidergirl gets sticky!":
                scene sokka_dirtymagazine_04 with dissolve

            "(page 55) spidergirl gets sticky (Naked)!":
                scene sokka_dirtymagazine_03 with dissolve

            "exit":
                return
            
        call pauseInterface

    return
###### Lesbian Orgy
label gallery_knock:
    call gallery_dCharacters_1
    
    show les with fade
    play music "audio/Unwritten Return.mp3"
    call pauseInterface
    show uml1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
    with dissolve
    st "come by for another look?"
    y "hell yes."
    "you take a final good look."
    hide uml1 with dissolve
    call pauseInterface

    st "goodbye for now, avatar..."
    return
###### [Una] Anal
label gallery_una_sex:
    call gallery_dCharacters_1
    
    hide uml1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
    with dissolve
    scene bg_ec_sittingdown with fade
    show ua2
    with dissolve
    st "come fuck me, avatar!"
    ym "oh shit, seriously?"
    show ua3
    with dissolve
    hide ua2
    st "yes!"

    st "it's been so long since i got a good fucking."
    show ua31
    with dissolve
    hide ua3
    st "that's right..."
    show ua32
    with dissolve
    hide ua31
    st "wait, that's not-"
    show ua33
    with dissolve
    hide ua32
    st "{i}ohhh..."
    ya "fuck, your ass is tight!"
    show ua34
    with dissolve
    hide ua33
    st "nghh..."
    show ua35
    with dissolve
    hide ua34
    st "it's been so long..."
    show ua3_
    with dissolve
    hide ua35
    st "yes, baby, yes!"
    st "ohhh yes, fuck me, fuck me!"
    show ua38
    with dissolve
    hide ua3_
    st "don't tease me!"
    st "pound my fucking asshole!"
    show ua4_
    with dissolve
    hide ua38
    st "ungh..."
    show ua4_1
    with dissolve
    hide ua4_
    st "oh fuck..."
    st "...."
    show ua34
    with dissolve
    hide ua4_1
    ym "i love being buried in your ass..."
    st "mmm... me too, baby..."
    ym "ready?"
    show ua39
    with dissolve
    hide ua34
    st "...ready?"
    hide ua39
    show ua36
    with dissolve
    st "for wh-"
    hide ua36
    show ua4_2 with ushake
    hide ua36
    st "fuck!"
    show ua4_3 with ushake
    hide ua4_2
    st "ungh, my poor little asshole!"
    ym "I'm gonna fuck those glasses right off your whore face!"
    st "*ung!-umph!-uh!*"
    show ua4_4
    with dissolve
    hide ua4_3
    st "oh!"
    ym "i fucking told you."
    show ua48 with dissolve
    hide ua4_4
    st "what... what are you doing?"
    ym "i want to get a good look."
    show ua49 with dissolve
    hide ua48
    ym "take off your skirt."
    show ua48 with dissolve
    hide ua49
    st "but i have class..."
    ya "i don't care."
    show ua49 with dissolve
    hide ua48
    st "mmm... yes, sir."
    show ua50 with fade
    hide ua49
    show ua51 with dissolve
    hide ua50
    st "how's this?"
    show ua52 with dissolve
    hide ua51
    ym "oh hell yeah."
    show ua53 with dissolve
    hide ua52
    st "oh fuck.."
    show ua5_ with dissolve
    hide ua53
    st "ungh..."
    st "i should be back by now..."
    st "uhh..."
    show ua5_1 with dissolve
    hide ua5_
    st "i need you to cum, cum for me!"
    st "come on, baby, cum for me!"
    show ua5_2 with dissolve
    hide ua5_1
    st "fill up this tight little butt!"
    
    menu:
        y "where should i finish?"
        "inside":
            call gallery_st_inside
        "outside":
            call gallery_st_outside

    return
    label gallery_st_inside:
        y "fuck!"
        show ua57 with dissolve
        show u_xxx_sperminside_01 at right
        with flash
        st "!!!"
        hide ua5_2
        show ua66 with dissolve
        hide ua66
        hide ua57
        show ua67 with ushake
        with flash
        st "!!!"
        show u_xxx_sperminside_02 at right
        with flash
        st "ahh..."
        show ua68 with dissolve
        hide ua68
        hide ua67
        show ua69 with ushake
        show u_xxx_sperminside_03 at right
        with flash
        st "yes baby, fill me up..."
        show ua73 with dissolve
        hide ua69
        show ua70 with dissolve
        hide ua68
        hide ua73
        st "oh my gosh..."
        show ua71 with dissolve
        hide ua70
        hide u_xxx_sperminside_03
        hide u_xxx_sperminside_02
        hide u_xxx_sperminside_01
        st "there's so much!"
        show ua72 with fade
        hide ua71

        st "i gotta hurry back to class."
        hide ua72 with fade
        show um1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
        with dissolve
        y "but you're full of..."
        hide um1
        show uml2 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
        with dissolve
        st "i know, isn't it great?"
        st "teaching class with an ass full of jizz..."
        st "come back any time! Stop by tonight, maybe!"
        hide uml2
        show uml1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
        with dissolve
        st "bye, avatar!"
        hide uml1 with dissolve
        hide bg_ec_sittingdown

        return
    label gallery_st_outside:
        y "fuck!"
        show ua60 with dissolve
        show u_xxx_spermoutside_01 at right
        with flash
        st "!!!"
        show u_xxx_spermoutside_02 at right
        with flash
        st "!!!"
        show u_xxx_spermoutside_03 at right
        with flash
        show ua74 with dissolve
        hide ua60
        st "yes, baby! fucking cover me!"
        show ua75 with dissolve
        hide ua74
        hide u_xxx_spermoutside_01
        hide u_xxx_spermoutside_02
        hide u_xxx_spermoutside_03
        st "there's so much!"

        show ua76 with fade
        hide ua75

        st "i gotta hurry back to class."
        show ua77 with dissolve
        with ushake
        hide ua76
        st "oh!"
        show ua78 with dissolve
        hide ua77
        st "...naughty."
        hide ua57
        hide ua5_2
        hide ua78 with fade
        show um1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
        with dissolve
        y "um... you've got stains on your clothes."
        hide um1
        show uml2 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
        with dissolve
        st "i know, isn't it great? hopefully no one'll know what it is."
        st "come back any time! Stop by tonight, maybe!"
        hide uml2
        show uml1 at Position (xpos = 0.88, xanchor=0.5, ypos=.42, yanchor=0.5)
        with dissolve
        st "bye, avatar!"
        hide uml1 with dissolve
        hide bg_ec_sittingdown

        return
###### [Kya] Blowjob
label gallery_kya_blowjob:
    call gallery_dCharacters_1
    
    show kaky kaky52 with Dissolve(1.0)
    call pauseInterface
    kya "hello, aang."
    show kaky kaky50 with dissolve
    kya "did you want something?"
    kya "maybe to pump jizz down my throat?"
    show kaky kaky51 with dissolve
    kya "i hope you didn't call me for something else..."
    y "no, it's pretty much that."
    kya "wonderful!"
    kya "let's get to it, i've been thinking about this cock..."

    show kaky kaky01 with Dissolve(1.0)
    call pauseInterface
    kya "alright, sweetie."
    kya "let's get a good look at you."
    show kaky kaky02 with dissolve
    kya "mmm.... i'm so jealous of my daughter."
    kya "getting to enjoy... this."
    kya "now, let me thank you for helping my katara."
    show kaky kaky03 with dissolve

    call pauseInterface
    kya "....let's take care of {i}you{/i}."
    show kaky kaky04 with dissolve
    play sound "audio/kiss.mp3"
    with pflash
    "{size=+5}*smooch!*"
    call pauseInterface
    kya "mmmmm......"
    "kya breathes in deeply, taking in the heady smell of your cock."
    play sound "audio/lick_b.mp3"
    "kya licks the underside of your cock, focusing on just below the head."
    play sound "audio/lick_b.mp3"
    kya "you smell.... so strong.... i never thought i'd have this again...."
    kya "mmmm... is that katara's scent...?"
    play sound "audio/lick_b.mp3"
    "she licks you again."
    kya "i can smell her on your cock, avatar..."
    show kaky kaky05 with dissolve
    kya "*mmmm....*"
    kya "and taste her..."
    call pauseInterface
    kya "you're so thick...."
    show kaky kaky06 with dissolve
    kya "*sluuurp...*"
    call pauseInterface
    show kaky kaky05 with dissolve
    kya "ready?"
    y "y-"
    show kaky kaky100
    call pauseInterface
    kya "*slurp* *gltch* *gulp*"
    y "fuuuck..."
    show kaky kaky100_2
    call pauseInterface
    kya "mmm... does that feel nice?"
    kya "...thank...you..."
    kya "...for helping my katara..."
    show kaky kaky100_1
    call pauseInterface
    y "fuck..."
    y "i don't even remember your name..."
    kya "it's k-"
    y "i'm gonna call you \"katara's mom\"."
    kya "...."
    y "suck my cock, katara's mom!"
    kya "......"
    show kaky kaky101
    call pauseInterface
    "kya speeds up, taking you deeper and faster."
    "you {i}feel{/i} her moaning into your cock."
    kya "*mmmmm....*"

    show kaky kaky05 with dissolve
    kya "do you get how much i love my daughter?"
    y "i'm starting to."
    kya "i'm doing this for you...."
    kya "but i'm doing this for me, too."

    show kaky kaky102
    call pauseInterface
    kya "i love it."
    kya "my sweet little katara has no idea how good she has it..."

    show kaky kaky102_2
    call pauseInterface
    kya "*slurp* *gulp* *sluurp*"
    kya "your cock is in my throat, dear."
    kya "that seems rude."

    show kaky kaky102_1
    call pauseInterface
    kya "mmmm.... you're eager...."
    kya "you must be enjoying this..."


    show kaky kaky103
    call pauseInterface
    kya "but not nearly as much as i am...."
    kya "i never thought i'd get to suck a cock again...."
    show kaky kaky103_1
    call pauseInterface

    y "oh, fuck!"
    kya "mmm! mmm! yes!"

    show kaky kaky101_1
    call pauseInterface
    "kya slurps and gulps on you with inhuman intensity... you feel her suctioning the sperm right out of you..."
    kya "cum for me, aang!"

    menu:
        "nut on kya's face":
            show kaky kaky03 with dissolve
            kya "yes!"
            play sound "audio/splurt2.ogg"
            show kaky_spermonface_1
            with flash
            y "ngh!"
            play sound "audio/splurt2.ogg"
            show kaky_spermonface_2
            hide kaky_spermonface_1
            with flash
            kya "yes.... get it all out..."
            y "fuck...."
            kya "hmmm..."
            kya "that's nice, dear."
            kya "but i think you’ve got one more in you."
            "you feel an unearthly presence in your sack..."
            y "what the fuck....."
            "kya's spirit reaches into your depths and pulls out one, huge, final load...."
            play sound "audio/splurt3.ogg"
            show kaky_spermonface_3
            hide kaky_spermonface_2
            with flash
            ya "hnghn....!"
            ya "...what the shit!?"
            kya "mmm... there you go. you like cumming on my face, don’t you?"
            kya "you can never tell katara that you came on her mother's face."
            hide kaky_spermonface_3
            show kaky kaky52
            show kaky_idle_sperm
            with dissolve
            kya "i must leave for now..."
            hide kaky_idle_sperm
            show kaky_idle_smile
            show kaky_idle_sperm
            with dissolve
            kya "but simply return to your house at night and call for me, and i'll suck you off."

        "nut in kya's mouth":
            play sound "audio/splurt2.ogg"
            show kaky kaky16
            show kaky_sperminmouth_1 with flash
            kya "yes!"
            play sound "audio/splurt1.ogg"
            show kaky_sperminmouth_2
            hide kaky_sperminmouth_1
            with flash
            y "ngh!"
            play sound "audio/splurt3.ogg"
            show kaky_sperminmouth_3
            hide kaky_sperminmouth_2
            with flash
            kya "yes, get it all out..."
            show kaky kaky03
            hide kaky_sperminmouth_3
            show kaky_sperm_lingering
            with dissolve
            "she pulls off with a long *sluuuurp*"
            kya "hmm...."
            kya "that's nice, dear."
            kya "but i think you’ve got one more in you."
            "you feel an unearthly presence in your sack..."
            y "what the fuck....."
            "kya's spirit reaches into your depths and pulls out one, huge, final load...."
            play sound "audio/splurt2.ogg"
            show kaky_spermonface_1
            with flash
            ya "hnghn....!"
            ya "...what the shit!?"
            kya "mmm... there you go. you like cumming on my face, don’t you?"
            kya "you can never tell katara that you came in her mother's mouth."
            hide kaky_sperm_lingering
            hide kaky_spermonface_1
            show kaky kaky52
            show kaky_idle_sperm
            with dissolve
            kya "i must leave for now..."
            hide kaky_idle_sperm
            show kaky_idle_smile
            show kaky_idle_sperm
            with dissolve
            kya "but simply return to your house at night and call for me, and i'll suck you off."

    return
#--

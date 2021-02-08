init -999:
    $ mods = [];

init:
    $ gallery_version = "0.9.1"
    $ mods.append("Gallery")

    $ gallery_Book = 0;
    $ gallery_Route = 0;
    $ gallery_Choice = 0;
    
    # Pagination
    $ gallery_Page = 0;
    $ gallery_PageLength = 0;
    $ gallery_MaxPerPage = 8;


    python:
        class GalleryItem():
            def __init__(self, book, route, title, link, has): #Description, Image
                self.Book = book
                self.Route = route
                self.Title = title
                self.Link = link
                self.Has = has

        #class GalleryObj():
        #    def __init__(self, book, name, image):
        #        self.Book = book
        #        self.Name = name
        #        self.Image = image

    $ Gallery_Books = [
        "",
        "Water Tribe",
        "Fire Nation",
        "Earth Kingdom",
        "Republic City",
    ];
    
    $ Gallery_Routes = [
        "",
        "Neutral",
        "Slave",
        "Love",
    ];

    $ Gallery = [ #{b}New{/b} 
        ### Book 1 Neutral ###
        GalleryItem(1, 1, 'Alley Fuck', 'gallery_yue_bj', True),
        GalleryItem(1, 1, 'Lesbian Orgy', 'gallery_knock', True),
        GalleryItem(1, 1, 'PornLove 23', 'gallery_magazine_1', True),
        GalleryItem(1, 1, '[Nami] Blowjob', 'gallery_shop_bj_scene', True),
        GalleryItem(1, 1, '[Kya] Blowjob', 'gallery_kya_blowjob', True),
        GalleryItem(1, 1, '[Una] Anal', 'gallery_una_sex', True),

        ### Book 1 Slave ###
        GalleryItem(1, 2, 'Naked', 'gallery_slave_naked', True),
        GalleryItem(1, 2, 'Titfuck', 'gallery_slave_titfuck', True),
        GalleryItem(1, 2, 'Blowjob 1', 'gallery_slave_first_blowjob', True),
        GalleryItem(1, 2, 'Blowjob 2', 'gallery_slave_blowjob', True),
        GalleryItem(1, 2, 'Sex', 'gallery_slave_sex', True),
        GalleryItem(1, 2, 'Anal', 'gallery_slave_anal', True),
        GalleryItem(1, 2, 'Ending', 'gallery_slave_ending', True),

        ### Book 1 Love ###
        GalleryItem(1, 3, 'Handjob', 'gallery_love_handjob', True),
        GalleryItem(1, 3, 'Masturbate', 'gallery_love_masturbation', True),
        GalleryItem(1, 3, 'Footjob', 'gallery_love_footjob', True),
        GalleryItem(1, 3, 'Blowjob', 'gallery_love_blowjob', True),
        GalleryItem(1, 3, 'Sex', 'gallery_love_sex', True),
        GalleryItem(1, 3, 'Anal', 'gallery_love_anal', True),
        GalleryItem(1, 3, 'Ending', 'gallery_love_ending', True),

        ### Book 2 Neutral ###
        GalleryItem(2, 1, 'PornLove 42', 'gallery_pornlove42', True),
        GalleryItem(2, 1, '[Cow] Fuck', 'gallery_cow', True),

        GalleryItem(2, 1, '[Rei] Blowjob', 'gallery_rei_blowjob', True),
        GalleryItem(2, 1, '[Rei] Fuck', 'gallery_rei_fuck', True),

        GalleryItem(2, 1, '[Lia] Masturbate', 'gallery_lia_mast', True),
        GalleryItem(2, 1, '[Lia] Handjob', 'gallery_lia_handjob', True),
        GalleryItem(2, 1, '[Lia] Blowjob', 'gallery_lia_blowjob', True),
        GalleryItem(2, 1, '[Lia] Fuck', 'gallery_lia_fuck', True),

        GalleryItem(2, 1, '[Azula] Throne Lick feet', 'gallery_throne_lick', True),
        GalleryItem(2, 1, '[Azula] Throne Whip', 'gallery_throne_whip', True),
        GalleryItem(2, 1, '[Azula] Throne Strap-on', 'gallery_throne_strapon', True),

        ### Book 2 Slave ###
        GalleryItem(2, 2, '[Azula] Piss', 'gallery_apissjob', True),
        GalleryItem(2, 2, '[Azula] Footjob', 'gallery_afootjob4', True),
        GalleryItem(2, 2, '[Azula] Boobjob', 'gallery_aboobjob4', True),
        GalleryItem(2, 2, '[Azula] Buttjob', 'gallery_abuttjob4', True),
        GalleryItem(2, 2, '[Azula] Blowjob', 'gallery_ablowjob4', True),
        GalleryItem(2, 2, '[Azula] Anal', 'gallery_aanal5', True),
        GalleryItem(2, 2, '[Azula] Pussy Grind', 'gallery_agrind4', True),
        GalleryItem(2, 2, '[Azula] Tentacle Anal', 'gallery_tentacle_training', True),
        GalleryItem(2, 2, '[Azula] Prision Fuck', 'gallery_aprison_lick', True),
        GalleryItem(2, 2, '[Azula + Lia] Blowjob', 'gallery_lia_azula_bj', True),

        GalleryItem(2, 2, '[Ty Lee] Drink Piss', 'gallery_tylee_drinkpiss', True),
        GalleryItem(2, 2, '[Ty Lee] Blowjob', 'gallery_tylee_blowjob', True),
        GalleryItem(2, 2, '[Ty Lee] Fuck', 'gallery_tylee_sex', True),

        GalleryItem(2, 2, '[Ending] Group Sex', 'gallery_fpalace_day10', True),
        GalleryItem(2, 2, '[Ending] Tower Fuck', 'gallery_fpalace_day12', True),

        ### Book 2 Love ###
        GalleryItem(2, 3, '[Azula] Rub', 'gallery_za_beachrub', True),
        GalleryItem(2, 3, '[Azula] Masturbate', 'gallery_zfpalace_night20', True),
        GalleryItem(2, 3, '[Azula] Shower', 'gallery_ashower', True),
        GalleryItem(2, 3, '[Azula] Piss/Lick', 'gallery_zazula_piss', True),
        GalleryItem(2, 3, '[Azula] Fuck her Tits', 'gallery_afucktits', True),
        GalleryItem(2, 3, '[Azula] Handjob', 'gallery_za_handjob', True),
        GalleryItem(2, 3, '[Azula] Blowjob', 'gallery_za_blowjob', True),
        GalleryItem(2, 3, '[Azula] Anal', 'gallery_za_anal', True),
        GalleryItem(2, 3, '[Azula] Fuck', 'gallery_za_sex', True),
        GalleryItem(2, 3, '[Azula] Anal over Mai', 'gallery_sleepy_azula_anal', True),
       
        GalleryItem(2, 3, 'Naked', 'gallery_beach_naked', True),
        GalleryItem(2, 3, 'Bottle in the Ass', 'gallery_truth_or_dare', True),

        GalleryItem(2, 3, '[Ursa] Blowjob', 'gallery_ursa_zuko', True),
        GalleryItem(2, 3, '[Ursa] Images', 'gallery_ursa_pics', True),
       
        GalleryItem(2, 3, '[Ty Lee] Vibrator', 'gallery_tylee_vibrator', True),
        GalleryItem(2, 3, '[Ty Lee] Masturbation', 'gallery_tylee_dickwatch', True),
       
        GalleryItem(2, 3, '[Mai] Boob Massage', 'gallery_zem_boob', True),
        GalleryItem(2, 3, '[Mai] Blowjob', 'gallery_zem_blowjob', True),
        GalleryItem(2, 3, '[Mai] Anal', 'gallery_zem_anal', True),
        GalleryItem(2, 3, '[Mai] Fuck', 'gallery_zem_sex_start', True),
        GalleryItem(2, 3, '[Mai] Lick Azula', 'gallery_lick_azula', True),

        GalleryItem(2, 3, '[Ending] Azula Blowjob', 'gallery_azula_blowjob', True),
        GalleryItem(2, 3, '[Ending] Mai Sex', 'gallery_mai_ring_on', True),
        GalleryItem(2, 3, '[Ending] Throne Fuck', 'gallery_zthronebone1', True),
        GalleryItem(2, 3, '[Ending] Foursome', 'gallery_zuko_true_end', True),

        ### Book 3 Neutral ###
        GalleryItem(3, 1, '[PL] Smellerbee (Slave)', 'gallery_pornlove_bk3_slave', True), 
        GalleryItem(3, 1, '[PL] Smellerbee (Love)', 'gallery_pornlove_bk3_love_2', True), 
        GalleryItem(3, 1, '[PL] Hama (Love)', 'gallery_pornlovebk3_love', True), 

        GalleryItem(3, 1, '[Katara] Lake Blowjob', 'gallery_after_store_train', True),
        GalleryItem(3, 1, 'Fight Fuck', 'gallery_winnerfuckall_menu', True),
        GalleryItem(3, 1, 'Fist some Guard', 'gallery_fist_some_guard', True),
        GalleryItem(3, 1, '[Toph] Dancing', 'gallery_toph_drinking', True),

        ### Book 3 Slave ###
        GalleryItem(3, 2, '[Toph] Tit Massage', 'gallery_toph_titmassage', True),
        GalleryItem(3, 2, '[Toph] Titfuck', 'gallery_toph_titfuck', True),
        GalleryItem(3, 2, '[Toph] Footjob (Version 1)', 'gallery_toph_footjob1_3', True),
        GalleryItem(3, 2, '[Toph] Footjob (Version 2)', 'gallery_toph_footjob2_3', True),
        GalleryItem(3, 2, '[Toph] Blowjob', 'gallery_toph_blowjob3', True),
        GalleryItem(3, 2, '[Toph] Fuck', 'gallery_toph_sex3', True),
        GalleryItem(3, 2, '[Toph] Anal', 'gallery_toph_anal3', True),
        GalleryItem(3, 2, '[Toph] Anal with Katara', 'gallery_toph_anal1', True),
        GalleryItem(3, 2, '[Toph] Earthbend Blowjob', 'gallery_toph_rockbound2', True),
        GalleryItem(3, 2, '[Toph] Group Sex', 'gallery_tophgrouptug', True),
        GalleryItem(3, 2, '[Toph] Clean Fuck', 'gallery_toph_clean_fuck', True),

        GalleryItem(3, 2, '[Toph + Kat] Masturbation', 'gallery_toph_katara_masturbation', True),
        GalleryItem(3, 2, '[Toph + Kat] Dildo', 'gallery_toph_katara_chair_sex', True),

        GalleryItem(3, 2, '[Katara] Handjob', 'gallery_katara_handjob', True),

        GalleryItem(3, 2, '[Ajala] Nipple Play', 'gallery_ajala_nipplerub_menu', True),
        GalleryItem(3, 2, '[Ajala] Suki Lick', 'gallery_ajala_suki_lick', True),
        GalleryItem(3, 2, '[Ajala] Fuck', 'gallery_ajala_fuck', True),

        GalleryItem(3, 2, '[Jin] Buttjob', 'gallery_jin_buttjob', True),
        GalleryItem(3, 2, '[Jin] Blowjob', 'gallery_jin_sucks2', True),
        GalleryItem(3, 2, '[Jin] Fuck', 'gallery_jin_sex3', True),

        GalleryItem(3, 2, '[Jo Dee] Play with her tits', 'gallery_jodee_tits', True),
        GalleryItem(3, 2, '[Jo Dee] Fuck', 'gallery_jodee_sex1', True),
        GalleryItem(3, 2, '[Jo Dee] Pregnant Fuck', 'gallery_jdpregfuck', True),

        GalleryItem(3, 2, '[June] Cum on Hairy Pussy', 'gallery_cumhairypussy', True),
        GalleryItem(3, 2, '[June] Slap Ass', 'gallery_june_slap_ass', True),
        GalleryItem(3, 2, '[June] Blowjob', 'gallery_june_blowjob', True),
        GalleryItem(3, 2, '[June] Thigh Job', 'gallery_june_thighjob', True),
        GalleryItem(3, 2, '[June] Anal', 'gallery_june_sex', True),

        GalleryItem(3, 2, '[Naga] Small Body', 'gallery_naga_smallbody', True),
        GalleryItem(3, 2, '[Naga] Blowjob', 'gallery_naga_blowjob', True),
 
        GalleryItem(3, 2, '[Poppy + Toph] Fuck', 'gallery_tophmomfuck2', True),
        GalleryItem(3, 2, '[Poppy] Prego Anal', 'gallery_tophmomfuck3', True),
        
        GalleryItem(3, 2, '[Skye] Group Anal', 'gallery_ty_suki_skye1', True),

        GalleryItem(3, 2, '[Suki] Face Dicked', 'gallery_suki_bj', True),
        GalleryItem(3, 2, '[Suki] Dildo', 'gallery_suki_dildo_fuck2', True),
        GalleryItem(3, 2, '[Suki] Fuck', 'gallery_suki_dildo_fuck3', True),

        GalleryItem(3, 2, '[Ty Lee] Wall Blowjob', 'gallery_tylee_wall_bj', True),
        GalleryItem(3, 2, '[Ty Lee] Balance Ball', 'gallery_tylee_balanceball', True),
        GalleryItem(3, 2, '[Ty Lee] Kitty Sex', 'gallery_pussycrush', True),

        GalleryItem(3, 2, '[Ending] Toph Appa Fuck', 'gallery_toph_appa_fuck', True),

        ### Book 3 Love ###
        GalleryItem(3, 3, '[Toph] Camp Naked', 'gallery_earthtraining5', True),
        GalleryItem(3, 3, '[Toph] Titplay', 'gallery_toph_titplay3', True),
        GalleryItem(3, 3, '[Toph] Footjob', 'gallery_love_toph_footjob1', True),
        GalleryItem(3, 3, '[Toph] Blowjob', 'gallery_love_toph_blowjob', True),
        GalleryItem(3, 3, '[Toph] Cowgirl', 'gallery_toph_shadow_fuck', True),
        GalleryItem(3, 3, '[Toph] Missionary', 'gallery_toph_fuckonback', True),
        GalleryItem(3, 3, '[Toph] Sleep Masturbation', 'gallery_toph_chat22', True),
        GalleryItem(3, 3, '[Toph] Ass Massage', 'gallery_toph_ass_massage2', True),
        GalleryItem(3, 3, '[Toph] Prone Anal', 'gallery_love_toph_anal1', True),
        GalleryItem(3, 3, '[Toph] Cowgirl Anal', 'gallery_love_toph_anal2', True),

        GalleryItem(3, 3, '[Toph + Katara] Scissor', 'gallery_katara_toph_scissor', True),
        GalleryItem(3, 3, '[Toph + Katara] Blowjob', 'gallery_kat_toph_bj', True),

        GalleryItem(3, 3, '[Ajala] Anal', 'gallery_ajala_assfuck', True),
        GalleryItem(3, 3, '[Ajala] Dildos', 'gallery_ajala_dildos', True),
        GalleryItem(3, 3, '[Ajala] Fuck (Wall)', 'gallery_ajala_wonfight_10', True),
        GalleryItem(3, 3, '[Ajala] Fuck', 'gallery_ajala_dunk', True),

        GalleryItem(3, 3, '[Katara] Train Handjob', 'gallery_love_train_hj', True),
        GalleryItem(3, 3, '[Katara] Party Sex', 'gallery_katara_party_fuck2', True),
        GalleryItem(3, 3, '[Katara] Fuck', 'gallery_katara_rub_sex', True),

        GalleryItem(3, 3, '[Smellerbee] Blowjob', 'gallery_smellerbee_blowjob2', True),
        GalleryItem(3, 3, '[Smellerbee] Fuck', 'gallery_smellerbee_fuck', True),

        GalleryItem(3, 3, '[June] Masturbate', 'gallery_june_headlock_scene', True),
        GalleryItem(3, 3, '[June] Play with her Tits', 'gallery_june_titplay_standing', True),
        GalleryItem(3, 3, '[June] Handjob', 'gallery_love_june_handjob2', True),
        GalleryItem(3, 3, '[June] Fuck', 'gallery_june_lovefuck', True),

        GalleryItem(3, 3, '[Suki] Anal Fingering', 'gallery_suki_headlock_removal', True),
        GalleryItem(3, 3, '[Suki] Masturbate', 'gallery_love_suki_mast', True),
        GalleryItem(3, 3, '[Suki] Cowgirl', 'gallery_suki_lovefuck', True),
        GalleryItem(3, 3, '[Suki] Bar Blowjob', 'gallery_suki_barblow', True),

        GalleryItem(3, 3, '[Jo Dee] Titjob', 'gallery_joodee_boobjob', True),
        GalleryItem(3, 3, '[Jo Dee] Fuck', 'gallery_jd_full_nelson', True),

        GalleryItem(3, 3, '[Mean Girls] Maze Lick', 'gallery_meangirls_maze_licking', True),
        GalleryItem(3, 3, '[Mean Girls] Reward', 'gallery_meangirls_reward', True),
        
        GalleryItem(3, 3, '[Jin] Maze Fuck', 'gallery_jin_had_mazesex', True),
        GalleryItem(3, 3, '[Jin] Blowjob', 'gallery_jin_loveblowjob2', True),
        GalleryItem(3, 3, '[Jin] Fuck & Anal', 'gallery_love_jin_sex_anal', True),

        
        GalleryItem(3, 3, '[Ty Lee] Footjob', 'gallery_love_ty_footjob', True),
        GalleryItem(3, 3, '[Ty Lee] Blowjob', 'gallery_ty_cabbage_bj', True),
        GalleryItem(3, 3, '[Ty Lee] Fuck', 'gallery_tylee_lovefuck', True),
        GalleryItem(3, 3, '[Ty Lee] Dildo Fuck', 'gallery_tylee_lovedildo', True),

        GalleryItem(3, 3, '[Naga] Clawjob', 'gallery_naga_clawjob', True),
        GalleryItem(3, 3, '[Guard] Fuck', 'gallery_guard_fuck', True),
        GalleryItem(3, 3, '[Guard] Appa Fuck', 'gallery_appa_tug', True),

        GalleryItem(3, 3, '[Ending] Toph Fuck', 'gallery_bk3_love_final', True),
        GalleryItem(3, 3, '[Ending] Katara Fuck', 'gallery_katara_pregfuck', True),
        GalleryItem(3, 3, '[Ending] Ty Lee Lick', 'gallery_tylee_rub', True),
        
        #Book 4 Neutral
        GalleryItem(4, 1, 'PornLove Slave', 'gallery_pornlove_bk4', True),
        GalleryItem(4, 1, 'Memory Images', 'gallery_memory_paper', True),
        
        #Book 4 Slave
        GalleryItem(4, 2, '[Korra] Blowjob (Amon)', 'gallery_korra_blowjob1', True),
        GalleryItem(4, 2, '[Korra] Cum on her Pants', 'gallery_korra_cum_pants', True),
        GalleryItem(4, 2, '[Korra] Anal', 'gallery_bk4_s_korra_anal', True),
        GalleryItem(4, 2, '[Korra] Fuck (Amon)', 'gallery_korra_tiefuck1', True),
        GalleryItem(4, 2, '[Korra] Rub', 'gallery_korra_rubbing3', True),
        GalleryItem(4, 2, '[Korra] Titplay', 'gallery_korra_happytitplay1', True),
        GalleryItem(4, 2, '[Korra] Boobjob', 'gallery_korra_boobjob2', True),
        GalleryItem(4, 2, '[Korra] Spank', 'gallery_korra_happyspank1', True),
        GalleryItem(4, 2, '[Korra] Footjob', 'gallery_korra_footjob1', True),
        GalleryItem(4, 2, '[Korra] Fingerbang', 'gallery_korra_fingerbang', True),
        GalleryItem(4, 2, '[Korra] Eatout', 'gallery_korra_eatout1', True),
        GalleryItem(4, 2, '[Korra] Fuck', 'gallery_korra_happyfuck1', True),
        GalleryItem(4, 2, '[Korra] Gang Rape', 'gallery_korra_tunnel_cont1', True),

        GalleryItem(4, 2, '[Korra] Washroom BJ', 'gallery_bk4_jinorawashes', True),

        GalleryItem(4, 2, '[Korra] Blowjob', 'gallery_korra_blimp_sex', True),
        GalleryItem(4, 2, '[Korra + Senna] Sex', 'gallery_korra_senna_bang', True),
        GalleryItem(4, 2, '[Korra + Asami] Sex', 'gallery_asami_korra_sex', True),
        GalleryItem(4, 2, '[Korra] Dogwalk', 'gallery_korra_park_walk1', True),
        GalleryItem(4, 2, '[Korra] Pregnant Sex', 'gallery_korra_preg_fuck', True),

        GalleryItem(4, 2, '[Pema] Fuck', 'gallery_pema_vag2', True),
        GalleryItem(4, 2, '[Pema] Handjob', 'gallery_pema_handjob3', True),
        GalleryItem(4, 2, '[Pema] Blowjob', 'gallery_pema_blowjob1', True),
        GalleryItem(4, 2, '[Pema + Lin] Fuck', 'gallery_pema_lin_sex', True),

        GalleryItem(4, 2, '[Asami] Tits', 'gallery_asami_tits2', True),
        GalleryItem(4, 2, '[Asami] Blowjob', 'gallery_asami_blowjob2', True),
        GalleryItem(4, 2, '[Asami] Girls Titsuck', 'gallery_korra_asami_titsuck1', True),
        GalleryItem(4, 2, '[Asami] Vag/Anal', 'gallery_asami_vag1', True),

        GalleryItem(4, 2, '[Jinora] Fuck', 'gallery_bk4_home_day3_1', True),
        GalleryItem(4, 2, '[Jinora] Blowjob', 'gallery_b4_jinoralick_1', True),
        GalleryItem(4, 2, '[Jinora] Sleep Fuck', 'gallery_bk4_korra_day6', True),
        GalleryItem(4, 2, '[Jinora + Pema] Fuck', 'gallery_jinora_tower_fuck', True),

        GalleryItem(4, 2, '[Kyoshi] Pussy Fan', 'gallery_kyoshi_pussyfan1', True),

        GalleryItem(4, 2, '[Senna] Dildo', 'gallery_bk4_senna_talk', True),
        GalleryItem(4, 2, '[Senna] Anal', 'gallery_bk4_korra_night2_1', True),

        GalleryItem(4, 2, '[Eska] Blowjob', 'gallery_bk4_eska_night3_1', True),
        GalleryItem(4, 2, '[Eska] Anal', 'gallery_bk4_eska_day4_1', True),
        GalleryItem(4, 2, '[Eska] Fuck', 'gallery_eskavag1', True),
        GalleryItem(4, 2, '[Desna] Anal', 'gallery_bk4_des_anal', True),

        GalleryItem(4, 2, '[Equalist] Fuck', 'gallery_equa_fuck_suck', True),
        GalleryItem(4, 2, '[Ginger] Fuck', 'gallery_fuck_ginger_1', True),
        GalleryItem(4, 2, '[3 Girls] Fuck', 'gallery_wolfbat2', True),

        GalleryItem(4, 2, '[Lin] Jerk off', 'gallery_lin_handjob3', True),
        GalleryItem(4, 2, '[Lin] Buttjob', 'gallery_lin_buttjob2', True),
        GalleryItem(4, 2, '[Lin] Pussy Rub', 'gallery_lin_rub2', True),
        GalleryItem(4, 2, '[Lin] Fuck', 'gallery_lin_cell_fuck', True),

        GalleryItem(4, 2, '[Yangchen] Blowjob', 'gallery_bk4_windpuzzle_end', True),
        GalleryItem(4, 2, '[Yangchen] Titjob', 'gallery_yang_boobjob2', True),
        GalleryItem(4, 2, '[Yangchen] Vag/Anal', 'gallery_yang_sex2', True),

        GalleryItem(4, 2, '[Zhuli] Blowjob', 'gallery_zh_bj1', True),
        GalleryItem(4, 2, '[Zhuli] Fuck', 'gallery_zhu_fuck1', True),

        GalleryItem(4, 2, '[Katara] Sauna', 'gallery_bk4_council_day4_1', True),
        GalleryItem(4, 2, '[Ending] Anal', 'gallery_b4_skyhigh_fuck', True),
        GalleryItem(4, 2, '[Ending] Asami Sex', 'gallery_asami_ending', True), # From D

        #Book 4 Love
        GalleryItem(4, 3, '[Katara] Handjob', 'gallery_bk4l_katara_hj', True),
        GalleryItem(4, 3, '[Katara] Sex', 'gallery_bk4l_katara_sex1', True),
        GalleryItem(4, 3, '[Kya] Masturbation 1', 'gallery_bk4l_kya_mast2', True),
        GalleryItem(4, 3, '[Kya] Masturbation 2', 'gallery_bk4l_kya_mast3', True),
        GalleryItem(4, 3, '[Korra] Water Session', 'gallery_bk4l_bath_sessions2', True),
        GalleryItem(4, 3, '[Korra] Massage', 'gallery_bk4l_korra_massage2', True),

        GalleryItem(4, 3, '{b}New{/b} [Jinora] Naked', 'gallery_bk4l_jinora_naked',True),
        GalleryItem(4, 3, '{b}New{/b} [Asami] Photos', 'gallery_bk4l_asami_photos',True),
        GalleryItem(4, 3, '{b}New{/b} [Opal] Exercise', 'gallery_bk4l_opal_exercise',True),
        GalleryItem(4, 3, '{b}New{/b} [Kya] Blowjob', 'gallery_bk4l_kya_bj',True),
        GalleryItem(4, 3, '{b}New{/b} [Kora] Kiss', 'gallery_bk4l_kora_kiss',True),
        GalleryItem(4, 3, '{b}New{/b} [Movers] Nuktuk Outtakes', 'gallery_bk4l_ginger_fuck',True),
        GalleryItem(4, 3, '{b}New{/b} [Captain] Anal', 'gallery_bk4l_lotus_anal1',True),
    ];

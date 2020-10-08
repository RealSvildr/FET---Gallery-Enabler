init 999:
    screen main_menu() tag menu:
        window:
            style "mm_root"

        frame:
            style_group "mm"
            xalign .98
            yalign .98

            has vbox
            textbutton _("New Game") action Start()
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Gallery") action Start("gallery_menu")
            textbutton _("Help") action Help()
            textbutton _("Support Us!") action OpenURL("http://www.patreon.com/mity")
            textbutton _("Disclaimer") action ShowMenu("disclaimer")
            textbutton _("Quit") action Quit(confirm=False)

        
        if gallery_version in config.version:
            text "v[config.version] + Gallery" xpos 10 ypos 10
        else:
            text "v[config.version] + Gallery ([gallery_version] Check for Updates)" xpos 10 ypos 10

screen gallery_screen():
    text "{size=40}Gallery":
        xalign 0.5 ypos 25

    vbox pos (150, 100):
        imagebutton:
            action [SetVariable("gallery_Book", 1), Jump("gallery_menu_book")]
            idle Transform("mods/Gallery/Images/BK1/cover.webp", zoom=0.4)
            hover Transform(im.MatrixColor("mods/Gallery/Images/BK1/cover.webp", im.matrix.brightness(0.12)), zoom=0.402)

        text "{size=30}[Gallery_Books[1]]":
            xalign 0.5

    vbox pos (540, 100):
        imagebutton:
            action [SetVariable("gallery_Book", 2), Jump("gallery_menu_book")]
            idle Transform("mods/Gallery/Images/BK2/cover.webp", zoom=0.4)
            hover Transform(im.MatrixColor("mods/Gallery/Images/BK2/cover.webp", im.matrix.brightness(0.12)), zoom=0.402)

        text "{size=30}[Gallery_Books[2]]":
            xalign 0.5

    vbox pos (150, 375):
        imagebutton:
            action [SetVariable("gallery_Book", 3), Jump("gallery_menu_book")]
            idle Transform("mods/Gallery/Images/BK3/cover.webp", zoom=0.4)
            hover Transform(im.MatrixColor("mods/Gallery/Images/BK3/cover.webp", im.matrix.brightness(0.12)), zoom=0.402)

        text "{size=30}[Gallery_Books[3]]":
            xalign 0.5

    vbox pos (540, 375):
        imagebutton:
            action [SetVariable("gallery_Book", 4), Jump("gallery_menu_book")]
            idle Transform("mods/Gallery/Images/BK4/cover.webp", zoom=0.4)
            hover Transform(im.MatrixColor("mods/Gallery/Images/BK4/cover.webp", im.matrix.brightness(0.12)), zoom=0.402)

        text "{size=30}[Gallery_Books[4]]":
            xalign 0.5

    vbox pos (20, 670):
        imagebutton:
            action Jump("gallery_exit")
            idle Transform("mods/Gallery/Images/Common/main_menu.webp", zoom=0.65)
            hover Transform(im.MatrixColor("mods/Gallery/Images/Common/main_menu.webp", im.matrix.brightness(0.12)), zoom=0.65)


screen gallery_route_screen():
    $ temp_Name = Gallery_Books[gallery_Book]

    text "{size=40}[temp_Name]":
        xalign 0.5 ypos 25

    vbox pos (360, 100):
        imagebutton:
            action [SetVariable("gallery_Route", 1), Jump("gallery_menu_route")]
            idle Transform("mods/Gallery/Images/Common/[Gallery_Routes[1]].webp", zoom=0.36)
            hover Transform(im.MatrixColor("mods/Gallery/Images/Common/%s.webp" %Gallery_Routes[1], im.matrix.brightness(0.12)), zoom=0.362)

        text "{size=30}[Gallery_Routes[1]]":
            xalign 0.5

    vbox pos (100, 375):
        imagebutton:
            action [SetVariable("gallery_Route", 2), Jump("gallery_menu_route")]
            idle Transform("mods/Gallery/Images/Common/[Gallery_Routes[2]].webp", zoom=0.36)
            hover Transform(im.MatrixColor("mods/Gallery/Images/Common/%s.webp" %Gallery_Routes[2], im.matrix.brightness(0.12)), zoom=0.362)

        text "{size=30}[Gallery_Routes[2]]":
            xalign 0.5

    vbox pos (620, 375):
        imagebutton:
            action [SetVariable("gallery_Route", 3), Jump("gallery_menu_route")]
            idle Transform("mods/Gallery/Images/Common/[Gallery_Routes[3]].webp", zoom=0.36)
            hover Transform(im.MatrixColor("mods/Gallery/Images/Common/%s.webp" %Gallery_Routes[3], im.matrix.brightness(0.12)), zoom=0.362)

        text "{size=30}[Gallery_Routes[3]]":
            xalign 0.5

    vbox pos (20, 670):
        imagebutton:
            action Jump("gallery_menu")
            idle Transform("mods/Gallery/Images/Common/back.webp", zoom=0.65)
            hover Transform(im.MatrixColor("mods/Gallery/Images/Common/back.webp", im.matrix.brightness(0.12)), zoom=0.65)

screen gallery_choice_screen():
    $ temp_Book = Gallery_Books[gallery_Book]
    $ temp_Route = Gallery_Routes[gallery_Route]
    $ temp_Page = gallery_Page + 1

    text "{size=40}[temp_Book]{/size=40}":
        xalign 0.5 ypos 25

    text "{size=25}Route: [temp_Route]{/size=25}":
        xalign 0.5 ypos 70

    text "Page: [temp_Page]":
        xalign 0.5 ypos 580

    # First Line
    if len(menu_list) > 0:
        if menu_list[0].Has:
            vbox pos (45, 150):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[0].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[0].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[0].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[0].Title]":
                    xalign 0.5
        else:
            vbox pos (45, 150):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[0].Title]":
                    xalign 0.5

    if len(menu_list) > 1:
        if menu_list[1].Has:
            vbox pos (285, 150):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[1].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[1].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[1].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[1].Title]":
                    xalign 0.5
        else:
            vbox pos (285, 150):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[1].Title]":
                    xalign 0.5
            
    if len(menu_list) > 2:
        if menu_list[2].Has:
            vbox pos (525, 150):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[2].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[2].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[2].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[2].Title]":
                    xalign 0.5
        else:
            vbox pos (525, 150):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[2].Title]":
                    xalign 0.5
    if len(menu_list) > 3:
        if menu_list[3].Has:
            vbox pos (760, 150):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[3].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[3].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[3].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[3].Title]":
                    xalign 0.5
        else:
            vbox pos (760, 150):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[3].Title]":
                    xalign 0.5

    # Second Line
    if len(menu_list) > 4:
        if menu_list[4].Has:
            vbox pos (45, 350):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[4].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[4].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[4].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[4].Title]":
                    xalign 0.5
        else:
            vbox pos (45, 350):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[4].Title]":
                    xalign 0.5

    if len(menu_list) > 5:
        if menu_list[5].Has:
            vbox pos (285, 350):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[5].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[5].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[5].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[5].Title]":
                    xalign 0.5
        else:
            vbox pos (285, 350):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[5].Title]":
                    xalign 0.5
        
    if len(menu_list) > 6:
        if menu_list[6].Has:
            vbox pos (525, 350):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[6].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[6].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[6].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[6].Title]":
                    xalign 0.5
        else:
            vbox pos (525, 350):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[6].Title]":
                    xalign 0.5
            
    if len(menu_list) > 7:
        if menu_list[7].Has:
            vbox pos (760, 350):
                imagebutton:
                    action [SetVariable("gallery_Choice", menu_list[7].Link), Jump("gallery_sender")]
                    idle Transform("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[7].Link.replace('gallery_', '')), zoom=0.4)
                    hover Transform(im.MatrixColor("mods/Gallery/Images/BK%d/%s/%s.webp" %(gallery_Book, temp_Route, menu_list[7].Link.replace('gallery_', '')), im.matrix.brightness(0.12)), zoom=0.402)

                text "{size=15}[menu_list[7].Title]":
                    xalign 0.5
        else:
            vbox pos (760, 350):
                imagebutton:
                    idle Transform("mods/Gallery/Images/Common/locked.webp", zoom=0.4)

                text "{size=15}[menu_list[7].Title]":
                    xalign 0.5

    # Paging
    if gallery_Page > 0:
        vbox pos(205, 580):
            imagebutton:
                action [SetVariable("gallery_Page", gallery_Page - 1), Jump("gallery_menu_route")]
                idle Transform("mods/Gallery/Images/Common/last_page.webp", zoom=0.65)
                hover Transform(im.MatrixColor("mods/Gallery/Images/Common/last_page.webp", im.matrix.brightness(0.12)), zoom=0.65)
    else:
        vbox pos(205, 580):
            imagebutton:
                idle Transform(im.MatrixColor("mods/Gallery/Images/Common/last_page.webp", im.matrix.brightness(0.30)), zoom=0.65)

    if gallery_Page < gallery_PageLength:
        vbox pos(565, 580):
            imagebutton:
                action [SetVariable("gallery_Page", gallery_Page + 1), Jump("gallery_menu_route")]
                idle Transform("mods/Gallery/Images/Common/next_page.webp", zoom=0.65)
                hover Transform(im.MatrixColor("mods/Gallery/Images/Common/next_page.webp", im.matrix.brightness(0.12)), zoom=0.65)
    else:
        vbox pos(565, 580):
            imagebutton:
                idle Transform(im.MatrixColor("mods/Gallery/Images/Common/next_page.webp", im.matrix.brightness(0.30)), zoom=0.65)

    # Go Back
    vbox pos (20, 670):
        imagebutton:
            action Jump("gallery_menu_book")
            idle Transform("mods/Gallery/Images/Common/back.webp", zoom=0.65)
            hover Transform(im.MatrixColor("mods/Gallery/Images/Common/back.webp", im.matrix.brightness(0.12)), zoom=0.65)
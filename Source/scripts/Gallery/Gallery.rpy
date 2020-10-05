label clearInterface:
    stop music
    hide text
    scene white

    return

label pauseInterface:
    show ctc
    pause
    hide ctc

    return

label gallery_exit:
    $ MainMenu(confirm=False)()

label gallery_menu:
    call clearInterface
    $ gallery_Book = 0

    # scene expression "images/Gallery/Common/background.webp"
    call screen gallery_screen

label gallery_menu_book:
    call clearInterface
    $ gallery_Route = 0
    $ gallery_Page = 0

    if gallery_Book == 0:
        jump gallery_menu

    # scene expression "images/Gallery/BK[gallery_Book]/background.webp"
    call screen gallery_route_screen

label gallery_menu_route:
    call clearInterface

    if gallery_Book == 0:
        jump gallery_menu

    if gallery_Route == 0:
        jump gallery_menu_book

    # scene expression "images/Gallery/BK[gallery_Book]/background.webp"
    python:
        list = [item for item in Gallery if item.Book == gallery_Book and item.Route == gallery_Route]
        menu_list = []

        # Pagination
        gallery_PageLength = (len(list) / gallery_MaxPerPage) 

        if len(list) % gallery_MaxPerPage == 0:
            gallery_PageLength -= 1

        if gallery_PageLength > 0:
            minValItem = (gallery_Page * gallery_MaxPerPage)
            maxValItem = minValItem + gallery_MaxPerPage;

            if maxValItem > len(list):
                maxValItem = len(list)

            while minValItem < maxValItem:
                menu_list.append(list[minValItem])
                minValItem += 1

        else:
            menu_list = list

    call screen gallery_choice_screen

label gallery_sender:
    if gallery_Choice == 0:
        call gallery_menu_route

    scene black
    $ renpy.call(gallery_Choice)

    jump gallery_menu_route

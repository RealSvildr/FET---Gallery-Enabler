##### [PornLove] Banned
label gallery_pornlove_bk4:
    while True:
        menu:
            "Page 1":
                scene expression "bk4/backgrounds/pl_1.jpg" with dissolve
            "Page 2":
                scene expression "bk4/backgrounds/pl_2.jpg" with dissolve
            "Page 3":
                scene expression "bk4/backgrounds/pl_3.jpg" with dissolve
            "Exit":
                return

        call pauseInterface
##### [Memory] Images
label gallery_memory_paper:
    scene
    show expression "bk4_xtra/memory_paper/white_solid.png"
    
    call screen gallery_memory_paper_selector


screen gallery_memory_paper_selector:
    modal True

    imagebutton:
        idle "mp 1"
        hovered SetVariable("mp_num",1)
        hover "mp_hover1"
        pos (0,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",1)]

    imagebutton:
        idle "mp 2"
        hovered SetVariable("mp_num",2)
        hover "mp_hover1"
        pos (100,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",2)]

    imagebutton:
        idle "mp 3"
        hovered SetVariable("mp_num",3)
        hover "mp_hover1"
        pos (200,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",3)]

    imagebutton:
        idle "mp 4"
        hovered SetVariable("mp_num",4)
        hover "mp_hover1"
        pos (300,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",4)]

    imagebutton:
        idle "mp 5"
        hovered SetVariable("mp_num",5)
        hover "mp_hover1"
        pos (400,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",5)]

    imagebutton:
        idle "mp 6"
        hovered SetVariable("mp_num",6)
        hover "mp_hover1"
        pos (500,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",6)]

    imagebutton:
        idle "mp 7"
        hovered SetVariable("mp_num",7)
        hover "mp_hover1"
        pos (600,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",7)]

    imagebutton:
        idle "mp 8"
        hovered SetVariable("mp_num",8)
        hover "mp_hover1"
        pos (700,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",8)]

    imagebutton:
        idle "mp 9"
        hovered SetVariable("mp_num",9)
        hover "mp_hover1"
        pos (800,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",9)]

    imagebutton:
        idle "mp 10"
        hovered SetVariable("mp_num",10)
        hover "mp_hover1"
        pos (900,0)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",10)]

    imagebutton:
        idle "mp 11"
        hovered SetVariable("mp_num",11)
        hover "mp_hover1"
        pos (0,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",11)]

    imagebutton:
        idle "mp 12"
        hovered SetVariable("mp_num",12)
        hover "mp_hover1"
        pos (100,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",12)]

    imagebutton:
        idle "mp 13"
        hovered SetVariable("mp_num",13)
        hover "mp_hover1"
        pos (200,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",13)]

    imagebutton:
        idle "mp 14"
        hovered SetVariable("mp_num",14)
        hover "mp_hover1"
        pos (300,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",14)]

    imagebutton:
        idle "mp 15"
        hovered SetVariable("mp_num",15)
        hover "mp_hover1"
        pos (400,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",15)]

    imagebutton:
        idle "mp 16"
        hovered SetVariable("mp_num",16)
        hover "mp_hover1"
        pos (500,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",16)]

    imagebutton:
        idle "mp 17"
        hovered SetVariable("mp_num",17)
        hover "mp_hover1"
        pos (600,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",17)]

    imagebutton:
        idle "mp 18"
        hovered SetVariable("mp_num",18)
        hover "mp_hover1"
        pos (700,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",18)]

    imagebutton:
        idle "mp 19"
        hovered SetVariable("mp_num",19)
        hover "mp_hover1"
        pos (800,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",19)]

    imagebutton:
        idle "mp 20"
        hovered SetVariable("mp_num",20)
        hover "mp_hover1"
        pos (900,100)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",20)]

    imagebutton:
        idle "mp 21"
        hovered SetVariable("mp_num",21)
        hover "mp_hover1"
        pos (0,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",21)]

    imagebutton:
        idle "mp 22"
        hovered SetVariable("mp_num",22)
        hover "mp_hover1"
        pos (100,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",22)]

    imagebutton:
        idle "mp 23"
        hovered SetVariable("mp_num",23)
        hover "mp_hover1"
        pos (200,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",23)]

    imagebutton:
        idle "mp 24"
        hovered SetVariable("mp_num",24)
        hover "mp_hover1"
        pos (300,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",24)]

    imagebutton:
        idle "mp 25"
        hovered SetVariable("mp_num",25)
        hover "mp_hover1"
        pos (400,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",25)]

    imagebutton:
        idle "mp 26"
        hovered SetVariable("mp_num",26)
        hover "mp_hover1"
        pos (500,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",26)]

    imagebutton:
        idle "mp 27"
        hovered SetVariable("mp_num",27)
        hover "mp_hover1"
        pos (600,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",27)]

    imagebutton:
        idle "mp 28"
        hovered SetVariable("mp_num",28)
        hover "mp_hover1"
        pos (700,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",28)]

    imagebutton:
        idle "mp 29"
        hovered SetVariable("mp_num",29)
        hover "mp_hover1"
        pos (800,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",29)]

    imagebutton:
        idle "mp 30"
        hovered SetVariable("mp_num",30)
        hover "mp_hover1"
        pos (900,200)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",30)]

    imagebutton:
        idle "mp 31"
        hovered SetVariable("mp_num",31)
        hover "mp_hover1"
        pos (0,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",31)]

    imagebutton:
        idle "mp 32"
        hovered SetVariable("mp_num",32)
        hover "mp_hover1"
        pos (100,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",32)]

    imagebutton:
        idle "mp 33"
        hovered SetVariable("mp_num",33)
        hover "mp_hover1"
        pos (200,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",33)]

    imagebutton:
        idle "mp 34"
        hovered SetVariable("mp_num",34)
        hover "mp_hover1"
        pos (300,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",34)]

    imagebutton:
        idle "mp 35"
        hovered SetVariable("mp_num",35)
        hover "mp_hover1"
        pos (400,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",35)]

    imagebutton:
        idle "mp 36"
        hovered SetVariable("mp_num",36)
        hover "mp_hover1"
        pos (500,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",36)]

    imagebutton:
        idle "mp 37"
        hovered SetVariable("mp_num",37)
        hover "mp_hover1"
        pos (600,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",37)]

    imagebutton:
        idle "mp 38"
        hovered SetVariable("mp_num",38)
        hover "mp_hover1"
        pos (700,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",38)]

    imagebutton:
        idle "mp 39"
        hovered SetVariable("mp_num",39)
        hover "mp_hover1"
        pos (800,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",39)]

    imagebutton:
        idle "mp 40"
        hovered SetVariable("mp_num",40)
        hover "mp_hover1"
        pos (900,300)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",40)]

    imagebutton:
        idle "mp 41"
        hovered SetVariable("mp_num",41)
        hover "mp_hover1"
        pos (0,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",41)]

    imagebutton:
        idle "mp 42"
        hovered SetVariable("mp_num",42)
        hover "mp_hover1"
        pos (100,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",42)]

    imagebutton:
        idle "mp 43"
        hovered SetVariable("mp_num",43)
        hover "mp_hover1"
        pos (200,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",43)]

    imagebutton:
        idle "mp 44"
        hovered SetVariable("mp_num",44)
        hover "mp_hover1"
        pos (300,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",44)]

    imagebutton:
        idle "mp 45"
        hovered SetVariable("mp_num",45)
        hover "mp_hover1"
        pos (400,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",45)]

    imagebutton:
        idle "mp 46"
        hovered SetVariable("mp_num",46)
        hover "mp_hover1"
        pos (500,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",46)]

    imagebutton:
        idle "mp 47"
        hovered SetVariable("mp_num",47)
        hover "mp_hover1"
        pos (600,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",47)]

    imagebutton:
        idle "mp 48"
        hovered SetVariable("mp_num",48)
        hover "mp_hover1"
        pos (700,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",48)]

    imagebutton:
        idle "mp 49"
        hovered SetVariable("mp_num",49)
        hover "mp_hover1"
        pos (800,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",49)]

    imagebutton:
        idle "mp 50"
        hovered SetVariable("mp_num",50)
        hover "mp_hover1"
        pos (900,400)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",50)]

    imagebutton:
        idle "mp 51"
        hovered SetVariable("mp_num",51)
        hover "mp_hover1"
        pos (0,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",51)]

    imagebutton:
        idle "mp 52"
        hovered SetVariable("mp_num",52)
        hover "mp_hover1"
        pos (100,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",52)]

    imagebutton:
        idle "mp 53"
        hovered SetVariable("mp_num",53)
        hover "mp_hover1"
        pos (200,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",53)]

    imagebutton:
        idle "mp 54"
        hovered SetVariable("mp_num",54)
        hover "mp_hover1"
        pos (300,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",54)]

    imagebutton:
        idle "mp 55"
        hovered SetVariable("mp_num",55)
        hover "mp_hover1"
        pos (400,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",55)]

    imagebutton:
        idle "mp 56"
        hovered SetVariable("mp_num",56)
        hover "mp_hover1"
        pos (500,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",56)]

    imagebutton:
        idle "mp 57"
        hovered SetVariable("mp_num",57)
        hover "mp_hover1"
        pos (600,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",57)]

    imagebutton:
        idle "mp 58"
        hovered SetVariable("mp_num",58)
        hover "mp_hover1"
        pos (700,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",58)]

    imagebutton:
        idle "mp 59"
        hovered SetVariable("mp_num",59)
        hover "mp_hover1"
        pos (800,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",59)]

    imagebutton:
        idle "mp 60"
        hovered SetVariable("mp_num",60)
        hover "mp_hover1"
        pos (900,500)
        focus_mask True
        action [Jump("gallery_mem_scene"), SetVariable("mp_num",60)]

    textbutton "exit" action Call('gallery_menu_route'):
            xalign 0.5 yalign 0.93

label gallery_mem_scene:
    show expression "bk4_xtra/memory_paper/mem[mp_num].jpeg"
    pause

    jump gallery_memory_paper
#####
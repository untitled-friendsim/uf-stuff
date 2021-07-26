init offset = 2

# Splash screen on first load

label splashscreen:
    if persistent.firstscreen:
        scene black
        fscreen "Untitled Friendsim is built upon the concepts presented in Homestuck, Pesterquest and the Homestuck Epilogues. However, prior knowledge of these and the general universe they take place in is not needed to properly experience the game and it's lore.\n\n\nUntitled Friendsim contains flashing lights and similar imagery. You may disable these animations in the options menu.\n\n\nUntitled Friendsim contains mature content and sensitive themes. For detailed content warnings, consult the {a=call:dlc_warnings}\"Warnings\"{/a} menu."
        $ persistent.firstscreen = False
    return

# Main menu for default liteskin
# Offset = 2 to override SYS overrides

image menu_background = "gui/game_menu.png"
define config.main_menu_music = "music/main_menu.mp3"

define splashtext = [
    "example of a splash!",
    "may contain traces of nuts",
    "totally tubular!",
    "your momma",
    "penis",
    "how",
    "nugget biscuit, nugget in a biscuit"
]

transform titlemove:
    zoom 0.65
    #ypos 50
    #ease 2.0 ypos 60
    #pause (0.4)
    #ease 2.0 ypos 50
    #pause (0.8)
    #repeat

transform menumove:
    zoom 1.5
    xpos 20
    on hover:
        linear .25 xpos 50
        linear .1 zoom 1.55

    on idle:
        linear .25 xpos 20
        linear .1 zoom 1.5

transform minecraftsplash:
        subpixel True
        rotate 345
        ease 0.25 zoom 1.1
        linear 0.3 zoom 1.0
        repeat


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add "menu_background"

    $ splash_groups = [splashtext]

    default splashtext = renpy.random.choice(renpy.random.choice(splash_groups))
    default splashaction = NullAction()

    imagebutton auto "gui/title_%s.png" action SetScreenVariable("splashtext", renpy.random.choice(renpy.random.choice(splash_groups))) yanchor 0 xanchor 0 xpos 30 ypos 30 at titlemove

    imagebutton auto "gui/start_%s.png" action ShowVolSelectAction pos (20, 345) at menumove
    imagebutton auto "gui/load_%s.png" action ShowMenuFallback('load') pos (20, 405) at menumove
    imagebutton auto "gui/options_%s.png" action ShowMenuFallback("preferences") pos (20, 465) at menumove
    imagebutton auto "gui/friends_%s.png" action ShowMenuFallback('dlc_achievements') pos (20, 525) at menumove
    imagebutton auto "gui/credits_%s.png" action ShowMenuFallback('credits') pos (20, 585) at menumove
    imagebutton auto "gui/exit_%s.png" action Quit() pos (20, 645) at menumove
    textbutton _("Check for Updates") action updater.Update("https://out-of-print-flight.000webhostapp.com/uf/updates.json") pos (980, 660) at right



    textbutton splashtext at minecraftsplash:
        action splashaction
        xpadding 10
        ypadding 10
        xmargin 5
        ymargin 5
        xpos 600
        ypos 175
        xanchor 0.5
        yanchor 0.5
        text_font "Minecraftia-Regular.ttf"
        text_size 20
        text_color "#dddd00"
        text_xsize 500
        text_outlines [(0, '#444400', 2.5, 2.5)]
        text_text_align 0.0
        text_layout "subtitle"

    # use mainmenu_devbox
    key "trickster" action getMousePosition, ShowMenuFallback('mainmenu_devbox')

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("Untitled Friendsim", accent=True)

style main_menu_title:
    properties gui.text_properties("Untitled Friendsim")

style main_menu_version:
    properties gui.text_properties("updatetest1")

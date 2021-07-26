init offset = 1

init python:
    QuirkStore["mixiek"] = [(",", ",,"), ("'", ","), ("s|S", "$"), ("\.", ","), ("(.+? .+?)( .+)", "\\1,,\\2")]

define __p__mixiekq = HtagChar("??????", quirklist=["mixiek"], kind=hiveswap, image="mixiek", show_blood="gold")
define __p__mixiekaq = HtagChar("MIXIEK", quirklist=["mixiek"], kind=hiveswap, image="mixiek", show_blood="gold")

image mixiek = Image("{{assets}}/images/mixiek_idle.png", yanchor=860)
image mixiek idle = Image("{{assets}}/images/mixiek_idle.png", yanchor=860)
image mixiek idle talk = Image("{{assets}}/images/mixiek_idle_talk.png", yanchor=860)
image mixiek idle_scarf = Image("{{assets}}/images/mixiek_idle_scarf.png", yanchor=860)
image mixiek shocked = Image("{{assets}}/images/mixiek_shocked.png", yanchor=860)
image mixiek startled = Image("{{assets}}/images/mixiek_startled.png", yanchor=860)
image mixiek intrigue = Image("{{assets}}/images/mixiek_intrigue.png", yanchor=860)
image mixiek dazed = Image("{{assets}}/images/mixiek_dazed.png", yanchor=860)
image mixiek pity = Image("{{assets}}/images/mixiek_pity.png", yanchor=860)
image mixiek angry_scarf1 = Image("{{assets}}/images/mixiek_angryscarf1.png", yanchor=860)
image mixiek angry_scarf2 = Image("{{assets}}/images/mixiek_angryscarf2.png", yanchor=860)
image mixiek angry_scarf3 = Image("{{assets}}/images/mixiek_angryscarf3.png", yanchor=860)
image mixiek angry_scarf4 = Image("{{assets}}/images/mixiek_angryscarf4.png", yanchor=860)
image mixiek thinking = Image("{{assets}}/images/mixiek_thinking.png", yanchor=860)

image background pavement = Image("{{assets}}/images/pavement.png")
image background city_background1 = Image("{{assets}}/images/city_background1.png")
image background city_background2 = Image("{{assets}}/images/city_background2.png")
image background city_background2_sand = Image("{{assets}}/images/city_background2_sand.png")
image background alleyway = Image("{{assets}}/images/alleyway.png")
image background dumpster = Image("{{assets}}/images/dumpster.png")
image background house_outside = Image("{{assets}}/images/house_outside.png")
image background house_inside = Image("{{assets}}/images/house_outside.png")

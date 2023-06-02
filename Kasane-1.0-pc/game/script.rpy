# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Fuchi Kasane", color = "#d9d2e9")
define fs = Character ("Fuchi Sukeyo", color = "#8e7cc3")
define i = Character("Ichika", color = "#f44336")
define o = Character("Others", color = "#f44336")
define t = Character("Teacher", color = "#498cc6")
define t2 = Character("Teacher", color = "#498cc6")
define s = Character("Students", color = "#f44336")
define a = Character("Audience", color = "#f44336")
define s1 = Character ("Sister 1", color = "#f44336")
define s2 = Character ("Sister 2", color = "#f44336")
define b = Character ("Both", color = "#f44336")
define l = Character ("Loudspeaker", color = "#f44336")
define n = Character ("Narrator")

# Piano minigame
init python:

    def create_button_pattern(type):
        pattern = []
        if type == "easy":
            for i in range(4):
                pattern.append(renpy.random.randint(0,12))
        if type == "medium":
            for i in range(6):
                pattern.append(renpy.random.randint(0,12))
        if type == "hard":
            for i in range(10):
                pattern.append(renpy.random.randint(0,12))
        return pattern
    def set_difficulty(button):
        global current_difficulty
        if button == "right" and difficulties.index(current_difficulty) < len(difficulties)-1:
            current_difficulty = difficulties[difficulties.index(current_difficulty)+1]
        elif button == "left" and difficulties.index(current_difficulty) > 0 :
            current_difficulty = difficulties[difficulties.index(current_difficulty)-1]
        renpy.restart_interaction()
    def light_keys():
        global input_ready
        global correct_picks
        global current_button_index
        global c_lit
        global d_lit
        global e_lit
        global f_lit
        global g_lit
        global a_lit
        global b_lit
        global c1_lit
        global d1_lit
        global e1_lit
        global f1_lit
        global g1_lit
        global a1_lit

        if current_button_index < len(current_button_pattern):
            button_lit = buttons[current_button_pattern[current_button_index]]
            c_lit = False
            d_lit = False
            e_lit = False
            f_lit = False
            g_lit = False
            a_lit = False
            b_lit = False
            c1_lit = False
            d1_lit = False
            e1_lit = False
            f1_lit = False
            g1_lit = False
            a1_lit = False
            if button_lit == "c":
                c_lit = True
            elif button_lit == "d":
                d_lit = True
            elif button_lit == "e":
                e_lit = True
            elif button_lit == "f":
                f_lit = True 
            elif button_lit == "g":
                g_lit = True
            elif button_lit == "a":
                a_lit = True
            elif button_lit == "b":
                b_lit = True
            elif button_lit == "c1":
                c1_lit = True     
            elif button_lit == "d1":
                d1_lit = True
            elif button_lit == "e1":
                e1_lit = True
            elif button_lit == "f1":
                f1_lit = True
            elif button_lit == "g1":
                g1_lit = True
            elif button_lit == "a1":
                a1_lit = True

            if correct_picks == current_button_index:
                input_ready = True
                correct_picks = 0
            
            current_button_index +=1
            renpy.restart_interaction()

        else: 
            input_ready = True
            renpy.restart_interaction()
        
    def off_keys():
        global c_lit
        global d_lit
        global e_lit
        global f_lit
        global g_lit
        global a_lit
        global b_lit
        global c1_lit
        global d1_lit
        global e1_lit
        global f1_lit
        global g1_lit
        global a1_lit

        c_lit = False
        d_lit = False
        e_lit = False
        f_lit = False
        g_lit = False
        a_lit = False
        b_lit = False
        c1_lit = False
        d1_lit = False
        e1_lit = False
        f1_lit = False
        g1_lit = False
        a1_lit = False
        
    def check_user_input(button):
        global current_button_index
        global input_ready
        global correct_picks
        global user_picks
        global selected_button_index

        if buttons.index(button) == current_button_pattern[selected_button_index]:
            correct_picks +=1
            user_picks +=1
            if current_button_index == user_picks:
                selected_button_index = 0
                current_button_index = 0
                user_picks = 0
                input_ready = False
            else: 
                selected_button_index += 1
            renpy.restart_interaction()
        else:
            renpy.play("audio/piano_game_over.mp3")
            renpy.hide_screen("piano_keys")
            renpy.show_screen("game_over")
        if correct_picks == len(current_button_pattern):
            renpy.show_screen ("you_win")
            renpy.transition(Fade(1,0,1))
            renpy.play("audio/small-win.mp3")
            renpy.hide_screen("piano_keys")
            
    def reset_piano_keys():
        global current_button_index
        global selected_button_index
        global input_ready
        global correct_picks
        global user_picks
        global current_button_pattern

        global c_lit
        global d_lit
        global e_lit
        global f_lit
        global g_lit
        global a_lit
        global b_lit
        global c1_lit
        global d1_lit
        global e1_lit
        global f1_lit
        global g1_lit
        global a1_lit

        current_button_index = 0
        selected_button_index = 0
        correct_picks = 0
        user_picks = 0
        input_ready = False

        c_lit = False
        d_lit = False
        e_lit = False
        f_lit = False
        g_lit = False
        a_lit = False
        b_lit = False
        c1_lit = False
        d1_lit = False
        e1_lit = False
        f1_lit = False
        g1_lit = False
        a1_lit = False

        current_button_pattern = create_button_pattern(type=current_difficulty)
        renpy.restart_interaction()

    renpy.music.register_channel("myChannel", mixer="music", loop=False, stop_on_mute=False, tight=True, buffer_queue=True, movie=False, framedrop=True)

transform half_size1:
    zoom 0.5
screen game_over: 
    image "background.png" 
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            background None
            xysize (int(1548 / 2), int(941 / 2))
            align (0.5,0.5)
            image "UI/menu-background-game-over.png" at half_size1
            text "Darn! You got the wrong key...\nTry again." size 30 color "#FFFFFF" outlines [(absolute(2), "#000000", 0,0)]  align(0.5,0.45) text_align 0.5
            imagebutton idle "UI/try-again-button.png" action[Hide("game_over"), Show("piano_keys_menu")] anchor(0.5,0.5) align (0.3,0.8) at half_size1
            imagebutton idle "UI/quit-button.png"  action Return() anchor (0.5, 0.5) align (0.8, 0.8) at half_size1

screen you_win:
    image "you_win.png" 
    imagebutton idle "UI/quit-button.png" action Return() anchor (0.5, 0.5) align (0.5, 0.8) at half_size1

screen piano_keys:
    on "show" action Function(reset_piano_keys)
    image "background.png" 
    #Play(channel="myChannel", file= "audio/small-win.mp3")
    if c_lit:
        imagebutton idle "pianoKeys/g-key-lit.png" align(0.05, 0.9) 
    elif not c_lit:
        imagebutton auto "pianoKeys/g-key-%s.png" align(0.05, 0.9) action [SetVariable("c_lit",True), Function(check_user_input, button = "c"), Play(channel="myChannel", file= "audio/g2.mp3")] sensitive input_ready 
    
    if d_lit:
        imagebutton idle "pianoKeys/a-key-lit.png" align(0.125, 0.9) 
    elif not d_lit:
        imagebutton auto "pianoKeys/a-key-%s.png" align(0.125, 0.9) action [SetVariable("d_lit",True), Function(check_user_input, button = "d"), Play(channel="myChannel", file= "audio/a2.mp3")] sensitive input_ready 
    
    if e_lit:
        imagebutton idle "pianoKeys/b-key-lit.png" align(0.2, 0.9) 
    elif not e_lit:
        imagebutton auto "pianoKeys/b-key-%s.png" align(0.2, 0.9) action [SetVariable("e_lit",True), Function(check_user_input, button = "e"), Play(channel="myChannel", file= "audio/b2.mp3")] sensitive input_ready 

    if f_lit:
        imagebutton idle "pianoKeys/c-key-lit.png" align(0.275, 0.9) 
    elif not f_lit:
        imagebutton auto "pianoKeys/c-key-%s.png" align(0.275, 0.9) action [SetVariable("f_lit",True), Function(check_user_input, button = "f"), Play(channel="myChannel", file= "audio/c3.mp3")] sensitive input_ready 
    
    if g_lit:
        imagebutton idle "pianoKeys/d-key-lit.png" align(0.350, 0.9) 
    elif not g_lit:
        imagebutton auto "pianoKeys/d-key-%s.png" align(0.350, 0.9) action [SetVariable("g_lit",True), Function(check_user_input, button = "g"), Play(channel="myChannel", file= "audio/d3.mp3")] sensitive input_ready 

    if a_lit:
        imagebutton idle "pianoKeys/e-key-lit.png" align(0.425, 0.9) 
    elif not a_lit:
        imagebutton auto "pianoKeys/e-key-%s.png" align(0.425, 0.9) action [SetVariable("a_lit",True), Function(check_user_input, button = "a"), Play(channel="myChannel", file= "audio/e3.mp3")] sensitive input_ready 
    
    if b_lit:
        imagebutton idle "pianoKeys/f-key-lit.png" align(0.5, 0.9) 
    elif not b_lit:
        imagebutton auto "pianoKeys/f-key-%s.png" align (0.5, 0.9) action [SetVariable("b_lit",True), Function(check_user_input, button = "b"), Play(channel="myChannel", file= "audio/f3.mp3")] sensitive input_ready 
    if c1_lit:
        imagebutton idle "pianoKeys/g-key-lit.png" align(0.575, 0.9) 
    elif not c1_lit:
        imagebutton auto "pianoKeys/g-key-%s.png" align(0.575, 0.9) action [SetVariable("c1_lit",True), Function(check_user_input, button = "c1"), Play(channel="myChannel", file= "audio/g3.mp3")] sensitive input_ready 
    
    if d1_lit:
        imagebutton idle "pianoKeys/a-key-lit.png" align(0.650, 0.9) 
    elif not d1_lit:
        imagebutton auto "pianoKeys/a-key-%s.png" align(0.650, 0.9) action [SetVariable("d1_lit",True), Function(check_user_input, button = "d1"), Play(channel="myChannel", file= "audio/a3.mp3")] sensitive input_ready 
    
    if e1_lit:
        imagebutton idle "pianoKeys/b-key-lit.png" align(0.725, 0.9) 
    elif not e1_lit:
        imagebutton auto "pianoKeys/b-key-%s.png" align(0.725, 0.9) action [SetVariable("e1_lit",True), Function(check_user_input, button = "e1"), Play(channel="myChannel", file= "audio/b3.mp3")] sensitive input_ready 

    if f1_lit:
        imagebutton idle "pianoKeys/c-key-lit.png" align(0.8, 0.9) 
    elif not f1_lit:
        imagebutton auto "pianoKeys/c-key-%s.png" align(0.8, 0.9) action [SetVariable("f1_lit",True), Function(check_user_input, button = "f1"), Play(channel="myChannel", file= "audio/c4.mp3")] sensitive input_ready 
    
    if g1_lit:
        imagebutton idle "pianoKeys/d-key-lit.png" align(0.875, 0.9) 
    elif not g1_lit:
        imagebutton auto "pianoKeys/d-key-%s.png" align(0.875, 0.9) action [SetVariable("g1_lit",True), Function(check_user_input, button = "g1"), Play(channel="myChannel", file= "audio/d4.mp3")] sensitive input_ready 

    if a1_lit:
        imagebutton idle "pianoKeys/e-key-lit.png" align(0.95, 0.9) 
    elif not a1_lit:
        imagebutton auto "pianoKeys/e-key-%s.png" align(0.95, 0.9) action [SetVariable("a1_lit",True), Function(check_user_input, button = "a1"), Play(channel="myChannel", file= "audio/e4.mp3")] sensitive input_ready 
    #imagebutton idle "pianoKeys/c-key-idle.png" align(0.575, 0.9) 
    #imagebutton idle "pianoKeys/d-key-idle.png" align(0.650, 0.9) 
    #imagebutton idle "pianoKeys/e-key-idle.png" align(0.725, 0.9) 
    #imagebutton idle "pianoKeys/f-key-idle.png" align(0.8, 0.9) 
    #imagebutton idle "pianoKeys/g-key-idle.png" align(0.875, 0.9) 
    #imagebutton idle "pianoKeys/a-key-idle.png" align(0.950, 0.9) 
    
    if not input_ready:
        timer 1.0 action Function(light_keys) repeat True
    if c_lit or d_lit or e_lit or f_lit or g_lit or a_lit or b_lit or c1_lit or d1_lit or e1_lit or f1_lit or g1_lit or a1_lit:
        timer 0.5 action Function (off_keys) repeat True

screen piano_keys_menu:
    modal True
    image "background.png" 
    frame:
        background "#00000080" #80 for opaque
        xfill True          # to fill up entire screen
        yfill True          # to fill up entire screen
        frame:
            background Frame("UI/menu-background.png")
            xysize(int(1548/2),int(941/2))
            align(0.5,0.5) #center 
            text "Difficulty: [current_difficulty]" size 30 color "#ffffff"outlines[(absolute(2), "#000000", 0,0)]  align(0.5,0.45)
            imagebutton idle "UI/arrow-left.png" align (0.25,0.46) anchor (0.5,0.5) action Function(set_difficulty, button = "left") at half_size1
            imagebutton idle "UI/arrow-right.png" align (0.75,0.46) anchor (0.5,0.5) action Function(set_difficulty, button = "right") at half_size1
            imagebutton idle "UI/play-button.png" align (0.3, 0.8) anchor (0.5, 0.5) action[Hide("piano_keys_menu"), Show("piano_keys")] at half_size1
            imagebutton idle "UI/quit-button.png" align (0.8, 0.8) anchor (0.5, 0.5) action Return() at half_size1


#Abandoned house minigame
#drag-drop inventory

init python:
    def inventoryUpdate(st):
        if inventory_drag == True:
            for item in inventory_sprites:
                if item.type == item_dragged:
                    item.x = mousepos[0] - item.width / 2
                    item.y = mousepos[1] - item.height / 2
                    item.zorder = 99
            return 0
        return None

    def inventoryEvents(event, x, y, at):
        global mousepos
        global dialogue
        global inventory_drag
        global i_overlap
        global ie_overlap
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                for item1 in inventory_sprites:
                    if item1.visible == True:
                        if item1.x <= x <= item1.x + item1.width and item1.y <= y <= item1.y + item1.height:
                            inventory_drag = False
                            i_combine = False
                            ie_combine = False
                            for item2 in inventory_sprites:
                                items_overlap = checkItemsOverlap(item1, item2)
                                if items_overlap == True:
                                    i_overlap = True
                                    if (item1.type == "matches" or item1.type == "lantern") and (item2.type == "matches" or item2.type == "lantern"):
                                        i_combine = True
                                        if item1.type == "matches":
                                            removeInventoryItem(item1)
                                        else:
                                            removeInventoryItem(item2)

                                        lantern_image = Image("Inventory Items/inventory-lantern-lit.png")
                                        t = Transform(child = lantern_image, zoom = 0.75)
                                        inventory_sprites[inventory_items.index("lantern")].set_child(t)
                                        inventory_sprites[inventory_items.index("lantern")].item_image = lantern_image
                                        inventory_sprites[inventory_items.index("lantern")].state = "lit"
                                        renpy.show_screen("inspectItem", ["lantern"])
                                        characterSay(who = "Fuchi Kasane", what = ["The lantern is now lit!", "I can now read the books."], inspectItem = True)
                                        inventory_SM.redraw(0)
                                        renpy.restart_interaction()
                                        break
                                    else:
                                        item1.x = item1.original_x
                                        item1.y = item1.original_y
                                        item1.zorder = 0
                                        characterSay(who = "Fuchi Kasane", what = ["Hmm, that doesn't seem to work.", "Try something else."])
                                        break
                            if i_combine == False:
                                for item3 in environment_sprites:
                                    items_overlap = checkItemsOverlap(item1, item3)
                                    if items_overlap == True:
                                        ie_overlap = True
                                        if item1.type == "key" and item3.type == "box":
                                            ie_combine = True
                                            removeInventoryItem(item1)
                                            removeEnvironmentItem(item3)
                                            addToInventory(["matches", "lipstick","instruction"])
                                            renpy.show_screen("inspectItem", [ "matches", "lipstick", "instruction"])
                                            characterSay(who = "Fuchi Kasane", what = ["This is mother's lipstick.", "I finally have something to remind me of her.", "I can go home now.", "There is also a poem in the box.", "I wonder what does it mean."], inspectItem = True)
                                            inventory_SM.redraw(0)
                                            environment_SM.redraw(0)
                                            renpy.restart_interaction()
                                            break
                                    
                                        else:
                                            item1.x = item1.original_x
                                            item1.y = item1.original_y
                                            item1.zorder = 0
                                            characterSay(who = "Fuchi Kasane", what = ["Hmm, that doesn't seem to work.", "Try something else."])
                                            break
                            if i_combine == False and ie_combine == False:
                                item1.x = item1.original_x
                                item1.y = item1.original_y
                                item1.zorder = 0
        if event.type == renpy.pygame_sdl2.MOUSEMOTION:
            mousepos = (x, y)
            if inventory_drag == False:
                for item in inventory_sprites:
                    if item.visible == True:
                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                            renpy.show_screen("inventoryItemMenu", item = item)
                            renpy.restart_interaction()
                            break
                        else:
                            renpy.hide_screen("inventoryItemMenu")
                            renpy.restart_interaction()

    def environmentEvents(event, x, y, at):
        if event.type == renpy.pygame_sdl2.MOUSEMOTION:
            for item in environment_sprites:
                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                    t = Transform(child= item.hover_image, zoom = 1.0)
                    item.set_child(t)
                    environment_SM.redraw(0)
                    renpy.restart_interaction()
                    break
                else:
                    t = Transform(child= item.idle_image, zoom = 1.0)
                    item.set_child(t)
                    environment_SM.redraw(0)
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                for item in environment_sprites:
                    if i_overlap == False and ie_overlap == False:
                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                            if item.type == "key":
                                addToInventory(["key"])
                            elif item.type == "newspaper":
                                addToInventory(["newspaper"])
                            elif item.type == "lantern":
                                addToInventory(["lantern"])
                            elif item.type == "box":
                                characterSay(who = "Fuchi Kasane", what= ["Hmm, this box is locked. I think it needs a key."])
                            

                global i_overlap
                global ie_overlap
                i_overlap = False
                ie_overlap = False

    def startDrag(item):
        global inventory_drag
        global item_dragged
        inventory_drag = True
        item_dragged = item.type
        inventory_SM.redraw(0)

    def checkItemsOverlap(item1, item2):
        if abs((item1.x + item1.width / 2) - (item2.x + item2.width / 2)) * 2 < item1.width + item2.width and abs((item1.y + item1.height / 2) - (item2.y + item2.height / 2)) * 2 < item1.height + item2.height and item1.type != item2.type:
            return True
        else:
            return False

    def characterSay(who, what, inspectItem = False, jump_to = None):
        if isinstance(what, str):
            renpy.call_screen("characterSay", who = who, what = what, jump_to = jump_to) # pass on the jump_to parameter in case one chooses to jump to another scene after dialogue.
        elif isinstance(what, list):
            global dialogue
            dialogue = {"who" : who, "what" : what}
            if inspectItem == False:
                renpy.show_screen("characterSay", jump_to = jump_to) # pass on the jump_to parameter in case one chooses to jump to another scene after dialogue.
                renpy.restart_interaction()

    def repositionInventoryItems():
        global inventory_lb_enabled
        global inventory_rb_enabled

        for i, item in enumerate(inventory_sprites):
            if i == 0:
                item.x = inventory_first_slot_x
                item.original_x = item.x
            else:
                item.x = (inventory_first_slot_x + inventory_slot_size[0] * i) + (inventory_slot_padding * i)
                item.original_x = item.x
            if item.x < inventory_first_slot_x or item.x > (inventory_first_slot_x + (item.width * 7)) + (inventory_slot_padding * 5):
                setItemVisibility(item = item, visible = False)
            elif item != "":
                setItemVisibility(item = item, visible = True)

        if len(inventory_sprites) > 0:
            if inventory_sprites[-1].visible == True:
                inventory_rb_enabled = False
            else:
                inventory_rb_enabled = True
            if inventory_sprites[0].visible == True:
                inventory_lb_enabled = False
            else:
                inventory_lb_enabled = True

        renpy.retain_after_load()

    def addToInventory(items):
        for item in items:
            inventory_items.append(item)
            if item == "lantern":
                item_image = Image("Inventory Items/inventory-lantern-unlit.png")
            else:
                item_image = Image("Inventory Items/inventory-{}.png".format(item))

            t = Transform(child = item_image, zoom = 0.75)
            inventory_sprites.append(inventory_SM.create(t))
            inventory_sprites[-1].width = inventory_slot_size[0]
            inventory_sprites[-1].height = inventory_slot_size[1]
            inventory_sprites[-1].type = item
            inventory_sprites[-1].item_image = item_image
            inventory_sprites[-1].y = 912
            inventory_sprites[-1].original_y = 912
            inventory_sprites[-1].original_x = 0
            inventory_sprites[-1].visible = True

            if item == "lantern":
                inventory_sprites[-1].state = "unlit"
            else:
                inventory_sprites[-1].state = "default"

            for envitem in environment_sprites:
                if envitem.type == item:
                    removeEnvironmentItem(item= envitem)
                    break

            repositionInventoryItems()

            inventory_SM.redraw(0)
            environment_SM.redraw(0)
            renpy.restart_interaction()

    def removeEnvironmentItem(item):
        item.destroy()
        environment_items_deleted.append(item.type)
        environment_sprites.pop(environment_sprites.index(item))
        environment_items.pop(environment_items.index(item.type))

    def removeInventoryItem(item):
        item.destroy()
        inventory_sprites.pop(inventory_sprites.index(item))
        inventory_items.pop(inventory_items.index(item.type))
        repositionInventoryItems()

    def inventoryArrows(button):
        global inventory_lb_enabled
        global inventory_rb_enabled

        if len(inventory_sprites) > 7:
            citem = ""
            for i, item in enumerate(inventory_sprites):
                if button == "right" and inventory_rb_enabled == True:
                    if inventory_sprites[-1].visible == False:
                        item.x -= item.width + inventory_slot_padding
                        item.original_x = item.x
                        citem = item
                elif button == "left" and inventory_lb_enabled == True:
                    if inventory_sprites[0].visible == False:
                        reversed_index = (len(inventory_sprites) - 1) - i
                        inventory_sprites[reversed_index].x += item.width + inventory_slot_padding
                        inventory_sprites[reversed_index].original_x = inventory_sprites[reversed_index].x
                        citem = inventory_sprites[reversed_index]

                if citem != "" and (citem.x < inventory_first_slot_x or citem.x > (inventory_first_slot_x + (citem.width * 7)) + (inventory_slot_padding * 5)):
                    setItemVisibility(item = citem, visible = False)
                elif citem != "":
                    setItemVisibility(item = citem, visible = True)

            if inventory_sprites[-1].visible == True:
                inventory_rb_enabled = False
            else:
                inventory_rb_enabled = True
            if inventory_sprites[0].visible == True:
                inventory_lb_enabled = False
            else:
                inventory_lb_enabled = True

            if citem != "":
                inventory_SM.redraw(0)
                renpy.restart_interaction()

    def setItemVisibility(item, visible):
        if visible == False:
            item.visible = False
            t = Transform(child = item.item_image, zoom = 0.75, alpha = 0)
            item.set_child(t)
        else:
            item.visible = True
            t = Transform(child = item.item_image, zoom = 0.75, alpha = 100)
            item.set_child(t)
        inventory_SM.redraw(0)

    def prepareLoad():
        global dialogue
        global inventory_drag
        for item in inventory_sprites:
            if item_dragged == item.type:
                item.x = item.original_x
                item.y = item.original_y
                item.zorder = 0
        dialogue = {}
        inventory_drag = False
        renpy.hide_screen("characterSay")
        
screen UI:
    zorder 1
    image "UI/inventory-icon-bg.png" xpos 0 ypos 0.8 at threeoverfour
    imagebutton auto "UI/inventory-icon-%s.png" action If(renpy.get_screen("inventory") == None, true= Show("inventory"), false= Hide("inventory")) xpos 0.03 ypos 0.825 at threeoverfour

screen inventory:
    zorder 3
    image "UI/inventory-bg.png" xpos 0.17 ypos 0.8 at threeoverfour
    image "UI/inventory-slots.png" xpos 0.274 ypos 0.845 at threeoverfour
    imagebutton idle If(inventory_rb_enabled == True, true= "UI/inventory-arrow-right-enabled-idle.png", false= "UI/inventory-arrow-right-disabled.png") hover If(inventory_rb_enabled == True, true= "UI/inventory-arrow-right-enabled-hover.png", false= "UI/inventory-arrow-right-disabled.png") action Function(inventoryArrows, button = "right") xpos 0.921 ypos 0.86 at threeoverfour
    imagebutton idle If(inventory_lb_enabled == True, true= "UI/inventory-arrow-left-enabled-idle.png", false= "UI/inventory-arrow-left-disabled.png") hover If(inventory_lb_enabled == True, true= "UI/inventory-arrow-left-enabled-hover.png", false= "UI/inventory-arrow-left-disabled.png") action Function(inventoryArrows, button = "left") xpos 0.202 ypos 0.86 at threeoverfour

    add inventory_SM

screen inventoryItemMenu(item):
    zorder 7
    frame:
        xysize (inventory_slot_size[0], inventory_slot_size[1])
        background "#FFFFFF30"
        xpos int(item.x)
        ypos int(item.y)
        imagebutton auto "UI/view-inventory-item-%s.png" align (0.0, 0.5) at threeoverfour action [Show("inspectItem", items = [item.type]), Hide("inventoryItemMenu")]
        imagebutton auto "UI/use-inventory-item-%s.png" align (1.0, 0.5) at threeoverfour action [Function(startDrag, item = item), Hide("inventoryItemMenu")]

screen inspectItem(items):
    modal True
    zorder 4
    button:
        xfill True
        yfill True
        action If(len(items) > 1, true = RemoveFromSet(items, items[0]), false= [Hide("inspectItem"), If(len(dialogue) > 0, true= Show("characterSay"), false= NullAction())])
        image "Items Pop Up/items-pop-up-bg.png" align (0.5, 0.5) at threeoverfour

        python:
            item_name = ""
            item_desc = ""
            for name in inventory_item_names:
                temp_name = name.replace(" ", "-")
                if temp_name.lower() == items[0]:
                    item_name = name

        text "{}".format(item_name) size 40 align (0.5, 0.25) color "#000000"
        if items[0] == "lantern":
            $lantern_state = inventory_sprites[inventory_items.index("lantern")].state
            image "Items Pop Up/{}-{}-pop-up.png".format("lantern", lantern_state) align (0.5, 0.5) at threeoverfour
        else:
            image "Items Pop Up/{}-pop-up.png".format(items[0]) align (0.5, 0.5) at threeoverfour

screen characterSay(who = None, what = None, jump_to = None):
    modal True
    zorder 6
    style_prefix "say"

    window:
        id "window"
        window:
            padding (20, 20)
            id "namebox"
            style "namebox"
            if who is not None:
                text who id "who"
            else:
                text dialogue["who"]

        if what is not None:
            text what id "what" xpos 0.25 ypos 0.4 xanchor 0.0
        else:
            text dialogue["what"][0] xpos 0.25 ypos 0.4 xanchor 0.0

    button:
        xfill True
        yfill True
        if what is None:
            action If(len(dialogue["what"]) > 1, true= RemoveFromSet(dialogue["what"], dialogue["what"][0]), false= [Hide("characterSay"), SetVariable("dialogue", {}), If(jump_to is not None, true = Jump("{}".format(jump_to)), false = NullAction())])
        else:
            action [Return(True), If(jump_to is not None, true = Jump("{}".format(jump_to)), false = NullAction())]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen map_first_floor:
    add environment_SM
    imagebutton:
        xpos 54
        ypos 54
        idle "map/kitchen_idle.png"
        hover "map/kitchen_hover.png"
        action Jump("setupKitchen") 
    imagebutton:
        xpos 1230
        ypos 54
        idle "map/library_idle.png"
        hover "map/library_hover.png"
        action Jump("setupLibrary")

    imagebutton:
        xpos 705
        ypos 54
        idle "map/stair1_idle.png"
        hover "map/stair1_hover.png"
        action Jump("setupSecondFloor")

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/exit_%s.png"
        action If("lipstick" in inventory_items, true = [Hide("UI"), Hide("inventory"), Jump("start2")], false  = Jump("noExit")) 

label noExit:

    python: 
        characterSay(who = "Fuchi Kasane", what = ["I can't go yet.","I haven't found what I need."])
        renpy.jump("setupFirstFloor")

screen map_second_floor:
    add environment_SM
    imagebutton:
        xpos 705
        ypos 54
        idle "map/stair2_idle.png"
        hover "map/stair2_hover.png"
        action Jump("setupFirstFloor")
    imagebutton:
        xpos 54
        ypos 198
        idle "map/bathroom_idle.png"
        hover "map/bathroom_hover.png"
        action Jump("setupBathroom")

    imagebutton:
        xpos 54
        ypos 460
        idle "map/bedroom2_idle.png"
        hover "map/bedroom2_hover.png"
        action Jump("setupBedroom2")
        
    imagebutton:
        xpos 1230
        ypos 197
        idle "map/bedroom1_idle.png"
        hover "map/bedroom1_hover.png"
        action Jump("setupBedroom1")

screen kitchen:
    add environment_SM
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump("setupFirstFloor")
    #if a:
    imagebutton:
        xpos 355
        ypos 565
        idle "map/secret_lock_idle.png"
        hover "map/secret_lock_hover.png"
        action Jump("unlock") 
    

screen library:
    add environment_SM
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump("setupFirstFloor")
   
screen bathroom:
    add environment_SM
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump("setupSecondFloor")

screen bedroom1:
    add environment_SM
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump("setupSecondFloor")
    imagebutton:
        xpos 355
        ypos 565
        idle "map/secret_lock_idle.png"
        hover "map/secret_lock_hover.png"
        action Jump("unlock") 

label unlock:
    scene padlock
    # Close any active UI elements before asking for player input
    #$ renpy.ui.close()

    # Ask the player for input
    $password = ""
    python:
        password = renpy.input("This is a 4-number password. What is your guess?", length=4)
        password = password.strip()
    
        # Check the player's input
        if password == "1212":
            # Correct password, do something here
            renpy.jump ("setupSecretRoom")

        else:
            # Incorrect password, do something else here
            renpy.jump ("setupBedroom1")
            pass

screen secret_room:
    add environment_SM
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/back_%s.png"
        action Jump("setupBedroom1")
    imagebutton:
        xpos 1137
        ypos 238
        idle "map/miko_painting_idle.png"
        hover "map/miko_painting_hover.png"
        action [Jump ("mikoPainting"), Hide("characterSay")]
    imagebutton:
        xpos 1010
        ypos 690
        idle "map/book_idle.png"
        hover "map/book_hover.png"
        action [Jump ("book"), Hide("characterSay")]

label book:
    python:
        if "lantern" in inventory_items:
            if inventory_sprites[inventory_items.index("lantern")].state == "lit":
                characterSay(who = "Fuchi Kasane", what = ["This is an really old diary. It's about some kind of red minerals in a place called Akeiwa.", "There are so many hard words. I should put the book back."])
                renpy.jump("setupSecretRoom")
            else:
                characterSay(who = "Fuchi Kasane", what = ["It's too dark to read!"])
                renpy.jump("setupSecretRoom")
        else:
            characterSay(who = "Fuchi Kasane", what = ["It's too dark to read!"])
            renpy.jump("setupSecretRoom")
    
label mikoPainting:
    
    python: 
        characterSay(who = "Fuchi Kasane", what = ["This is an old painting of a miko dancing the Kagura dance.", "I wonder why it is here."])
        renpy.jump("setupSecretRoom")
       
screen bedroom2:
    add environment_SM
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump("setupSecondFloor")

label setupFirstFloor:
    $environment_items = []

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    scene map_first_floor
    call screen map_first_floor

label setupSecondFloor:
    $environment_items = []

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    scene map_second_floor
    call screen map_second_floor

label setupKitchen: 
    $environment_items = []

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    python:
        for item in environment_items:
            # Add items to environment, only if they haven't previously been deleted.
            if item not in environment_items_deleted:
                idle_image = Image("Environment Items/{}-idle.png".format(item))
                hover_image = Image("Environment Items/{}-hover.png".format(item))
                t = Transform(child= idle_image, zoom = 1.0)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

               

    scene kitchen 
    call screen kitchen
    

label setupLibrary:
    $environment_items = [ "key", "lantern", "newspaper"]

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    python:
        # Add items to environment, only if they haven't previously been deleted.
        for item in environment_items:
            if item not in environment_items_deleted:
                idle_image = Image("Environment Items/{}-idle.png".format(item))
                hover_image = Image("Environment Items/{}-hover.png".format(item))
                t = Transform(child= idle_image, zoom = 1.0)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

                if item == "newspaper":
                    environment_sprites[-1].width = 110
                    environment_sprites[-1].height = 81
                    environment_sprites[-1].x = 750
                    environment_sprites[-1].y = 770
                elif item == "key":
                    environment_sprites[-1].width = 101 *3/4
                    environment_sprites[-1].height = 55 *3/4
                    environment_sprites[-1].x = 1320
                    environment_sprites[-1].y = 1000
                elif item == "lantern":
                    environment_sprites[-1].width = 80 *3/4
                    environment_sprites[-1].height = 118 *3/4
                    environment_sprites[-1].x = 550
                    environment_sprites[-1].y = 750

    scene library
    call screen library

label setupBathroom:
    $environment_items = []

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    scene bathroom
    call screen bathroom

label setupBedroom1:
    $environment_items = []

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    scene bedroom1
    call screen bedroom1

label setupSecretRoom:
    $environment_items = ["box"]

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    python:
        # Add items to environment, only if they haven't previously been deleted.
        for item in environment_items:
            if item not in environment_items_deleted:
                idle_image = Image("Environment Items/{}-idle.png".format(item))
                hover_image = Image("Environment Items/{}-hover.png".format(item))
                t = Transform(child= idle_image, zoom = 1.0)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

                if item == "box":
                    environment_sprites[-1].width = 80
                    environment_sprites[-1].height = 53
                    environment_sprites[-1].x = 830
                    environment_sprites[-1].y = 470

    scene secret_room
    call screen secret_room

label setupBedroom2:
    $environment_items = []

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

    scene bedroom2
    call screen bedroom2

transform threeoverfour:
    zoom 0.75



# The game starts here.
label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    
    play music "audio/piano _sociopath.mp3" volume 0.6 fadein 1.0
    scene kasane 
    pause

##########################################################bedroom
    #scene bedroom with fade
   
    n "This is a story about Kasane.{p}A truly miserable girl, who has never felt like she deserve to live."
    n "A suffering soul trapped underneath the face of a hideous creature."
    n "And you will be watching this girl's journey, be the magical mirror to her Evil Queen."
    n "You will give advice as an outsider and guide her to the final 'happy ending'."
    n "Would she ever be able to find one though?"

##########################################################first chapter
    window hide
    show first_chapter with fade
    pause 
    

    scene playground with fade
    n "Once upon a time, there was a little girl, who was so ugly, people couldn't even look straight into her face without a grimace."
    n "People recoiled and avoided her whenever she comes close, as if she carries a contagious disease."
    n "Her name was Fuchi Kasane. She was daughter to the late legendary actress, Fuchi Sukeyo."

##########################################################bully
    scene bully with fade
    k "There were so many pretty children in my class."
    k "Even while they were bullying me, I couldn't help but wonder {p}'How does it feel like to look in the mirror everyday with such face ?'." 
    k "And the prettiest one of them, Nishizawa Ichika, always took great pleasure in torturing me."
    
    i "Hey, mind telling me again, who is your mother?"
    k "It's Sukeyo… {p}Fuchi Sukeyo…"
    o "AHAHAHA, you keep saying that!{p}You look nothing like her."
    o "*Sneeze* Oh, excuse me! I'm allergic to bullshit!"
    o "Her skin must be very thick to tell such lies."
    k "I didn't lie. My mother was really Fuchi Sukeyo. {p}But that doesn't really stop them from beating me."

##########################################################funeral    
    scene funeral with fade
    k "After all, my beautiful mother, who had made her name as a movie star, had long departed from this cruel world."

##########################################################park     
    scene park with fade
    k "Mama used to take me on long walks and tell me stuff I could never understand"
    k "But wherever she went, I would always happily follow her."
    show sukeyo_1 at right:
        zoom 1.0
    fs "Kasane, what do you want to be when you grow up?"
    show kasanewithmama at left:
        zoom 0.7
    k ""
    k "...An actress."
    fs ""
    fs "What if for some reason you were all alone {p}and it was really really hard for you to achieve your dream..."
    k "Mama?"
    fs "Take my red lipstick and..."

##########################################################kasane under the rain
    scene kasane_under_the_rain with fade
    k "I can't remember what mama said to me back then.{p}I really wish I do."
    k "Because at this time, I was having a really really really hard time."

##########################################################choice reject or accept role  
    scene shool hallway with fade
    "One day, during class..."
    pause 
    
    stop music fadeout 1.0


    play sound "<from 0.0 to 2.0>audio/school_bell.mp3" fadeout  1.5 volume 0.7
    scene classroom with fade 
    pause
    show teacher at right: 
        zoom 0.9
    play sound "audio/children_whispering.mp3" 
    t ""
    stop sound
    play sound "audio/clearingthroat.mp3"
    t "*clears her throat"
    stop sound
    t "Silent, children!"
    t "So we have all decided to play Cinderella for the art festival next month."
    t "Now we need to vote for the roles."
    t "Who want to take the lead role?"
    play sound "audio/children_whispering.mp3" volume 0.5
    t "Silence everyone! Who want the role can raise their hand!"
    show ichika_smiling at left:
        zoom 0.75
    i "Ma'am!"
    i "I think Kasane should take the lead role.{p}Her mother was a great actress, so the daughter must also be good at acting."
    s "*giggling{p}Me too.{p}I wanna see her acting too."
    s "I wonder what kind of acting skill could make up for that look."
    stop sound
    t "What do you think, Kasane?"
    hide ichika_smiling
    show kasane_original at left:
        zoom 0.75
    k "What should I do?"


    menu:
        "No, you will only humiliate yourself.":
            call rejecting from _call_rejecting
        "Yes, this is a chance to prove yourself.":
            call accepting from _call_accepting
    
##########################################################school_music_room
    scene school_music_room with fade
    show kasane_original:
        xalign 0.5
        yalign 1.0
        zoom 0.75
    k "I knew Ichika did this only to humiliate me on stage, but ever since I got the lead role, I started feeling a little bit excited. "
    k "Truth be told, I have always loved acting, just like mother."
    show kasane_original_eyeclosed :
        xalign 0.5
        yalign 1.0
        zoom 0.75
    k "Maybe if I perform well enough, even when I look nothing like her, people will start saying: ”She does take after Fuchi Sukeyo!!”"
    hide kasane_original_eyeclosed
    k "With that thought in mind, I went to the music room and trained by myself every day until my throat went hoarse."
    
##########################################################piano mini game    
    scene minigame_background with fade 
    "Up next, you will be helping Kasane with her voice training for the art festival."
    "Hit the correct pattern of keys to win the game."

    $button_pattern_easy = create_button_pattern("easy")
    $button_pattern_hard = create_button_pattern("hard")
    $button_pattern_medium = create_button_pattern("medium")
    $current_button_pattern = button_pattern_easy #initial value
    $difficulties = ["easy","medium","hard"]
    $current_difficulty = "easy" #initial value
    $c_lit = False
    $d_lit = False
    $e_lit = False
    $f_lit = False
    $g_lit = False
    $a_lit = False
    $b_lit = False
    $c1_lit = False
    $d1_lit = False
    $e1_lit = False
    $f1_lit = False
    $g1_lit = False
    $a1_lit = False
    
    $buttons = ("c", "d", "e", "f","g", "a", "b","c1", "d1", "e1", "f1", "g1", "a1")
    $current_button_index = 0
    $input_ready = False  #user can start pressing buttons or not
    $correct_picks = 0
    $user_picks = 0
    $selected_button_index = 0

    call screen piano_keys_menu
    hide screen you_win
    hide screen game_over

##########################################################going home

    scene dark_street with fade
    show kasane_original:
        xalign 0.5
        yalign 1.0
        zoom 0.75
    k "I had been training by myself until late evening for a whole week."
    show kasane_original_eyeclosed :
        xalign 0.5
        yalign 1.0
        zoom 0.75
    k "My aunt, who adopted me after mother's death, never came pick me up, so I always walked home alone."
    hide kasane_original_eyeclosed
    k "I suddenly felt like visiting my old home. {p}After all, her house never makes me feel like home."

    scene abandoned_house with fade
    pause
    show kasane_original :
        xalign 0.5
        yalign 1.0
        zoom 0.75
    k "It only takes a 15-minute detour to go there."
    k "The house we lived in used to be a beautiful 2-story house in the suburb of the town, but now it look like a mess."
    k "The lock is long broken.{p}There is nothing valuable left to take anyway."
    hide kasane_original
    n "Up next, you will be exploring where Kasane grew up before her mother's early demise."
    n "Be careful, you won't get out until you find what need to be found."

    #call screen map_first_floor
    
##########################################################abandoned house mini game
    
    
    $config.after_load_callbacks = [prepareLoad]
    $config.rollback_enabled = False
    $quick_menu = False
    $environment_SM = SpriteManager(event = environmentEvents)
    $inventory_SM = SpriteManager(update= inventoryUpdate, event= inventoryEvents)
    $environment_sprites = []
    $inventory_sprites = []
    $environment_items = []
    $inventory_items = []
    $environment_item_names = []
    $inventory_item_names = {"Key", "Lantern", "Matches", "Newspaper", "Lipstick", "Instruction"} # Add kitchen inventory item names.
    $environment_items_deleted = []
    $current_scene = "map_first_floor"
    $inventory_rb_enabled = False
    $inventory_lb_enabled = False
    $inventory_slot_size = (int(215 *3/4), int(196 *3/4))
    $inventory_slot_padding = 22 *3/4
    $inventory_first_slot_x = 525
    $dialogue = {}
    $inventory_drag = False
    $item_dragged = ""
    $mousepos = (0.0, 0.0)
    $i_overlap = False
    $ie_overlap = False




    play music "audio/Heartbreaking.mp3" volume 0.7 fadein 1.0
    show screen UI
    jump setupFirstFloor

    
    # call screen map_first_floor
    #hide screen map_first_floor
    #hide screen map_second_floor
    #hide screen kitchen
    #hide screen library
    #hide screen bathroom
    #hide screen bedroom1
    #hide screen bedroom2

    return


label rejecting:
    show kasane_original_sad at left:
        zoom 0.75
    k "No teacher, I can't play Cinderella. {p}I don't want to stand in front of so many people."
    show teacher at right: 
        zoom 0.9
    t "Okay, just tell me if you change your mind."

    scene after_class with fade
    "Ichika and her friends had been waiting for me on my way home."
    show ichika_angry at right:
        zoom 0.75
    i "Hey, what did you think you were doing?"
    show kasane_original_sad at left:
        zoom 0.75
    k "What do you mean? I was only..."
    
    play sound "<from 0.0 to 2.5>audio/body-punching.mp3" fadeout  1.5 volume 0.7
   
    
    scene beating with fade
    
    
    i "Don’t you dare talk back to Ichika. {p}You made Ichika look like a bad person in front of the teacher."
    i "Now go back to the teacher and tell her you want to play Cinderella!!"

    scene classroom after school with fade
    play sound "audio/door_knocking_softly.mp3"
    k ""
    stop sound
  
    k "H-hello, is anyone there?"
    show teacher at right: 
        zoom 0.9
    t "Yes. Please come in."

    play sound "audio/sliding-door.mp3" volume 1.0
    k ""
    stop sound
  
    show teacher_speaking_upset at right: 
        zoom 0.9
    show kasane_original_sad_bruised_dirt at left: 
        zoom 0.75
    t "Kasane, what's the matter?"
    t "You got a bruise on your cheek!!"
    k "N-no. It's nothing, really.{p}I just trip and fell on my way here."
    hide teacher_speaking_upset
    show teacher_speaking at right:
        zoom 0.9
    t "What make you so hurried to come and tell me?"
    k "I just need to tell you... that if no one want to have the role,{p}I can play Cinderella..."
    hide teacher_speaking
    show teacher at right:
        zoom 0.9
    t "That's great new, Kasane. I am so glad that you finally want to participate class activities."
    hide teacher
    show teacher_speaking at right:
        zoom 0.9
    t "You have always been so quiet in class.{p}Kasane, are you crying?"
    show kasane_original_sad_bruised_eyeclosed_crying_dirt at left: 
        zoom 0.75
    k "It's just...{p}I am happy I can be Cinderella."
    t "It's okay to be nervous, Kasane. Let's do our best this time, shall we?"
    k "Yes, teacher."

    return

label accepting:
    "I knew I was being put on the spot to be humiliated on stage.{p}Yet a strange pride came over me and I couldn't bring myself to say no."
    k "Yes, teacher. I will play Cinderella if that’s what everyone wants.{p}Please let me do it."
    t "Then that’s settled."
    return

label start2:
    stop music fadeout 0.5
    
    $config.rollback_enabled = True
    $quick_menu = True
    scene abandoned_house_night with fade
    show kasane_original_dark:
        xalign 0.5
        yalign 1.0
        zoom 0.75
    k "It's getting dark. I should go back soon."
    k "I wonder if there is anything left at home for me to eat."
    play music "audio/mysterious_2.mp3" volume 0.7
    scene school_fair with fade 
    k "The big day has finally come."
    k "The school is crowded with eager little boys and girls, with their proud parents."
    k "I don't know if it's a good thing or not that my aunt doesn't come. {p}I cant helped but feel fear and shame as people walked by pointing at me, whispering."
    
    scene auditorium with fade
    k "The auditorium is lavishly decorated by the PA of the class. {p}They must really dote on their children to spend so much time and money just for an elementary school play"
    k "The clothes and the props are so fancy, they look like real deal."

    k "The glare of the lights, the size of the stage.{p}Everything makes me feel nervous and stiffen up."

    show ichika_smiling_angry at right: 
        zoom 0.75

    i "You even got that ugly makeup on, Kasane. Are you that excited to be in the play?"
    show kasane_the_play at left:
        zoom 0.75
    k "..."
    hide ichika_smiling_angry
    show ichika_speaking_angry at right: 
        zoom 0.75
    i "What you think you are doing? {p}GO!! It's your turn."
    o "That's right.{p}Get out there already!"
    "I have trained days and nights for this very moment, but right now I don't feel my leg. I can't even speak back a word."

    i "Seems like somebody need a little motivation, right everyone?"
    hide ichika_speaking_angry
    hide kasane_the_play

    play sound "audio/falling-down.mp3" volume 0.4
    "*Kasane being kicked and fell out of the back stage in front of the audience."
    stop sound

    scene kasane_on_stage with fade
    a "*whispering{p}What's that?{p}There's no way that's the lead role!"
    a "That red lipstick on her is hideous. She looks more of the step mother than Cinderella."
    "I told myself to calm down. {p}This is mother's world. She is watching me."
    "Right now, I am not Kasane. {p}I am ..."
    
    scene twoEvilSisters with fade 
    s1 "Oh, there you are, Cinderella. {p}We are going to the castle for the ball now."
    s2 "You stay home and clean the house."
    k "B-but, I have already done my all chores.{p}I want to go to the ball too"
    s1 "Then we can just create more chores for you to do."

    play sound "<from 0.0 to 6.0>audio/many-stuff-falling.mp3" 
    k "No, sisters. Please don't..."
    s1 "Now you can't complain about not having have enough chores!"
    stop sound
    s2 "Be sure to do your duty and clean up nicely. {p}We want the house to be squeaky clean by the time we come back, got it?"
    b "HAHAHAHA"
    scene the_wish with fade
    "My hands still tremble, but I can finally say my lines."
    k " "
    k "An elegant dress... {p}A delicious feast ...{p}A glittering chandelier ..."
    k "Just once, I would like to be able to see it for myself and get away from this place."
    k "But the only one who can hear my voice is the moon."

    "Gazing up at the roof of the auditorium, I send my wish to the imaginary moon."
    "My voice echoing throughout the entire space."
    play sound "audio/crowd-murmuring-adult.mp3" volume 0.5
    a "She is better than I thought.{p}Of course she can act. Her mother was an actress."
    stop sound

    "Even when they don't like me, just that much was enough to make me feel like my effort didn't go to waste."
    "I was finally recognized, was seen, not just as the ugly Kasane but the actress Kasane."
    k "Oh, my dear moon. Just this once, please grant me my wish and make my dream come true."

    scene blackout with fade
    stop music
    play sound "audio/light-turned-on.mp3"
    "Suddenly, the light went out. Someone covers my mouth from behind and point something sharp to my back."
    l "Attention, everyone. We'll take a short break to assist a student who suddenly came down ill.{p}The play will continue in 10 minutes."
    stop sound
    scene ichika_threat with fade
    "And then I hear Ichika's voice"
    i "Shh-, don't move."
    k "UMHHHPH-"
    i "Do as I say, else I will strip you naked with this knife and turn on the lighting"

    play music "audio/mysterious.mp3" volume 0.7
    scene backstage with fade
    show teacher_speaking_upset at right:
        zoom 0.9
    t2 "Are you guys okay?{p}Who is it that came down sick?"
    show ichika_smiling_speaking at left:
        zoom 0.75
    i "Ma'am. It's Kasane. She suddenly gets dizzy and her hands keep trembling."
    hide teacher_speaking_upset
    show teacher_speaking at right:
        zoom 0.9
    t2 "Is it true, Kasane?"
    k "*mumbling"
    i "Teacher is asking you. You gotta speak louder, Kasane."
    k "Y-yes, teacher."
    hide ichika_smiling_speaking
    show ichika_smiling at left:
        zoom 0.75
    i "Ma'am. {p}I will be walking her to the nurse's office and change into her costume to continue the play."
    i "I know all the lines!"
    t2 "What a good girl you are, Ichika. "
    t2 "Kasane, you go get some rest and feel better. {p}Don’t worry too much, Ichika will be covering for you."
    k "Yes, teacher."

    scene mirror_at_stair_turn with fade
    "Silent and despondent, I walked with a heavy heart to the nurse's office, knowing full well that no one would believe me if I ever spoke up about what Ichika had done. "
    "It was futile, no matter how heinous her actions or how loud my voice, her pretty facade would always conceal her sins"
    "I envy her.{p}Even when all she got is her face."

    show ichika_speaking_angry at right:
        zoom 0.75
    i "Hey, walk faster. I got a role to play, you know that."
    show kasane_the_play at left:
        zoom 0.75
    k "..."
    show kasane_the_play_eyeclosed at left:
        zoom 0.75
    "If only I had her face..."
    i "What are you scowling at?{p}START WALKING, you wretch!!!"
    show kasane_the_play_angry at left:
        zoom 0.75
    "I can't take it anymore. {p}I want that face!"
    hide ichika_speaking_angry
    hide kasane_the_play_angry
    hide kasane_the_play
    hide kasane_the_play_eyeclosed
    "Chase the yearnings of your heart alive-"

    scene the_kiss with fade
    "A passionate kiss to seal the deal-"
    i "What do you think you are-{p}MMMPHH---"

    scene new_face with fade
    "And your dream shall materialize and reveal."
    pause
    i "KYAHHHHH-"
    i "WHY DOES MY FACE LOOK LIKE THI-"
    k "Shut up, or I will cut you."
    i "*sobbing{p}M-My face. Gimme back my face..."

    scene backstage with fade
    "I told Ichika to wait for me in the bathroom of the abandoned building and went back to the play."
    "It seems like we has exchanged our face."
    "This must be magic. {p}My face looked exactly like Ichika’s, I even sounded like her."
    "No one would ever suspect a thing."
    show teacher at right: 
        zoom 0.9
    t2 "Here you are, Ichika.{p}Let's get dressed for the next scene."
    show kasane_transform_the_play at left:
        zoom 0.7
    k "Yes, ma'am."
    hide teacher
    hide kasane_transform_the_play
    scene the_bright_stage with fade 
    pause
    "I went back to the light of the stage, where I belonged."
    "A new dress given by the fairy godmother, and a new face from my own mother."
    "The world is suddenly filled with more vibrant colours."
    "There was no look of contempt nor pity, only the admiration."
    "The ugly, bitter, and foolish Kasane, there was no trace of her left in me."
    "So mother has always felt this way… {p}This difference..."

    scene the_ball with fade 
    "The fairy tale has reached its finale."
    "The beautiful princess will live happily ever after with the prince."
    "However, it is time for me to return to the real world."
    "Because my magical journey, like Cinderella's, must come to an end."
    "I will have to return this face to Ichika, who is waiting for me in the dark of the old building, even when I don't know how to."
    "After all, I didn't expect this to work."


    n "Do you think Kasane should return the face to Ichika?"
    menu:
        "Yes, Kasane shouldn't steal another's identity.":
            call return_the_face from _call_return_the_face
        "No, Ichika deserves that.":
            call do_not_return_the_face from _call_do_not_return_the_face


    return

    label return_the_face:
        stop music  
        play music "audio/abandoned_house.mp3" volume 0.4 fadein 1.0
        scene school_hallway_night with fade
        "As a precaution in case she try to attack me, I keep a knife in my pocket."

        
        show ichika_transform_blindfolded at right:
            zoom 0.8
        i "Hey…"
        i "Where are you taking me?{p}Why am I blindfolded?"
        show kasane_transform at left:
            zoom 0.7
        k "…"
        i "Please say something. Is it already dark out?{p}Mama will be worried about me…"
        hide kasane_transform
        hide ichika_transform_blindfolded
        stop music
        play music "audio/wind.mp3" fadein 1.0
        scene the_rooftop with fade
        show kasane_transform at left:
            zoom 0.7
        k "Sit down next to me and have a chat, shall we?"
        show ichika_transform at right:
            zoom 0.8
        i "…"
        show kasane_transform_talking at left:
            zoom 0.7
        k "Now do you understand how hard it’s for me to live with that face?"
        k "It’s beautiful... the world I see through your eyes."
        show kasane_transform_eyeclosed at left:
            zoom 0.7
        k "It is so very different."
        hide kasane_transform_eyeclosed
        hide kasane_transform_talking
        i "Uhm…"

        show ichika_transform_eyeclosed at right:
            zoom 0.8
        i "I am very sorry.{p}For everything…"
        i "I have also thought about what you have gone through."
        hide ichika_transform_eyeclosed

        i "I won't bully you anymore from now on…"
        k "I just wish I can live in peace, you know."
        i "Then let's be friend.{p}Let me make it up to you."
        k "Really?"
        i "Yes."
        show kasane_transform_talking_smiling at left:
            zoom 0.7
        k "Could we really be fr-"
        hide kasane_transform_talking_smiling 
        hide ichika_transform
        

        show ichika_transform_pointing_knife at right:
            zoom 0.8
        "Ichika suddenly grap the knife and point it at my face."
        i "CUT THE CRAP ALREADY!{p}I am sick of this! {p}Change us back, NOW!"
        show kasane_transform_eyeclosed at left:
            zoom 0.7
        "I should have known better."
        "Ichika would never change."
        "And I would forever be envious of her beauty."
        hide kasane_transform_eyeclosed
        hide kasane_transform
        hide ichika_transform_pointing_knife     
        hide ichika_transform

        scene scar with fade
        i "Wha- Are you crazy!!?"
        k "If you’re gonna use that knife on me, {p}your mouth might also be sliced open when we switch back."
        i "I- IT WILL!?"
        k "Who knows?"
        i "What do you mean? {p}STOP BITING IT THEN!!"
        k "*bites harder"
        i "I TOLD YOU TO STOPP-"
        play sound "audio/falling-down.mp3" volume 0.4

        scene black with fade 
        "Ichika lost balance, slipped and fell to the ground."
        stop sound
        "I sat there in shock and mouth sliced in half."
        "I look at the other me, laid dead on the ground, motionless."
        "I wonder if her death means I would finally be free from the ugly curse."
        "I must leave right now."
        stop music
        play music "audio/last-and-first-light.mp3" volume 0.4 fadein 1.0
        scene remorse_scar with fade 
        pause
        "The next day, my face returns. {p}And this time, even uglier with a big wound on my right cheek."
        "My first thought was I should commit suicide.{p}There was no reason left to live."
        "A creature like me, horrible on both inside and outside, shouldn’t exist to begin with."
        k "If only I do look like a normal person…"
        k "If only I were not this hideous…"
        k "I wouldn’t have ended up like this."

        scene mother_illusion_scar with fade 
        
        "All of a sudden, I caught sight of my deceased mother. "
        "I couldn't believe it, this had to be a trick of the mind. "
        "She looked even more stunning than my memories of her."
        k "Mother, I didn’t want to kill Nishizawa…{p}I am just…"
        fs "There’s no need to explain.{p}You did what you have to do, so you can get rid of your face."
        k "Since you were gone, nobody has ever loved me, mother…"
        fs "Exactly. And no one ever will if you die here. "
        fs "That’s why you need to take it from them. {p}Their face, their identity, their love."
        pause

        scene credit with fade
        pause
        return

    label do_not_return_the_face:
        "I don't want to go back.{p}I don't want to think of that ugly self of me waiting in the bathroom stall."
        "But what will I do if I return to normal?"
        "I don't know when will that happen, but I wanted this magic to last, just a little longer."
        "And a lonely night in the bathroom stall should teach a bully like Ichika a lesson."
        
        scene good_night with fade 
        "I secretly sneaked out of the crowd to avoid Ichika’s parents and went home."
        "That night I barely slept. I kept looking at the new me in the mirror in awe. "
        "I was so happy I couldn't stop smiling."
        "Finally, I fall asleep soundly, without dreaming."
        scene black with fade 
        "The next thing I knew, I woke up and was already back to my ugly self."

        scene after_class with fade
        
        "I rushed to the school to find Ichika."

        show teacher_speaking_upset at right:
            zoom 0.9
        t2 "What are you doing here, Kasane?{p}Please get back home, the school is shut down for today."
        show kasane_original_sad at left:
            zoom 0.75
        k "Teacher, I can't. I have to find…"
        hide teacher_speaking_upset
        hide kasane_original_sad

        stop music
        play music "<from 3.0>audio/last-and-first-light.mp3" volume 0.4 fadein 1.0
        scene ichika_laying_on_ground_morning with fade 
        "Ichika, laying on the grass next to the abandoned building."
        "She is motionless and lifeless, surrounded by some policemen and her crying parents."
        "She lays there, with blood splattering everywhere.{p}And yet she is still so beautiful."
        "She couldn’t handle being me for one night, so she killed herself."
        "Or was it I who killed her?"

        scene remorse with fade 
        pause
        "The next day, my first thought was I should commit suicide.{p}There was no reason left to live."
        "A creature like me, horrible on both inside and outside, shouldn’t exist to begin with."
        k "If only I do look like a normal person…"
        k "If only I were not this hideous…"
        k "I wouldn’t have ended up like this."

        scene mother_illusion with fade
        
        "All of a sudden, I caught sight of my deceased mother. "
        "I couldn't believe it, this had to be a trick of the mind. "
        "She looked even more stunning than my memories of her."
        k "Mother, I didn’t want to kill Nishizawa…{p}I am just…"
        fs "There’s no need to explain.{p}You did what you have to do, so you can get rid of your face."
        k "Since you were gone, nobody has ever loved me, mother…"
        fs "Exactly. And no one ever will if you die here. "
        fs "That’s why you need to take it from them. {p}Their face, their identity, their love."
        pause

        scene credit with fade
        pause
        return

# This ends the game.
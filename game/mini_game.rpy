screen fifteen_scr:
    

    if timer_on:
        timer 1.0 action If(fifteen_timer > 0, [SetVariable("fifteen_timer", fifteen_timer-1), Return("smth")], Return("time_is_up") ) repeat True
        text str(fifteen_timer) xalign 0.1 yalign 0.1
    

    frame:
        xalign 0.5 yalign 0.5
        background Solid("#ccc") 

        grid grid_width grid_height spacing 0:
            for every_tile in tiles_list:
                if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                    null

                else:
                    button:

                        left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                        left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                        add LiveCrop( ( (every_tile["tile_value"]-1)%grid_width*tile_width,
                                        (every_tile["tile_value"]-1)//grid_width*tile_height,
                                        tile_width,
                                        tile_height),
                                        chosen_img)
                            
                        
                        action [ 
                                If (every_tile["tile_number"] not in top_row,
                                    true = If (tiles_list[every_tile["tile_number"]-grid_width]["tile_value"] == empty_tile_value,
                                    true = [SetDict( tiles_list[every_tile["tile_number"]-grid_width], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                    false = None),
                                    false = None),
                                If (every_tile["tile_number"] not in bottom_row,
                                    true = If (tiles_list[min(len(tiles_list)-1, every_tile["tile_number"]+grid_width)]["tile_value"] == empty_tile_value,
                                    true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+grid_width))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                    false = None),
                                    false = None),
                                If (every_tile["tile_number"] not in left_column,
                                    true = If (tiles_list[every_tile["tile_number"]-1]["tile_value"] == empty_tile_value,
                                    true = [SetDict( tiles_list[every_tile["tile_number"]-1], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                    false = None),
                                    false = None),
                                If (every_tile["tile_number"] not in right_column,
                                    true = If (tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))]["tile_value"] == empty_tile_value,
                                    true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                    false = None),
                                    false = None), Return("smth")
                            ]
    
    textbutton "{color=#ffffff}Выйти из мини-игры" action Jump("quit_fifteen_game") xalign 0.9 yalign 0.1
    
    textbutton "{color=#ffffff}Показать/скрыть картинку" action If( renpy.get_screen("full_image"), Hide("full_image"), Show("full_image") ) xalign 0.5 yalign 0.1


screen full_image:
    add chosen_img xalign 0.5 yalign 0.5 at pic_trans


transform pic_trans:
    alpha 0.0 zoom 0.7
    on show:
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 0.6 zoom 1.2
            linear 0.4 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0



label fifteen_game:

    $ grid_width = 3
    $ grid_height = 3
    
    $ chosen_img = "600 на 600.png"
    $ chosen_img_width, chosen_img_height = renpy.image_size(chosen_img)
    $ tile_width = int(chosen_img_width/grid_width)
    $ tile_height = int(chosen_img_height/grid_height)


    $ top_row = []
    python:
        for i in range(0, grid_width):
            top_row.append (i)
    $ bottom_row = []
    python:
        for i in range(0, grid_width):
            bottom_row.append ( (grid_width*(grid_height-1)+i) )
    $ left_column = []
    python:
        for i in range(0, grid_height):
            left_column.append (grid_width*i)
    $ right_column = []
    python:
        for i in range(0, grid_height):
            right_column.append (grid_width*(i+1)-1)

    $ tiles_list = []
    python:
        for i in range (0, grid_height):
            for j in range (0, grid_width):
                tiles_list.append ( {"tile_number":(i*grid_width+j), "tile_value":(i*grid_width+(j+1))} )

    $ empty_tile_value = grid_width*grid_height

    $ fifteen_is_solved = False
    $ fifteen_timer = 300
    $ timer_on = False
    
    show screen fifteen_scr
    

    $ shuffle_moves = 21
    label tiles_shuffle:
        if shuffle_moves >0:
            python:
                possible_moves_list = []
                for j in tiles_list:
                    if j["tile_value"] == empty_tile_value:
                        if j["tile_number"] not in top_row:
                            possible_moves_list.append ("top")
                        if j["tile_number"] not in bottom_row:
                            possible_moves_list.append ("bottom")
                        if j["tile_number"] not in left_column:
                            possible_moves_list.append ("left")
                        if j["tile_number"] not in right_column:
                            possible_moves_list.append ("right")
                        move_tile = renpy.random.choice (possible_moves_list)
                        if move_tile == "top":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-grid_width]["tile_value"]
                            tiles_list[j["tile_number"]-grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "bottom":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+grid_width]["tile_value"]
                            tiles_list[j["tile_number"]+grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "left":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-1]["tile_value"]
                            tiles_list[j["tile_number"]-1]["tile_value"] = empty_tile_value
                        elif move_tile == "right":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+1]["tile_value"]
                            tiles_list[j["tile_number"]+1]["tile_value"] = empty_tile_value
                        shuffle_moves -= 1
                        #renpy.pause(0.1)
                        renpy.jump("tiles_shuffle")
                

    $ timer_on = True
    
    label fifteen_game_loop:
        $ result = ui.interact()
        $ fifteen_timer = fifteen_timer
        if result == "time_is_up":
            jump fifteen_lose
        python:
            for j in tiles_list:
                if j["tile_value"]-1 != j["tile_number"]: # will continue the game if at least one tile is not in its place
                    renpy.jump("fifteen_game_loop")
        jump fifteen_win

label fifteen_win:
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
    
    $ fifteen_is_solved = True
    
    "Вы выйграли!"
    hide screen fifteen_scr
    if help_agree == False:
        jump disagree_cont
    else:
        jump agree_cont

label fifteen_lose:
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
    "У вас не получилось."
    hide screen fifteen_scr
    if help_agree == False:
        jump disagree_cont
    else:
        jump agree_cont

label quit_fifteen_game:
    hide screen fifteen_scr
    "Пока что достаточно..."
    if help_agree == False:
        jump disagree_cont
    else:
        jump agree_cont
    
label act_4:
    show ins_nxt_w
    with fade
    pause
    hide ins_nxt_w
    show ins
    show gg
    ma "Уже прошла целая неделя моей учебы здесь. И не было ни одного дня, когда я скучала."
    ma "Каждый день происходят интересные события. Я рада, что выбрала учёбу именно в Институте радиоэлектроники и информационных технологий."
    hide ins
    hide gg

    show hall
    with fade
    show fr at left
    show gg_h at right
    v "Алиса, привет, срочно бежим в штаб!"
    a "Что случилось?"
    hide fr
    show fr_a
    v "Нет времени рассказывать, там всё и узнаешь."
    a "Хорошо. Бежим."
    hide fr_a
    hide gg_h
    hide hall

    show bs
    with fade
    show gl
    show fr at left
    show gg_h at right
    g "Наконец-то вы пришли. У нас большие неприятности. "
    a "Что? Что произошло?"
    g "Кто-то взломал систему базы данных нашего университета, никакие сайты не работают, нужно срочно наладить работу!"
    hide gg_h
    show gg_a at right
    a "Нужно немедленно что-то предпринять."
    g "Я собрал всю нашу команду ЛВТ. Они уже начали поиск утечки данных."
    g "Но нам нужна помощь, так что присоединяйтесь скорее. Вот ваши места."
    hide bs
    hide fr
    hide gg_a
    hide gl
    hide comp
    # (фон штаб// места)
    show comp
    with fade
    show fr_a at left
    show gg at right
    a "Ну что, приступим."
    v "Пора действовать."
    
    hide fr_a
    hide gg
    hide comp
    show sh_20_min
    with fade
    pause
    hide sh_20_min
    show comp
    show fr_a at left
    show gg_a at right

    a "Кто мог взломать? И главное зачем это сделали?"
    v "Ну понятное дело кто - конкуренты."
    v "Для того, чтобы нарушить работу университета."
    a "Что же теперь придётся делать?"
    v "Видимо нам придётся \"взломать\" самих взломщиков."
    hide fr_a
    hide gg_a
    hide comp
    if authority == 2:
        jump best_end
    elif authority == 1:
        jump neutral_end
    elif authority == 0:
        jump bad_end
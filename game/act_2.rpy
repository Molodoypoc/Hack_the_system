label act_2:
    play movie "september_inst.ogv"
    
    show ins
    with fade
    show gg
    ma "Даже не верится, что я всё-таки смогла поступить!"
    ma "Интересно, какого это учиться здесь? Надеюсь, будет интересно."
    hide ins
    
    show ak
    with fade
    # (фон институт// актовый зал)
    show pr
    if count == 1:
        p "Добрый день, ребята, Меня зовут Владислав Максимович, приветствую вас в Институте радиоэлектроники и информационных технологий!"
    elif count == 0:
        "Добрый день, ребята, Меня зовут Владислав Максимович, приветствую вас в Институте радиоэлектроники и информационных технологий!"
    p "С сегодняшнего дня вы начнёте свою учёбу в нашем инситуте, у кого-то уже сегодня будут первые лекции."
    p "Не буду много говорить, скажу одно; в нашем институте очень много возможностей развиваться самостоятельно, главное не упустите их."
    p "Если будут какие-то вопросы, не бойтесь, можете задать их или попросить совета, вам никогда не откажут в помощи. На сегодня всё, а теперь идите на лекции."
    hide ak
    
    show hall
    with fade
    # (фон институт// коридор)
    show gg
    ma "А вдруг я не найду друзей, тогда учёба точно будет скучной."
    hide gg


    show gg at left
    show fr at right
    v "Алиса! Не ожидал тебя здесь увидеть. Ты же вроде в другой город собирался поступать?"
    a "О, Ваня! Ты же вроде в другой город собирался поступать?"
    v "Собирался, но в итоге решил сюда всё-таки поступать."
    a "А ты на каком направлении учишься?"
    v "Информационная безопасность, а ты?"
    a "Не представляешь, я тоже. А ты в какой группе?"
    v "В РИ-141003"
    a "Вот совпадение мы с тобой в одной группе! Прикольно, значит опять вместе учиться будем!"
    v "Давай поспешим в аудиторию, а то скоро лекция начнётся."
    a "Хорошо."
    hide gg
    hide fr
    hide hall
    # (фон институт//аудитория)
    
    show au
    with fade
    image prepod = "препод_по_проге.png"
    show prepod
    # Change name
    " Добрый день, меня зовут Василий Сергеевич. Сегодня мы начнём с обсуждения того, что такое информационная безопасность и с чем его едят."
    play movie "1,5hourlater.ogv"
    pr "На сегодня всё."
    pr "Так, совсем забыл вам сказать. У нас объявляется конкурс, поучаствовать может каждый, кто захочет."
    pr "Конкурс по информационной безопасности, точнее он будет проверять ваши навыки в данном направлении."
    pr "Всю подробную информацию я скину вам позже в группу."
    hide prepod
    hide au
    show hall
    with fade

    show gg at left
    show fr at right
    a "Ты будешь участвовать в этом конкурсе?"
    v "Наверное, нет. Дел много, времени вообще нет."
    a "А я, наверное, всё-таки поучаствую."
    v "Я в тебя верю!"
    hide gg
    hide fr
    hide hall
    
    play movie "week_later_inst.ogv"
    show ins
    with fade
    show gg
    ma "Сегодня результаты, я так волнуюсь."
    hide gg
    hide ins

    show au
    with fade
    show prepod
    show gg at left
    show fr at right
    pr "Сегодня я подведу итоги конкурса. Мы выявили одного победителя среди всего потока, а точнее одну победителбницу..."
    menu:
        "Так, ну я видела все работы, объективно моя лучшая. Надеюсь, он назовёт моё имя, хотя нет, он обязан назвать моё имя.":
            jump aa
        "Возможно я выиграю, не уверена, что у меня лучшая работа. Но надеяться стоит.":
            jump bb
label aa:
    pr "Итак, победила Зонова Елизавета. К сожалению, она не из вашей группы."
    ma "Что? Почему не я? Я же видела её работу, моя лучше."
    pr "Конечно, в вашей группе тоже были достойные работы, но Елизавета справилась лучше."
    pr " На сегодня занятия закончились, если есть какие-то вопросы, можете подойти сегодня на консультацию."
    hide prepod
    with fade
    ma "Не понимаю, почему я не выиграла, я обязательно сегодня подойду к нему."
    v "Алиса, не расстраивайся. В следующий раз, ты обязательно выиграешь. Думаю, ещё будет много конкурсов, в которых ты сможешь поучаствовать."
    a "Да, я понимаю, просто я видела её работу, моя лучше."
    v "Ну, я думаю, преподу виднее..."
    a "Ладно, не буду с тобой спорить, просто подойду к нему сегодня."
    v "Как знаешь."
    hide gg
    hide fr
    jump continuee

label bb:
    pr "Итак, победила Зонова Елизавета. К сожалению, она не из вашей группы."
    ma "Ну вот, не выиграла. Ну видимо у неё работа лучше моей была."
    pr "Конечно, в вашей группе тоже были достойные работы, но Елизавета справилась лучше."
    pr "На сегодня занятия закончились, если есть какие-то вопросы, можете подойти сегодня на консультацию."
    ma "Наверное стоит к нему подойти и спросить, какие ошибки я допустила."
    v "Алиса, не переживай. В следующий раз, ты обязательно выиграешь, просто тебе видимо ещё опыта надо набраться."
    a " Наверное ты прав."
    hide gg
    hide fr
    hide prepod
    jump continuee


label continuee:
    play movie "1,5hourlater.ogv"
    # (фон институт//аудитория)
    show prepod at left
    show gg at right
    a "Ещё раз добрый день, вы сказали подойти если будут вопросы."
    pr "Да, внимательно слушаю."
    a "А почему я не выиграла? В моей работе вроде нет недочётов."
    pr "Ты права, у тебя лучшая работа. Просто  мне нужно было тебя завалить."
    a "А почему вы тогда меня завалили?"
    pr "Знаешь, надо было тебе раньше сказать, на самом деле я не просто преподаватель..."
    pr "Я один из председателей секретной организации, которая разбирается с разными проблемами университета и не только. Также мы сотрудничаем с государственной организацией."
    pr "Хочу предложить вступить в нашу организацию. Ты согласна?"
    a "Ахах. Очень смешно, а я ещё думала, что в интитуте скучно будет. Ахахаха."
    pr "В этом нет ничего смешного, я серьёзно говорю."
    a "Да да, конечно, секреная организиция, в университете, в которую предлагают мне вступить. Похоже на начало какого-то фильма."
    a "Ещё скажите, что у вас тут потайные двери или ваша организация находится под нами."
    a "Ахаха"
    pr " Нет, наша организаця находится не под нами, а левее. Потайные двери есть, если вступишь к нам в организацию, то обязательно о них узнаешь."
    menu:
        " Как это странно, он вроде серьёзно говорит, но в реальности такое смешно представить. Подыграю ему, жутко интересно, что будет дальше.":
            jump act_2_agree
        " Как это странно, он вроде серьёзно говорит, но в реальности такое смешно представить. Лучше не буду подыграю ему, посмотрю, что он будет делать дальше.":
            jump act_2_disagree


label act_2_agree:
    a "Хорошо, я всуплю в вашу организацию."
    pr " Идём за мной."
    hide au
    hide prepod
    hide gg

    show bshall
    with fade
    pause
    hide bshall

    # (фон штаб секретной организации)
    show bs
    with fade
    show prepod at left
    show gg at right
    a "Офигеть, я думала это всё шутка."
    pr " Я же говорил, что всё серьёзно."
    a "Просто сложное такое в реальности представить. До сих пор не верю, всё будто сон."
    jump act_3

label act_2_disagree:
    a "Нет, не буду вступать в организацию."
    pr "Почему? Понимаю, ты мне не веришь, но я могу тебе доказать, что состою в этой организации."
    pr " Идём за мной."
    hide au
    hide prepod
    hide gg

    show bshall
    with fade
    pause
    hide bshall

    # (фон штаб секретной организации)
    show bs
    with fade
    show prepod at left
    show gg at right
    a "Офигеть, я думала это всё шутка."
    pr " Я же говорил, что всё серьёзно."
    a "Просто сложное такое в реальности представить. До сих пор не верю, всё будто сон."
    jump act_3
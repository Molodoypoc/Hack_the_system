# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Алиса', color="#f32307")
define ma = Character('Мысли Алисы', color="#b84b3d")
define v = Character('Ваня', color="#c8ffc8")
define t = Character('Учитель', color="#8ff3f3")
define p = Character('Владислав Максимович', color="#95f32a")
define mom = Character('Мама Алисы', color="#f8b117")
define pr = Character('Василий Сергеевич', color="#1046f7")
define g = Character('Агент X', color="#a907d1")
default authority = 0
default count = 0
default help_agree = False

image gg = "главный_герой1.png"
image gg_a = "главный_герой_сердитый.png"
image gg_h = "главный_герой_удивление.png"
image fr = "друг_гг.png"
image fr_a = "друг_гг_сердитый.png"
image fr_h = "друг_гг_удивление.png"
image cr = im.Scale("classroom.png", 1920, 1080)
image st = im.Scale("street.png", 1920, 1080)
image gg_room = im.Scale("gg_room.png", 1920, 1080)
image cc = im.Scale("computer_class.png", 1920, 1080)
image au = im.Scale("auditoria.png", 1920, 1080)
image hall = im.Scale("hall.png", 1920, 1080)
image ak = im.Scale("aktoviy_zal.png", 1920, 1080)
image ins = im.Scale("institute.png", 1920, 1080)
image bs = im.Scale("base.png", 1920, 1080)
image bshall = im.Scale("фон_коридор_секретной_орг.png", 1920, 1080)
image comp = im.Scale("фон_личные_комп.png", 1920, 1080)
image dr = im.Scale("фон_столовая.png", 1920, 1080)
image 1 = im.Scale("1.png", 1920, 1080)
image 2 = im.Scale("2.png", 1920, 1080)
image 3 = im.Scale("3.png", 1920, 1080)
image 4 = im.Scale("4.png", 1920, 1080)
image 5 = im.Scale("5.png", 1920, 1080)
image 6 = im.Scale("6.png", 1920, 1080)

image fnxtday = im.Scale("фон класс на след день.png", 1920, 1080)
image cc_20 = im.Scale("фон комп класс спустя 2 часа.png", 1920, 1080)
image gg_r_v = im.Scale("фон комн алисы этим же вечером.png", 1920, 1080)
image september_inst = im.Scale("фон институт сентябрь.png", 1920, 1080)
image au_1_5 = im.Scale("фон аудитория спустя 1.5 часа.png", 1920, 1080)
image ins_nxt_w = im.Scale("фон институт спустя неделю.png", 1920, 1080)
image 1_h_gg_room = im.Scale("фон комната алисы спустя час.png", 1920, 1080)
image nxt_day_au = im.Scale("фон аудитория на след день.png", 1920, 1080)
image dr_a_l = im.Scale("фон столовая после пары.png", 1920, 1080)
image dr_story = im.Scale("фон_столовая_подробный_рассказ_вани.png", 1920, 1080)
image sh_20_min = im.Scale("фон штаб места спустя 20 мин.png", 1920, 1080)
image sh_1_h = im.Scale("фон штаб спустя час.png", 1920, 1080)
image sh_7_y = im.Scale("фон штаб спустя 7 лет.png", 1920, 1080)
image sh_w_l = im.Scale("фон штаб спустя неделю.png", 1920, 1080)

init:
    define vpunch3 = Move ((0, 10), (0, -10),.10, bounce=True, repeat=True, delay=.275*4)
# Игра начинается здесь:
label start:
    jump act_1
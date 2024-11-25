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

# Игра начинается здесь:
label start:
    jump act_1
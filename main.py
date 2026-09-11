Gun = SpriteKind.create()
Enventory = SpriteKind.create()
def Projectile_wall_hit(sprite, location):
    sprites.destroy(sprite)

scene.on_hit_wall(SpriteKind.Projectile,Projectile_wall_hit)

tiles.set_current_tilemap(tilemap("""맵타일"""))
# -------------------------
# 플레이어
# -------------------------
user = sprites.create(img("""
    . . . . . . f f f f . . . . . . .
    . . . . f f f 2 2 f f f . . . . .
    . . . f f f 2 2 2 2 f f f . . . .
    . . f f f e e e e e e f f f . . .
    . . f f e 2 2 2 2 2 2 e e f . . .
    . . f e 2 f f f f f f 2 e f . . .
    . . f f f f e e e e f f f f . . .
    . f f e f b f 4 4 f b f e f f . .
    . f e e 4 1 f d d f 1 4 e e f . .
    . . f e e d d d d d d e e f . . .
    . . . f e e 4 4 4 4 e e f . . . .
    . . e 4 f 2 2 2 2 2 2 f 4 e . . .
    . . 4 d f 2 2 2 2 2 2 f d 4 . . .
    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . .
    . . . . . f f f f f f . . . . . .
    . . . . . f f . . f f . . . . . .
"""),
    SpriteKind.player)
# 시작 위치
tiles.place_on_tile(user, tiles.get_tile_location(5, 5))
# 카메라가 플레이어 따라가기
scene.camera_follow_sprite(user)
user.set_position(200, 200)
last_left=-100
last_right=-100
last_up=-100
last_down=-100
player_shape=10
weapon=0
pistol=sprites.create(img("""."""),Gun)
pistol_shape=0
enventory=[
    ["test","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""]
]
enventory_sprite=sprites.create(img("""."""),Enventory)
enventoryx=0
enventoryy=0
enventorying=False
enventory_items={"test" : sprites.create(img("""."""), Enventory),
                 "" : sprites.create(img("""."""), Enventory)}
controller.move_sprite(user, 100, 100)

def update_player(asdf=None):
    if not enventorying:
        global player_shape
        if not asdf is None:
            player_shape=asdf
        ps = player_shape+100*weapon
        if ps==10:
            user.set_image(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
            """))
        elif ps==20:
            user.set_image(img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
            """))
        elif ps==30:
            user.set_image(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
            """))
        elif ps==40:
            user.set_image(img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
            """))
        elif ps==11:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 2 2 2 2 2 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
            """))
        elif ps==12:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 2 2 2 2 2 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
            """))
        elif ps==21:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 2 2 2 2 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
            """))
        elif ps==22:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 2 2 f . . .
                . . . . f f f e e f 5 5 f . . .
                . . . . f f f f f f f f f . . .
                . . . . . f f . . f f f . . . .
            """))
        elif ps==31:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 2 2 2 2 2 2 e f f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 2 2 2 2 f e f . .
                . . . e d d e 2 2 2 2 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
            """))
        elif ps==32:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
            """))
        elif ps==41:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 2 2 2 2 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
            """))
        elif ps==42:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 2 2 e d d e f . . . . .
                . . . f 5 5 f e e f f f . . . .
                . . . f f f f f f f f f . . . .
                . . . . f f f . . f f . . . . .
            """))
        elif ps==110:
            user.set_image(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . 4 f e e e e e e e e f 4 . .
                . . e 4 f f f f f f f f 4 e . .
                . . . . f 2 2 2 2 2 2 f . . . .
                . . . . f 4 4 4 4 4 4 f . . . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
            """))
        elif ps==120:
            user.set_image(img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d e e f . .
                . . . f e e e 4 d d e d d e . .
                . . . . f f e e 4 4 e d d e . .
                . . . . . f 2 2 2 2 2 e e . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . . f 4 4 4 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
            """))
        elif ps==130:
            user.set_image(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e e d d d d e e e f . .
                . . . e d d e 4 4 e d d e . . .
                . . . e d d e 2 2 e d d e . . .
                . . . f e e 2 2 2 2 e e f . . .
                . . . . f 4 4 5 5 4 4 f . . . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
            """))
        elif ps==140:
            user.set_image(img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e e d f 1 4 d 4 e e f . .
                . . e d d e d d 4 e e e f . . .
                . . e d d e 4 4 e e f f . . . .
                . . . e e 2 2 2 2 2 f . . . . .
                . . . f 2 2 2 2 2 2 f . . . . .
                . . . f 5 5 4 4 4 4 f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
            """))
        elif ps==111:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . 4 f e e e e e e e e f 4 . .
                . . e 4 f f f f f f f f 4 e . .
                . . . . f 2 2 2 2 2 2 f . . . .
                . . . . f f f f f f f f . . . .
                . . . . f f f . . . . . . . . .
            """))
        elif ps==112:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . 4 f e e e e e e e e f 4 . .
                . . e 4 f f f f f f f f 4 e . .
                . . . . f 2 2 2 2 2 2 f . . . .
                . . . . f f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
            """))
        elif ps==121:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d e e f . .
                . . . f e e 4 4 d d e d d e . .
                . . . . f f 4 4 4 4 e d d e . .
                . . . . . f 2 2 2 2 2 e e . . .
                . . . . . f 4 4 4 4 5 5 f f . .
                . . . . . f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
            """))
        elif ps==122:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . f f f f f f . . . . .
                . . . f f e e e e f 2 f . . . .
                . . f f e e e e f 2 2 2 f . . .
                . . f e e e f f e e e e f . . .
                . . f f f f e e 2 2 2 2 e f . .
                . . f e 2 2 2 f f f f e 2 f . .
                . f f f f f f f e e e f f f . .
                . f f e 4 4 e b f 4 4 e e f . .
                . f e e 4 d 4 1 f d e e f . . .
                . . f e e e e e d e d d e . . .
                . . . . f 4 4 4 4 e d d e . . .
                . . . . f 2 2 2 2 2 e e . . . .
                . . . f f 4 4 4 4 5 5 f . . . .
                . . . f f f f f f f f f . . . .
                . . . . f f . . f f f . . . . .
            """))
        elif ps==131:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 2 2 2 2 2 2 e f f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e e d d d d e e f . . .
                . . . e d d e 2 2 e d d e . . .
                . . . e d d e 2 2 e d d e . . .
                . . . . e e f 5 5 4 e e . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
            """))
        elif ps==132:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e e d d d d e e f . . .
                . . . e d d e 2 2 e d d e . . .
                . . . e d d e 2 2 e d d e . . .
                . . . . e e 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
            """))
        elif ps==141:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e e d f 1 4 d 4 e e f . .
                . . e d d e d d 4 e e f f . . .
                . . e d d e 4 4 4 4 f . . . . .
                . . . e e 2 2 2 2 2 f . . . . .
                . . f f 5 5 4 4 4 4 f . . . . .
                . . f f f f f f f f f . . . . .
                . . . f f f . . . f f . . . . .
            """))
        elif ps==142:
            user.set_image(img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e e d f 1 4 d 4 e e f . .
                . . e d d e d e e e e e f . . .
                . . e d d e 4 4 4 4 f . . . . .
                . . . e e 2 2 2 2 2 f . . . . .
                . . . f 5 5 4 4 4 4 f f . . . .
                . . . f f f f f f f f f . . . .
                . . . . f f f . . f f . . . . .
            """))

def update_enventory():
    if enventorying:
        enventory_sprite.set_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f111f1fff1f1fff1f111f1fff1f11111ff111ff111ff1fff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f1fff11ff1f1fff1f1fff11ff1fff1fff1fff1f1ff1ff1f1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f111f1f1f1ff1f1ff111f1f1f1fff1fff1fff1f111ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f1fff1ff11ff1f1ff1fff1ff11fff1fff1fff1f1f1ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f111f1fff1fff1fff111f1fff1fff1ffff111ff1ff1fff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f1111111111111111f
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
        enventory_sprite.set_position(user.x, user.y)
        '''
        for i in range(3):
            for j in range(9):
                enventory_item=enventory_items["test"]
        '''
                
    else:
        enventory_sprite.set_image(img("""."""))

def update_weapon(asdf=None):
    if not enventorying:
        global weapon
        if not asdf is None:
            weapon=asdf
        if weapon==1:
            global pistol
            global pistol_shape
            if player_shape//10==2:
                if pistol_shape!=2:
                    sprites.destroy(pistol)
                    pistol=sprites.create(img("""
                    b f b f b f b
                    f f f f f f f
                    f f e f . . .
                    f f f f . . .
                    f f . . . . .
                    """),Gun)
                    pistol_shape=2
                pistol.set_position(user.x+8,user.y+2)
            elif player_shape//10==4:
                if pistol_shape!=4:
                    sprites.destroy(pistol)
                    pistol=sprites.create(img("""
                        b f b f b f b
                        f f f f f f f
                        . . . f e f f
                        . . . f f f f
                        . . . . . f f
                    """))
                    pistol_shape=4
                pistol.set_position(user.x-8,user.y+2)
            elif player_shape//10==3:
                if pistol_shape!=3:
                    sprites.destroy(pistol)
                    pistol=sprites.create(img("""
                        f b
                        f f
                        f b
                        f f
                        f b
                        f f
                        f b
                    """))
                    pistol_shape=3
                pistol.set_position(user.x,user.y+6)
            elif player_shape//10==1:
                if pistol_shape!=1:
                    sprites.destroy(pistol)
                    pistol=sprites.create(img("""
                        f b
                        f f
                        f b
                    """))
                    pistol_shape=1
                pistol.set_position(user.x,user.y-8)
        else:
            sprites.destroy(pistol)
            pistol_shape=0

def left_pressed():
    if controller.left.is_pressed():
        if not enventorying:
            global last_left
            global player_shape
            if game.runtime()-last_left>=250:
                last_left=game.runtime()
                if player_shape==41:
                    player_shape=42
                else:
                    player_shape=41
game.on_update(left_pressed)

def right_pressed():
    if controller.right.is_pressed():
        if not enventorying:
            global last_right
            global player_shape
            if game.runtime()-last_right>=250:
                last_right=game.runtime()
                if player_shape==21:
                    player_shape=22
                else:
                    player_shape=21
game.on_update(right_pressed)

def up_pressed():
    if controller.up.is_pressed():
        if not enventorying:
            global last_up
            global player_shape
            if game.runtime()-last_up>=250:
                last_up=game.runtime()
                if player_shape==11:
                    player_shape=12
                else:
                    player_shape=11
game.on_update(up_pressed)

def down_pressed():
    if controller.down.is_pressed():
        if not enventorying:
            global last_down
            global player_shape
            if game.runtime()-last_down>=250:
                last_down=game.runtime()
                if player_shape==31:
                    player_shape=32
                else:
                    player_shape=31
game.on_update(down_pressed)

def nothing_pressed():
    if (not controller.down.is_pressed()
        and not controller.up.is_pressed()
        and not controller.left.is_pressed()
        and not controller.right.is_pressed()):
            if not enventorying:
                global player_shape
                player_shape=player_shape//10*10
game.on_update(nothing_pressed)

def B_pressed():
    if controller.B.is_pressed():
        if not enventorying:
            global weapon
            weapon+=1
            weapon=weapon%2
controller.B.on_event(ControllerButtonEvent.PRESSED, B_pressed)

def A_pressed():
    global enventorying
    if weapon==1:
        bullet=sprites.create(img("""."""), SpriteKind.projectile)
        if pistol_shape==1:
            bullet.set_position(pistol.x-1, pistol.y-4)
            bullet.set_image(img("""
                4 4
                4 4
                4 4
            """))
            bullet.set_velocity(0, -200)
        elif pistol_shape==2:
            bullet.set_position(pistol.x+4, pistol.y-2)
            bullet.set_image(img("""
                4 4 4
                4 4 4
            """))
            bullet.set_velocity(200, 0)
        elif pistol_shape==3:
            bullet.set_position(pistol.x-1, pistol.y+4)
            bullet.set_image(img("""
                4 4
                4 4
                4 4
            """))
            bullet.set_velocity(0, 200)
        elif pistol_shape==4:
            bullet.set_position(pistol.x-6, pistol.y-2)
            bullet.set_image(img("""
                4 4 4
                4 4 4
            """))
            bullet.set_velocity(-200, 0)
    elif weapon==0:
        enventorying=not enventorying
controller.A.on_event(ControllerButtonEvent.PRESSED, A_pressed)

def on_on_update():
    if enventorying:
        controller.move_sprite(user,0,0)
    elif not enventorying:
        controller.move_sprite(user,100,100)
    update_player()
    update_weapon()
    update_enventory()
game.on_update(on_on_update)

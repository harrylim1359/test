let Gun = SpriteKind.create()
scene.onHitWall(SpriteKind.Projectile, function Projectile_wall_hit(sprite: Sprite, location: tiles.Location) {
    sprites.destroy(sprite)
})
tiles.setCurrentTilemap(tilemap`맵타일`)
//  -------------------------
//  플레이어
//  -------------------------
let user = sprites.create(img`
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
        `, SpriteKind.Player)
//  시작 위치
tiles.placeOnTile(user, tiles.getTileLocation(5, 5))
//  카메라가 플레이어 따라가기
scene.cameraFollowSprite(user)
user.setPosition(200, 200)
controller.moveSprite(user, 100, 100)
let last_left = -100
let last_right = -100
let last_up = -100
let last_down = -100
let player_shape = 10
let weapon = 0
let pistol = sprites.create(img`.`, Gun)
let pistol_shape = 0
let enventory = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
let enventoryx = 0
let enventoryy = 0
let enventorying = false
function update_player(asdf: number = null) {
    
    if (!(asdf === null)) {
        player_shape = asdf
    }
    
    let ps = player_shape + 100 * weapon
    if (ps == 10) {
        user.setImage(img`
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
        `)
    } else if (ps == 20) {
        user.setImage(img`
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
        `)
    } else if (ps == 30) {
        user.setImage(img`
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
        `)
    } else if (ps == 40) {
        user.setImage(img`
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
        `)
    } else if (ps == 11) {
        user.setImage(img`
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
        `)
    } else if (ps == 12) {
        user.setImage(img`
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
        `)
    } else if (ps == 21) {
        user.setImage(img`
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
        `)
    } else if (ps == 22) {
        user.setImage(img`
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
        `)
    } else if (ps == 31) {
        user.setImage(img`
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
        `)
    } else if (ps == 32) {
        user.setImage(img`
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
        `)
    } else if (ps == 41) {
        user.setImage(img`
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
        `)
    } else if (ps == 42) {
        user.setImage(img`
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
        `)
    } else if (ps == 110) {
        user.setImage(img`
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
        `)
    } else if (ps == 120) {
        user.setImage(img`
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
        `)
    } else if (ps == 130) {
        user.setImage(img`
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
        `)
    } else if (ps == 140) {
        user.setImage(img`
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
        `)
    } else if (ps == 111) {
        user.setImage(img`
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
        `)
    } else if (ps == 112) {
        user.setImage(img`
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
        `)
    } else if (ps == 121) {
        user.setImage(img`
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
        `)
    } else if (ps == 122) {
        user.setImage(img`
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
        `)
    } else if (ps == 131) {
        user.setImage(img`
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
        `)
    } else if (ps == 132) {
        user.setImage(img`
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
        `)
    } else if (ps == 141) {
        user.setImage(img`
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
        `)
    } else if (ps == 142) {
        user.setImage(img`
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
        `)
    }
    
}

function update_enventory() {
    if (enventorying) {
        
    }
    
}

function update_weapon(asdf: number = null) {
    
    if (!(asdf === null)) {
        weapon = asdf
    }
    
    if (weapon == 1) {
        
        
        if (Math.idiv(player_shape, 10) == 2) {
            if (pistol_shape != 2) {
                sprites.destroy(pistol)
                pistol = sprites.create(img`
                b f b f b f b
                f f f f f f f
                f f e f . . .
                f f f f . . .
                f f . . . . .
                `, Gun)
                pistol_shape = 2
            }
            
            pistol.setPosition(user.x + 8, user.y + 2)
        } else if (Math.idiv(player_shape, 10) == 4) {
            if (pistol_shape != 4) {
                sprites.destroy(pistol)
                pistol = sprites.create(img`
                    b f b f b f b
                    f f f f f f f
                    . . . f e f f
                    . . . f f f f
                    . . . . . f f
                `)
                pistol_shape = 4
            }
            
            pistol.setPosition(user.x - 8, user.y + 2)
        } else if (Math.idiv(player_shape, 10) == 3) {
            if (pistol_shape != 3) {
                sprites.destroy(pistol)
                pistol = sprites.create(img`
                    f b
                    f f
                    f b
                    f f
                    f b
                    f f
                    f b
                `)
                pistol_shape = 3
            }
            
            pistol.setPosition(user.x, user.y + 6)
        } else if (Math.idiv(player_shape, 10) == 1) {
            if (pistol_shape != 1) {
                sprites.destroy(pistol)
                pistol = sprites.create(img`
                    f b
                    f f
                    f b
                `)
                pistol_shape = 1
            }
            
            pistol.setPosition(user.x, user.y - 8)
        }
        
    } else {
        sprites.destroy(pistol)
        pistol_shape = 0
    }
    
}

game.onUpdate(function left_pressed() {
    if (controller.left.isPressed()) {
        
        
        if (game.runtime() - last_left >= 250) {
            last_left = game.runtime()
            if (player_shape == 41) {
                player_shape = 42
            } else {
                player_shape = 41
            }
            
        }
        
    }
    
})
game.onUpdate(function right_pressed() {
    if (controller.right.isPressed()) {
        
        
        if (game.runtime() - last_right >= 250) {
            last_right = game.runtime()
            if (player_shape == 21) {
                player_shape = 22
            } else {
                player_shape = 21
            }
            
        }
        
    }
    
})
game.onUpdate(function up_pressed() {
    if (controller.up.isPressed()) {
        
        
        if (game.runtime() - last_up >= 250) {
            last_up = game.runtime()
            if (player_shape == 11) {
                player_shape = 12
            } else {
                player_shape = 11
            }
            
        }
        
    }
    
})
game.onUpdate(function down_pressed() {
    if (controller.down.isPressed()) {
        
        
        if (game.runtime() - last_down >= 250) {
            last_down = game.runtime()
            if (player_shape == 31) {
                player_shape = 32
            } else {
                player_shape = 31
            }
            
        }
        
    }
    
})
game.onUpdate(function nothing_pressed() {
    if (!controller.down.isPressed() && !controller.up.isPressed() && !controller.left.isPressed() && !controller.right.isPressed()) {
        
        player_shape = Math.idiv(player_shape, 10) * 10
    }
    
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function B_pressed() {
    if (controller.B.isPressed()) {
        
        weapon += 1
        weapon = weapon % 2
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function A_pressed() {
    let bullet: Sprite;
    let envenorying: boolean;
    if (weapon == 1) {
        bullet = sprites.create(img`.`, SpriteKind.Projectile)
        if (pistol_shape == 1) {
            bullet.setPosition(pistol.x - 1, pistol.y - 4)
            bullet.setImage(img`
                4 4
                4 4
                4 4
            `)
            bullet.setVelocity(0, -200)
        } else if (pistol_shape == 2) {
            bullet.setPosition(pistol.x + 4, pistol.y - 2)
            bullet.setImage(img`
                4 4 4
                4 4 4
            `)
            bullet.setVelocity(200, 0)
        } else if (pistol_shape == 3) {
            bullet.setPosition(pistol.x - 1, pistol.y + 4)
            bullet.setImage(img`
                4 4
                4 4
                4 4
            `)
            bullet.setVelocity(0, 200)
        } else if (pistol_shape == 4) {
            bullet.setPosition(pistol.x - 6, pistol.y - 2)
            bullet.setImage(img`
                4 4 4
                4 4 4
            `)
            bullet.setVelocity(-200, 0)
        }
        
    } else if (weapon == 0) {
        envenorying = true
    }
    
})
game.onUpdate(function on_on_update() {
    update_player()
    update_weapon()
    update_enventory()
})

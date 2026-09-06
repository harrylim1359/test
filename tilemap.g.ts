// 자동 생성된 코드입니다. 편집하지 마십시오.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile2 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "맵타일":
            case "수준2":return tiles.createTilemap(hex`190019000b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b01010101010101010101010101010101010101010101010b0b0106040404040404040404040404040404040404040a010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01030202020202020202020202020202020202020209010b0b01070505050505050505050505050505050505050508010b0b01010101010101010101010101010101010101010101010b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b`, img`
2222222222222222222222222
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2.......................2
2222222222222222222222222
`, [myTiles.transparency16,sprites.castle.tileGrass2,sprites.castle.tilePath5,sprites.castle.tilePath4,sprites.castle.tilePath2,sprites.castle.tilePath8,sprites.castle.tilePath1,sprites.castle.tilePath7,sprites.castle.tilePath9,sprites.castle.tilePath6,sprites.castle.tilePath3,sprites.builtin.brick], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
            case "myTile":
            case "tile1":return tile1;
            case "myTile0":
            case "tile2":return tile2;
        }
        return null;
    })

}
// 자동 생성된 코드입니다. 편집하지 마십시오.

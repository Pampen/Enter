const mirrorRoomJoy = {
    color: "green",
    name: 'Mirror Room Joy',
    id: 'MIRROR_ROOM_JOY',
    cellName: 'MRJ',
    connections: [
        'N', 'S'
    ]
}
const mirrorRoomAnger = {
    color: "red",
    name: 'Mirror Room Anger',
    id: 'MIRROR_ROOM_ANGER',
    cellName: 'MRA',
    connections: [
        'N', 'S'
    ]
}
const mirrorRoomLove = {
    color: 'pink',
    name: 'Mirror Room Love',
    id: 'MIRROR_ROOM_LOVE',
    cellName: 'MRL',
    connections: [
        'N', 'S'
    ]
}
const mirrorRoomSadness = {
    color: 'blue',
    name: 'Mirror Room Sadness',
    id: 'MIRROR_ROOM_SADNESS',
    cellName: 'MRS',
    connections: [
        'S'
    ]
}
const mirrorRoomMap = [
    [mirrorRoomSadness],
    [mirrorRoomLove],
    [mirrorRoomAnger],
    [mirrorRoomJoy]
];

export default mirrorRoomMap
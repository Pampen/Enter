const mirrorRoom1 = {
    color: "white",
    name: 'Mirror Room 1',
    id: 'MIRROR_ROOM_1',
    cellName: 'MR',
    connections: [
        'E'
    ]
}
const mirrorRoom2 = {
    color: "white",
    name: 'Mirror Room 2',
    id: 'MIRROR_ROOM_2',
    cellName: 'MR',
    connections: [
        'W', 'N'
    ]
}
const joy = {
    color: "green",
    name: 'Joy',
    id: 'JOY',
    cellName: 'J',
    connections: [
        'W', 'S'
    ]
}
const anger1 = {
    color: "red",
    name: 'Anger 1',
    id: 'ANGER_1',
    cellName: 'A',
    connections: [
        'E', 'N'
    ]
}
const anger2 = {
    color: "red",
    name: 'Anger 2',
    id: 'ANGER_2',
    cellName: 'A',
    connections: [
        'E', 'S'
    ]
}
const love = {
    color: 'pink',
    name: 'Love',
    id: 'LOVE',
    cellName: 'L',
    connections: [
        'N', 'W'
    ]
}
const sadness1 = {
    color: 'blue',
    name: 'Sadness 1',
    id: 'SADNESS_1',
    cellName: 'S',
    connections: [
        'S', 'W'
    ]
}
const sadness2 = {
    color: 'blue',
    name: 'Sadness 2',
    id: 'SADNESS_2',
    cellName: 'S',
    connections: [
        'E'
    ]
}
const mirrorRoomMap = [
    [null, null, sadness2, sadness1],
    [null, null, anger2, love],
    [null, null, anger1, joy],
    [null, null, mirrorRoom1, mirrorRoom2]
];

export default mirrorRoomMap
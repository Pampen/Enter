const mirrorRoom = {
    color: "white",
    name: 'Mirror Room',
    id: 'MIRROR_ROOM',
    cellName: 'MR',
    connections: [
        'N'
    ]
}
const joy = {
    color: "green",
    name: 'Joy',
    id: 'JOY',
    cellName: 'J',
    connections: [
        'N', 'S'
    ]
}
const anger = {
    color: "red",
    name: 'Anger',
    id: 'ANGER',
    cellName: 'A',
    connections: [
        'N', 'S'
    ]
}
const love = {
    color: 'pink',
    name: 'Love',
    id: 'LOVE',
    cellName: 'L',
    connections: [
        'N', 'S'
    ]
}
const sadness = {
    color: 'blue',
    name: 'Sadness',
    id: 'SADNESS',
    cellName: 'S',
    connections: [
        'S'
    ]
}
const mirrorRoomMap = [
    [sadness],
    [love],
    [anger],
    [joy],
    [mirrorRoom]
];

export default mirrorRoomMap
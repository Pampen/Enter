const beach = {
    color: "green",
    name: "Beach",
    id: 'BEACH',
    cellName: 'B',
    connections: [
        "W", "E", "N"
    ]
}
const shed = {
    color: "green",
    stairs: [true, "N"],
    name: 'Shed',
    id: 'SHED',
    cellName: 'S',
    connections: [
        "E", "N"
    ]
}
const shedFrontDoor = {
    color: 'green',
    name: 'Shed Front Door',
    id: 'SHED_FRONT_DOOR',
    cellName: 'SF',
    connections: [
        'E', "W"
    ]
}
const cellar = {
    color: 'green',
    stairs: [true, "S"],
    name: 'Cellar',
    id: 'CELLAR',
    cellName: 'C',
    connections: [
        'N'
    ]
}
const beachEastSide = {
    color: 'green',
    name: 'Beach Eastside',
    id: 'BEACH_EAST_SIDE',
    cellName: 'BE',
    connections: [
        'W', "E"
    ]
}
const shipwreck = {
    color: 'green',
    name: 'Shipwreck',
    id: 'SHIPWRECK',
    cellName: 'SW',
    connections: [
        'W', "E"
    ]
}
const captainsCabin = {
    color: 'green',
    name: 'Captains Cabin',
    id: 'CAPTAINS_CABIN',
    cellName: 'CC',
    connections: [
        'W'
    ]
}
const gate = {
    color: 'green',
    name: 'Gate',
    id: 'GATE',
    cellName: 'G',
    connections: [
        'N', "S"
    ]
}
const lighthouseOutside = {
    color: 'green',
    name: 'LighthouseOutside',
    id: 'LIGHTHOUSE_OUTSIDE',
    cellName: 'LO',
    connections: [
        'N', "S"
    ]
}
const lighthouse = {
    color: 'green',
    name: 'Lighthouse',
    id: 'LIGHTHOUSE',
    cellName: 'L',
    connections: [
        'N', "S"
    ]
}
const lighthouseTopFloor = {
    color: 'green',
    name: 'Lighthouse Topfloor',
    id: 'LIGHTHOUSE_TOP_FLOOR',
    cellName: 'LTF',
    connections: [
        'S'
    ]
}

const greenRoomMap = [
    [null, null, lighthouseTopFloor, null, null, null],
    [null, null, lighthouse, null, null, null],
    [null, null, lighthouseOutside, null, null, null],
    [cellar, null, gate, null, null, null],
    [shed,shedFrontDoor, beach, beachEastSide, shipwreck, captainsCabin]
];

export default greenRoomMap
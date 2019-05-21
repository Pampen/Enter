const livingRoom = {
    color: "red",
    name: "Living Room",
    id: 'LIVING_ROOM',
    cellName: 'LR',
    connections: [
        'E', 'W'
    ]
}

const kitchen = {
    color: "red",
    stairs: [true, "S"],
    name: "Kitchen",
    id: 'KITCHEN',
    cellName: 'K',
    connections: [
        'W', 'S'
    ]
}

const basement = {
    color: "red",
    stairs: [true, "N"],
    name: "Basement",
    id: 'BASEMENT',
    cellName: 'B',
    connections: [
        'N'
    ]
}

const hall = {
    color: "red",
    stairs: [true, "N"],
    name: "Hall",
    id: 'HALL',
    cellName: 'H',
    connections: [
        'E', 'N'
    ]
}

const upperFloor = {
    color: "red",
    stairs: [true, "S"],
    name: "Upper Floor",
    id: 'UPPER_FLOOR',
    cellName: 'UF',
    connections: [
        'S', 'W', 'N'
    ]
}

const attic = {
    color: "red",
    name: "Attic",
    id: 'ATTIC',
    cellName: 'A',
    connections: [
        'S'
    ]
}

const bedroom = {
    color: "red",
    name: "Bedroom",
    id: 'BEDROOM',
    cellName: 'BR',
    connections: [
        'E'
    ]
}

const angerMap = [
    [null, attic, null, null],
    [bedroom, upperFloor, null, null],
    [null, hall, livingRoom, kitchen],
    [null, null, null, basement]
];

export default angerMap
const blueStart = {
    color: "blue",
    name: "Labyrinth",
    id: 'BLUE_START',
    cellName: 'BS',
    connections: [
        'W', 'N'
    ]
}

const blueTorch = {
    color: "blue",
    name: "Finish",
    id: 'BLUE_TORCH_ROOM',
    cellName: 'BT',
    connections: [
        'E'
    ]
}

const blueQuestion = {
    color: "blue",
    name: "Bedroom",
    id: 'BLUE_CORRIDOR_1',
    cellName: '?',
    connections: [
    ]
}

const blueFinish = {
    color: "blue",
    name: "Bedroom",
    id: 'BLUE_FINISH',
    cellName: 'BF',
    connections: [
        'S'
    ]
}

const sadnessMap = [
    [null, blueFinish],
    [null, blueQuestion],
    [blueTorch, blueStart]
];

export default sadnessMap
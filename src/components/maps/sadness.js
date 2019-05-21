const blueStart = {
    color: "blue",
    name: "???",
    id: 'BLUE_START',
    cellName: '?',
    connections: [
        'W', 'N'
    ]
}

const blueTorch = {
    color: "blue",
    name: "Torch Room",
    id: 'BLUE_TORCH_ROOM',
    cellName: 'TR',
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
const mainHall = {
    color: "white",
    name: '???',
    id: 'MAIN_HALL',
    cellName: '?'
}
const porch = {
    color: "orange",
    name: 'Porch',
    id: 'PORCH',
    cellName: 'P',
    connections: [
        'N', 'S'
    ]
}
const greenhouse = {
    color: 'orange',
    name: 'Greenhouse',
    id: 'GREENHOUSE',
    cellName: 'GH',
    connections: [
        'E'
    ]
}
const outside = {
    color: 'orange',
    name: 'Outside',
    id: 'OUTSIDE',
    cellName: 'O',
    connections: [
        'N', 'W'
    ]
}
const tutorialMap = [
    [ null, mainHall],
    [null, porch],
    [greenhouse, outside]
];

export default tutorialMap
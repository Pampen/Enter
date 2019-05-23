const mainHall = {
    color: "grey",
    name: 'Mainhall',
    id: 'MAIN_HALL_RETURN_FROM_RED',
    cellName: 'MH',
    connections: [
        'E'
    ]
}
const mainHallToPinkMap = [
    [null, null, null],
    [null, null, mainHall, null, null],
    [null, null, null]
];

export default mainHallToPinkMap
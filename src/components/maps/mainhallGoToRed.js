const mainHall = {
    color: "grey",
    name: 'Mainhall',
    id: 'MAIN_HALL_RETURN_FROM_GREEN',
    cellName: 'MH',
    connections: [
        'N'
    ]
}
const mainHallToRedMap = [
    [null, null, null],
    [null, null, mainHall, null, null],
    [null, null, null]
];

export default mainHallToRedMap
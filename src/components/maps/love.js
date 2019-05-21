const cribRoom = {
    color: 'pink',
    name: 'Crib Room',
    id: 'CRIB_ROOM',
    cellName: 'CR',
    connections: [
        'N', 'E'
    ]
}
const toyCarRoom = {
    color: 'pink',
    name: 'Toy Car Room',
    id: 'TOY_CAR_ROOM',
    cellName: 'TCR',
    connections: [
        'N', 'S'
    ]
}
const babyRoom = {
    color: 'pink',
    name: 'Baby Room',
    id: 'BABY_ROOM',
    cellName: 'BR',
    connections: [
        'E', 'S'
    ]
}
const nursingRoom = {
    color: 'pink',
    name: 'Nursing Room',
    id: 'NURSING_ROOM',
    cellName: 'NR',
    connections: [
        'W', 'S'
    ]
}
const studyRoom = {
    color: 'pink',
    name: 'Study Room',
    id: 'STUDY_ROOM',
    cellName: 'SR',
    connections: [
        'N', 'S'
    ]
}
const messyRoom = {
    color: 'pink',
    name: 'Messy Room',
    id: 'MESSY_ROOM',
    cellName: 'MR',
    connections: [
        'N', 'W'
    ]
}

const loveMap = [
    [babyRoom, nursingRoom],
    [toyCarRoom, studyRoom],
    [cribRoom, messyRoom]
]

export default loveMap
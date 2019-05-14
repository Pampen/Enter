const cribRoom = {
    color: 'pink',
    name: 'Crib Room',
    id: 'CRIB_ROOM',
    cellName:'CR',
    connections: [
        'N', 'E'
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
        'W', 'S', 'E'
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
    [null, studyRoom],
    [cribRoom, messyRoom]
]

export default loveMap
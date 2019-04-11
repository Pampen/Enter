from blueDoor import handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleBlueStart, handleBlueFinish, handleTorchRoom
from tutorial import handleGreenHouse, handleOutside, handlePorch
from MainHall import handleMainHall
from redDoor import handleUpperFloor, handleLivingRoom, handleKitchen, handleHall, handleBedroom, handleBasement, handleAttic
from pinkDoor import handleBabyroom, handleCribroom, handleMessyroom, handleNursingroom, handleStudyroom
from greenDoor import handleBeach, handleCabin, handleCellar, handleGate, handleOutsideShed, handleShed, handleOutsideShipwreck, handleShipwreck, handleLighthouse, handleLighthouseOutside, handleLighthouseTop, handleOcean

levels = {
    'OUTSIDE': handleOutside,
    'GREENHOUSE': handleGreenHouse,
    'PORCH': handlePorch,
    'BEACH': handleBeach,
    'CABIN': handleCabin,
    'CELLAR': handleCellar,
    'GATE': handleGate,
    'OUTSIDE_SHED': handleOutsideShed,
    'SHED': handleShed,
    'OUTSIDE_SHIPWRECK': handleOutsideShipwreck,
    'SHIPWRECK': handleShipwreck,
    'LIGHTHOUSE_OUTSIDE': handleLighthouseOutside,
    'LIGHTHOUSE': handleLighthouse,
    'LIGHTHOUSE_TOP': handleLighthouseTop,
    'Blue start': handleBlueStart,
    'Blue Torch Room': handleTorchRoom,
    'Blue Corridor 1': handleBlueCorridor1,
    'Blue Corridor 2': handleBlueCorridor2,
    'Blue Corridor 3': handleBlueCorridor3,
    'Blue Corridor 4': handleBlueCorridor4,
    'Blue Corridor 5': handleBlueCorridor5,
    'Blue Corridor 6': handleBlueCorridor6,
    'Blue Corridor 7': handleBlueCorridor7,
    'Blue Corridor 8': handleBlueCorridor8,
    'Blue Corridor 9': handleBlueCorridor9,
    'Blue Finish': handleBlueFinish,
    'MAIN HALL': handleMainHall,
    'LIVING ROOM': handleLivingRoom,
    'KITCHEN': handleKitchen,
    'HALL': handleHall,
    'UPPER FLOOR': handleUpperFloor,
    'BEDROOM': handleBedroom,
    'BASEMENT': handleBasement,
    'ATTIC': handleAttic,
    'CRIBROOM': handleCribroom,
    'BABYROOM': handleBabyroom,
    'NURSINGROOM': handleNursingroom,
    'STUDYROOM': handleStudyroom,
    'MESSYROOM': handleMessyroom
}

def levelChecker(userInput, state):   
    level = state['level']
    return levels[level](userInput, state)
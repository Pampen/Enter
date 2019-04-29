from blueDoor import handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleBlueStart, handleBlueFinish, handleTorchRoom
from tutorial import handleGreenHouse, handleOutside, handlePorch
from MainHall import handleMainHall
from redDoor import handleUpperFloor, handleLivingRoom, handleKitchen, handleHall, handleBedroom, handleBasement, handleAttic
from pinkDoor import handleBabyroom, handleCribroom, handleMessyroom, handleNursingroom, handleStudyroom
from greenDoor import handleBeach, handleCabin, handleCellar, handleGate, handleOutsideShed, handleShed, handleOutsideShipwreck, handleShipwreck, handleLighthouse, handleLighthouseOutside, handleLighthouseTopFloor, handleOcean

levels = {
    'OUTSIDE': handleOutside,
    'GREENHOUSE': handleGreenHouse,
    'GREENHOUSE_LIGHT_ON': handleGreenHouse,
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
    'LIGHTHOUSE_TOP': handleLighthouseTopFloor,
    'BLUE_START': handleBlueStart,
    'BLUE_TORCH_ROOM': handleTorchRoom,
    'BLUE_CORRIDOR_1': handleBlueCorridor1,
    'BLUE_CORRIDOR_2': handleBlueCorridor2,
    'BLUE_CORRIDOR_3': handleBlueCorridor3,
    'BLUE_CORRIDOR_4': handleBlueCorridor4,
    'BLUE_CORRIDOR_5': handleBlueCorridor5,
    'BLUE_CORRIDOR_6': handleBlueCorridor6,
    'BLUE_CORRIDOR_7': handleBlueCorridor7,
    'BLUE_CORRIDOR_8': handleBlueCorridor8,
    'BLUE_CORRIDOR_9': handleBlueCorridor9,
    'BLUE_FINISH': handleBlueFinish,
    'MAIN_HALL': handleMainHall,
    'LIVING_ROOM': handleLivingRoom,
    'LIVING_ROOMItem': handleKitchen,
    'KITCHEN': handleKitchen,
    'HALL': handleHall,
    'UPPER_FLOOR': handleUpperFloor,
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
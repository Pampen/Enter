from tutorial import handleGreenHouse, handleOutside, handlePorch
from MainHall import handleMainHall
from greenDoor import handleBeach, handleCaptainsCabin, handleCellar, handleGate, handleShedFrontDoor, handleShed, handleBeachEastSide, handleShipwreck, handleLighthouse, handleLighthouseOutside, handleLighthouseTopFloor, handleOcean
from redDoor import handleUpperFloor, handleLivingRoom, handleKitchen, handleHall, handleBedroom, handleBasement, handleAttic
<<<<<<< HEAD
from pinkDoor import handleBabyroom, handleCribroom, handleMessyroom, handleNursingroom, handleStudyroom, handleBabyroomcrib, handleBabyroomdoll, handleBabyroomblanket, handleBabyroompacifier, handleBabyroomkey
from greenDoor import handleBeach, handleCabin, handleCellar, handleGate, handleOutsideShed, handleShed, handleOutsideShipwreck, handleShipwreck, handleLighthouse, handleLighthouseOutside, handleLighthouseTopFloor, handleOcean
=======
from pinkDoor import handleBabyRoom, handleCribRoom, handleMessyRoom, handleNursingRoom, handleStudyRoom
from blueDoor import handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleBlueStart, handleBlueFinish, handleTorchRoom
>>>>>>> 3eecd09b533e04a835fd4e16a88358969bebebef

levels = {
    'OUTSIDE': handleOutside,
    'GREENHOUSE': handleGreenHouse,
    'GREENHOUSE_LIGHT_ON': handleGreenHouse,
    'GREENHOUSE_LIGHT_AND_KEY_ON': handleGreenHouse,
    'PORCH': handlePorch,
    'MAIN_HALL': handleMainHall,
    'BEACH': handleBeach,
    'CAPTAINS_CABIN': handleCaptainsCabin,
    'CELLAR': handleCellar,
    'GATE': handleGate,
    'SHED_FRONT_DOOR': handleShedFrontDoor,
    'SHED': handleShed,
    'BEACH_EAST_SIDE': handleBeachEastSide,
    'SHIPWRECK': handleShipwreck,
    'LIGHTHOUSE_OUTSIDE': handleLighthouseOutside,
    'LIGHTHOUSE': handleLighthouse,
    'LIGHTHOUSE_TOP_FLOOR': handleLighthouseTopFloor,
    'LIVING_ROOM': handleLivingRoom,
    'KITCHEN': handleKitchen,
    'HALL': handleHall,
    'UPPER_FLOOR': handleUpperFloor,
    'BEDROOM': handleBedroom,
    'BASEMENT': handleBasement,
    'ATTIC': handleAttic,
    'CRIB_ROOM': handleCribRoom,
    'BABY_ROOM': handleBabyRoom,
    'NURSING_ROOM': handleNursingRoom,
    'STUDY_ROOM': handleStudyRoom,
    'MESSY_ROOM': handleMessyRoom,
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
<<<<<<< HEAD
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
    'MESSYROOM': handleMessyroom,
    'BABYROOMCRIB' : handleBabyroomcrib,
    'BABYROOMDOLL' : handleBabyroomdoll,
    'BABYROOMBLANKET' : handleBabyroomblanket,
    'BABYROOMPACIFIER': handleBabyroompacifier,
    'BABYROOMKEY' : handleBabyroomkey    
        }
=======
    'BLUE_FINISH': handleBlueFinish
}
>>>>>>> 3eecd09b533e04a835fd4e16a88358969bebebef

def levelChecker(userInput, state):   
    level = state['level']
    return levels[level](userInput, state)
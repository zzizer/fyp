import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint, FINGERPRINT_CHARBUFFER1
from LCD.display import DisplayOnLCD


def search_fingerprint():

    display = DisplayOnLCD()

    try:
        # Initialize the fingerprint sensor
        f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)
        
        # Verify the sensor password
        if not f.verifyPassword():
            raise ValueError('The given fingerprint sensor password is wrong!')
    
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        return None
    try:
        # print('Waiting for finger...')
        display.random_message('Place Finger...')
        
        # Wait until a finger is read
        while not f.readImage():
            pass

        # Convert the read image to characteristics and store it in charbuffer 1
        f.convertImage(FINGERPRINT_CHARBUFFER1)
        
        # Search for the fingerprint in the stored templates
        result = f.searchTemplate()
        
        positionNumber = result[0]
        accuracyScore = result[1]
        
        if positionNumber == -1:
            # print('No match found!')
            display.random_message('No Student Found...')
            return -1
        else:
            # print('Found template at position #' + str(positionNumber))
            # print('The accuracy score is: ' + str(accuracyScore))
            return positionNumber
    
    except Exception as e:
        # print('Operation failed!')
        # print('Exception message: ' + str(e))
        display.random_message('Operation Error')
        return None
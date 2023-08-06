import sys, pyautogui, logging, time

def printReceipt():
    # Prevent PIL from adding to log
    logging.getLogger('PIL').setLevel(logging.WARNING)

    # Configure logging module
    logging.basicConfig(level=logging.DEBUG, filename="print.log", filemode="w")

    # Get coords for and click the ticket dropdown
    coords = pyautogui.locateCenterOnScreen('imgs/img.png')

    # Quit program execution when coords = None
    if coords is None:
        sys.exit("Ticket dropdown not found.")

    pyautogui.click(x=coords.x, y=coords.y, interval=0.1)

    # Move mouse to most recent ticket and click it
    offset = (0, 40)
    pyautogui.moveRel(offset)
    pyautogui.click(interval=0.1)

    # Wait for prompt to load
    time.sleep(0.5)

    # Look for get routing prompt
    promptCoords = pyautogui.locateCenterOnScreen('imgs/prompt.png')
    if promptCoords is not None:
        # We have found the prompt, click the ok button.
        xCoord = promptCoords.x - 80
        yCoord = promptCoords.y
        pyautogui.click(x=xCoord, y=yCoord)

    # Trigger an F9 key press
    #pyautogui.press('f9')
    #pyautogui.typewrite('.')
    #pyautogui.press('enter')



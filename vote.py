"""
Script for voting for the icrar page a bunch.
"""

import time
import pyautogui
from rich.progress import track


def move_and_click(x: int, y: int, delay: float = 0.5) -> None:
    """
    Move the mouse to (x, y) and click.
    Args:
        x (int): X-coordinate on the screen.
        y (int): Y-coordinate on the screen.
        delay (float): Delay before and after clicking (default 0.5 seconds).
    """
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(delay)
    pyautogui.click()
    pyautogui.click()
    time.sleep(delay)


def refresh_page(delay: float = 2.0) -> None:
    """
    Refresh the current page (simulate pressing F5).
    Args:
        delay (float): Delay before the refresh (default 0.5 seconds).
    """
    time.sleep(delay)
    pyautogui.keyDown("command")
    pyautogui.press("r")
    pyautogui.keyUp("command")


def main() -> None:
    """
    Main for keeping variables in scope.
    """
    # Define coordinates for actions
    vote_button_position = (400, 800)
    song_position = (365, 630)

    # Move to song, click, then move to vote button and click
    for _ in track(range(1000), "Voting for the best song!"):
        move_and_click(*song_position)
        move_and_click(*vote_button_position)
        refresh_page()


if __name__ == "__main__":
    main()

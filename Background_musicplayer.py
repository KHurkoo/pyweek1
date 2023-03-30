import pygame
import os
import time

def main():
    # Initialize Pygame
    pygame.init()

    # Set the music file's path 
    music_path = os.path.join(os.getcwd(), "background-music1.wav")

    # Open the music file.
    try:
        pygame.mixer.music.load(music_path)
    except pygame.error as e:
        print(f"Unable to load music file: {str(e)}")
        return

    # Make the music loop endlessly. 
    try:
        pygame.mixer.music.play(loops=-1)
    except pygame.error as e:
        print(f"Unable to play music file: {str(e)}")
        return

    # Continually run the code while the music is playing 
    try:
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt gracefully
        pass
    except SystemExit:
        #Manage system shutdown (such as a power outage) effectively 
        pass

    # Stop the music and quit Pygame
    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()

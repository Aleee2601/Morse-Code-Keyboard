# Morse-Code-Keyboard
LINK: https://www.tinkercad.com/things/kQ6hXCGQYym-morse-code-keyboard?sharecode=HF8FjvM98KxyiWDN-gokzRl477Wp5w61GvisSgwPQPI
## Project Overview
The Morse Code Keyboard is an innovative project that allows users to input Morse code through a set of buttons, which are mapped to Morse signals (dots and dashes). Inspired by the "Tap Strap" wearable keyboard, this project simplifies the process of typing Morse code by using a microcontroller, buttons, and an LCD for visual feedback. This project is designed for users who are learning Morse code, those who enjoy experimenting with alternative input methods, or individuals with communication disabilities seeking alternative ways to interact with devices.

## How the Project Was Created
This project was inspired by the Tap Strap, a wearable keyboard that translates finger gestures into text. My idea was to take this concept and adapt it to Morse code, simplifying it for easy implementation using basic hardware and an online simulator. The goal was to create an accessible, easy-to-use Morse code keyboard with basic components while still allowing full functionality.

I started by outlining how Morse code could be input through simple button presses, with each button corresponding to a different Morse code signal or control function (e.g., separating letters and words). After finalizing the design, I moved on to implementing the hardware connections, using an Arduino microcontroller for managing the input from buttons and displaying the output on an LCD screen.

## Key Steps in Development:
1. Concept Design:
- The idea was to simplify Morse code input by assigning each finger a specific role* The index finger inputs dots (short signals).
  - The middle finger inputs dashes (long signals). 
  - The ring finger is used to separate letters.
  - The pinky finger separates words.

2. Hardware Prototyping:
- I selected components based on availability and ease of use.
- Four buttons were connected to the Arduino to represent the Morse signals and delimiters.
- An LCD screen was added for visual feedback of the input text.
- Optional LEDs were included to give visual confirmation of each input, further enhancing usability.
- I used resistors, a potentiometer, and a breadboard to stabilize the circuit and ensure accurate signals were being processed by the Arduino.

3. Coding:
- I wrote the core program in C/C++ for the Arduino, focusing on detecting button presses and differentiating between short and long presses.
- A debounce method was added to ensure that each button press was accurately read by the microcontroller without registering false inputs.
- The Morse code input was mapped to a pre-defined dictionary of characters for conversion into text.
- The output was displayed on the LCD screen using the I2C_LCD_driver library, with each letter appearing after a complete signal sequence was inputted.

4. Testing and Refining:
- During the development, several issues arose, such as incorrect signal detection and text display errors on the LCD.
- I implemented a debouncing algorithm for more accurate button presses and resolved display problems by adjusting the initialization of the LCD screen.

5. Challenges:
- Ensuring stable hardware connections, especially on the breadboard.
- Implementing a user-friendly software interface for smooth interaction.
- Correctly integrating the hardware and software, such as synchronizing the button inputs with the LCD output.

## Features
- Morse Code Input: Each button press is mapped to Morse code signals:
  - Dot (.) – Index finger
  - Dash (-) – Middle finger
  - Letter Separator – Ring finger
  - Word Separator – Pinky finger
- Real-Time Text Display: The LCD screen displays the decoded text as the user inputs Morse code.
- LED Feedback: Optional LEDs provide visual confirmation for each input.
- Debounced Button Presses: To prevent false input readings, button presses are debounced, ensuring only valid inputs are processed.

## Hardware Requirements
To recreate this project, you will need the following components:

- Arduino Microcontroller: Serves as the central unit for processing inputs and displaying output.
- 4 Buttons: Each button corresponds to a specific Morse code signal or control.
- LCD Screen: Displays the decoded Morse code in real-time.
- 4 LEDs (Optional): Provides visual feedback for button presses.
- Potentiometer (250kΩ): Used to adjust the voltage and current in the circuit.
- Resistors, wires, and breadboard: Required for connecting components and stabilizing the circuit.
## Software Requirements
- Arduino IDE: Used to write and upload the code to the Arduino microcontroller.
- Libraries:
  - `gpiozero`: For reading button inputs and managing the hardware interaction.
  - `I2C_LCD_driver`: For controlling the LCD display.
## Code Functionality
1. Button Input Detection:

- The system detects which button is pressed and for how long to distinguish between dots and dashes. The debouncing code ensures the system doesn’t register multiple presses from a single input.
2. Morse Code Conversion:

- The program converts the button presses into dots and dashes, which are then translated into corresponding letters or numbers based on the Morse code dictionary.
3. Text Display:

- The converted characters are displayed on the LCD screen. Separating characters or words is achieved by pressing the appropriate buttons, and the LCD screen updates accordingly.
## Setup Instructions
### Hardware Setup
1. Connect the buttons to the Arduino's digital input pins.
2. Attach the LCD screen using I2C communication to the designated Arduino pins.
3. Connect the LEDs (optional) to the output pins.
4. Ensure resistors and a potentiometer are placed appropriately for voltage control
5. Use the breadboard to stabilize the connections.
### Software Setup
1. Install the required libraries (`gpiozero`, `I2C_LCD_driver`) in the Arduino IDE.
2. Upload the Morse code translation code to the Arduino using the IDE.
3. Ensure all connections are secure and start testing the inputs.
## Troubleshooting
1. Incorrect Inputs: If the buttons are not registering properly, double-check the connections and ensure the debounce code is functioning.
2. LCD Display Issues: Ensure the LCD is initialized correctly, and the I2C connection is working as expected. If characters are missing or garbled, try adjusting the timing in the code.
3. Signal Detection Errors: Check the button press durations and confirm they align with the defined dot and dash timings.
## Future Development
1. Glove Implementation: In the future, I plan to integrate the buttons into a glove, making it more ergonomic and wearable for real-time usage.
2. Gesture Support: Adding functionality for pressing multiple buttons simultaneously to further enhance user input and reduce button clutter.
3. Wireless Version: Potential integration with wireless communication modules to send Morse code remotely.
## Conclusion
The Morse Code Keyboard project offers an alternative input method that combines simplicity with educational value. It provides a hands-on learning experience with Morse code while being highly customizable and adaptable. This project has room for further development, including more advanced features such as gesture recognition or a wearable design.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Inspired by the "Tap Strap" concept and various Morse code simulators.
Special thanks to the open-source community for providing essential libraries and support.

# Morse-Code-Keyboard
LINK: https://www.tinkercad.com/things/kQ6hXCGQYym-morse-code-keyboard?sharecode=HF8FjvM98KxyiWDN-gokzRl477Wp5w61GvisSgwPQPI
Morse Code Keyboard
Morse Code Keyboard is an innovative hardware project that transforms tactile button inputs into Morse code, providing an engaging way to learn Morse code or offer alternative communication means. By using a simple Arduino microcontroller, dedicated buttons for dots and dashes, and an LCD for real-time text display, this project bridges the gap between traditional Morse signals and modern digital interfaces.

Features
Morse Code Input:

Four dedicated buttons:
Index Finger: Inputs dots (.)
Middle Finger: Inputs dashes (-)
Ring Finger: Acts as a letter separator
Pinky Finger: Acts as a word separator
Real-Time Text Display:
The LCD screen instantly converts Morse code signals into text, giving users immediate visual feedback.

LED Feedback (Optional):
LEDs provide visual confirmation of each button press to enhance the user experience.

Debounced Button Presses:
Integrated debouncing algorithms ensure accurate signal registration, eliminating false or repeated inputs.

Accessible & Educational:
Ideal for Morse code learners, enthusiasts exploring alternative input methods, and individuals seeking assistive communication solutions.

Technologies Used
Hardware
Arduino Microcontroller:
Serves as the central processing unit for detecting inputs and driving the display.

Input Components:

4 Tactile Buttons for Morse signals
Optional LEDs for visual input confirmation
Display Component:

LCD Screen with I2C communication for real-time text output
Supporting Components:

Resistors, a 250kΩ Potentiometer, wires, and a breadboard for circuit stability and voltage control
Software
Programming Environment:

Arduino IDE for writing and uploading code
Libraries:

I2C_LCD_driver for LCD control
Debounce handling routines for accurate input detection
Coding Language:

C/C++ for Arduino
Installation and Setup
Prerequisites
Arduino Microcontroller and essential components (buttons, LCD, LEDs, resistors, potentiometer, breadboard)
Arduino IDE installed on your computer
Hardware Setup
Assemble the Circuit:
Connect the four buttons to designated digital input pins on the Arduino.
Attach the LCD screen using I2C communication lines.
(Optional) Connect LEDs to output pins for visual feedback.
Use resistors, a potentiometer, and a breadboard to secure and stabilize all connections.
Software Setup
Configure the Development Environment:

Open the Arduino IDE and load the Morse Code Keyboard project code.
Ensure the required libraries (I2C_LCD_driver and debounce routines) are installed.
Upload and Test:

Upload the code to the Arduino.
Test the device to verify:
Correct detection of button presses as dots and dashes.
Accurate conversion of Morse code to text on the LCD.
Proper operation of LED indicators (if used).
Troubleshooting
Button Input Issues:
Check the wiring and confirm that the debounce code is effectively filtering multiple signals.

LCD Display Problems:
Verify the I2C connection and adjust the LCD initialization settings if characters appear garbled.

Signal Timing Errors:
Ensure that the button press durations match the defined timing for dots and dashes.

Future Enhancements
Wearable Integration:
Adapt the design into a glove form factor for a more ergonomic, real-time input experience.

Gesture Support:
Develop multi-button gesture recognition to further streamline Morse code input and reduce clutter.

Wireless Capability:
Incorporate wireless communication modules to enable remote Morse code transmission.

# Morse-Code-Keyboard
LINK: https://www.tinkercad.com/things/kQ6hXCGQYym-morse-code-keyboard?sharecode=HF8FjvM98KxyiWDN-gokzRl477Wp5w61GvisSgwPQPI

Morse Code Keyboard is an innovative hardware project that transforms tactile button inputs into Morse code, providing an engaging way to learn Morse code or offer alternative communication means. By using a simple Arduino microcontroller, dedicated buttons for dots and dashes, and an LCD for real-time text display, this project bridges the gap between traditional Morse signals and modern digital interfaces.

## Features

- **Morse Code Input:**  
  - **Dot (.)** – Activated by the index finger button  
  - **Dash (-)** – Activated by the middle finger button  
  - **Letter Separator** – Triggered by the ring finger button  
  - **Word Separator** – Triggered by the pinky finger button

- **Real-Time Text Display:**  
  An LCD screen displays the decoded Morse code instantly, providing clear visual feedback.

- **LED Feedback (Optional):**  
  LEDs illuminate on each button press to confirm input actions.

- **Debounced Button Presses:**  
  Integrated debounce algorithms ensure that each press is accurately registered without false triggers.

---

## Technologies Used

### Hardware

- **Arduino Microcontroller:**  
  The central processing unit responsible for reading inputs and managing the output display.

- **Input Components:**  
  - 4 Tactile Buttons for representing Morse code signals  
  - Optional LEDs for visual feedback

- **Display Component:**  
  - LCD Screen using I2C communication for displaying text

- **Supporting Components:**  
  - Resistors, a 250kΩ Potentiometer, wires, and a breadboard for reliable circuit connections

### Software

- **Development Environment:**  
  - Arduino IDE for code development and uploading to the Arduino

- **Programming Language:**  
  - C/C++ for Arduino firmware development

- **Libraries:**  
  - `I2C_LCD_driver` for controlling the LCD display  
  - Custom debounce routines to ensure accurate input detection

---

## Installation and Setup

### Prerequisites

- Arduino Microcontroller and essential components (buttons, LCD, LEDs, resistors, potentiometer, breadboard)
- Arduino IDE installed on your computer

### Hardware Setup

1. **Circuit Assembly:**
   - Connect the four buttons to the designated digital input pins on the Arduino.
   - Attach the LCD screen using I2C communication.
   - (Optional) Connect the LEDs to the Arduino's output pins.
   - Use resistors, a potentiometer, and a breadboard to secure and stabilize all connections.

### Software Setup

1. **Configure the Arduino IDE:**
   - Open the Arduino IDE and load the Morse Code Keyboard project code.
   - Install the required libraries (`I2C_LCD_driver` and any debounce libraries).

2. **Upload and Test:**
   - Upload the code to the Arduino.
   - Test the project to ensure:
     - Correct detection of button presses as dots and dashes.
     - Accurate translation of Morse code into text on the LCD.
     - Proper functioning of optional LED indicators.

---

## Troubleshooting

- **Incorrect Button Inputs:**  
  Verify all wiring connections and ensure the debounce algorithm is correctly filtering out noise.

- **LCD Display Issues:**  
  Confirm that the I2C connection is secure and adjust the LCD initialization settings if characters appear garbled.

- **Signal Timing Errors:**  
  Ensure that the duration of button presses accurately corresponds to the defined timings for dots and dashes.

---

## Future Enhancements

- **Wearable Integration:**  
  Adapt the design into a glove form factor for a more ergonomic, real-time Morse code input experience.

- **Gesture Recognition:**  
  Implement multi-button gesture support to streamline input and reduce reliance on sequential button presses.

- **Wireless Capability:**  
  Explore incorporating wireless communication modules to enable remote Morse code transmission.


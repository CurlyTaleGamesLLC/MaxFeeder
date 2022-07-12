/*
 * capabilities
*/
#define NUMBER_OF_FEEDER 34
#define HAS_ENABLE_PIN
#define HAS_FEEDBACKLINES
#define NO_ANALOG_IN
#define NO_POWER_OUTPUTS
#define SOFT_SERVO_NUMBER 3

/*
* feederPinMap: Map IO-pins to specific feeder. First feeder is at index 0 (N0). Last feeder is NUMBER_OF_FEEDER-1
*/
const static uint8_t feederPinMap[NUMBER_OF_FEEDER] = {
  A0,    // Servo Feeder 0
  A2,    // Servo Feeder 1
  A4,    //...
  A5,
  A6,
  A7,
  A8,
  A9,
  53,
  51,
  49,
  47, // Servo Feeder 11

  45, // Servo Feeder 12
  27,
  43,
  29,
  41,
  31,
  39,
  33,
  37,
  35, // Servo Feeder 21

  12, // Servo Feeder 22
  10,
  8,
  6,
  4,
  2,
  14,
  16,
  18,
  21,
  23,
  25 // Servo Feeder 33
};


/*
* feederFeedbackPinMap: Map IO-pins to feedback-line to specific feeder. First feeder is at index 0 (N0). Last feeder is NUMBER_OF_FEEDER-1
* Feedback-line is usually connected to a microswitch to determine whether the feeder has a tape loaded and cover tape is tensioned
*
* to disable feedback-functionality completely at compile-time set pin to -1
*/
const static int8_t feederFeedbackPinMap[NUMBER_OF_FEEDER] = {
  A1,    // Feeder Feedback 0
  A3,    // Feeder Feedback 1
  A10,
  A11,
  A12,
  A13,
  A14,
  A15,
  
  52,
  50,
  48,
  46, // Feeder Feedback 11

  44, // Feeder Feedback 12
  26,
  42,
  28,
  40,
  30,
  38, // 18
  32, // 19
  36,
  34, // Feeder Feedback 21

  13, // Feeder Feedback 22
  11,
  9,
  7,
  5,
  3,
  15,
  17,
  19,
  20,
  22,
  24 // Feeder Feedback 33

};

/*
* FEEDER_ENABLE_PIN
* IO-pin with a mosfet to switch power to all feeder on/off
*
* all lines that include "FEEDER_ENABLE_PIN" have been commented out for the MAX Feeder Shield
*/
#define FEEDER_ENABLE_PIN -1



/* ----------------
  MOSFET power output pinmap

  on pcb 4 output are prepared. output 1 is at index 0 in pwrOutputPinMap
*/

#define NUMBER_OF_POWER_OUTPUT 0
const static uint8_t pwrOutputPinMap[NUMBER_OF_POWER_OUTPUT] = {

};

const static uint8_t softwareServoPins[SOFT_SERVO_NUMBER] = {
    A10,
    A12,
    A14
  };

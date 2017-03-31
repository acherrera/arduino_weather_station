/*
Combining date logger and BME 280 chip. This should get and log data

TODO need to get the LED to stop when card is pulled out. 
*/

#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include "RTClib.h"

#define BME_SCK 7
#define BME_MISO 6
#define BME_MOSI 5
#define BME_CS 4
//Change this for accurate altitude readings. Comment out for no alitutde
#define SEALEVELPRESSURE_HPA (1013.25)

int led = 2;
int led_blink;
const int chipSelect = 10; // for datalogger
RTC_DS1307 rtc; //for time information
char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI for BME

//char fileName[12]; // Used for file name later
//File dataFile;
//DateTime now = rtc.now(); //For time Logging
//sprintf(fileName,"%04u%02u%02u_%02u%02u%02u",now.year(), now.month(), now.day(), now.hour(),now.minute(),now.second());



//TODO get ride of the Serial printing stuff on final design
//TODO better implement the date and time methods
//Maybe find better way of setting up the file system
//TODO add light to show if it is working
void setup() {
  pinMode(led, OUTPUT); // Set LED pin
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  bool status;
  status = bme.begin();

  // Make sure everything is working
  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while(1);
  }
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while(1);
  }
  if (! rtc.isrunning()) {
    Serial.println("RTC is NOT running!");
    while(1);
  }

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    while(1);
    // don't do anything more:
  }
  Serial.println("card initialized.");

  for (int i = 0; i < 10; i++) {
    digitalWrite(led, HIGH);
    delay(100);
    digitalWrite(led, LOW);
    delay(100);
  }
}


//Create the correct file



void loop() {
  // one second delay in readings. Could be faster but... meh.

  delay(1000);
  digitalWrite(led, LOW);

  // make a string for assembling the data to log:
  DateTime now = rtc.now(); //For time Logging
  String dataString = "";

  char dateTimeString[40];
  sprintf(dateTimeString, "%04d%02d%02d_%02d%02d%02d", now.year(), now.month(), now.day(),
          now.hour(), now.minute(), now.second());

  dataString += dateTimeString;
  dataString += ",";
  dataString += String(bme.readTemperature());
  dataString += ",";
  dataString += String(bme.readPressure() / 100.0F);
  dataString += ",";
  dataString += String(bme.readHumidity());



  // open the file. note that only one file can be open at a time,
  // close this one before opening another.
  // File dataFile = SD.open("datalog.txt", FILE_WRITE); // This creates the file object
  // if the file is available, write to it:

  File dataFile = SD.open("Datalog.txt", FILE_WRITE);

  if (dataFile) {
    if (led_blink > 10) {
      // this is just to make sure that it is sill working
      digitalWrite(led, HIGH);
      led_blink = 0;
    }
    led_blink += 1;
    dataFile.println(dataString);
    dataFile.close();
    Serial.println(dataString); // mainly for testing

  }
  // if the file isn't open, pop up an error:
  // No idea why this part doesn't work correctly.
  else {
    for (int i = 0; i < 5; i++) {
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      delay(100);
    }
    Serial.println("error opening file");
  }
}









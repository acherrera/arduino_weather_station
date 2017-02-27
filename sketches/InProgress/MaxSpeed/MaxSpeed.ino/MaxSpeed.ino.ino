/*
  Combining date logger and BME 280 chip. This should get and log data
  Max Speed - no serial, no delay, no problem

  //TODO better implement the date and time methods
  //Maybe find better way of setting up the file system
  //TODO get LED working better - doesn't stop when chip is pulled


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

int led = 2;
int led_blink;
const int chipSelect = 10; // for datalogger
RTC_DS1307 rtc; //for time information
char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI for BME

void setup() {
  pinMode(led, OUTPUT); // Set LED pin
  bool status;
  status = bme.begin();

  // Make sure everything is working stop is not working
  if (!status) {
    while (1);
  }
  if (! rtc.begin()) {
    while (1);
  }
  if (! rtc.isrunning()) {
    while (1);
  }

  if (!SD.begin(chipSelect)) {
    while (1);
  }
  Serial.println("card initialized.");


  // if checks pass blink light a few times
  for (int i = 0; i < 10; i++) {
    digitalWrite(led, HIGH);
    delay(100);
    digitalWrite(led, LOW);
    delay(100);
  }
}


//Create the correct file



void loop() {
  // no delay - full speed ahead!

  String dataString = ""; 

  dataString += String(millis()); // time has now become milliseconds since start. For speed!
  dataString += ",";
  dataString += String(bme.readTemperature());
  dataString += ",";
  dataString += String(bme.readPressure() / 100.0F);
  dataString += ",";
  dataString += String(bme.readHumidity());



  // open the file. note that only one file can be open at a time,
  // close this one before opening another.
  // if the file is available, write to it:
  File dataFile = SD.open("Datalog.txt", FILE_WRITE);

  if (dataFile) {
    if (led_blink > 10) {
      // this is just to make sure that it is sill working
    }
    dataFile.println(dataString);
    dataFile.close();
  }
  // if the file isn't open, pop up an error:
  // No idea why this part doesn't work correctly.
  else {
    while (!dataFile) {
      //just keep trying I guess.
      File dataFile = SD.open("Datalog.txt", FILE_WRITE);
      for (int i = 0; i < 5; i++) {
        digitalWrite(led, HIGH);
        delay(100);
        digitalWrite(led, LOW);
        delay(100);
      }
    }
  }
}









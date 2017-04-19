  /*
  Anthony Herrera
  
  Scrapping together the BME180 logger, the SD card writer and the time function to make 
  a functioning data logger	 
 */
 
 
#include <SD.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085_U.h>
#include "RTClib.h"

Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified(10085);
RTC_DS1307 rtc;

int led = 5;
int n;  //Used for counting with the LED later
int p;
const int chipSelect = 10;

void setup(void)
{

  pinMode(10, OUTPUT);
  pinMode(5, OUTPUT);
  
 // Open serial communications and wait for port to open:
  Serial.begin(9600);

  
  // Testing SD card ============================================

  Serial.print("Initializing SD card...");
  // make sure that the default chip select pin is set to
  // output, even if you don't use it:
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    while(1); // stop the program
  }
  
  Serial.println("card initialized.");
  
  // Testing the BME180 sensor ==================================
  
  Serial.println("Pressure Sensor Test"); Serial.println("");
  
  /* Initialise the sensor */
  if(!bmp.begin())
  {
    /* There was a problem detecting the BMP085 ... check your connections */
    Serial.print("Ooops, no BMP085 detected ... Check your wiring or I2C ADDR!");
    while(1); // STOP THE PRESSES!!
  }  


  //Flash LED if everything turns on correctly
  for (int i =0; i < 10; i++){
    digitalWrite(led,HIGH);
    delay(100);
    digitalWrite(led,LOW);
    delay(100);
  }
}

void loop(void)
{
  // LED and delay handling ================================

  // To get different delay lengths, have to work this a little bit. 
  n+=1; // counts how many seconds since last write
  p+=1; // counts how many seconds since last blink
  
  if (p>=10){  // after ten loops - ten seconds - blink LED
    p=0;
    digitalWrite(led,HIGH);
  }

  // This causes the one second loop delay
  delay(1000);
  digitalWrite(led,LOW);

  // for testing
  Serial.print(n);
  Serial.print(" : ");
  Serial.println(p);

  //after 30 loops - 30 seconds - run the main portion
  if (n>=30) {
    n=0;
    // Get pressure data =====================================
    /* Get a new sensor event */ 
    sensors_event_t event;
    bmp.getEvent(&event);
   
    /* Display the results (barometric pressure is measure in hPa) */
    if (!event.pressure)
    {
      Serial.println("Sensor error");
    }
    
    /* Get a new sensor event */ 
    bmp.getEvent(&event);
   
  
    /* Display atmospheric pressue in hPa */
    float pressure = event.pressure;
  
    /* First we get the current temperature from the BMP085 */
    float temperature;
    bmp.getTemperature(&temperature);
    
    String dataString;
    
    DateTime now = rtc.now(); //For time Logging
    
    char dateTimeString[40];
    sprintf(dateTimeString, "%04d%02d%02d_%02d%02d%02d", now.year(), now.month(), now.day(),
            now.hour(), now.minute(), now.second());
            
  
    dataString += dateTimeString;
    dataString += ",";
    dataString += String(temperature);
    dataString += ",";
    dataString += String(pressure);
    dataString += ",";
    dataString += "M"; // relative humidity is missing. Doing it like ASOS
    
    
    Serial.println(dataString); // for testing
   
    
    // Writeto SD card ===================================
  
    // open the file. note that only one file can be open at a time,
    // so you have to close this one before opening another.
    File dataFile = SD.open("datalog.txt", FILE_WRITE);
  
    // if the file is available, write to it:
    if (dataFile) {
      dataFile.println(dataString);
      dataFile.close();
      // print to the serial port too:
    }
      
    // if the file isn't open, pop up an error:
    else {
      Serial.println("error opening datalog.txt");
      
    } 
  } 
}



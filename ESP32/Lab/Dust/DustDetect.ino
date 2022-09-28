/*
測試得到的資料和空氣品質對照：
3000 + = 很差
1050-3000 = 差
300-1050 = 一般
150-300 = 好
75-150 = 很好
0-75 = 非常好

https://www.taiwaniot.com.tw/product/sharp-%E5%8E%9F%E8%A3%9D%E5%A4%8F%E6%99%AE-gp2y1014au-pm2-5%E7%81%B0%E5%A1%B5%E7%B2%89%E5%A1%B5%E7%A9%BA%E6%B0%A3%E5%93%81%E8%B3%AA%E6%84%9F%E6%B8%AC%E5%99%A8/
*/
int dustPin=0;

float dustVal=0;
 
int ledPower=2;
int delayTime=280;
int delayTime2=40;
float offTime=9680;
void setup(){
Serial.begin(9600);
pinMode(ledPower,OUTPUT);
pinMode(dustPin, INPUT);
}
 
void loop(){
// ledPower is any digital pin on the arduino connected to Pin 3 on the sensor
digitalWrite(ledPower,LOW); 
delayMicroseconds(delayTime);
dustVal=analogRead(dustPin); 
delayMicroseconds(delayTime2);
digitalWrite(ledPower,HIGH); 
delayMicroseconds(offTime);
 
delay(1000);
if (dustVal>36.455)
Serial.println((float(dustVal/1024)-0.0356)*120000*0.035);
}
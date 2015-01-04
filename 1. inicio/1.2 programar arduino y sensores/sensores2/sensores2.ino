int motor = 3;
const int sensor1 = A0;
const int sensor2 = A2;
const int ledRojo = 12;
const int ledAzul = 9;
const int ledVerde = 10;
const int ledEmisor = 13;

//variables
long miliVolts1;
long miliVolts2;
long intensidad1;
long intensidad2;
int brillo1;
int brillo2;

void setup()
{
  Serial.begin(9600);
  pinMode(ledAzul, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledEmisor, OUTPUT);
}

void Velo0()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 0;
      analogWrite(motor, velocidad);
      delay(20);
}

void Velo1()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 5;
      analogWrite(motor, velocidad);
}

void Velo2()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 60;
      analogWrite(motor, velocidad);
}

void Velo3()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 75;
      analogWrite(motor, velocidad);
}

void Velo4()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 90;
      analogWrite(motor, velocidad);
}

void Velo5()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 105;
      analogWrite(motor, velocidad);
}

void Velo6()
{
      int  velocidad = map(velocidad,'0', '5', 0, 255);
      velocidad = 120;
      analogWrite(motor, velocidad);
      
}

void Inten1()
{
  miliVolts1 = (analogRead(sensor1) *3000L) /1023; //opteniendo el valor sensor
  intensidad1 =miliVolts1;
  brillo1 = map(intensidad1, 0, 250, 0, 255); //funcion map (mapeo) convierte la variable y le da un rango y un dominio
  brillo1 = constrain(brillo1, 0, 255); //funcion constrain o contenido en el intervalo de analogWrite (0, 255)
  analogWrite(ledAzul, brillo1 ); //Salida del led si esta el obstaculo esta lejos
  analogWrite(ledVerde, 255 - brillo1 ); //Salida del led si el obstaculo esta cerca
  Serial.print(" "); //salida al Serialport
  Serial.print(intensidad1);
  Serial.println(" ");
  delay (60);
}

void Inten2()
{
  miliVolts2 = (analogRead(sensor2) *3000L) /1023; //opteniendo el valor sensor
  intensidad2 =miliVolts2;
  brillo2 = map(intensidad2, 0, 250, 0, 255); //funcion map (mapeo) convierte la variable y le da un rango y un dominio
  brillo2 = constrain(brillo2, 0, 255); //funcion constrain o contenido en el intervalo de analogWrite (0, 255)
  digitalWrite(ledEmisor, HIGH);
  analogWrite(ledAzul, brillo2 ); //Salida del led si esta el obstaculo esta lejos
  analogWrite(ledVerde, 255 - brillo2 ); //Salida del led si el obstaculo esta cerca
  Serial.print(" "); //salida al Serialport
  Serial.print(intensidad2);
  Serial.println(" ");
  delay (60);
}

void inicio()
{
  digitalWrite(ledRojo, HIGH);   // turn the LED on (HIGH is the voltage level)
  analogWrite(ledAzul, LOW);
  analogWrite(ledVerde, LOW);
  delay(150);               // wait for a second
  digitalWrite(ledRojo, LOW);    // turn the LED off by making the voltage LOW
  analogWrite(ledAzul, LOW);
  analogWrite(ledVerde, LOW);
  delay(150);
}

void Menu()
{
  
  char opcion = Serial.read();
  switch (opcion )
  {
    case 'a': 
            
              
              while(opcion=='a')
              {
                inicio();
                Velo0();
                Menu();              
              }
              break;
              
      case 'b': 
            
              
              while(opcion=='b')
              {
                inicio();
                Velo1();
                Menu();              
              }
              break;
              
      case 'c': 
             while(opcion=='b')
              {
                inicio();
                Velo2();
                Menu();              
              }
              break;
 
     case 'd': 
            while(opcion=='d')
              {
                inicio();
                Velo3();
                Menu();              
              }
              break;
              
      case 'e': 
              while(opcion=='e')
              {
                inicio();
                Velo4();
                Menu();              
              }
              break;
              
      case 'f': 
              while(opcion=='f')
              {
                inicio();
                Velo5();
                Menu();              
              }
              break;
 
      case 'g': 
              while(opcion=='g')
              {
                inicio();
                Velo6();
                Menu();              
              }
              break;
              
      case 'h': 
              while(opcion=='h')
              {
                Velo0();
                Inten1();
                Menu();              
              }
              break;
              
      case 'i': 
              while(opcion=='i')
              {
                Velo1();
                Inten1();
                Menu();              
              }
              break;
 
     case 'j': 
            while(opcion=='j')
              {
                Velo2();
                Inten1();
                Menu();              
              }
              break;
              
      case 'k':
                
              while(opcion=='k')
              {
                Velo3();
                Inten1();
                Menu();             
              }
              break;
              
      case 'l': 
              while(opcion=='l')
              {
                Velo4();
                Inten1();
                Menu();              
              }
              break;
       
       case 'm': 
              while(opcion=='m')
              {
                Velo5();
                Inten1();
                Menu();              
              }
              break;
              
      case 'n': 
              while(opcion=='n')
              {
                Velo6();
                Inten1();
                Menu();              
              }
              break;
 
     case 'z': 
            while(opcion=='z')
              {
                Velo0();
                Inten2();
                Velo0();
                Menu();              
              }
              break;
              
      case 'o': 
              while(opcion=='o')
              {
                Velo1();
                Inten2();
                Menu();              
              }
              break;
              
      case 'p': 
              while(opcion=='p')
              {
                Velo2();
                Inten2();
                Menu();              
              }
              break;
 
    case 'q': 
            while(opcion=='q')
              {
                Velo3();
                Inten2();
                Menu();              
              }
              break;
              
      case 'r': 
              while(opcion=='r')
              {
                Velo4();
                Inten2();
                Menu();              
              }
              break;
              
      case 's': 
              while(opcion=='s')
              {
                Velo5();
                Inten2();
                Menu();              
              }
              break; 
              
      case 't': 
              while(opcion=='t')
              {
                Velo6();
                Inten2();
                Menu();              
              }
              break; 
 
   }
  
}

void loop()
{
  
  inicio();
  Menu();
    
}

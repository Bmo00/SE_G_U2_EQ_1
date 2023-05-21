int P1 = 2 , P2 = 3, P3 = 4, P4 = 5, P5=6, P6=7, P7=8, P8=9 ;
//p1 boton arriba, p2 boton abajo, p3 boton izquierda, p4 boton derecha, p5 select, p6 start, p7 B, P8 A
void setup() {
  pinMode(P1,INPUT_PULLUP);
  pinMode(P2,INPUT_PULLUP);
  pinMode(P3,INPUT_PULLUP);
  pinMode(P4,INPUT_PULLUP);
  pinMode(P5,INPUT_PULLUP);
  pinMode(P6,INPUT_PULLUP);
  pinMode(P7,INPUT_PULLUP);
  pinMode(P8,INPUT_PULLUP);

  Serial.begin(9600);
  Serial.setTimeout(10);
}

int sA,sB,sC, sD, sE, sF, sG, sH;
void loop() {
  sA=digitalRead(P1)==1?0:1;
  sB=digitalRead(P2)==1?0:1;
  sC=digitalRead(P3)==1?0:1;
  sD=digitalRead(P4)==1?0:1;
  sE=digitalRead(P5)==1?0:1;
  sF=digitalRead(P6)==1?0:1;
  sG=digitalRead(P7)==1?0:1;
  sH=digitalRead(P8)==1?0:1;

  //Armar la cadena que se enviara
  String cadena = String(sA)+" "+String(sB)+" "+String(sC)+" "+String(sD)+" "+String(sE)+" "+String(sF)+" "+String(sG)+" "+String(sH);
  Serial.println(cadena);
  delay(100);
}

#define BUTTON_PIN    A1
#define LED_PIN       A0

#define DELAY_TIME    100
#define DEBOUNCE_TIME 1000

void setup()
{
  delay(5000);
  
  Serial.begin(9600);
  Serial.println("Beginning...");
  
  pinMode(BUTTON_PIN, INPUT);
  digitalWrite(BUTTON_PIN, HIGH); // connect internal pull-up

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
}

boolean handle_button()
{
  int button_pressed = !digitalRead(BUTTON_PIN); // pin low -> pressed
  return button_pressed;
}

void loop()
{
  // handle button
  boolean button_pressed = handle_button();

  if (button_pressed)
  {
    Serial.println("press");
    delay(DEBOUNCE_TIME);
  }
  
  while (Serial.available())
  {
    char cmd = Serial.read();
    
    if (cmd == '1')
    {
      digitalWrite(LED_PIN, LOW);
    }
    else if (cmd == '0')
    {
      digitalWrite(LED_PIN, HIGH);
    }
  }

  delay(DELAY_TIME);
}




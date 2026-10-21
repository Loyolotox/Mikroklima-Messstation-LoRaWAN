# 🌡️  Microclimate Monitoring (LoRaWAN)

Dies ist ein modularer Baustein unseres Hauptprojekts **„Rasenpflege leicht gemacht!“**. Es konzentriert sich auf die Erfassung von Umgebungsdaten in Echtzeit mithilfe eines **BME280-Sensormoduls**, das direkt auf Höhe der Grasnarbe am Mähroboter angebracht ist.

---

## 📊 Ziel des Teilprojekts

Druck, relative Luftfeuchtigkeit und Temperatur direkt am Boden weichen oft stark von den normalen Wetterdaten ab. Diese Werte helfen uns dabei:
- **Trocken- und Hitzestress zu erkennen:** Hohe Feuchtigkeit und spezifische Temperaturen beeinflussen das Rasenwachstum und das Pilzrisiko.
- **Optimale Zeitfenster für Düngung & Bewässerung zu finden:** Dünger darf nicht bei extremer Hitze/Sonne ausgebracht werden. Die Temperaturkurven zeigen die besten Zeitpunkte.
- **Energieeffiziente Datenübertragung:** Über funkbasierte Telemetrie (LoRa/LoRaWAN) werden die Messwerte stromsparend an den Server übertragen.

---

## 📈 Live-Telemetrie & Dashboard-Beispiel

Das folgende Diagramm zeigt die erfassten Sensordaten unseres Testaufbaus (gehostet über unsere IoT-Plattform auf `loramint.de`). Es dokumentiert den Verlauf von Luftdruck, Luftfeuchtigkeit und Temperatur über mehrere Tage:

<img width="1214" height="468" alt="Bildschirmfoto_2026-10-21_20-22-38" src="https://github.com/user-attachments/assets/9f471f7c-b16f-4d2f-92ef-0156fe481a95" />


*Diese Umgebungsdaten werden später direkt mit den Messwerten des optischen NIR-Sensors und den Bodenfeuchtesensoren kombiniert, um den Zustand des Rasens präzise zu kartieren.*

---

## 📂 Struktur 

<img width="4202" height="3358" alt="grafik" src="https://github.com/user-attachments/assets/f61bb659-6905-4eab-97c0-f424e1490a4f" />


ESP32 ↔ LA66 (Funkmodul)
ESP32	LA66
GPIO17 (TX = Senden)	RX (PIN 11)
GPIO16 (RX = Empfangen)	TX (PIN 10)
GND (Minus)	GND
3V3 (Strom)	3V3

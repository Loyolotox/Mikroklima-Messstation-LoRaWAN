

import machine
from machine import Pin

import ds18x20
import onewire
from loramint import LoRaMINT, MintValue

UPLINK_INTERVAL = 60  # seconds of deep sleep between measurements

# DS18B20 on a 1-Wire bus (ESP32-S3 pin; change to match your board)
ONEWIRE_DATA = 4

# Stop bridge: connect this pin to GND (a jumper wire is enough) to keep the
# cycle from starting. Deep sleep leaves the board reachable for only the few
# seconds it is awake, which makes it hard to interrupt from Thonny or mpremote;
# with the bridge in place the program ends right here and hands you the REPL.
#
# Pick a free pin, never a strapping pin - on the ESP32-S3 those are GPIO0, 3,
# 45 and 46. They are sampled at reset, and waking from deep sleep *is* a reset,
# so a bridge on one of them would put the board into download mode instead.
STOP_PIN = 5

LOCATION = "Raum 101"


def sleep_until_next_cycle():
    """Enter deep sleep. Never returns - the ESP32 restarts on wake-up."""
    machine.deepsleep(UPLINK_INTERVAL * 1000)


# Checked before anything else, so the bridge works even when the sensor, the
# LA66 or the wiring is at fault.
if not Pin(STOP_PIN, Pin.IN, Pin.PULL_UP).value():
    raise SystemExit("Stop bridge on GPIO{} - cycle not started.".format(STOP_PIN))

bus = ds18x20.DS18X20(onewire.OneWire(Pin(ONEWIRE_DATA)))

# Every failure has to end in deep sleep too. A node that just stops here stays
# awake at full clock until the battery is empty - more expensive than running
# normally - and never gets a second chance.
roms = bus.scan()
if not roms:
    print("No DS18B20 on the 1-Wire bus - retrying after deep sleep.")
    sleep_until_next_cycle()
rom = roms[0]  # use the first sensor on the bus

lora = LoRaMINT()

if not lora.check_connection():
    print("No UART connection to the LA66 - retrying after deep sleep.")
    sleep_until_next_cycle()

print("Joining LoRaWAN network...")
if not lora.join():
    print("Join failed - retrying after deep sleep.")
    sleep_until_next_cycle()
print("Joined.")

if machine.reset_cause() != machine.DEEPSLEEP_RESET:
    # Cold start only: after a wake-up this would be sent on every cycle. A
    # press on RST counts as a cold start, which is intended - it makes an
    # unplanned restart visible in the backend.
    #
    # The first measurement follows in the next cycle: sending it right after
    # the log entry would make it fail on the LA66's receive windows.
    if lora.sendLog("ESP32 gestartet"):
        print("Log entry sent.")
    sleep_until_next_cycle()

# Trigger a conversion, then wait for it (>=750 ms at 12-bit resolution). The
# sensor converts on its own, so the ESP32 can spend the wait in light sleep.
bus.convert_temp()
machine.lightsleep(750)
temperature = bus.read_temp(rom)

if lora.sendValue(MintValue(temperature, "*C", LOCATION, "Temperatur", "DS18B20")):
    print("Measurement sent:", temperature)

sleep_until_next_cycle()

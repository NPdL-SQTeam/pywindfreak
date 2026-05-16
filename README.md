# pywindfreak

Python drivers for Windfreak Technologies RF signal generators: [SynthHD Mini](https://windfreaktech.com/product/synthhd-mini/) (single-channel) and [SynthHD / SynthHD PRO](https://windfreaktech.com/product/microwave-signal-generator/) (dual-channel).

## Installation

Install from a private GitHub repository using a classic Personal Access Token (PAT):

```bash
pip install git+https://<PAT>@github.com/NPdL-SQTeam/pywindfreak.git
```

Replace `<PAT>` with your GitHub Personal Access Token (classic).

## Usage

Pass the bare port name — the driver resolves the full path automatically (e.g. `"tty.usbmodemXXXX"` on macOS, `"ttyACM0"` on Linux, `"COM6"` on Windows).

### SynthHD Mini (single channel)

```python
from pywindfreak import SynthHDMini, ReferenceMode

# On init: rf_enable=False, reference_mode=ReferenceMode.INTERNAL_27MHZ
synth = SynthHDMini("COM6")

synth.reference_mode = ReferenceMode.INTERNAL_27MHZ
synth.frequency = 1e9   # Hz
synth.power = -10.0     # dBm
synth.rf_enable = True

synth.rf_enable = False
synth.close()
```

### SynthHD / SynthHD PRO (dual channel)

```python
from pywindfreak import SynthHD, ReferenceMode

# On init: both channels rf_enable=False, reference_mode=ReferenceMode.EXTERNAL,
#          external reference frequency set to 10 MHz
synth = SynthHD("COM6")

synth[0].frequency = 1e9    # channel A, Hz
synth[0].power = -10.0      # dBm
synth[0].rf_enable = True

synth[1].frequency = 2e9    # channel B, Hz
synth[1].power = 0.0
synth[1].rf_enable = True

synth[0].rf_enable = False
synth[1].rf_enable = False
synth.close()
```

### `ReferenceMode` values

| Value | Description |
|---|---|
| `ReferenceMode.EXTERNAL` | External reference |
| `ReferenceMode.INTERNAL_27MHZ` | Internal 27 MHz reference |
| `ReferenceMode.INTERNAL_10MHZ` | Internal 10 MHz reference |

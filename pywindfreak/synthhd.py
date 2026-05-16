import os

import serial

from .enums import ReferenceMode


def _resolve_port(port: str) -> str:
    if os.name != "nt" and not port.startswith("/"):
        return f"/dev/{port}"
    return port


class _Channel:
    def __init__(self, device: "SynthHD", index: int) -> None:
        self._device = device
        self._index = index

    def _select(self) -> None:
        self._device._send(f"C{self._index}")

    @property
    def frequency(self) -> float:
        """Frequency in Hz."""
        self._select()
        return float(self._device._query("f?")) * 1e6

    @frequency.setter
    def frequency(self, freq_hz: float) -> None:
        self._select()
        self._device._send(f"f{freq_hz / 1e6:.6f}")

    @property
    def power(self) -> float:
        """Output power in dBm."""
        self._select()
        return float(self._device._query("W?"))

    @power.setter
    def power(self, power_dbm: float) -> None:
        self._select()
        self._device._send(f"W{power_dbm:.2f}")

    @property
    def rf_enable(self) -> bool:
        self._select()
        return bool(int(self._device._query("E?")))

    @rf_enable.setter
    def rf_enable(self, enabled: bool) -> None:
        self._select()
        self._device._send(f"E{1 if enabled else 0}")


class SynthHD:
    """Driver for the Windfreak Technologies SynthHD and SynthHD PRO signal generators."""

    def __init__(self, port: str, timeout: float = 1.0) -> None:
        self._serial = serial.Serial(_resolve_port(port), baudrate=9600, timeout=timeout)
        self._channels = [_Channel(self, 0), _Channel(self, 1)]
        for ch in self._channels:
            ch.rf_enable = False
        self.reference_mode = ReferenceMode.EXTERNAL
        self._send("*10.0")

    def __getitem__(self, index: int) -> _Channel:
        return self._channels[index]

    def close(self) -> None:
        self._serial.close()

    def _send(self, cmd: str) -> None:
        self._serial.write(cmd.encode())

    def _query(self, cmd: str) -> str:
        self._send(cmd)
        return self._serial.readline().decode().strip()

    @property
    def reference_mode(self) -> ReferenceMode:
        return ReferenceMode(int(self._query("P?")))

    @reference_mode.setter
    def reference_mode(self, mode: ReferenceMode) -> None:
        self._send(f"P{int(mode)}")

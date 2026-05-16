import os

import serial

from .enums import ReferenceMode


def _resolve_port(port: str) -> str:
    if os.name != "nt" and not port.startswith("/"):
        return f"/dev/{port}"
    return port


class SynthHDMini:
    """Driver for the Windfreak Technologies SynthHD Mini signal generator."""

    def __init__(self, port: str, timeout: float = 1.0) -> None:
        self._serial = serial.Serial(_resolve_port(port), baudrate=9600, timeout=timeout)
        self.rf_enable = False
        self.reference_mode = ReferenceMode.INTERNAL_27MHZ

    def close(self) -> None:
        self.rf_enable = False
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

    @property
    def rf_enable(self) -> bool:
        return bool(int(self._query("E?")))

    @rf_enable.setter
    def rf_enable(self, enabled: bool) -> None:
        self._send(f"E{1 if enabled else 0}")

    @property
    def frequency(self) -> float:
        """Frequency in Hz."""
        return float(self._query("f?")) * 1e6

    @frequency.setter
    def frequency(self, freq_hz: float) -> None:
        self._send(f"f{freq_hz / 1e6:.6f}")

    @property
    def power(self) -> float:
        """Output power in dBm."""
        return float(self._query("W?"))

    @power.setter
    def power(self, power_dbm: float) -> None:
        self._send(f"W{power_dbm:.2f}")

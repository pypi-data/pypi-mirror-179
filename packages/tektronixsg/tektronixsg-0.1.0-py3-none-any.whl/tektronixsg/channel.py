import time

SIGNAL_TYPES_AFG1022 = {"sine": "SIN", "square": "SQU", "pulse": "PULS",
                        "ramp": "RAMP", "noise": "PRN", "dc": "DC",
                        "memory1": "EMEM"}

SIGNAL_TYPES_AFG31000 = {"sine": "SIN", "square": "SQU", "pulse": "PULS",
                         "ramp": "RAMP", "noise": "PRN", "dc": "DC",
                         "gauss": "GAUS", "lorentz": "LOR",
                         "expo rise": "ERIS", "expo decay": "EDEC",
                         "haversine": "HAV", "memory1": "EMEM",
                         "memory2": "EMEM2"}

BURST_MODE = {"triggered": "TRIG", "gated": "GAT"}

PULSE_HOLD = {"width": "WIDT", "duty": "DUTY"}


class Channel:
    """Class that represents the channel of the signal generator.

    Attributes:
        generator: Reference of :class:`.SignalGenerator`.
        channel_number (int): Number of the channel.

    .. note::
        In order to set a voltage of a signal there are two options. Use
        either the properties voltage_max and voltage_min or voltage_offset
        and voltage_amplitude. Both options are equivalent, but trying set
        the desired voltage in combination is not recommended. As an
        example, if you manipulate voltage_max, voltage_offset
        and voltage_amplitude automatically get modified as well.

    """
    def __init__(self, generator, channel_number):
        """Initialize the signal generator.

        Args:
            generator: Reference of the :class:`.SignalGenerator` object.
            channel_number (str): Number of the channel.
        """
        self.generator = generator
        self.channel_number = channel_number

    @property
    def output_on(self):
        """Enable or disable the output."""
        return self.generator.query_bool("OUTP{}?".format(self.channel_number))

    @output_on.setter
    def output_on(self, value):
        self.generator.write(
            "OUTP{} {}".format(self.channel_number, int(value)))

    @property
    def voltage_max(self):
        """Set or get the maximum voltage of the current signal in Volt.

        Not supported by the AFG1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:VOLT:HIGH?".format(self.channel_number))

    @voltage_max.setter
    def voltage_max(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:VOLT:HIGH {}".format(self.channel_number, value))

    @property
    def voltage_min(self):
        """Set or get the minimum voltage of the current signal in Volt.

        Not supported by the AFG1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:VOLT:LOW?".format(self.channel_number))

    @voltage_min.setter
    def voltage_min(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:VOLT:LOW {}".format(self.channel_number, value))

    @property
    def voltage_offset(self):
        """Set or get the voltage offset."""
        return self.generator.query_float(
            "SOUR{}:VOLT:OFFS?".format(self.channel_number))

    @voltage_offset.setter
    def voltage_offset(self, value):
        self.generator.write(
            "SOUR{}:VOLT:OFFS {}".format(self.channel_number, value))

    @property
    def voltage_amplitude(self):
        """Set the amplitude (range) of the signal."""
        return self.generator.query_float(
            "SOUR{}:VOLT?".format(self.channel_number))

    @voltage_amplitude.setter
    def voltage_amplitude(self, value):
        self.generator.write(
            "SOUR{}:VOLT {}".format(self.channel_number, value))

    @property
    def signal_type(self):
        """Set or get type of the signal.

        Possible options are stated in SIGNAL_TYPES for the different devices.
        """
        if self.generator.connected_device == "AFG1022":
            signal_types = SIGNAL_TYPES_AFG1022
        elif self.generator.connected_device == "AFG31052":
            signal_types = SIGNAL_TYPES_AFG31000
        value = self.generator.query_str(
            "SOUR{}:FUNC?".format(self.channel_number))
        for item in signal_types.items():
            if item[1] == value:
                return item[0]

    @signal_type.setter
    def signal_type(self, value):
        if self.generator.connected_device == "AFG1022":
            signal_types = SIGNAL_TYPES_AFG1022
        elif self.generator.connected_device == "AFG31052":
            signal_types = SIGNAL_TYPES_AFG31000
        self.generator.write(
            "SOUR{}:FUNC {}".format(self.channel_number, signal_types[value]))

    @property
    def impedance(self):
        """Set or get the impedance of the output in Ohm."""
        return self.generator.query_float(
            "OUTP{}:IMP?".format(self.channel_number))

    @impedance.setter
    def impedance(self, value):
        self.generator.write(
            "OUTP{}:IMP {}".format(self.channel_number, value))

    @property
    def frequency(self):
        """Set or get the frequency of the signal."""
        return self.generator.query_float(
            "SOUR{}:FREQ?".format(self.channel_number))

    @frequency.setter
    def frequency(self, value):
        self.generator.write(
            "SOUR{}:FREQ {}".format(self.channel_number, value))

    @property
    def phase(self):
        """Set or get the phase of the signal in radiant."""
        return self.generator.query_float(
            "SOUR{}:PHAS?".format(self.channel_number))

    @phase.setter
    def phase(self, value):
        self.generator.write(
            "SOUR{}:PHAS {}".format(self.channel_number, value))

    @property
    def burst_on(self):
        """Enable or disable the burst mode.

        Only supported by the first channel of the AFG1022.
        """
        if self.generator.connected_device == "AFG1022" and \
                self.channel_number == "2":
            raise NotImplementedError
        return self.generator.query_bool(
            "SOUR{}:BURS:STAT?".format(self.channel_number))

    @burst_on.setter
    def burst_on(self, value):
        if self.generator.connected_device == "AFG1022" and \
                self.channel_number == "2":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:BURS:STAT {}".format(self.channel_number, int(value)))

    @property
    def burst_mode(self):
        """Set or get the burst mode. Possible options are stated in
        BURST_MODE.

        Only supported by the first channel of the AFG1022.
        """
        if self.generator.connected_device == "AFG1022" and \
                self.channel_number == "2":
            raise NotImplementedError
        value = self.generator.query_str(
            "SOUR{}:BURS:MODE?".format(self.channel_number))
        for item in BURST_MODE.items():
            if item[1] == value:
                return item[0]

    @burst_mode.setter
    def burst_mode(self, value):
        if self.generator.connected_device == "AFG1022" and \
                self.channel_number == "2":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:BURS:MODE {}".format(self.channel_number,
                                         BURST_MODE[value]))

    @property
    def burst_cycles(self):
        """Set or get the amount of burst cycles.

        Only supported by the first channel of the AFG1022.
        """
        if self.generator.connected_device == "AFG1022" and \
                self.channel_number == "2":
            raise NotImplementedError
        return self.generator.query_int(
            "SOUR{}:BURS:NCYC?".format(self.channel_number))

    @burst_cycles.setter
    def burst_cycles(self, value):
        self.generator.write(
            "SOUR{}:BURS:NCYC {}".format(self.channel_number, value))

    @property
    def burst_delay(self):
        """Set or get the burst delay in seconds.

        Not supported by the AFG1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:BURS:TDEL?".format(self.channel_number))

    @burst_delay.setter
    def burst_delay(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:BURS:TDEL {}".format(self.channel_number, value))

    @property
    def pulse_width(self):
        """Set or get the pulse width in seconds.

        Available for the signal type "pulse".

        Not supported by the AFG1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:PULS:WIDT?".format(self.channel_number))

    @pulse_width.setter
    def pulse_width(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:PULS:WIDT {}".format(self.channel_number, value))

    @property
    def pulse_duty(self):
        """Get or set the duty cycle of the pulse in percent.

        Minimum steps are 0.1%.

        Available for the the signal type "pulse".

        The duty cycle is essentially the same as th pulse width. By
        multiplying the duty cycle with the period you get the
        pulse width.
        """
        return self.generator.query_float(
            "SOUR{}:PULS:DCYC?".format(self.channel_number))

    @pulse_duty.setter
    def pulse_duty(self, value):
        self.generator.write(
            "SOUR{}:PULS:DCYC {}".format(self.channel_number, value))

    @property
    def pulse_delay(self):
        """Get or set the delay of the pulse.

        Available for the the signal type "pulse".

        Not supported by the AFG1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:PULS:DEL?".format(self.channel_number))

    @pulse_delay.setter
    def pulse_delay(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:PULS:DEL {}".format(self.channel_number, value))

    @property
    def pulse_hold(self):
        """Get or set the pulse hold.

        Pulse hold decides whether the width setting or the duty setting
        should be kept when manipulating the signal period (frequency).

        Not supported by the AFG 1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        value = self.generator.query_str(
            "SOUR{}:PULS:HOLD?".format(self.channel_number))
        for item in PULSE_HOLD.items():
            if item[1] == value:
                return item[0]

    @pulse_hold.setter
    def pulse_hold(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:PULS:HOLD {}".format(self.channel_number,
                                         PULSE_HOLD[value]))

    @property
    def pulse_period(self):
        """Set or get the pulse period in seconds.

        Available for the the signal type "pulse".

        Is equivalent to 1/:meth:`frequency`.
        """
        if self.generator.connected_device == "AFG1022":
            return 1/self.frequency
        else:
            return self.generator.query_float(
                "SOUR{}:PULS:PER?".format(self.channel_number))

    @pulse_period.setter
    def pulse_period(self, value):
        if self.generator.connected_device == "AFG1022":
            self.frequency = 1/value
        else:
            self.generator.write(
                "SOUR{}:PULS:PER {}".format(self.channel_number, value))

    @property
    def pulse_leading_transition(self):
        """Set or get the leading pulse transition in seconds.

        The leading transition is the time it takes for a pulse to reach its
        maximum.

        Available for the the signal type "pulse".

        Not supported by the AFG 1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:PULS:TRAN:LEAD?".format(self.channel_number))

    @pulse_leading_transition.setter
    def pulse_leading_transition(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:PULS:TRAN:LEAD {}".format(self.channel_number, value))

    @property
    def pulse_trailing_transition(self):
        """Set or get the trailing pulse transition in seconds.

        The trailing transition is the time it takes for a pulse to reach its
        minimum.

        Available for the the signal type "pulse".

        Not supported by the AFG 1022.
        """
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        return self.generator.query_float(
            "SOUR{}:PULS:TRAN:TRA?".format(self.channel_number))

    @pulse_trailing_transition.setter
    def pulse_trailing_transition(self, value):
        if self.generator.connected_device == "AFG1022":
            raise NotImplementedError
        self.generator.write(
            "SOUR{}:PULS:TRAN:TRA {}".format(self.channel_number, value))

    def set_arbitrary_signal(self, voltage_vector):
        """Convenience method to instantly set an arbitrary signal with an
        one dimensional vector for the voltage.

        Args:
            voltage_vector (numpy.ndarray): Voltage vector as numpy array.
        """
        # Memory number corresponds to channel number,
        # selecting memory 1 on channel 2 is not possible
        memory = self.channel_number
        if len(voltage_vector) > 8192:
            raise ValueError("Maximum waveform length is 8192")
        if len(voltage_vector) < 2:
            raise ValueError("Minimum waveform length is 2")
        min_voltage = min(voltage_vector)
        max_voltage = max(voltage_vector)
        voltage_range = abs(max_voltage-min_voltage)
        voltage_offset = (min_voltage+max_voltage)/2
        normed_voltage = abs(voltage_vector-min_voltage)/voltage_range
        tmp = 16383*normed_voltage
        voltage_bits = tmp.astype(int)
        self.generator.write_data_emom(voltage_bits, memory)
        time.sleep(0.2)
        self.signal_type = "memory{}".format(memory)
        self.voltage_amplitude = voltage_range
        self.voltage_offset = voltage_offset

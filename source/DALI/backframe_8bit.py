class Backframe8Bit:
    def __init__(self, frame, address_field_width):
        self.address_string = " " * address_field_width
        self.command_string = f"DATA 0x{frame:02X} = {frame:3} = {frame:08b}b"

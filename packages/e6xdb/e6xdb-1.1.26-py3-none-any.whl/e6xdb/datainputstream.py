import struct
import logging
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)


class DataInputStream:
    def __init__(self, stream):
        self.stream = stream

    def read_boolean(self):
        return struct.unpack('?', self.stream.read(1))[0]

    def read_bytes(self, byte_array):
        for i in range(len(byte_array)):
            byte_array[i] = struct.unpack('B', self.stream.read(1))[0]
        return byte_array

    def read_int_96(self):
        return struct.unpack('B', self.stream.read(12))[0]

    def read_byte(self):
        return struct.unpack('b', self.stream.read(1))[0]

    def read_unsigned_byte(self):
        return struct.unpack('B', self.stream.read(1))[0]

    def read_char(self):
        return chr(struct.unpack('>H', self.stream.read(2))[0])

    def read_double(self):
        return struct.unpack('>d', self.stream.read(8))[0]

    def read_float(self):
        return struct.unpack('>f', self.stream.read(4))[0]

    def read_short(self):
        return struct.unpack('>h', self.stream.read(2))[0]

    def read_unsigned_short(self):
        return struct.unpack('>H', self.stream.read(2))[0]

    def read_long(self):
        return struct.unpack('>q', self.stream.read(8))[0]

    def read_utf(self):
        utf_length = struct.unpack('>H', self.stream.read(2))[0]
        return self.stream.read(utf_length)

    def read_int(self):
        return struct.unpack('>i', self.stream.read(4))[0]

    def read_unsigned_int(self):
        return struct.unpack('>I', self.stream.read(4))[0]


def get_query_columns_info(buffer):
    result_meta_bytes = DataInputStream(buffer)
    rowcount = result_meta_bytes.read_long()
    field_count = result_meta_bytes.read_int()
    columns_description = list()

    for i in range(field_count):
        col = result_meta_bytes.read_utf().decode()
        col += ":" + result_meta_bytes.read_utf().decode()
        columns_description.append(col)

    return rowcount, columns_description


def read_values_from_array(query_columns_description: list, dis: DataInputStream) -> list:
    value_array = list()
    for i in query_columns_description:
        dtype = i.split(":")[1].upper()
        isPresent = dis.read_byte()
        if isPresent == 0:
            value_array.append(None)
            continue
        try:
            if dtype == "LONG":
                value_array.append(dis.read_long())
            elif dtype == "DATE":
                epoch_days = dis.read_long() * 86400
                date = datetime.fromtimestamp(epoch_days)
                value_array.append(date.strftime("%Y-%m-%d"))
            elif dtype == "DATETIME":
                epoch_days = dis.read_long() / 1000_000
                date_time = datetime.fromtimestamp(epoch_days)
                value_array.append(date_time.strftime("%Y-%m-%d %H:%M:%S"))
            elif dtype == "STRING":
                value_array.append(dis.read_utf().decode())
            elif dtype == "INT":
                value_array.append(dis.read_int())
            elif dtype == "DOUBLE":
                value_array.append(dis.read_double())
            elif dtype == "BINARY":
                value_array.append(dis.read_utf())
            elif dtype == "FLOAT":
                value_array.append(dis.read_float())
            elif dtype == "CHAR":
                value_array.append(dis.read_char())
            elif dtype == "BOOLEAN":
                value_array.append(dis.read_boolean())
            elif dtype == "SHORT":
                value_array.append(dis.read_short())
            elif dtype == "BYTE":
                value_array.append(dis.read_byte())
            elif dtype == "INT96":
                julian_day = dis.read_int()
                time = dis.read_long()
                date_time = datetime.fromtimestamp((julian_day - 2440588) * 86400)
                date_time_with_nanos = date_time + timedelta(microseconds=(time / 1000))
                value_array.append(date_time_with_nanos.strftime("%Y-%m-%d %H:%M:%S"))
            elif dtype == "INTEGER":
                value_array.append(dis.read_int())
        except Exception as e:
            _logger.error(e)
            value_array.append('Failed to parse.')

    return value_array


def read_rows_from_batch(query_columns_description: list, dis: DataInputStream):
    is_row_present = dis.read_byte()
    if not is_row_present:
        return None
    rows = list()
    while is_row_present == 1:
        if is_row_present:
            row = read_values_from_array(query_columns_description, dis)
            rows.append(row)
            #   if rows become 1000, break it
            # if len(rows) == 1000:
            #     _logger.info("Read Batch - Breaking the loop after 1000 records")
            #     break
        is_row_present = dis.read_byte()
    return rows

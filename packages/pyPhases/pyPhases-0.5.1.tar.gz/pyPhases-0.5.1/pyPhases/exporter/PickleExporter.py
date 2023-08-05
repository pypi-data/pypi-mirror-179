import pickle

from pyPhases.exporter.DataExporter import DataExporter

class PickleExporter(DataExporter):
    supportedTypes = []

    try:
        import pandas
        supportedTypes.append(pandas.DataFrame)
    except ImportError: pass

    try:
        import numpy
        supportedTypes.append(numpy.ndarray)
    except ImportError: pass

    """ An Exporter that supports a lot of default formats using pyarrow"""

    def checkType(self, type):
        return type in self.supportedTypes or issubclass(type, (str, int, bool, float, list, dict, tuple))

    def importData(self, byteString, options={}):
        return pickle.loads(byteString)

    def export(self, object, options={}):
        return pickle.dumps(object)

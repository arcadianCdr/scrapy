from scrapy.exporters import JsonItemExporter
from scrapy.utils.python import to_bytes

class SceneItemExporter(JsonItemExporter):

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',')
            self._beautify_newline()
        itemdict = dict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict)
        self.file.write(to_bytes('"{}": '.format(str(item['id']).replace(":", "_")) + data, self.encoding))


from dingdian.items import DingdianItem


class DingDianPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,DingdianItem):
            name_id = item['name_id']
            ret = Sql.sele
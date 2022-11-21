from odoo import api, fields, models

def _get_uid_from_group(self,group_id):
    sql = """
    select uid from res_groups_users_rel where gid = %s
    """ % (group_id)
    self._cr.execute(sql)
    res = self._cr.dictfetchall()
    res = [x['uid']for x in res]
    return res
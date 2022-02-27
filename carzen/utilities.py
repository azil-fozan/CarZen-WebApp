from django.db import connections


class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)


def execute_read_query(query):
    cursor = connections['default'].cursor()
    data=[]
    try:
        cursor.execute(query)
        data = cursor.fetchall()
    except Exception as e:
        pass
    cursor.close()
    return data
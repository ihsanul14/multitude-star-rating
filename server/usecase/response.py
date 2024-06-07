def resp(data):
    res = {}
    res['code'] = data['code']
    if data["code"] == 200:
        res["success"] = True
    else:
        data["success"] = False
    if 'data' in res.keys():
        res['data'] = data['data']
    return res

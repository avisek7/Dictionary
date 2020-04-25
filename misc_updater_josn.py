import json,sys,copy
# update_path = "pradr.addr"
# update_path = "pradr.addr.building_details"
update_path = "."
# keys_for_update = {"st":"street","loc":"locality","bno":"block_number"}
# keys_for_update = {"flno":"floor_number","lt":"latitude","lg":"longitude","adadr":""}
keys_for_update = {"stjCd":"state_jurisdiction_code","dty":"tax_payer_type","lgnm":"legal_name","sts":""}
json_data = {"stjCd":"PY001","stj":"Goods Division - I (Pondicherry Municipality)I","dty":"Regular","lgnm":"RITHWIK PROJECTS PRIVATE LIMITED","gstin":"34AABCR5748L1Z1","cxdt":"01/12/2018","nba":["Works Contract"],"lstupdt":"01/01/2019","rgdt":"12/10/2018","ctb":"Private Limited Company","pradr":{"addr":{"bnm":"","st":"SWAMINATHA NAICKER STREET","loc":"ARIYANKUPPAM","bno":"NO. 113","stcd":"Puducherry","dst":"Pondicherry","city":"","pncd":"605007","building_details":{"flno":"","lt":"","lg":"","adadr":[]}},"ntr":"Works Contract"},"ctjCd":"XQ0105","tradeNam":"RITHWIK PROJECTS PRIVATE LIMITED","sts":"Cancelled","ctj":"RANGE I-E"}
def process_update_json(update_path,keys_for_update,json_data):
    print "Before Update Json DATA","\n",json.dumps(json_data)
    try:
        data = copy.deepcopy(json_data)
        update_path = update_path.split('.')
        if len(update_path) > 0 and update_path[0] != "": #trying to find the inner dictonary where the key's has to update
            for i in update_path:
                if i in data:
                    data = data.get(i)
            for j in keys_for_update: #updating the dictionary to with all new key's
                new_key = keys_for_update.get(j)
                val_fr_new_key = data.get(j)
                del data[j]
                if new_key != "": 
                    data[new_key] = val_fr_new_key
            sub = json_data
            for k in update_path[:-1]: # altering the data with newly created inner dictionary 
                sub = sub[k]
            del sub[update_path[-1]]
            sub[update_path[-1]] = data
        else:
            for l in keys_for_update:   #updating the keys only for outer keys
                root_new_key = keys_for_update.get(l)
                root_val_for_new_key = json_data.get(l)
                del json_data[l]
                if root_new_key != "":
                    json_data[root_new_key] = root_val_for_new_key
        print "\n\n\nAfter Update Json DATA\n",json.dumps(json_data)
    except Exception as e:
            print e
    return json.dumps(json_data)

#input parameter's  - 
    # 1. update_path - this argument will the JSON path where we have to update the key, means the path to find the inner dictionary where we have to update the keys
    # 2. keys_for_update - this will be a dictionary where we have to send the mapping for old key and new key ex - {"old_key1": "new_key1","old_key2":""}, also you can delete a old key which you don't want to keep in the data the pass it as old_key2
    # 3. json_data - The JSON data where we have to update the keys.

ab = process_update_json(update_path,keys_for_update,json_data)
# print "\n\n",ab


local cjson = require 'cjson'

jsonfile="/home/c-nrong/VQA/HieCoAttenVQA/data/vqa_raw_test.json"
local file = io.open(jsonfile, 'r')
local text = file:read()
file:close()
local info = cjson.decode(text)
print(#info)
print(info[1])

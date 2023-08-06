# ESET Connect

## API Docs
http://epcpublicapi-test.westeurope.cloudapp.azure.com/swagger/

## Quickstart

### Install
```bash
pip install esetconnect
```

### Get detections
```python
from esetconnect import EsetConnect

USERNAME = "username"
PASSWORD = "password"

with EsetConnect(USERNAME, PASSWORD) as ec:
    for detection in ec.get_detections().detections:
        print(detection.json())
```

```json
{
   "category":"DETECTION_CATEGORY_UNSPECIFIED",
   "context":{
      "circumstances":"Event occurred on a modified file.",
      "device_uuid":"83c7522f-f4a7-4a80-a055-8e1329201129",
      "process":{
         "path":"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
      },
      "user_name":"DESKTOP-7DAP322\\username"
   },
   "display_name":"Eicar",
   "network_communication":null,
   "object_hash_sha1":"3395856CE81F2B7382DEE72602F798B642F14140",
   "object_name":"file:///C:/Users/username/AppData/Local/Temp/2f7545df-d894-4768-8741-944d7ef059f6.tmp",
   "object_type_name":"File",
   "object_url":"",
   "occur_time":"2022-12-07T09:26:13",
   "responses":{
      "description":null,
      "device_restart_required":null,
      "display_name":null,
      "protection_name":null
   },
   "severity_level":"SEVERITY_LEVEL_MEDIUM",
   "type_name":"nil",
   "uuid":"ec879237-d1c3-3742-ecab-05fed9ea9a58"
}
```

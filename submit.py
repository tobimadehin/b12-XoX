import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

SECRET = b"hello-there-from-b12"
URL = "https://b12.io/apply/submission"

payload = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "name": "Emmanuel Madehin",
    "email": "emmanuelmadehin@gmail.com",
    "resume_link": "https://drive.google.com/file/d/1_r1GwHnYAfnycblcyr1yhqwVR5b28gME/view?usp=sharing",
    "repository_link": "https://github.com/tobimadehin/b12-XoX",
    "action_run_link": "WILL_BE_FILLED_FROM_GITHUB_ACTION"
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True)

signature = hmac.new(
    SECRET,
    body.encode(),
    hashlib.sha256
).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}"
}

response = requests.post(URL, data=body, headers=headers)
response.raise_for_status()

print("RECEIPT:")
print(response.text)

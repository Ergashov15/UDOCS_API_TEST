from dotenv import get_key
from pathlib import Path
from credentials.credential_data import TIN_PIN
file_path = Path("guid_id")
guid = get_key(str(file_path), "GUID")

document_create_payloads={
  "document": {
    "template": "cyber_sec_test",
    "data": {
      "number": "TSH-101",
      "date": "2025-07-11",
      "contract_number": "mjmXt",
      "contract_date": "2025-07-11",
      "service_bank_manager_name": "77cKN",
      "credit_user_name": "DvW9g",
      "service_bank_stir": 129,
      "district": "j10DD",
      "service_bank_name": "kqK1D",
      "credit_user_org_name": "wJyIL",
      "credir_user_org_stir": 117
    }
  },
  "signers": [
    {
      "tin_pin": TIN_PIN
    }
  ]
}

document_access_payloads={
  "guid": guid,
  "tin_pin": TIN_PIN,
  "redirect_url": "https://api.udocs.realtest.uz/api/client/document/access"}
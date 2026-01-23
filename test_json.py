import json
import re

response_str = '{"fr":{"translation":"orage","confidence_score":0.97},"es":{"translation":"tormenta eléctrica","confidence_score":0.98},"de":{"translation":"Gewitter","confidence_score":0.99},"fi":{"translation":"salama-arkku","confidence_score":0.92},"ru":{"translation":"грозовой шторм","confidence_score":0.95},"ua":{"translation":"гроза","confidence_score":0.96},"it":{"translation":"temporale con tuono","confidence_score":0.95},"pt":{"translation":"tempestade de raios","confidence_score":0.95},"bs":{"translation":"grmljavina","confidence_score":0.92},"ch":{"translation":"雷暴","confidence_score":0.99}}'

print(f"String length: {len(response_str)}")
try:
    res = json.loads(response_str)
    print("Direct json.loads worked")
except Exception as e:
    print(f"Direct json.loads failed: {e}")
    match = re.search(r'\{.*\}', response_str, re.DOTALL)
    if match:
        try:
            res = json.loads(match.group(0))
            print("Regex fallback worked")
        except Exception as e2:
            print(f"Regex fallback failed: {e2}")
    else:
        print("Regex match failed")

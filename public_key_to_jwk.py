from jwcrypto import jwk
from cryptography.hazmat.primitives import serialization

# Load the PEM public key
with open("public_key.pem", "rb") as f:
    pem_data = f.read()

# Create JWK from PEM
key = jwk.JWK.from_pem(pem_data)
jwk_json = key.export(private_key=False)

# Add the "alg" property
import json
jwk_dict = json.loads(jwk_json)
jwk_dict['alg'] = 'RS256'

# Print the updated JWK
print(json.dumps(jwk_dict, indent=2))
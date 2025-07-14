from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from encryptor import encrypt_text, decrypt_text
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve static HTML files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

# Request models
class InputText(BaseModel):
    text: str

class EncryptedText(BaseModel):
    encrypted_text: str

# Encrypt Endpoint
@app.post("/encrypt")
def encrypt_endpoint(input_data: InputText):
    try:
        encrypted = encrypt_text(input_data.text)
        print(f"Input: {input_data.text} → Encrypted: {encrypted}")
        return {"encrypted_text": encrypted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Decrypt Endpoint
@app.post("/decrypt")
def decrypt_endpoint(data: EncryptedText):
    try:
        decrypted = decrypt_text(data.encrypted_text)
        print(f"Encrypted: {data.encrypted_text} → Decrypted: {decrypted}")
        return {"decrypted_text": decrypted}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Invalid encrypted string or key.")

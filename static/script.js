async function encryptText() {
    const text = document.getElementById("inputText").value;
    const response = await fetch("/encrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    document.getElementById("outputText").value = data.encrypted_text || "Error encrypting.";
}

async function decryptText() {
    const encrypted = document.getElementById("inputText").value;
    const response = await fetch("/decrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ encrypted_text: encrypted })
    });

    const data = await response.json();
    document.getElementById("outputText").value = data.decrypted_text || "Error decrypting.";
}

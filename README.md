# Encryption
Encrypt your keys on your local computer for [trader1.co](https://trader1.co).

1. Create account on [app.trader1.co](https://app.trader1.co).
2. Get your api keys from your exchange.
3. Encrypt your keys as described here.
4. Create exchange with encrypted credentials on Trader1.

## Requirements

### Ubuntu / Debian
```
sudo apt install python3-pip
pip3 install pycrypto
```

## Encrypt Your Keys

```
git clone https://github.com/Trader1bot/encryption.git
cd encryption/
python trader1-encrypt.py
```

### Example

[![asciicast](https://asciinema.org/a/EnRSDY39tJc9eamLxhYLltOp9.png)](https://asciinema.org/a/EnRSDY39tJc9eamLxhYLltOp9)

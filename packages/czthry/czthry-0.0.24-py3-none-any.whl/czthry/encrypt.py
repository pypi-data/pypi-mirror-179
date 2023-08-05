import rsa
import base64


# encrypt

def _encrypt(content: str, public_key: rsa.PublicKey) -> str:
    encrypted = rsa.encrypt(content.encode(), public_key)
    result = base64.b64encode(encrypted).decode('utf-8')
    return result

def encrypt_by_key(content: str, public_key_str: str) -> str:
    public_key_bytes = public_key_str.encode()
    public_key = rsa.PublicKey.load_pkcs1(public_key_bytes)
    result = _encrypt(content, public_key)
    return result

def encrypt_by_pem(content: str, public_pem: str) -> str:
    try:
        with open(public_pem, 'r') as file:
            public_key_str = file.read()
    except:
        return None
    return encrypt_by_key(content, public_key_str)

# decrypt

def _decrypt(secret: str, private_key: rsa.PrivateKey) -> str:
    decrypted = base64.b64decode(secret.encode())
    result = rsa.decrypt(decrypted, private_key).decode()
    return result

def decrypt_by_key(secret: str, private_key_str: str) -> str:
    private_key_bytes = private_key_str.encode()
    private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes)
    result = _decrypt(secret, private_key)
    return result

def decrypt_by_pem(secret: str, private_pem: str) -> str:
    try:
        with open(private_pem, 'r') as file:
            private_key_str = file.read()
    except:
        return None
    return decrypt_by_key(secret, private_key_str)

# make public/private key pem

def generate_keys(name: str='') -> (rsa.PublicKey, rsa.PrivateKey):
    public_key, private_key = rsa.newkeys(1024)
    public = public_key.save_pkcs1('PEM')  # default 'PEM'
    private = private_key.save_pkcs1('PEM')
    if name:
        prefix = name + '_'
        with open(prefix+'public_key.pem', 'wb') as file:
            file.write(public)
        with open(prefix+'private_key.pem', 'wb') as file:
            file.write(private)
    return public_key, private_key

# test

def test1():
    # public, private = generate_keys('test')
    public = '''
    -----BEGIN RSA PUBLIC KEY-----
    MIGJAoGBAIDZn/enhx0RRdNioXblQBywJJSuvcIwF8NPXcBaaplD6einSeC2NzoX
    N2sda4nO25hajiQBD41t2a0g5jP4nF1WWnya9ketnJXLZjotRd8VvxI3Swk+9tSQ
    vcJGBEfzhJ9iUuuygHM7SnxzPosDWm9VtYEJsUIavldLWZ4p4X/nAgMBAAE=
    -----END RSA PUBLIC KEY-----
    '''
    private = '''
    -----BEGIN RSA PRIVATE KEY-----
    MIICYAIBAAKBgQCA2Z/3p4cdEUXTYqF25UAcsCSUrr3CMBfDT13AWmqZQ+nop0ng
    tjc6FzdrHWuJztuYWo4kAQ+NbdmtIOYz+JxdVlp8mvZHrZyVy2Y6LUXfFb8SN0sJ
    PvbUkL3CRgRH84SfYlLrsoBzO0p8cz6LA1pvVbWBCbFCGr5XS1meKeF/5wIDAQAB
    AoGAG2CiObfR4J477OdHEYEydyYCD8l1Ll6Tnf8uF2HexoQEnld1PhbZczFdqBfP
    Mq/OPvf2vbWv/Uf6+WtE+zCWH9n1EG3zXme/DhQ2XYG7+unst4il+srtwrPkW8HA
    eci3Cgys0ximi7DkewLjKuJdS9/PcQf5WFZLllpythB5MgkCRQCmQVnvNuZPUl0Y
    WSDn5+9JYzC9pjS0o4ZS3MKSKET+hIellTRuAPgaK5os3a9DBwabSGo5ZN46J+Kt
    bSmxgxk0EN1VRQI9AMZnShZsGt3OK4vvj6Vmd+zfsdDhlbuGL2Ih/O91pWWh8J2B
    ANFw6vlqfXoDqHTegd8MG8IxFCPyP2qFOwJFAIL1QUk73minASvXsSLbQFJ3boJE
    tImBsaH9wMnuLIKrlEnq4JSx8Lx0kgo7SP2sQBj7DqlM+funRVfEgC4SjTzE+ANd
    Ajw+h6k6/eFNzL++v8bnGy9q0Wmqap6VVooyhIHCOrLhIDPEgDbwy4TTDPP085gx
    FTubP6a0AmHVnnDMMqcCRDv3fzyM1cFm3Uc2RV7IqJUC2ekVbDn2MKfUnBlJs6hk
    25fcLCtYJYYAZvLBcUg/bb7bNwZfAmTBWtYOxiXlO9JT9HAI
    -----END RSA PRIVATE KEY-----
    '''

    s = "hello, world"
    ss = encrypt_by_key(s, public)
    print(ss)

    s = decrypt_by_key(ss, private)
    print(s)

def test2():
    public, private = generate_keys()
    s = "hello, world"
    ss = _encrypt(s, public)
    print(ss)

    s = _decrypt(ss, private)
    print(s)

def test3():
    s = "hello, world"
    ss = encrypt_by_pem(s, 'test_public_key.pem')
    print(ss)

    s = decrypt_by_pem(ss, 'test_private_key.pem')
    print(s)

if __name__ == '__main__':
    test3()

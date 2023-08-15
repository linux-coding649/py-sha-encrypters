import hashlib

# v0.0.2a written by Ethan Su / linux649 on 15.08.2023 using GPL v2 or higher

def py_sha_256(ste):
    '''A hashlib-powered function to convert inputs to a hexadecimal-digested sha256 string'''
    return hashlib.sha256(str(ste).encode()).hexdigest()

def py_sha_384(ste):
    '''A hashlib-powered function to convert inputs to a hexadecimal-digested sha384 string'''
    return hashlib.sha384(str(ste).encode()).hexdigest()

def py_sha_512(ste):
    '''A hashlib-powered function to convert inputs to a hexadecimal-digested sha512 string'''
    return hashlib.sha512(str(ste).encode()).hexdigest()

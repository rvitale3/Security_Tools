#!/usr/bin/env python3

# Title: Key/CSR pair generation from data contained in old x509 certificates   
# Date: 2024-06-26
# Author: Rubenangel Vitale
# Version: 1.0

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import os

# Function to load and decode an existing certificate
def load_certificate(cert_path):
    """
    Load the x509 certificate
    ---------
    Arguments
    ---------
    cert_path    : will be provided from the list text file.
    ---------
    Returns
    ---------
    cert  :  return the loaded certificate from file list.
    """
    with open(cert_path, 'rb') as cert_file:
        cert_data = cert_file.read()
        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    return cert

# Function to extract subject values from the certificate
def get_subject_info(cert):
    """
    Extract the certificate subject information.
    ---------
    Arguments
    ---------
    cert    : To use the cert returned from fnc load_certificate.
    ---------
    Returns
    ---------
    subject_info  :  return the extracted subject information from the cert.
    """
    subject = cert.subject
    subject_info = {}
    for oid in [NameOID.COMMON_NAME, NameOID.COUNTRY_NAME, NameOID.STATE_OR_PROVINCE_NAME,
                NameOID.LOCALITY_NAME, NameOID.ORGANIZATION_NAME, NameOID.ORGANIZATIONAL_UNIT_NAME,
                NameOID.EMAIL_ADDRESS]:
        try:
            subject_info[oid] = subject.get_attributes_for_oid(oid)[0].value
        except IndexError:
            subject_info[oid] = None
    return subject_info

# Function to generate a new key pair
def generate_key_pair():
    """
    Generates a RSA private key 2048 bits.
    ---------
    Arguments
    ---------
    No Arguments
    ---------
    Returns
    ---------
    private_key  :  return a 2048 bits RSA private key.
    """    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

# Function to create a CSR
def create_csr(private_key, subject_info):
    """
    Creates a Certificate Signing Request derived frmo the newly create Private Key
    and the information extracted from the certificate from the list.
    ---------
    Arguments
    ---------
    private_key    : Uses the 2048 bits RSA private key generated.
    subject_info   : The subject information extracted from the certificate
    ---------
    Returns
    ---------
    csr  :  return the Certificate Signing Request.
    """
    name_attributes = []
    for oid, value in subject_info.items():
        if value:
            name_attributes.append(x509.NameAttribute(oid, value))
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name(name_attributes)).sign(private_key, hashes.SHA256(), default_backend())
    return csr

# Function to save the private key and CSR to files
def save_to_files(private_key, csr, key_path, csr_path):
    """
    Creates a Certificate Signing Request derived frmo the newly create Private Key
    and the information extracted from the certificate from the list.
    ---------
    Arguments
    ---------
    private_key    : Uses the 2048 bits RSA private key generated.
    key_path       : The system path where the new key will be stored, by default is
                    /path/output/base_name_key.pem
    csr            : Uses the CSR generated derived from the new key and the old cert
                     information
    csr_path       : The system path where the new CSR will be stored, by default
                    /path/output/base_name_csr.pem
    ---------
    Returns
    ---------
    No returns but stored the key and csr in the OS file system.
    """
    # Save the private key
    with open(key_path, 'wb') as key_file:
        key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    # Save the CSR
    with open(csr_path, 'wb') as csr_file:
        csr_file.write(csr.public_bytes(serialization.Encoding.PEM))

# Main function
def main(cert_list_path, output_dir):
    """
    Main function where all other functions are called.
    ---------
    Arguments
    ---------
    cert_list_path   : Uses a list of certificate files, the data is parsed as a txt list of 
                       certificates.
    output_dir       : Hardcoded as "output" if the directory does not exist, it is created 
                       when first run
    ---------
    Returns
    ---------
    No returns but prints the file system path where the Key and the CSR are stored.
    """
    with open(cert_list_path, 'r') as f:
        cert_paths = f.read().splitlines()

    for cert_path in cert_paths:
        if not os.path.exists(cert_path):
            print(f"Certificate file {cert_path} not found. Skipping...")
            continue

        cert = load_certificate(cert_path)
        subject_info = get_subject_info(cert)
        private_key = generate_key_pair()
        csr = create_csr(private_key, subject_info)

        # Generate output file paths
        base_name = os.path.basename(cert_path)
        base_name = base_name.split(".")[0]
        key_path = os.path.join(output_dir, f"{base_name}_key.pem")
        csr_path = os.path.join(output_dir, f"{base_name}_csr.pem")

        save_to_files(private_key, csr, key_path, csr_path)
        print(f"New key and CSR for {cert_path} have been saved to {key_path} and {csr_path} respectively.")

# Replace 'cert_list.txt' and 'output' with your actual file list path and desired output directory
if __name__ == "__main__":
    cert_list_path = 'cert_list.txt'
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    main(cert_list_path, output_dir)

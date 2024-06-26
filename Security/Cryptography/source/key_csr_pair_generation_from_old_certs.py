from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import os

# Function to load and decode an existing certificate
def load_certificate(cert_path):
    with open(cert_path, 'rb') as cert_file:
        cert_data = cert_file.read()
        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    return cert

# Function to extract subject values from the certificate
def get_subject_info(cert):
    subject = cert.subject
    subject_info = {}
    for oid in [NameOID.COMMON_NAME, NameOID.COUNTRY_NAME, NameOID.STATE_OR_PROVINCE_NAME,
                NameOID.LOCALITY_NAME, NameOID.ORGANIZATION_NAME, NameOID.ORGANIZATIONAL_UNIT_NAME,
                NameOID.EMAIL_ADDRESS]:
        try:
            subject_info[oid._name] = subject.get_attributes_for_oid(oid)[0].value
        except IndexError:
            subject_info[oid._name] = None
    return subject_info

# Function to generate a new key pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

# Function to create a CSR
def create_csr(private_key, subject_info):
    name_attributes = []
    for oid_name, value in subject_info.items():
        if value:
            oid = getattr(NameOID, oid_name)
            name_attributes.append(x509.NameAttribute(oid, value))
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name(name_attributes)).sign(private_key, hashes.SHA256(), default_backend())
    return csr

# Function to save the private key and CSR to files
def save_to_files(private_key, csr, key_path, csr_path):
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
        key_path = os.path.join(output_dir, f"new_{base_name}_key.pem")
        csr_path = os.path.join(output_dir, f"new_{base_name}_csr.pem")

        save_to_files(private_key, csr, key_path, csr_path)
        print(f"New key and CSR for {cert_path} have been saved to {key_path} and {csr_path} respectively.")

# Replace 'cert_list.txt' and 'output' with your actual file list path and desired output directory
if __name__ == "__main__":
    cert_list_path = 'cert_list.txt'
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    main(cert_list_path, output_dir)

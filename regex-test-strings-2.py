regex_test_strings = {
    "phone_fax_valid": [
        "123-456-7890",
        "(123) 456-7890",
        "+1 123 456 7890",
        "1234567890",
    ],
    "phone_fax_invalid": [
        "123-45-6789",
        "123 456 789",
        "12345678901",
    ],
    "email_valid": [
        "user@example.com",
        "user.name+tag@example.co.uk",
        "user-name@example.org",
    ],
    "email_invalid": [
        "user@example",
        "user@.com",
        "@example.com",
    ],
    "ssn_valid": [
        "123-45-6789",
        "123456789",
    ],
    "ssn_invalid": [
        "123-45-678",
        "12345-6789",
        "123-456-789",
    ],
    "med_records_valid": [
        "MR12345678",
        "MED-987-654-321",
        "MEDREC-ABC-123",
    ],
    "med_records_invalid": [
        "MR1234",
        "MED-12345",
        "MEDREC123",
    ],
    "health_plan_valid": [
        "ABC123456789",
        "XYZ-987-654-321",
        "HPBN-123-45-6789",
    ],
    "health_plan_invalid": [
        "HP12345",
        "HPBN-123",
        "123456789",
    ],
    "account_numbers_valid": [
        "1234567890",
        "ACCT-123-456-789",
        "A1B2C3D4E5F6",
    ],
    "account_numbers_invalid": [
        "ACCT-123",
        "12345",
        "ABCDEFGHIJ",
    ],
    "cert_license_valid": [
        "ABC-123-XYZ",
        "LIC1234567890",
        "CERT-A1B2C3D4",
    ],
    "cert_license_invalid": [
        "LIC-123",
        "CERT123",
        "ABC-XYZ",
    ],
    "vehicle_id_valid": [
        "1HGCM82633A004352",
        "WAUEH74F77N904530",
        "JH4TB2H26CC000000",
    ],
    "vehicle_id_invalid": [
        "1HGCM82633A0043",
        "WAUEH74F77N9045301",
        "JH4TB2H26CC",
    ],
    "serial_numbers_valid": [
        "SN1234567890",
        "ABC-123-XYZ-789",
        "SERIAL-A1B2C3D4",
    ],
    "serial_numbers_invalid": [
        "SN-123",
        "SERIAL123",
        "ABC-XYZ",
    ],
    "device_id_valid": [
        "DEV-1234567890",
        "DEVICE-ABC-123-XYZ",
        "DID:A1B2C3D4E5F6",
    ],
    "device_id_invalid": [
        "DEV-123",
        "DEVICE123",
        "DID:",
    ],
    "web_urls_valid": [
        "https://www.example.com",
        "http://subdomain.example.co.uk/page",
        "https://example.org/path/to/page?param=value",
    ],
    "web_urls_invalid": [
        "www.example.com",
        "https://example",
        "http://.com",
    ],
    "ipv4_valid": [
        "192.168.0.1",
        "10.0.0.255",
        "172.16.0.1",
    ],
    "ipv4_invalid": [
        "256.0.0.1",
        "192.168.0",
        "1.2.3.4.5",
    ],
    "ipv6_valid": [
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        "fe80::1ff:fe23:4567:890a",
        "::1",
    ],
    "ipv6_invalid": [
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334:5678",
        "fe80::1ff:fe23:4567:890a:1234",
        ":::",
    ]
}

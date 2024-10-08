regex_patterns = {
    "phone_fax_regex": r"^\+?1?\s*\(?[2-9]\d{2}\)?[-.\s]?\d{3}[-.\s]?\d{4}$",
    
    "email_regex": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    
    "ssn_regex": r"^(?!000|666|9\d{2})\d{3}-?(?!00)\d{2}-?(?!0000)\d{4}$",
    
    "med_records_regex": r"^(MR|MED|MEDREC)[-]?\d{6,8}$",
    
    "health_plan_regex": r"^[A-Z]{3,5}[-]?\d{9,12}$",
    
    "account_numbers_regex": r"^(ACCT[-]?)?\d{8,12}$",
    
    "cert_license_regex": r"^(([A-Z]{3,5}[-]?)?\d{6,12})|([A-Z]{1,5}[-]?\d{1,5}[-]?[A-Z]{1,5}[-]?\d{1,5})$",
    
    "vehicle_id_regex": r"^[A-HJ-NPR-Z0-9]{17}$",
    
    "serial_numbers_regex": r"^(SN|SERIAL)[-]?[A-Z0-9]{8,12}$",
    
    "device_id_regex": r"^(DEV|DEVICE|DID)[-:]?[A-Z0-9]{8,16}$",
    
    "web_urls_regex": r"^(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$",
    
    "ipv4_regex": r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
    
    "ipv6_regex": r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"
}

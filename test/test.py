import tools

assert tools.en_name_validator("Artemiss") == True
assert tools.en_name_validator("Artemiss86") == False

assert tools.fa_name_validator("آرتمیس ل") == True
assert tools.fa_name_validator("آرتمیسA") == False

assert tools.en_family_validator("Lotfi") == True
assert tools.en_family_validator("Ltfi132ش") == False

assert tools.fa_family_validator("لطفی") == True
assert tools.fa_family_validator("لطفی 86") == False

assert tools.address_validator("saadatabad ,pelak 12") == True
assert tools.address_validator("pelak 12") == False

assert tools.mobile_validator("09944981902") == True
assert tools.mobile_validator("9126853385") == False

assert tools.email_validator("artemiss8686@gmail.com") == True
assert tools.email_validator("artemiss.com") == False

assert tools.national_code_validator("0183734885") == True
assert tools.national_code_validator("9384756") == False

assert tools.postal_code_validator("9375103865") == True
assert tools.postal_code_validator("0000000000") == False
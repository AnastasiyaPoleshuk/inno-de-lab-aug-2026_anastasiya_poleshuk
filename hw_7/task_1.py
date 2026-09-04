raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

def transform_str(string_val, sep, divider, prefix):
    uid, name, city, status = [s.strip() for s in string_val.split(sep)]

    uid = f"{prefix}{uid}"
    name = name.title().replace("_", " ")
    city = city.upper()
    status = status.lower()

    return divider.join([uid, name, city, status])


print(transform_str(raw_user_record, ";", " | ", "UID-"))

raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

def transform_str(string_val, sep, divider, prefix):
    str_arr = string_val.split(sep)
    
    for i in range(len(str_arr)):
        s = str_arr[i].strip().title()
        
        if i == 0:
            s = f"{prefix}{s}"
        elif i == 1:
            s = s.replace("_", " ")
        elif i == 2:
            s = s.upper()
        elif i == 3:
            s = s.lower()
            
        str_arr[i] = s

    return divider.join(str_arr)


print(transform_str(raw_user_record, ";", " | ", " UID-"))
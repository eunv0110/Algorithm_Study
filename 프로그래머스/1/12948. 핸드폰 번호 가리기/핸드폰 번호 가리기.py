def solution(phone_number):
    phone_number_end=phone_number[-4:]
    phnoe_number_star=''.join(list('*' for _ in range(len(phone_number[:-4]))))
    return phnoe_number_star+phone_number_end
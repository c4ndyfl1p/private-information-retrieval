import numpy as np

#using matrices (when you have m samples)


def sampleLWE(m,n,q,error_values, s):
    A= np.random.randint(0, q, (m,n))
    
    e= np.random.normal(error_values["loc"], error_values["sigma"], (m) )

    print(f"A = {A}")
    print(f"s = {s}")
    # print(f"e = {e}")


    # Computing the dot product and adding the error

    # Outputting the vectors a, s and the value b

    b = (np.dot(A,s)  + e ) % q
    print(f"b = As + e mod q = {b}")
    # b_prime = (np.dot(A,s) % q + e) % q


    return A, b

# Encryption

def regevEncrypt(b, x, p, q):
    scaling_factor = np.floor(q/p)
    c =( b + scaling_factor*x ) 
    c_mod_q = c % q

    

    # print(f"c= As + e + (floor(q/p) * x) \n \\ \
    # = As + e + {scaling_factor}*{x} = {c} = {c_mod_q}")

    return c_mod_q

#Decryption

# print(np.dot(a, s), np.dot(a,s) % q)

def rounding(x, round_off_to):
    """
    Rounds off a number x to the nearest multiple of round_off_to.

    :param x: The number to be rounded off.
    :param round_off_to: The nearest multiple to which x needs to be rounded off.
    :return: The rounded off value.
    """
    return np.round(x / round_off_to) * round_off_to

def regevDecrpt(A, s, q, p, c):
    scaling_factor = np.floor(q/p)
    # a_s_mod_q = np.dot(A,s)%q 
    # print(f"a_s_modq = as mod q = ", a_s_mod_q)

    d_hat = (c - np.dot(A, s)) % q 

    # print(f"d_hat = c - as mod q= {c} - {np.dot(A,s)} mod q = ", d_hat)
    rounded_d = rounding(d_hat, scaling_factor)



    # print(f"rounded d = {rounded_d}")
    
    d = rounded_d / scaling_factor

    for i in range(d.shape[0]):
        if d[i] == 991:
            d[i]=0

    # print(f"d = rounded_d/ floor(q/p)= {rounded_d}/ {scaling_factor} = {d}" )

    

    return d 







# void mod_exp(const Bignum& exponent, const Bignum& mod) {
# 	//TODO IMPLEMENT THIS PLEASE
#     Bignum Y(1);
#     while(exponent > 1){
#       Digit square[2 * DIGITS]
#       if(exponent.is_odd()){
#         exponent -= 1;
#         Y *= *this;
#       }
#       simple_mult(square, _data, _data);
#       (*this) = (square) % mod;
#       exponent.divide_by_two();
#     }
#     (*this) *= Y;
# 	}

def mod_exp(base, exponent, mod):
    y = 1
    while exponent > 1:
        if exponent % 2:
            exponent -= 1
            y *= base
            y %= mod
        base *= base
        base %= mod
        exponent //= 2
    return (base * y) % mod

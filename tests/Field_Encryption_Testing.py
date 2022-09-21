
import ElGamalEllipticCurves.modNum as md
import ElGamalEllipticCurves.EllipticCurve as ellip
import ElGamalEllipticCurves.ElGamalEncryption as eg
import pytest



#Testing Addition
def test_add_same_field():
    assert (md.modNum(3,7) + md.modNum(5,7)) == md.modNum(1,7)

def test_add_same_field_reverse():
    assert (md.modNum(5,7) + md.modNum(3,7)) == md.modNum(1,7)

def test_add_dif_field():
    with pytest.raises(AssertionError):
        (md.modNum(3,7) + md.modNum(3,5))

def test_add_dif_field_reverse():
    with pytest.raises(AssertionError):
        (md.modNum(3,5) + md.modNum(3,7))

def test_add_zero_same_field():
    assert (md.modNum(3,7) + md.modNum(0,7)) == md.modNum(3,7)

def test_add_zero_same_field_reverse():
    assert (md.modNum(3,7) + md.modNum(0,7)) == md.modNum(3,7)



#Testing Subtraction
def test_sub_same_field():
    assert (md.modNum(3,7) - md.modNum(5,7)) == md.modNum(5,7)

def test_sub_same_field_reverse():
    assert (md.modNum(5,7) - md.modNum(3,7)) == md.modNum(2,7)

def test_sub_dif_field():
    with pytest.raises(AssertionError):
        (md.modNum(3,7) - md.modNum(3,5))

def test_sub_dif_field_reverse():
    with pytest.raises(AssertionError):
        (md.modNum(3,5) - md.modNum(3,7))

def test_sub_zero_same_field():
    assert (md.modNum(3,7) - md.modNum(0,7)) == md.modNum(3,7)

def test_sub_zero_same_field_reverse():
    assert (md.modNum(0,7) - md.modNum(3,7)) == md.modNum(4,7)




#Testing Multiplication
def test_mul_same_field():
    assert (md.modNum(3,7) * md.modNum(5,7)) == md.modNum(1,7)

def test_mul_same_field_reverse():
    assert (md.modNum(5,7) * md.modNum(3,7)) == md.modNum(1,7)

def test_mul_dif_field():
    with pytest.raises(AssertionError):
        (md.modNum(3,7) * md.modNum(3,5))

def test_mul_dif_field_reverse():
    with pytest.raises(AssertionError):
        (md.modNum(3,5) * md.modNum(3,7))

def test_mul_one_same_field():
    assert (md.modNum(3,7) * md.modNum(1,7)) == md.modNum(3,7)

def test_mul_one_same_field_reverse():
    assert (md.modNum(3,7) * md.modNum(1,7)) == md.modNum(3,7)




#Testing Division
def test_div_same_field():
    assert (md.modNum(3,7) / md.modNum(5,7)) == md.modNum(2,7)

def test_div_same_field_reverse():
    assert (md.modNum(5,7) / md.modNum(3,7)) == md.modNum(4,7)

def test_div_dif_field():
    with pytest.raises(AssertionError):
        (md.modNum(3,7) / md.modNum(3,5))

def test_div_dif_field_reverse():
    with pytest.raises(AssertionError):
        (md.modNum(3,5) / md.modNum(3,7))

def test_div_one_same_field():
    assert (md.modNum(3,7) / md.modNum(1,7)) == md.modNum(3,7)

def test_div_one_same_field_reverse():
    assert (md.modNum(1,7) / md.modNum(3,7)) == md.modNum(5,7)



#Testing Equality
def test_equals_same():
    assert (md.modNum(3,7) == md.modNum(3,7)), "Equals Test Fails"
    
def test_equals_dif_value():
    assert (not(md.modNum(3,7) == md.modNum(5,7))), 'Equals Dif Value Fails'

def test_equals_dif_field():
    assert ( not(md.modNum(3,7) == md.modNum(3,5))), 'Equals Dif Field Fails'

def test_equals_dif_field_dif_value():
    assert ( not(md.modNum(2,7) == md.modNum(3,5))), 'Equals Dif Field Dif Value Fails'

def test_equals_dif_value_reverse():
    assert (not(md.modNum(5,7) == md.modNum(3,7))), 'Equals Dif Value Fails'

def test_equals_dif_field_reverse():
    assert ( not(md.modNum(3,5) == md.modNum(3,7))), 'Equals Dif Field Fails'

def test_equals_dif_field_dif_value_reverse():
    assert ( not(md.modNum(3,5) == md.modNum(2,7))), 'Equals Dif Field Dif Value Fails'



#Testing String Representation
def test_print():
    assert str(md.modNum(3,7)) == "3 in Field N7"



#Testing Init
# Note: Regular init cases are well covered above, will only further test edge cases
def test_init_base():
    assert (md.modNum(3,7) is not md.modNum(3,7)), "A is B and it shouldn't be"

def test_init_non_int_value():
    with pytest.raises(AssertionError):
        md.modNum(3.5,7)

def test_init_non_int_prime():
    with pytest.raises(AssertionError):
        md.modNum(3,7.5)

def test_init_non_int_value_non_int_prime():
    with pytest.raises(AssertionError):
        md.modNum(3.5,7.5)

def test_init_zero_prime():
    with pytest.raises(Exception):
        md.modNum(3,0)

def test_init_value_greater_than_prime():
    assert md.modNum(9,7) == md.modNum(2,7), 'Allowing init to values outside of field'

def test_init_value_sub_zero():
    assert md.modNum(-1,7) == md.modNum(6,7), 'Allowing init to negative values'

def test_init_negative_prime():
    with pytest.raises(Exception):
         md.modNum(3,-1)



#Testing for +=
def test_plus_equals():
    p1 = md.modNum(3,7)
    p1 += md.modNum(5,7)
    assert p1 == md.modNum(1,7), 'Plus Equals is being weird'

def test_plus_equals_zero():
    p1 = md.modNum(3,7)
    p1 += md.modNum(0,7)
    assert p1 == md.modNum(3,7), "Plus Equals didn't handle addition of zero properly"

def test_plus_equals_zero_reverse():
    p1 = md.modNum(0,7)
    p1 += md.modNum(3,7)
    assert p1 == md.modNum(3,7), "Plus Equals didn't handle addition of zero properly when reversed"



#Testing for -=
def test_minus_equals():
    p1 = md.modNum(3,7)
    p1 -= md.modNum(5,7)
    assert p1 == (md.modNum(3,7) - md.modNum(5,7)), 'Minus Equals is being weird'

def test_minus_equals_zero():
    p1 = md.modNum(3,7)
    p1 -= md.modNum(0,7)
    assert p1 == md.modNum(3,7), "Minus Equals didn't handle subtraction of zero properly"

def test_minus_equals_zero_reverse():
    p1 = md.modNum(0,7)
    p1 -= md.modNum(3,7)
    assert p1 == (md.modNum(0,7)-md.modNum(3,7)), "Minus Equals didn't handle subtraction of zero properly when reversed"



#Testing *=
def test_multiplication_equals():
    p1 = md.modNum(3,7)
    p1 *= md.modNum(5,7)
    assert p1 == md.modNum(1,7), 'Multiplication Equals is being weird'

def test_multiplication_equals_one():
    p1 = md.modNum(3,7)
    p1 *= md.modNum(1,7)
    assert p1 == md.modNum(3,7), "Multiplication Equals didn't handle multiplication of one properly"

def test_multiplication_equals_one_reverse():
    p1 = md.modNum(1,7)
    p1 *= md.modNum(3,7)
    assert p1 == md.modNum(3,7), "Multiplication Equals didn't handle multiplication of one properly when reversed"



#Testing /=
def test_division_equals():
    p1 = md.modNum(3,7)
    p1 /= md.modNum(5,7)
    assert p1 == md.modNum(2,7), 'Division Equals is being weird'

def test_division_equals_one():
    p1 = md.modNum(3,7)
    p1 /= md.modNum(1,7)
    assert p1 == md.modNum(3,7), "Division Equals didn't handle division of one properly"

def test_division_equals_one_reverse():
    p1 = md.modNum(1,7)
    p1 /= md.modNum(3,7)
    assert p1 == md.modNum(5,7), "Division Equals didn't handle division of one properly when reversed"




#Testing for **
def test_pow_reg():
    assert (md.modNum(3,7) ** 5) == md.modNum(5,7), "Exponentiation implemented incorrectly"

def test_pow_float():
    with pytest.raises(Exception):
        md.modNum(3,7)**5.5

def test_pow_not_numberic():
    with pytest.raises(Exception):
        md.modNum(3,7)**'a'

def test_pow_equals():
    p1 = md.modNum(3,7)
    p1 **= 5
    assert p1 == md.modNum(5,7), "Exponentiation Equals implemented incorrectly"

def test_pow_zero():
    assert (md.modNum(3,7)**0) == md.modNum(1,7), "Zero Exponent not working correctly"

def test_pow_one():
    assert (md.modNum(3,7)**1) == md.modNum(3,7), "One Exponent not working correctly"



#Testing SquareRoot
def test_sqrt_not_modNum():
    with pytest.raises(AssertionError):
        md.modNum.sqrt(5)

def test_sqrt_has_root():
    assert (md.modNum.sqrt(md.modNum(2,7))) == (md.modNum(4,7)), 'Square Root is choosing the wrong number'

def test_sqrt_has_no_root():
    assert (md.modNum.sqrt(md.modNum(3,7))) == md.modNum(0,7), 'Square Root is saying a number w/o root has a root'


## Things to add test for Elliptic Curves
# Want to test that you can't change the prime, a,b,or init point values
def test_ellip_change_prime():
    with pytest.raises(AttributeError):
        print(ellip.EllipticCurve.__prime)

def test_ellip_change_a():
    with pytest.raises(AttributeError):
        print(ellip.EllipticCurve.__a)

def test_ellip_change_b():
    with pytest.raises(AttributeError):
        print(ellip.EllipticCurve.__b)

def test_ellip_change_init_point():
    with pytest.raises(AttributeError):
        print(ellip.EllipticCurve.__init_point)

def test_ellip_change_w():
    with pytest.raises(AttributeError):
        print(ellip.EllipticCurve.__w)

def test_ellip_get_prime():
    ec = ellip.EllipticCurve(0,0)
    assert (ec.get_prime() ) == 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF, "Didn't return proper value for prime"

def test_ellip_get_a():
    ec = ellip.EllipticCurve(0,0)
    assert (ec.get_a() ) == md.modNum(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC,ec.get_prime()), "Didn't return proper value for a"

def test_ellip_get_b():
    ec = ellip.EllipticCurve(0,0)
    assert (ec.get_b() ) == md.modNum(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B,ec.get_prime()), "Didn't return proper value for b"

def test_ellip_get_init_point():
    ec = ellip.EllipticCurve(0,0)
    assert (ec.get_init_point() ) == (0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296, 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5), "Didn't return proper value for init_point"

def test_ellip_get_x():
    ec = ellip.EllipticCurve(0,0)
    assert ec.get_x() == md.modNum(0,ec.get_prime()), "Get X isn't returning the proper value"

def test_ellip_get_w():
    ec = ellip.EllipticCurve(0,0)
    assert (ec.get_w() ) == 2**8, "Didn't return proper value for w"

def test_ellip_set_w_valid():
    ec = ellip.EllipticCurve(0,0)
    ec.set_w(5)
    assert (ec.get_w()) == 5, "Didn't actually change value of w"

def test_ellip_get_w_after_set_w_elsewhere():
    ec = ellip.EllipticCurve(0,0)
    ec.set_w(5)
    ec2 = ellip.EllipticCurve(0,0)
    assert (ec2.get_w() ) == 5, "Didn't change value of w for whole class"

def test_ellip_cant_change_zero_inf():
    with pytest.raises(AttributeError):
        ec = ellip.EllipticCurve(0,0)
        print(ec.__zero_inf)

def test_ellip_get_zero_inf_true():
    ec = ellip.EllipticCurve(0,0)
    assert ec.get_zero_inf() == True, "Infinity point not initiating properly"

def test_get_zero_inf_false():
    ec = ellip.EllipticCurve(0,0)
    init_point = ec.get_init_point()
    ec2 = ellip.EllipticCurve(init_point[0],init_point[1])
    assert ec2.get_zero_inf() == False, "Zero Inf Flag not getting set properly on init for valid points"

def test_ellip_string_inf():
    ec = ellip.EllipticCurve(0,0)
    assert str(ec) == f"Infinity on curve y^2 = x^3 + {int(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC)}x + {int(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B)}", print(ec)

def test_ellip_string_valid():
    ec = ellip.EllipticCurve(0,0)
    init_point = ec.get_init_point()
    ec2 = ellip.EllipticCurve(init_point[0],init_point[1])
    assert str(ec2) == f"Point ({int(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296)},{int(0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)}) on curve y^2 = x^3 + {int(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC)}x + {int(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B)}", print(ec2)

def test_ellip_string_inf_iter():
    ec = ellip.EllipticCurve(0,0)
    ec = [ec]
    assert str(ec) == f"[Infinity on curve y^2 = x^3 + {int(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC)}x + {int(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B)}]", print(ec)

def test_ellip_string_valid_iter():
    ec = ellip.EllipticCurve(0,0)
    init_point = ec.get_init_point()
    ec2 = ellip.EllipticCurve(init_point[0],init_point[1])
    ec2 = [ec2]
    assert str(ec2) == f"[Point ({int(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296)},{int(0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)}) on curve y^2 = x^3 + {int(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC)}x + {int(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B)}]", print(ec2)

def test_ellip_init_invalid_point():
    with pytest.raises(AssertionError):
        ec = ellip.EllipticCurve(0,1)

def test_ellip_init_invalid_type_x():
    with pytest.raises(AssertionError):
        ec = ellip.EllipticCurve('x',0)

def test_ellip_init_invalid_type_y():
    with pytest.raises(AssertionError):
        ec = ellip.EllipticCurve(0,'y')

def test_ellip_init_invalid_type_x_and_y():
    with pytest.raises(AssertionError):
        ec = ellip.EllipticCurve('x','y')

def test_ellip_mul_zero_zero():
    ec = ellip.EllipticCurve(0,0)
    ec2 = ellip.EllipticCurve(0,0)
    test = ellip.EllipticCurve(0,0)
    assert (ec * ec2) == test, "0 * 0 != 0"

def test_ellip_mul_zero_init():
    ec = ellip.EllipticCurve(0,0)
    init = ec.get_init_point()
    ec2 = ellip.EllipticCurve(init[0],init[1])
    test = ellip.EllipticCurve(init[0],init[1])
    assert (ec * ec2) == test, "0 * a != a"

def test_ellip_mul_init_zero():
    ec = ellip.EllipticCurve(0,0)
    init = ec.get_init_point()
    ec2 = ellip.EllipticCurve(init[0],init[1])
    test = ellip.EllipticCurve(init[0],init[1])
    assert (ec * ec2) == test, "a * 0 != a"

def test_ellip_mul_init_init():
    ec = ellip.EllipticCurve(0,0)
    init = ec.get_init_point()
    ec = ellip.EllipticCurve(init[0],init[1])
    ec2 = ellip.EllipticCurve(init[0],init[1])
    test = ellip.EllipticCurve(0x7cf27b188d034f7e8a52380304b51ac3c08969e277f21b35a60b48fc47669978,0x7775510db8ed040293d9ac69f7430dbba7dade63ce982299e04b79d227873d1)
    assert (ec * ec2) == test, "Problem with elliptic curve operation on points with same X and Y values"

def test_ellip_mul_2x_init_init():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    ec2 = ellip.EllipticCurve(0x7cf27b188d034f7e8a52380304b51ac3c08969e277f21b35a60b48fc47669978,0x7775510db8ed040293d9ac69f7430dbba7dade63ce982299e04b79d227873d1)
    assert (ec * ec2) == ellip.EllipticCurve(0x5ecbe4d1a6330a44c8f7ef951d4bf165e6c6b721efada985fb41661bc6e7fd6c,0x8734640c4998ff7e374b06ce1a64a2ecd82ab036384fb83d9a79b127a27d5032), "Problem with elliptic curve operation on points with different X values"

def test_ellip_mul_init_invert_init():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    prime = ec.get_prime()
    ec2 = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,( (-0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5) % prime) )
    assert (ec * ec2) == ellip.EllipticCurve(0,0)

def test_ellip_group_inv_zero():
    ec = ellip.EllipticCurve(0,0)
    ec2 = ec.group_inv()
    assert ec == ec2, "Inverting zero on elliptic curve isn't returning zero"

def test_ellip_group_inv_non_zero():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    ec2 = ec.group_inv()
    prime = ec.get_prime()
    assert ( ec2 == ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296, ( (-0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5) %prime) )), "Not inverting properly on elliptic curves"

def test_ellip_pow_zero():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    ec2 = ec ** 0
    assert (ec2 == ellip.EllipticCurve(0,0)), "elliptic curve object to the zero power should be zero/infinity and it isn't"

def test_ellip_pow_pos_even():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    ec2 = ellip.EllipticCurve(0x7cf27b188d034f7e8a52380304b51ac3c08969e277f21b35a60b48fc47669978,0x7775510db8ed040293d9ac69f7430dbba7dade63ce982299e04b79d227873d1)
    assert ec ** 2 == ec2, "Elliptic Curve to even power not performing correcrtly"

def test_ellip_pow_pos_odd():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    assert ec ** 3 == (ec * ec * ec), "Powering Elliptic Curve to an odd value isn't working correctly"

def test_ellip_pow_one():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    assert ec ** 1 == ec, "Raising Elliptic Curve object to 1st power isn't returning the same object"

def test_ellip_pow_neg_one():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    assert (ec ** -1) == (ec.group_inv()), "Raising Ellipitic Curve to -1 isn't returning its inverse"

def test_ellip_pow_neg_odd():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    assert (ec ** -3) == (ec.group_inv() ** 3)

def test_ellip_pow_neg_even():
    ec = ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)
    assert (ec ** -2) == (ec.group_inv() ** 2)



### Add testing for ElGamal
#test that encoding the same message twice gives a diff result
# test encode/decode

def test_el_gamal_init():
    el = eg.ElGamal()

def test_el_gamal_get_prime():
    el = eg.ElGamal()
    assert el.get_group_prime() == 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF, "Prime isn't being initiated properly"

def test_el_gamal_get_public_key():
    el = eg.ElGamal()
    assert el.get_public_key() == ellip.EllipticCurve(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5), "Public key isn't being initated properly"

def test_el_gamal_get_h():
    el = eg.ElGamal()
    assert type(el.get_h()) == ellip.EllipticCurve, "type of h is incorrect"

def test_el_gamal_h_random():
    el = eg.ElGamal()
    el2 = eg.ElGamal()
    assert el.get_h() != el2.get_h(), "h isn't being set randomly"

def test_el_gamal_string():
    el = eg.ElGamal()
    assert str(el) == f"Field using {el.get_group_prime()}, public key {el.get_public_key()}, and h {el.get_h()}", "El Gamal not printing correctly with regualr print"

def test_el_gamal_repr():
    el = eg.ElGamal()
    el = [el]
    assert str(el) == f"[Field using {el[0].get_group_prime()}, public key {el[0].get_public_key()}, and h {el[0].get_h()}]", "El Gamal not printing correctly with regualr print"

def test_el_gamal_encrypt_decrypt():
    el = eg.ElGamal()
    plain_text = "Is this working?"
    cipher_text = eg.encrypt(el.get_group_prime(),el.get_public_key(), el.get_h(), plain_text)
    decrypted_message = el.decrypt(cipher_text)
    assert decrypted_message == plain_text, "Encrypt/Decrypt not functioning properly"

def test_el_gamal_encrypt():
    el = eg.ElGamal()
    plain_text = 'Test'
    specificH = ellip.EllipticCurve(21435461484816712922587089261995741808369832787364259539473306888134162107671,61107500123514607893307166514610823967491409884695182540382221791454428530586)
    encrypt_text = el.test_encrypt_DO_NOT_USE(el.get_group_prime(),el.get_public_key(), specificH, plain_text,1234)
    assert (str(encrypt_text) == "[(Point (92084571366670613904602541308993679489120835040445244546951039525115631749046,50926029405481653761666459627853514640350364067427483002765903219816118730183) on curve y^2 = x^3 + 115792089210356248762697446949407573530086143415290314195533631308867097853948x + 41058363725152142129326129780047268409114441015993725554835256314039467401291, Point (110634020051786816956304770816292382461590442864052437303634878047958956219122,92295863483870524271930697252731632797567313619653050621474492028564481132010) on curve y^2 = x^3 + 115792089210356248762697446949407573530086143415290314195533631308867097853948x + 41058363725152142129326129780047268409114441015993725554835256314039467401291)]"), "Error in __test_encrypt must have changed some functionality, maybe the prime, a, b, g. Or some other aspect"




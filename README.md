This package was written for learning purposes only. It should not be used in any situation where real security is required.

I have implemented the El Gamal method of asymetric key exchnge over elliptic curves. The field, curve, and starting point used in this implementation came from http://www.secg.org/sec2-v2.pdf under the nickname 'secp256r1'. I used this curve and field because it provides an adequate level of security while remaining relatively fast. It is my understanding that fields any larger cannot be proccessed quickly due to current hardware design limitations. One way around this is by using a larger field for an initial asymetric key which would be used to communicate a symmetric key. This would seem to be a best of both worlds type approach but more research would be needed to be certain.

I chose three different classes/objects for this project. The first is modNum.The class of modNum is an integer number that can be manipulated by the usual math functions of +,-,*,/,//,**,+=,...,/= as well as it's own sqrt() function.

The second class is EllipticCurve. The EllipticCurve class has immutable class variables that define the field and curve to be used. Instantiating  an instance of EllipticCurve takes two integers, x and y, and uses them to create two instances of the modNum class. The instantiation also confirms that the given x,y are valid points on the curve. This check is crucial since the field must be closed. This class also supercedes the built in functions for * and **. Multiplication becomes the elliptic curve group operation and ** powering using that group operation.

The third class is ElGamal. This class creates a random private key for each instance of the class and uses that private key to create a secondary public key, h. Using encrypt() you can encrypt any message by providing the prime and both public keys of the recipient of the message. Then using the specific instance ElGamal that generated the private key and secondary public key you can decrypt a message intended for for the create of that specifc instance. Obviously in a real application you would need to be able to store the private key. But I chose to not implement a method to do that since this code shouldn't be used in real applications.

I also wrote a full suite of tests for all exposed functions. I even wrote a specifc version of encrypt with a lower level of security to be used solely for testing purposes. 
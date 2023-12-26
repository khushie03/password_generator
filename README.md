# password_generator
Here you are able to create a strong password using a number provided by the user as well the name provided by you . This will allow you to create a strong captcha system.
You will receive a numerical value. Transform the provided decimal number into scientific notation. Simplify all the digits after the decimal point to a single digit by adding all the digits until it becomes single digit, and apply the same rule to the exponent.

Next, create a string by concatenating the first three letters of each digit when expressed as words, while keeping the symbols and letter 'e unchanged. This resultant string will be denoted as S1.

• If the digit resulting from reducing the value of exponent to a single digit is odd, concatenate all the letters at odd positions in the given name (using 1-based indexing). This string is referred to as S2.

Your desired password will be the combination of S1 and S2, separated by an "@" symbol, forming the format S1@S2

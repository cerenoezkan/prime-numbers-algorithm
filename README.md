# Prime Numbers Algorithm

## Problem Definition
The purpose of this project is to display all prime numbers that:
- Have exactly three digits
- Start with the digit 5

In other words, the algorithm finds all prime numbers between 500 and 599.

---

## Algorithm Description
The algorithm iterates through numbers from 500 to 599.
For each number, it checks whether the number is prime by testing
its divisibility starting from 2 up to half of the number.
If the number is not divisible by any of these values, it is considered prime
and printed as output.

---

## Pseudocode
START
    NUMBER ← 500
    WHILE NUMBER < 600 DO
        IS_PRIME ← TRUE
        DIVISOR ← 2

        WHILE DIVISOR ≤ NUMBER / 2 DO
            IF NUMBER MOD DIVISOR = 0 THEN
                IS_PRIME ← FALSE
                BREAK
            END IF
            DIVISOR ← DIVISOR + 1
        END WHILE

        IF IS_PRIME = TRUE THEN
            PRINT NUMBER
        END IF

        NUMBER ← NUMBER + 1
    END WHILE
END

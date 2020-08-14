# PARAM_1 (KEY STR)

The input Serial key string 

# PARAM_2

Some code? Unsure of what this is currently

# PARAM_3

The product ID. In this case: `M61-00032`

# PARAM_4

A memory address is passed on the stack.

However, unsure of what this is? Does not seem to change with correct or incorrect serial key??

# PARAM_5

`0x0` is passed on the stack??

# PARAM_6 (Return PID)

Parameter used to return the Product ID

# PARAM_7

The entire memory section has be calculated at `164 bytes` from `0xXXXF398` or `41 (0x29)` words

WHEN:

- `VALIDATION_RESULT` equals (`local_c >> 1`)

If the program flow gets to a certain stage a static `0xA4` is written here followed by a `0x03`.

```
00401d8b mov dword ptr [ebx], 0xa4
00401d91 mov word ptr ds:[ebx+4], 0x3
```

TickCount (4 bytes) gets written into `xxxF3E4`

UNIX timestamp (4 bytes) as a word gets written into `xxxF3E0`

Result of `uVar7 != 0` gets written into `xxxF3E8` ?? Note if `param_9` is not zero a `2` will be written her instead.

We then move onto a function that uses the `VALIDATION_RESULT` value and divides by `1000000`.

It then checks if the result with no remainder is either:

- 0x10e
    - Writes `3` into MEM

- 0x14f
    - Writes `6` into MEM

- 0x3d5
- 0x3d6
- 0x3d7

- VALIDATION_RESULT == 0x1b6b0b00

Then `FUN_00402394(VALIDATION_RESULT % 1000000)` does some binary operations to produce a value (`8431757`). This is the center of the PID (`75043-036-8431757-40381`)

The final section (`40381`) is produced by:

- First two chars (`40`) is (`param_8 >> 1 % 1000`) (TODO: What is `param_8`??)
- Followed by the last 3 chars (`381`) is the `TickCount / 10 % 1000`

The entire code is then combined:

- Param_2 (Random code)
- `VALIDATION_RESULT / 1000000 - (VALIDATION_RESULT % 1000000)` TODO: check this??
- middle pid section from `FUN_00402394`
- Final section (`40381` (See above))


Some words are then written into memory from `xxxF3D0` to `xxxF3DB`. TODO: What these do?

The Game code is then copied into memory starting at `xxxF3BC`

Param_4 is then written into memory at `xxxF3F4`. Though nothing seems to be there?

Then it calls a function `FUN_0040176d` that performs some operations and does some stuff. TODO: wat stuff

The value produced from above is written into `xxx  F400`

Then:

`xxxF40C`: Month + Year (`38` `0C`)?? 
`xxxF410`: Day + Day of Week??
`xxxF414`: Minute + Hour?

Then writes a CRC value into `xxxF438`

Finally the return value loaded from `xxxFEFE`C is placed into EAX and the function returns


# PARAM_8

# PARAM_9
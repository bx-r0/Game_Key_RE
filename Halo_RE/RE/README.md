# Halo

VALID KEY:
HQDT4
8FKPM
XHXK4
CFFGY
G34YM


The `setup.exe` copies it self into the appdata/local as a `MSGXXXX.Exe`

```
4ea571b9d6ac10da43e87e98390dd0fd  Setup.Exe
b764bd74bba73497b1ac2fa13ea3b075  SetupENU.dll
```

Becomes:

```
MSGXXXX.Exe
MSGXXXX.DLL
```

We have to attach `x32dbg` after execution due to way it does not follow the spawned treads


Entered code is written into memory at:

1st: 0x048AB88
2nd: 0x048AC8C
3rd: 0x048AD90
4th: 0x048AE94
5th: 0x048AE94

Function `0040d7f` is our key check!!

### FUN_0040D7F

Loads the value "M61-00032". This is the Game identifier

And the value "75043" ??? 


It calls PIDGenSimpA

With the following params


```
0573F004  0573F4C0  "1111122222333334444455555" # Full key
0573F008  0573F04C  "75043"                     # Unknown?
0573F00C  0573F054  "M61-00032"                 # Game Microsoft ID
```

The valid check seems to occur at `0x0040DA04` with the result coming from `PIDGenSimpA`

# PIDGEN

```
The PIDGEN call is performed at `0040DA00`
```

## MAIN --> 0x0401A51

Starts off by checking the length of the key

Returns `0x4` if the value is incorrect (L == 25)

Returns `0x5` if the product code is missing (`M61-00032`)

Returns `0x6` if the product code length is incorrect (L < 10)

Returns `0x7` on a blank `param_6` (The fuck is param_6??)

Returns `0x8` on a blank EBX register??

Returns `0xb` on a strange code that does not equal 5 length

## MAIN --> 0x0401b67

Function starts by loading "BINK" from the resources

`param_6` seems to define weather or not to load the BINK resources?


## [..] --> 0x04017ce 

Calls a method with the BINK VALUE as the key

First thing to notice tis the string being loaded 

`BCDFGHJKMPQRTVWXY2346789`. Comparing this value to the key suggests this is the alphabet of the code


It multiplies the length ()

x = 0x19 * 0x11E9 / 1000

y = (x % 8) + x / 8

== 0xf??

uVar5 == ebp - 18


local_1c??

Then loops through the alphabet and the key and checks if the element of the key exists in the alphabet.

If it does it will perform some binary operations and save in a memory location.


Output == BD E9 4D 6F 7A D3 9B DE F4 EE 8C 26 16 57 01 00
KEY    == "HHHHHHHHHHHHHHHHHHHHHHHHH"


It compares the number of bytes produced to 0x40??? Looking at the memory that seems to be the maximum space allocated

It just sets uVar8 to the max


It then loops around each value in the weird output and performs operations on the values

e.g. 

    
BD E9 4D 6F 7A D3 9B DE F4 EE 8C 26 16 57 01 00
    ^  ^
    2  1 

x = ([1] << 5) & 0xff
y = ([2] >> 3) & 0xff

z = x || y


Origin: BD E9 4D 6F 7A D3 9B DE `F4 EE 8C 26 16 57 01 00`
Result: BD E9 4D 6F 7A D3 9B DE `9D D1 C4 E2 2A 00 01 00`


## [..] --> 0x04017ce --> 0x04024f6 

The program then loads on three values from the memory

```
0xXXXXF04, 0xXXXXF08, 0xXXXXF14
```

## [..] --> 0x04024f6 --> 0x0402586

All this function does is check if the passed in values are equal to the values

Is check if the first value is 0x67 and set the params

to 0x1e4, 0x50 and 0x50 respectively?

## [..] --> 0x04024f6 --> 0x04024c6

Takes a single integer value and returns another integer

```
i: (i == 0)             - o: 0
i: (i == 2)             - o: 3
i: (i > 2 && i < 5)     - o: 1
i: (i == 10)            - o: 4
else:                   - o: 2
```

## [..] -> 0x04017ce --> 0x040253b

Does not really do much, seems like a harness for other functions

## [..] -> 0x040253b --> 0x0402bd2

A fucking huge function, 

Looks like the program creates and allocates the heap with the following params:

```C#
HeapAlloc(HeapPtr, HEAP_ZERO_MEMORY, Size=1800 Bytes)
```

`HEAP_ZERO_MEMORY`: All values are initiated with zeros

Returns:

`0x10` - On Heap creation error


## [..] -> 0x0402bd2 -> 0x0403098

This function takes the heap + 424 onwards and does some shifting and transposition

Running through the method, it seems to be writing blocks of seemingly random data onto the stack

In the all H example we get:

```
00744438  BD E9 4D 6F 00 00 00 00 00 00 00 00 F4 A6 37 BD
00744448  3B A3 89 05 00 00 00 00 00 00 00 00 57 01 00 00
```


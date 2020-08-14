# CHECK POINTS

## NOTE
The memory address `0048a35` keeps popping up.


## TOP LEVEL (`Setup.exe`)


# 0x40DA02

CMD: `cmp eax, ebx`

VALID: `eax == 0`

SOURCE: `PIDGenSimpA` --> `eax` 

---
### PIDGen.dll (0x401cdc)

CMD: `test eax, eax`

VALID: `eax == 0`

SOURCE: `FUN_00401a51 [Param_Check]` --> `eax`

EXPLANATION: This validates simple inputs by checking length etc. Hard to fail.

---

### PIDGen.dll (0x401d24)

CMD: `test eax, eax`

VALID: `eax == 0`

SOURCE: `FUN_00401b67 [Load_&_Use_BINK]` --> `eax`

EXPLANATION: Seems to do most of the key checking logic here, writes a lot of stuff into memory etc.

TODO: Reverse this logic

---

### PIDGen.dll (0x401d35)

CMD: `cmp eax, FFFFFFFF`

VALID: `eax != FFFFFFFF`

SOURCE: `Load_&_Use_BINK` takes the memory location that is checked as a param.

TODO: Where does `FFFFFFFF` come from. In Ghidra the variable is `local_c`

---

# 0x40DA15

CMD: `cmp eax, ebx`

VALID: `eax != 0`

SOURCE: `FUN_0040c670` --> `eax`

TODO: Reverse this logic



# TODO

MEMORY LOCATION: 0x0048a3bc

WRITES THE PID: 0x0048aa8



## General Notes

The memory address `0048a35` keeps popping up.

It always seems to be checked with an & operation and it's equality is checked against 0

This is some sort of flag check where binary it is being compared to values with a single 1 in their value

CHANGES TO FLAG:

### FUN_00410470
```
FLAG = -(uint)(param_1 != 0) & 0x40000 | FLAG & 0xfffbffff;
```


i.e. 
```
Position 1  0x1
Position 2  0x2
Position 3  0x4
Position 4  0x8
Position 5  0x10
Position 6  0x20
Position 7  0x40
Position 8  0x80
Position 9  0x100
Position 10 0x200
Position 11 0x400
Position 12 0x800
Position 13 0x1000
Position 14 0x2000
Position 15 0x4000
Position 16 0x8000
Position 17 0x10000
Position 18 0x20000
Position 19 0x40000
Position 20 0x80000
Position 21 0x100000
Position 22 0x200000
Position 23 0x400000
Position 24 0x800000
Position 25 0x1000000
Position 26 0x2000000
Position 27 0x4000000
Position 28 0x8000000
Position 29 0x10000000
Position 30 0x20000000
Position 31 0x40000000
Position 32 0x80000000
```
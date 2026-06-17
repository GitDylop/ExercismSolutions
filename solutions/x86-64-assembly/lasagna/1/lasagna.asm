section .text

global expected_minutes_in_oven
expected_minutes_in_oven:
    mov rax, 40
    ret

global remaining_minutes_in_oven
remaining_minutes_in_oven:
    call expected_minutes_in_oven
    sub rax, rdi
    ret

global preparation_time_in_minutes
preparation_time_in_minutes:
    imul rdi, 2
    mov rax, rdi
    ret

global elapsed_time_in_minutes
elapsed_time_in_minutes:
    imul rdi, 2
    add rdi, rsi
    mov rax, rdi
    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif

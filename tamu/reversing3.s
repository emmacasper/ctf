	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14
	.globl	_concat                 ## -- Begin function concat
	.p2align	4, 0x90
_concat:                                ## @concat
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-8(%rbp), %rdi
	callq	_strlen
	movq	-16(%rbp), %rdi
	movq	%rax, -32(%rbp)         ## 8-byte Spill
	callq	_strlen
	movq	-32(%rbp), %rsi         ## 8-byte Reload
	addq	%rax, %rsi
	addq	$1, %rsi
	movq	%rsi, %rdi
	callq	_malloc
	movq	$-1, %rdx
	movq	%rax, -24(%rbp)
	movq	-24(%rbp), %rdi
	movq	-8(%rbp), %rsi
	callq	___strcpy_chk
	movq	$-1, %rdx
	movq	-24(%rbp), %rdi
	movq	-16(%rbp), %rsi
	movq	%rax, -40(%rbp)         ## 8-byte Spill
	callq	___strcpy_chk
	movq	-24(%rbp), %rdx
	movq	%rax, -48(%rbp)         ## 8-byte Spill
	movq	%rdx, %rax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$80, %rsp # rsp is 80 below rbp
	leaq	L_.str(%rip), %rdi
	movl	$3, %eax
	movl	$14, %ecx
	xorl	%esi, %esi
	movl	$8, %edx
                                        ## kill: def %rdx killed %edx
	leaq	-16(%rbp), %r8
	movq	___stack_chk_guard@GOTPCREL(%rip), %r9
	movq	(%r9), %r9
	movq	%r9, -8(%rbp)
	movl	$0, -20(%rbp)
	movq	%rdi, -56(%rbp)         ## 8-byte Spill
	movq	%r8, %rdi
	movl	%ecx, -60(%rbp)         ## 4-byte Spill
	movl	%eax, -64(%rbp)         ## 4-byte Spill
	callq	_memset # I'm going to guess we set it to all 0's
##    rbp-9:89,49,98,77,51,53,53,53,64
##    rbp-24:0,0,0,0,1,0,0,0,2,0,0,0:rbp-36
	movb	$65, -16(%rbp) # A
	movb	$53, -15(%rbp) # 5
	movb	$53, -14(%rbp) # 5
	movb	$51, -13(%rbp) # 3
	movb	$77, -12(%rbp) # M
	movb	$98, -11(%rbp) # b
	movb	$49, -10(%rbp) # 1
	movb	$89, -9(%rbp) # Y
	movl	$0, -28(%rbp)
	movl	$1, -32(%rbp)
	movl	$2, -36(%rbp)
	movl	-36(%rbp), %eax ## eax is 2
	imull	-36(%rbp), %eax ## eax is now 4
	imull	-36(%rbp), %eax ## eax is now 8
	movl	-28(%rbp), %ecx ## ecx is 0
	addl	-32(%rbp), %ecx ## ecx is now 1
	addl	-32(%rbp), %ecx ## exc is now 2
	addl	-32(%rbp), %ecx # ecx is now 3
	imull	%ecx, %eax # eax is now 24
	cltd 			# extends sign bit of eax (0) into edx.
	movl	-60(%rbp), %ecx         ## 4-byte Reload: ecx is now X
	idivl	%ecx					## you know what we're going to ignore ecx for now.
	movl	%eax, -40(%rbp) # rbp-40 is now 24
	movl	-36(%rbp), %eax # eax is 2
	imull	-36(%rbp), %eax # eax is 4
	imull	-36(%rbp), %eax # eax is 8
	movl	-28(%rbp), %esi # esi is 0
	addl	-32(%rbp), %esi # esi is 1
	addl	-32(%rbp), %esi # esi is 2
	imull	%esi, %eax		# eax is 8*2=16
	cltd			# extend sign bit again, why??
	movl	-64(%rbp), %esi         ## 4-byte Reload: esi is now something??
	idivl	%esi					# what
	movl	%eax, -44(%rbp) # rbp-44 is 16
	movl	-40(%rbp), %esi # esi is 24
	movq	-56(%rbp), %rdi         ## 8-byte Reload: rdi is now yet another thing
	movb	$0, %al			# eax was 16 so now it is 0
	callq	_printf # eax is going to have number of characters printed.
                    # this is probably 0
	leaq	L_.str.1(%rip), %rdi # rdi has a pointer to that string?
	movl	-44(%rbp), %esi # esi is 16
	movl	%eax, -68(%rbp)         ## 4-byte Spill: rsp+12 is probably 0
	movb	$0, %al			# eax is definitely 0 now
	callq	_printf			# eax is going to be something.
	leaq	L_.str.2(%rip), %rdi
	leaq	-16(%rbp), %rsi
	movl	%eax, -72(%rbp)         ## 4-byte Spill
	movb	$0, %al
	callq	_printf
	movq	___stack_chk_guard@GOTPCREL(%rip), %rsi
	movq	(%rsi), %rsi
	movq	-8(%rbp), %rdi
	cmpq	%rdi, %rsi
	movl	%eax, -76(%rbp)         ## 4-byte Spill
	jne	LBB1_2
## %bb.1:
	xorl	%eax, %eax
	addq	$80, %rsp
	popq	%rbp
	retq
LBB1_2:
	callq	___stack_chk_fail
	ud2
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"The answer: %d\n"

L_.str.1:                               ## @.str.1
	.asciz	"Maybe it's this:%d\n"

L_.str.2:                               ## @.str.2
	.asciz	"gigem{%s}\n"


.subsections_via_symbols

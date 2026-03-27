.global _start
.section .text
_start:
   LDR R0, =const_0
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_1
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
  VADD.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 0
    VPOP {D0}
    LDR R0, =resultado_0
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 0 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_0
    MOV R8, #1
    RSB R4, R4, #0
positivo_0:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_0
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_0
digito5_0:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_0:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_0
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_0:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_0
    STR R1, [R0]
   LDR R0, =const_2
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_3
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VSUB.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 1
    VPOP {D0}
    LDR R0, =resultado_1
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 1 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_1
    MOV R8, #1
    RSB R4, R4, #0
positivo_1:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_1
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_1
digito5_1:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_1:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_1
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_1:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_1
    STR R1, [R0]
   LDR R0, =const_4
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_5
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VMUL.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 2
    VPOP {D0}
    LDR R0, =resultado_2
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 2 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_2
    MOV R8, #1
    RSB R4, R4, #0
positivo_2:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_2
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_2
digito5_2:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_2:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_2
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_2:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_2
    STR R1, [R0]
   LDR R0, =const_6
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_7
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VDIV.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 3
    VPOP {D0}
    LDR R0, =resultado_3
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 3 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_3
    MOV R8, #1
    RSB R4, R4, #0
positivo_3:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_3
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_3
digito5_3:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_3:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_3
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_3:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_3
    STR R1, [R0]
   LDR R0, =const_8
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_9
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VDIV.F64 D0, D0, D1
   VCVT.S32.F64 S2, D0
   VCVT.F64.S32 D0, S2
  VPUSH {D0}
    @ resultado da linha 4
    VPOP {D0}
    LDR R0, =resultado_4
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 4 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_4
    MOV R8, #1
    RSB R4, R4, #0
positivo_4:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_4
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_4
digito5_4:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_4:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_4
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_4:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_4
    STR R1, [R0]
   LDR R0, =const_10
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_11
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VMOV.F64 D2, D0
   VDIV.F64 D0, D0, D1
   VCVT.S32.F64 S4, D0
   VCVT.F64.S32 D0, S4
   VMUL.F64 D0, D0, D1
   VSUB.F64 D0, D2, D0
  VPUSH {D0}
    @ resultado da linha 5
    VPOP {D0}
    LDR R0, =resultado_5
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 5 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_5
    MOV R8, #1
    RSB R4, R4, #0
positivo_5:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_5
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_5
digito5_5:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_5:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_5
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_5:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_5
    STR R1, [R0]
   LDR R0, =const_12
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_13
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VMOV.F64 D2, D0
   VCVT.S32.F64 S4, D1
   VMOV R1, S4
pot_loop_14:
   CMP R1, #1
   BLE pot_fim_14
   VMUL.F64 D0, D0, D2
   SUBS R1, R1, #1
   B pot_loop_14
pot_fim_14:
  VPUSH {D0}
    @ resultado da linha 6
    VPOP {D0}
    LDR R0, =resultado_6
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 6 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_6
    MOV R8, #1
    RSB R4, R4, #0
positivo_6:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_6
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_6
digito5_6:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_6:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_6
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_6:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_6
    STR R1, [R0]
   LDR R0, =const_15
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_16
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VDIV.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 7
    VPOP {D0}
    LDR R0, =resultado_7
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 7 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_7
    MOV R8, #1
    RSB R4, R4, #0
positivo_7:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_7
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_7
digito5_7:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_7:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_7
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_7:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_7
    STR R1, [R0]
   LDR R0, =const_17
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_18
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
  VADD.F64 D0, D0, D1
  VPUSH {D0}
   LDR R0, =const_19
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_20
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VMUL.F64 D0, D0, D1
  VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VSUB.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 8
    VPOP {D0}
    LDR R0, =resultado_8
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 8 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_8
    MOV R8, #1
    RSB R4, R4, #0
positivo_8:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_8
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_8
digito5_8:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_8:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_8
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_8:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_8
    STR R1, [R0]
   LDR R0, =const_21
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_22
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VDIV.F64 D0, D0, D1
  VPUSH {D0}
   LDR R0, =const_23
   VLDR.F64 D0, [R0]
   VPUSH {D0}
   LDR R0, =const_24
   VLDR.F64 D0, [R0]
   VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
  VADD.F64 D0, D0, D1
  VPUSH {D0}
    VPOP {D1}
    VPOP {D0}
   VMUL.F64 D0, D0, D1
  VPUSH {D0}
    @ resultado da linha 9
    VPOP {D0}
    LDR R0, =resultado_9
    VSTR.F64 D0, [R0]
    VPUSH {D0}
    @ --- mostrar linha 9 no display ---
    VPOP {D0}
    LDR R0, =const_cem
    VLDR.F64 D1, [R0]
    VMUL.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VMOV R4, S0
    MOV R8, #0
    CMP R4, #0
    BGE positivo_9
    MOV R8, #1
    RSB R4, R4, #0
positivo_9:
    LDR R5, =tabela_7seg
    MOV R6, #0
    MOV R7, #0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R6, R6, R0
    MOV R4, R2
    MOV R0, #0x08
    LSL R0, R0, #16
    ORR R6, R6, R0
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #24
    ORR R6, R6, R0
    MOV R4, R2
    BL div10
    LDR R0, [R5, R3, LSL #2]
    ORR R7, R7, R0
    MOV R4, R2
    CMP R8, #1
    BNE digito5_9
    MOV R0, #0x40
    LSL R0, R0, #8
    ORR R7, R7, R0
    B display_9
digito5_9:
    BL div10
    LDR R0, [R5, R3, LSL #2]
    LSL R0, R0, #8
    ORR R7, R7, R0
display_9:
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R7, [R0]
    LDR R0, =0xFF200000
    LDR R1, =led_linha_9
    LDR R2, [R1]
    STR R2, [R0]
espera_botao_9:
    LDR R0, =0xFF20005C
    LDR R1, [R0]
    TST R1, #1
    BEQ espera_botao_9
    STR R1, [R0]

    @ --- fim: apaga displays ---
    MOV R6, #0
    LDR R0, =0xFF200020
    STR R6, [R0]
    LDR R0, =0xFF200030
    STR R6, [R0]
    LDR R0, =0xFF200000
    STR R6, [R0]

    B _halt

div10:
    MOV R2, #0
    MOV R3, R4
div10_loop:
    CMP R3, #10
    BLT div10_fim
    SUB R3, R3, #10
    ADD R2, R2, #1
    B div10_loop
div10_fim:
    BX LR

_halt:
    B _halt

.section .data
const_cem: .double 100.0
tabela_7seg:
    .word 0x3F
    .word 0x06
    .word 0x5B
    .word 0x4F
    .word 0x66
    .word 0x6D
    .word 0x7D
    .word 0x07
    .word 0x7F
    .word 0x6F
const_0: .double 3.14
const_1: .double 2.0
const_2: .double 10.0
const_3: .double 3.0
const_4: .double 4.0
const_5: .double 2.5
const_6: .double 15.0
const_7: .double 4.0
const_8: .double 17.0
const_9: .double 5.0
const_10: .double 17.0
const_11: .double 5.0
const_12: .double 2.0
const_13: .double 8
const_15: .double 100.0
const_16: .double 3.0
const_17: .double 2.0
const_18: .double 3.0
const_19: .double 4.0
const_20: .double 2.0
const_21: .double 10.0
const_22: .double 2.0
const_23: .double 3.0
const_24: .double 1.0
resultado_0: .space 8
resultado_1: .space 8
resultado_2: .space 8
resultado_3: .space 8
resultado_4: .space 8
resultado_5: .space 8
resultado_6: .space 8
resultado_7: .space 8
resultado_8: .space 8
resultado_9: .space 8
led_linha_0: .word 1
led_linha_1: .word 3
led_linha_2: .word 7
led_linha_3: .word 15
led_linha_4: .word 31
led_linha_5: .word 63
led_linha_6: .word 127
led_linha_7: .word 255
led_linha_8: .word 511
led_linha_9: .word 1023
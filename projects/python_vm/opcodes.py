""" opcode symbols """
LOAD_CONSTANT = 0x64
LOAD_NAME = 0x65
STORE_NAME = 0x5a
PRINT_ITEM = 0x47
PRINT_NEWLINE = 0x48
COMPARE_OP = 0x6b
BINARY_ADD = 0x17
BINARY_MULTIPLY = 0x14
BINARY_DIVIDE = 0x15
BINARY_SUBTRACT = 0x18
BINARY_MODULO = 0x16
POP_JUMP_IF_FALSE = 0x72
POP_JUMP_IF_TRUE = 0x73
JUMP_FORWARD = 0x6e
JUMP_ABSOLUTE = 0x71
SETUP_LOOP = 0x78
POP_BLOCK = 0x57
MAKE_FUNCTION = 0x84
RETURN_VALUE = 0x53
UNARY_NOT = 0xc
CALL_FUNCTION = 0x83
LOAD_FAST = 0x7c
STORE_FAST = 0x7d
LOAD_GLOBAL = 0x74
POP_TOP = 0x1

""" types """
TYPE_TUPLE = 0x28
TYPE_INTEGER = 0x69
TYPE_STRING = 0x73
TYPE_CODE = 0x63
TYPE_NONE = 0x4e
TYPE_INTERN = 0x74
TYPE_SREF = 0x52
FUNCTION_START = 0x43

""" constants """
HAVE_ARG = 90
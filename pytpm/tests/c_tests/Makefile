TPM_PATH = ../../../src
override CFLAGS += -Wall -std=c99

$(NAME)_exe : $(NAME).c
				gcc $(CFLAGS) $(NAME).c -I$(TPM_PATH) $(TPM_PATH)/tpm/libtpm.a -lm  -o $(NAME)_exe

tstate_init_test_exe: tstate_init_test.c
				gcc $(CFLAGS) tstate_init_test.c print_tstate.c -I$(TPM_PATH) $(TPM_PATH)/tpm/libtpm.a -lm -o tstate_init_tstate_exe

tpm_data_test_exe: tpm_data_test.c print_tstate.c
				gcc $(CFLAGS) tpm_data_test.c print_tstate.c -I$(TPM_PATH) $(TPM_PATH)/tpm/libtpm.a -lm -o tpm_data_test_exe

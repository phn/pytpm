TPM_PATH = ../src
override CFLAGS += -Wall -std=c99

$(NAME)_exe : $(NAME).c
				gcc $(CFLAGS) $(NAME).c -I$(TPM_PATH) $(TPM_PATH)/tpm/libtpm.a -lm  -o $(NAME)_exe

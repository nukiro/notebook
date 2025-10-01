CC = gcc
STD = gnu23
CFLAGS = -Wall -Wextra -Wmissing-prototypes -Wmissing-declarations
DFLAGS = -g -Og -DDEBUG

SRC = $(shell find src -name '*.c')
OBJ = $(SRC:.c=.o)

all: bin main run

bin:
	mkdir bin

main: $(OBJ)
	$(CC) -std=$(STD) $(CFLAGS) $(DFLAGS) $(OBJ) -o bin/main

run:
	@echo "-------"
	@./bin/main

source: $(SRC)
	@printf '%s\n' $?


%.o: %.c
	$(CC) -std=$(STD) $(CFLAGS) $(DFLAGS) -I./include -c $< -o $@

clean:
	rm -f bin/main $(OBJ)
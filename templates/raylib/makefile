CC = gcc
STD = gnu23
CFLAGS = -Wall -Wextra -Wmissing-prototypes -Wmissing-declarations
DFLAGS = -g -Og -DDEBUG

# Raylib library
LRAY = -lraylib -lm -ldl -lpthread -lGL -lrt -lX11

SRC = $(shell find src -name '*.c')
OBJ = $(SRC:.c=.o)

all: bin main run

bin:
	@mkdir bin

main: $(OBJ)
	@$(CC) -std=$(STD) $(CFLAGS) $(DFLAGS) $(OBJ) -o bin/main $(LRAY)

run:
	@echo "-------"
	@./bin/main

s:
	@find src -name '*.c'

h:
	@find include -name '*.h'

o:
	@find src -name '*.o'

%.o: %.c
	@echo "Compiling: $<"
	@$(CC) -std=$(STD) $(CFLAGS) $(DFLAGS) -I./include -c $< -o $@

clean:
	@echo "Removing file in 'bin' and object files."
	@rm -f bin/main $(OBJ)
	@echo "Done!"
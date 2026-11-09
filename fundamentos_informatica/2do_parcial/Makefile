# Compila cada .cpp de esta carpeta como C++98 (lo que aceptan los Dev-C++ del docente).
# Ejecutables en build/ (ignorado por git).
CXX      = g++
CXXFLAGS = -std=c++98 -pedantic -Wall -Wextra

SRC = $(wildcard *.cpp)
BIN = $(SRC:%.cpp=build/%)

all: $(BIN)

build/%: %.cpp | build
	$(CXX) $(CXXFLAGS) $< -o $@

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean

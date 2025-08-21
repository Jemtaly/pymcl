# Makefile for pymcl development
# Provides convenient targets for testing and development

.PHONY: test test-smoke install install-dev clean build-mcl help

# Default target
help:
	@echo "Available targets:"
	@echo "  test        - Run the full test suite"
	@echo "  test-smoke  - Run quick smoke tests"
	@echo "  install     - Install pymcl (requires mcl library)"
	@echo "  install-dev - Install development dependencies"
	@echo "  build-mcl   - Build the MCL library dependency"
	@echo "  clean       - Clean build artifacts"
	@echo "  help        - Show this help message"

# Run the full test suite
test: install-dev
	pytest tests/ -v

# Run quick smoke tests
test-smoke: install-dev
	python tests/test_smoke.py

# Install pymcl package
install:
	pip install .

# Install development dependencies
install-dev:
	pip install -r requirements-dev.txt

# Build MCL library (Linux/macOS)
build-mcl:
	@if [ ! -d "mcl" ]; then \
		echo "Cloning MCL library..."; \
		git clone https://github.com/herumi/mcl; \
	fi
	@echo "Building MCL library..."
	cd mcl && make -j$$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)
	@echo "Building BN384_256 library..."
	cd mcl && g++ -c src/bn_c384_256.cpp -o obj/bn_c384_256.o \
		-g3 -Wall -Wextra -Wformat=2 -Wcast-qual -Wcast-align -Wwrite-strings \
		-Wfloat-equal -Wpointer-arith -Wundef -m64 -I include -I test \
		-fomit-frame-pointer -DNDEBUG -fno-stack-protector -O3 -fpic \
		-DMCL_FP_BIT=384 -DMCL_FR_BIT=256 -DMCL_USE_LLVM=1 -DMCL_BINT_ASM=1 -DMCL_MSM=1
	cd mcl && ar rv lib/libmclbn384_256.a obj/bn_c384_256.o

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
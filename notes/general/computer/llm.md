# LLM CPU

## Install necessary packages on ArchLinux/Manjaro

```sh
sudo pacman -S wget git cmake openblas ccache
```

## Get LLaMa.cpp

Get LLaMa.cpp

```sh
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp/
```

**NOTE:** The submodule **kompute** required for GPU Vulkan.
Unless supported by chipset, it's unnecessary to init this submodule.

## CMake Configure

Generate Makefile using CMake with supported options

Consideration:

- My Old Laptop CPU only support AVX but no AVX2.
- Using CPU only, it can use OpenBLAS.
- No need using Kompute or Vulkan.
- I dont need for test modules.

```sh
cmake -B build \
-DLLAMA_AVX2=OFF \
-DLLAMA_BLAS=ON \
-DLLAMA_BLAS_VENDOR=OpenBLAS \
-DLLAMA_BUILD_TESTS=OFF \
-DLLAMA_KOMPUTE=OFF \
-DLLAMA_VULKAN=OFF
```

## Build the LLM Interface

build using GCC using all CPU threads

```sh
export MAKEFLAGS=-j4
export GNUMAKEFLAGS=-j4

cmake --build build \
--config Release -j $(nproc)
```

## Get LLAMA 2 Quantized Model

As My Laptop only had 8GB memory, it only can use 7B variant with Quantization Level 3 (Q3)

Download from HuggingFace with wget

```sh
mkdir -p llm-models/
cd llm-models/

#wget -c https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q3_K_L.gguf
wget -c https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q3_K_S.gguf

cd ../
```

## Try interactive example

run **main** example using command:

```sh
./build/bin/main \
-m llm-models/llama-2-7b-chat.Q3_K_S.gguf \
-r "User:" -f prompts/chat-with-bob.txt \
-n 128 -b 1024 --repeat-penalty 1.0 --color -i
```

run **main** example with all model parts loaded to memory

```sh
./build/bin/main --no-mmap \
-m llm-models/llama-2-7b-chat.Q3_K_S.gguf \
-r "User:" -f prompts/chat-with-bob.txt \
-n 128 -b 1024 --repeat-penalty 1.0 --color -i
```


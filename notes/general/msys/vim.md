# Vim in MSYS2

## Setup Plug

```sh
mkdir -p ~/.vim/autoload/
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "call plug#begin('~/.vim/pack/plug/start')
call plug#end()" | tee ~/.vimrc

mkdir -p ~/.vim/pack/plug/start/
vim +PlugStatus
```

## Configurations

**NOTE:** Ultisnips are problematic in Windows

```sh
echo "
call plug#begin('~/.vim/pack/plug/start')
    Plug 'm-pilia/vim-pkgbuild'
    Plug 'dense-analysis/ale'
    Plug 'preservim/nerdcommenter'
    Plug 'preservim/nerdtree'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-commentary'
    Plug 'airblade/vim-gitgutter'
    Plug 'godlygeek/tabular'
    Plug 'preservim/tagbar'
    Plug 'preservim/vim-markdown'
    Plug 'chrisbra/csv.vim'
    Plug 'lervag/vimtex'
\"    Plug 'SirVer/ultisnips'
    Plug 'honza/vim-snippets'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

let g:coc_data_home = 'C:\\\\msys64\\\\home\\\\$USER\\\\.config\\\\coc'

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \\: \"\\<C-g>u\\<CR>\\<c-r>=coc#on_enter()\\<CR>\"

\":h cterm-colors
\":h gui-colors
\":hi
hi CocFloating ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow
hi CocInlayHint ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow

let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_toc_autofit = 1
let g:vim_markdown_autowrite = 1

autocmd BufWritePre * %s/\s\+$//e
filetype plugin on
filetype indent on
filetype plugin indent on
set expandtab ts=4 sw=4 ai
set conceallevel=0
set encoding=utf-8
set termguicolors
set ic is hls
set number
set wrap!
set mouse=a
let g:tagbar_width=20
let g:NERDTreeWinSize=20
syntax on" | tee ~/.vimrc
```

## CoC Plugins

```sh
mkdir -p ~/.config/coc/

vim +PlugInstall
vim -c "CocInstall coc-tsserver coc-vimtex"
vim -c "CocInstall coc-pairs coc-snippets"
vim -c "CocInstall coc-clangd coc-json"
vim -c "CocInstall coc-html coc-yaml"
vim -c "CocInstall coc-rust-analyzer"
vim +PlugClean
```

```sh
mkdir -p ~/.vim
rm -f ~/.vim/coc-settings.json

jq -n '
."clangd.arguments"=["-header-insertion=never"] |
."pairs.enableCharacters"=["(","[","\"","'\''","`"] |
."rust-analyzer.server.path"="/mingw64/bin/rust-analyzer" |
."snippets.ultisnips.enable"=false
' > ~/.vim/coc-settings.json
```

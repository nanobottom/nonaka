"vi setting (vimrc)
"Maintainer: Nonaka Ryo
set encoding=utf-8
set fileencoding=utf-8
set termencoding=utf-8
"履歴保存数
set history=1000
"クリップボードを利用する
set clipboard=unnamed
":eで開いたファイルを編集可能にする
set modifiable
"行番号の表示
set number
"編集コマンド実行後に変更された内容を表示する
set autoprint
"ステータスラインを常に表示
set laststatus=2
"ステータスラインの内容を表示
set statusline=%F%r%h%=
"ターミナルのタイトルをセット
set title
"検索文字列内で使用されるワイルドカード文字を特殊文字として扱う
set magic
"タブ幅
set tabstop=2
"タブを半角スペースで挿入する
set expandtab
"vimが読み込み時に生成するタブ幅
set shiftwidth=2
"改行時に自動でインデント
set smartindent
"空白文字の可視化
set list
"対応する括弧を表示
set showmatch
"対応する括弧に飛ぶ時間
set matchtime=1
"モードを表示
set showmode
"vi互換モードを切る（キーボード不具合に対処）
set nocompatible
"バックスペースキーの挙動
"set backspace=indent,eol,start
set ruler
set backspace=2
syntax on
"カラースキーム
"colorscheme hybrid
"colorscheme solarized
colorscheme darkblue
"colorscheme jellybeans
"colorscheme molokai
"colorscheme evening
"全角文字の幅を2に固定
set ambiwidth=double
"背景色
set background=dark
"折り返し表示
set wrap
"swapファイルを作成しない
set noswapfile
"半角文字の設定
set guifont=MS_Gothic:h9
"全角文字の設定
set guifontwide=MS_Gothic:h10
"論理行の移動を表示行の移動に変更
nnoremap k gk
nnoremap gk k
nnoremap j gj
nnoremap gj j
"{記入後に改行すると}を補完
inoremap ( ()<LEFT>
inoremap {<Enter> {}<Left><CR><ESC><S-o>
inoremap ( ()<ESC>i
inoremap (<Enter> ()<Left><CR><ESC><S-o>
"関数元にジャンプ
nnoremap <C-h> :vsp<CR> :exe("tjump ".expand('<cword>'))<CR>
nnoremap <C-k> :split<CR> :exe("tjump ".expand('<cword>'))<CR>
"複数宣言元が見つかった場合にリストにして選択できるようにする
nnoremap <C-h> :vsp<CR> :exe("tjump ".expand('<cword>'))<CR>
nnoremap <C-k> :split<CR> :exe("tjump ".expand('<cword>'))<CR>

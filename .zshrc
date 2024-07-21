# colors
NAME_COLOR='#00FFC6';
FIRST_PAW_COLOR='#85EF47';
SECOND_PAW_COLOR='#FF5722';
DIR_COLOR='#EA047E';
GIT_COLOR='#FFED00';


# functions
function git_branch_name () {
    branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
    if [[ $branch == "" ]]; then
        :
    else
        echo '\uE0A0(' $branch ') '
    fi
}

# setting for take in account / like a word separator in delete word
WORDCHARS=''

# setting history file
HISTFILE=~/.zsh_history

# setting history size
HISTSIZE=10000
SAVEHIST=10000

setopt prompt_subst
PS1="%F{$NAME_COLOR}%n %F{$FIRST_PAW_COLOR}  %F{$DIR_COLOR}%c %F{$GIT_COLOR}\$(git_branch_name)%F{$SECOND_PAW_COLOR}  %f"

# alias
# for open apps
alias v='nvim'

# shortcuts
alias l='LC_COLLATE=C ls -la --color=auto --group-directories-first --block-size=M'

alias pui='cd ~/workspace/portfolio-projects/pxndxs-ui'

# portfolio projects
alias nob='cd ~/workspace/portfolio/notices/notices-back'
alias nof='cd ~/workspace/portfolio/notices/notices-front'

# exports
export PATH="/home/pxndxs/.config/binaries/:$PATH"

# plugins
source ~/.config/zsh-plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
source ~/.config/zsh-plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# fnm
FNM_PATH="/home/pxndxs/.local/share/fnm"
if [ -d "$FNM_PATH" ]; then
  export PATH="/home/pxndxs/.local/share/fnm:$PATH"
  eval "`fnm env`"
fi

# bun completions
[ -s "/home/pxndxs/.bun/_bun" ] && source "/home/pxndxs/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

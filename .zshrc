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


setopt prompt_subst
PS1="%F{$NAME_COLOR}%n %F{$FIRST_PAW_COLOR}  %F{$DIR_COLOR}%c %F{$GIT_COLOR}\$(git_branch_name)%F{$SECOND_PAW_COLOR}  %f"

# alias
# for open apps
alias v='nvim'

# shortcuts
alias l='LC_COLLATE=C ls -la --color=auto --group-directories-first --block-size=M'

# offer-me
alias ofb='cd ~/workspace/portfolio-projects/offerme/offerme-back'
alias off='cd ~/workspace/portfolio-projects/offerme/offerme-front'

alias iff='cd ~/workspace/others/ing-mier/formulario/landing-formulario'
alias ifb='cd ~/workspace/others/ing-mier/formulario/formulario-back'

# exports
export PATH="/home/pxndxs/.config/binaries/:$PATH"

# bun completions
[ -s "/home/pxndxs/.bun/_bun" ] && source "/home/pxndxs/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

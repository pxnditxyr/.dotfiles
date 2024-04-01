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

alias jmf='cd ~/workspace/projects-twitch/landing-company/landing-company-front'
alias jmb='cd ~/workspace/projects-twitch/landing-company/landing-company-back'

alias pui='cd ~/workspace/portfolio-projects/pxndxs-ui'

# courses
alias c5n='cd ~/workspace/courses/node/05-noc'
alias c6n='cd ~/workspace/courses/node/06-json-server'
alias c7n='cd ~/workspace/courses/node/07-rest-web'
alias c8n='cd ~/workspace/courses/node/08-rest-server'

alias cn1="cd ~/workspace/courses/next/next-01"
alias cn2="cd ~/workspace/courses/next/next-02"

alias jgb="cd ~/workspace/others/jhonnael/eventride/eventride-back"
alias jgf="cd ~/workspace/others/jhonnael/eventride/eventride-front"

# portfolio projects
alias nob='cd ~/workspace/portfolio-projects/notices/notices-back'
alias nof='cd ~/workspace/portfolio-projects/notices/notices-front'


# exports
export PATH="/home/pxndxs/.config/binaries/:$PATH"

# bun completions
[ -s "/home/pxndxs/.bun/_bun" ] && source "/home/pxndxs/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
